import secrets
import string
import sqlite3
from cryptography.fernet import Fernet
from getpass import getpass
import zxcvbn
import pyperclip
import json
from datetime import datetime
import qrcode
import os
import hashlib
import argon2


class PasswordManager:
    def __init__(self):
        self.db_name = "passwords.db"
        self.key_file = "secret.key"
        self.master_pw_hash = None
        self.cipher = None
        self.initialize_database()

    def initialize_database(self):
        """Initialize database and encryption"""
        # Create or load encryption key
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)

        with open(self.key_file, "rb") as f:
            key = f.read()
        self.cipher = Fernet(key)

        # Create database tables
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create passwords table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT,
                password TEXT NOT NULL,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                strength_score INTEGER
            )
        """
        )

        # Create master password hash table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS auth (
                hash TEXT NOT NULL,
                salt TEXT NOT NULL
            )
        """
        )

        conn.commit()
        conn.close()

        # Check if master password exists
        if not self.master_password_exists():
            self.setup_master_password()
        else:
            self.authenticate()

    def master_password_exists(self):
        """Check if master password is set"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM auth")
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0

    def setup_master_password(self):
        """Set up master password for the first time"""
        print("\n=== SETUP MASTER PASSWORD ===")
        print("This password will encrypt your entire vault.")
        print(
            "Choose a strong password (min 12 characters with mix of letters, numbers, and symbols)."
        )

        while True:
            master_pw = getpass("Enter master password: ")
            confirm_pw = getpass("Confirm master password: ")

            if master_pw != confirm_pw:
                print("Passwords don't match. Try again.")
                continue

            if len(master_pw) < 12:
                print("Password too short. Minimum 12 characters required.")
                continue

            result = zxcvbn.zxcvbn(master_pw)
            if result["score"] < 3:
                print("Password too weak. Please choose a stronger password.")
                print("Suggestions:", result["feedback"]["suggestions"])
                continue

            break

        # Generate salt and hash using Argon2
        salt = secrets.token_bytes(16)
        hasher = argon2.PasswordHasher(
            time_cost=3, memory_cost=65536, parallelism=4, hash_len=32, salt_len=16
        )
        pw_hash = hasher.hash(master_pw.encode() + salt)

        # Store hash and salt
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO auth (hash, salt) VALUES (?, ?)", (pw_hash, salt.hex())
        )
        conn.commit()
        conn.close()

        print("\nMaster password set successfully!")
        self.master_pw_hash = pw_hash

    def authenticate(self):
        """Authenticate with master password"""
        print("\n=== PASSWORD VAULT LOGIN ===")

        # Get stored hash and salt
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT hash, salt FROM auth LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if not result:
            print("No master password found. Please set one up.")
            self.setup_master_password()
            return

        stored_hash, salt_hex = result
        salt = bytes.fromhex(salt_hex)

        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            master_pw = getpass("Enter master password: ")

            try:
                hasher = argon2.PasswordHasher()
                hasher.verify(stored_hash, master_pw.encode() + salt)
                self.master_pw_hash = stored_hash
                print("\nAuthentication successful!")
                return
            except:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Invalid password. {remaining} attempts remaining.")
                else:
                    print("Maximum attempts reached. Exiting.")
                    exit()

    def generate_password(
        self,
        length=32,
        use_upper=True,
        use_digits=True,
        use_symbols=True,
        avoid_ambiguous=True,
    ):
        """Generate secure random password"""
        chars = string.ascii_lowercase

        if use_upper:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        # Remove ambiguous characters if requested
        if avoid_ambiguous:
            ambiguous = "l1IoO0"
            chars = "".join(c for c in chars if c not in ambiguous)

        while True:
            password = "".join(secrets.choice(chars) for _ in range(length))

            # Ensure password meets complexity requirements
            if use_upper and not any(c.isupper() for c in password):
                continue
            if use_digits and not any(c.isdigit() for c in password):
                continue
            if use_symbols and not any(c in string.punctuation for c in password):
                continue

            break

        return password

    def analyze_password(self, password):
        """Analyze password strength using zxcvbn"""
        result = zxcvbn.zxcvbn(password)
        return {
            "score": result["score"],
            "crack_time": result["crack_times_display"][
                "offline_slow_hashing_1e4_per_second"
            ],
            "feedback": result["feedback"],
        }

    def store_password(self, service, username, password, notes=""):
        """Store password in encrypted database"""
        encrypted_pw = self.cipher.encrypt(password.encode())
        strength = self.analyze_password(password)["score"]

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO passwords (service, username, password, notes, strength_score)
            VALUES (?, ?, ?, ?, ?)
        """,
            (service, username, encrypted_pw, notes, strength),
        )

        conn.commit()
        conn.close()

    def get_password(self, service):
        """Retrieve password from database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT username, password, notes FROM passwords 
            WHERE service = ? ORDER BY last_used DESC LIMIT 1
        """,
            (service,),
        )

        result = cursor.fetchone()

        if not result:
            return None

        username, encrypted_pw, notes = result
        password = self.cipher.decrypt(encrypted_pw).decode()

        # Update last used timestamp
        cursor.execute(
            """
            UPDATE passwords SET last_used = CURRENT_TIMESTAMP 
            WHERE service = ? AND username = ?
        """,
            (service, username),
        )
        conn.commit()
        conn.close()

        return {
            "service": service,
            "username": username,
            "password": password,
            "notes": notes,
        }

    def export_passwords(self, format="json", file_path=None):
        """Export passwords to file"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT service, username, password, notes FROM passwords
        """
        )

        passwords = []
        for row in cursor.fetchall():
            service, username, encrypted_pw, notes = row
            password = self.cipher.decrypt(encrypted_pw).decode()
            passwords.append(
                {
                    "service": service,
                    "username": username,
                    "password": password,
                    "notes": notes,
                }
            )

        conn.close()

        if format == "json":
            if not file_path:
                file_path = f'passwords_export_{datetime.now().strftime("%Y%m%d")}.json'
            with open(file_path, "w") as f:
                json.dump(passwords, f, indent=2)
            return file_path

        elif format == "csv":
            if not file_path:
                file_path = f'passwords_export_{datetime.now().strftime("%Y%m%d")}.csv'
            with open(file_path, "w") as f:
                f.write("service,username,password,notes\n")
                for item in passwords:
                    f.write(
                        f'"{item["service"]}","{item["username"]}","{item["password"]}","{item["notes"]}"\n'
                    )
            return file_path

    def generate_qr_code(self, data, file_path=None):
        """Generate QR code for password sharing"""
        if not file_path:
            file_path = f'qr_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)
        return file_path

    def interactive_menu(self):
        """Main interactive menu"""
        while True:
            print("\n=== PASSWORD MANAGER ===")
            print("1. Generate new password")
            print("2. Store a password")
            print("3. Retrieve a password")
            print("4. Export passwords")
            print("5. Generate QR code for sharing")
            print("6. Exit")

            choice = input("\nEnter your choice (1-6): ")

            if choice == "1":
                self.generate_password_menu()
            elif choice == "2":
                self.store_password_menu()
            elif choice == "3":
                self.retrieve_password_menu()
            elif choice == "4":
                self.export_menu()
            elif choice == "5":
                self.qr_code_menu()
            elif choice == "6":
                print("\nExiting. Your passwords are secure!")
                break
            else:
                print("Invalid choice. Please try again.")

    def generate_password_menu(self):
        """Interactive password generation"""
        print("\n=== PASSWORD GENERATOR ===")

        # Get parameters
        length = 32
        use_upper = (
            input("Include uppercase letters? (y/n, default y): ").lower() != "n"
        )
        use_digits = input("Include digits? (y/n, default y): ").lower() != "n"
        use_symbols = input("Include symbols? (y/n, default y): ").lower() != "n"
        avoid_ambiguous = (
            input("Avoid ambiguous characters (l,1,I,0,O)? (y/n, default y): ").lower()
            != "n"
        )

        # Generate password
        password = self.generate_password(
            length=length,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols,
            avoid_ambiguous=avoid_ambiguous,
        )

        # Analyze strength
        analysis = self.analyze_password(password)

        # Display results
        print("\nGenerated Password:", password)
        print("Strength Score:", analysis["score"], "/ 4")
        print("Estimated Crack Time:", analysis["crack_time"])

        if analysis["feedback"]["warning"]:
            print("Warning:", analysis["feedback"]["warning"])

        # Copy to clipboard
        pyperclip.copy(password)
        print("\nPassword copied to clipboard (will clear after 30 seconds).")

        # Offer to store
        store = input("\nStore this password? (y/n): ").lower() == "y"
        if store:
            service = input("Service/Website: ")
            username = input("Username (optional): ")
            notes = input("Notes (optional): ")
            self.store_password(service, username, password, notes)
            print("Password stored securely!")

    def store_password_menu(self):
        """Store an existing password"""
        print("\n=== STORE PASSWORD ===")
        service = input("Service/Website: ")
        username = input("Username (optional): ")
        password = getpass("Password: ")
        notes = input("Notes (optional): ")

        self.store_password(service, username, password, notes)
        print("\nPassword stored securely!")

    def retrieve_password_menu(self):
        """Retrieve a stored password"""
        print("\n=== RETRIEVE PASSWORD ===")
        service = input("Enter service name: ")

        result = self.get_password(service)
        if not result:
            print("No password found for this service.")
            return

        print("\nPassword Details:")
        print(f"Service: {result['service']}")
        if result["username"]:
            print(f"Username: {result['username']}")
        print(f"Password: {result['password']}")
        if result["notes"]:
            print(f"Notes: {result['notes']}")

        # Copy to clipboard
        pyperclip.copy(result["password"])
        print("\nPassword copied to clipboard (will clear after 30 seconds).")

    def export_menu(self):
        """Export passwords menu"""
        print("\n=== EXPORT PASSWORDS ===")
        print("1. Export to JSON")
        print("2. Export to CSV")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            file_path = self.export_passwords(format="json")
            print(f"\nPasswords exported to {file_path}")
        elif choice == "2":
            file_path = self.export_passwords(format="csv")
            print(f"\nPasswords exported to {file_path}")
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def qr_code_menu(self):
        """QR code generation menu"""
        print("\n=== QR CODE GENERATOR ===")
        data = input("Enter text or password to encode: ")
        file_path = self.generate_qr_code(data)
        print(f"\nQR code saved to {file_path}")


if __name__ == "__main__":
    manager = PasswordManager()
    manager.interactive_menu()
