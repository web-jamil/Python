import sys
import sqlite3
import json
import hashlib
import os
from datetime import datetime
from getpass import getpass


logo="""
                                        _       _                                   
                                       (_)     | |                                  
   ___ __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __    ___   ___  _ __  
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|  / _ \ / _ \| '_ \ 
 | (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |    | (_) | (_) | |_) |
  \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|     \___/ \___/| .__/ 
                                         | |                                 | |    
                                         |_|                                 |_|    """
# --- Configuration ---
CONFIG_FILE = "caesar_config.json"
DATABASE_FILE = "caesar_cipher.db"

# Default configuration
DEFAULT_CONFIG = {
    "max_login_attempts": 3,
    "password_min_length": 8,
    "history_limit": 100,
    "admin_username": "admin"
}

# --- Database Setup ---
def init_database():
    """Initialize the SQLite database with required tables"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        is_admin INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        last_login TEXT
    )
    ''')
    
    # Encryption history table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        operation TEXT NOT NULL,  -- 'encrypt' or 'decrypt'
        original_text TEXT NOT NULL,
        result_text TEXT NOT NULL,
        shift INTEGER,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    # Failed login attempts tracking
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        attempt_time TEXT DEFAULT CURRENT_TIMESTAMP,
        ip_address TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

# --- Configuration Management ---
def load_config():
    """Load configuration from JSON file or create default"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            # Merge with default to ensure all keys exist
            return {**DEFAULT_CONFIG, **config}
    else:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

# --- Password Handling ---
def generate_salt():
    """Generate a random salt for password hashing"""
    return os.urandom(16).hex()

def hash_password(password, salt):
    """Hash password with salt using SHA-256"""
    return hashlib.sha256((password + salt).encode()).hexdigest()

# --- User Management ---
def create_user(username, password, is_admin=False):
    """Create a new user account"""
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            'INSERT INTO users (username, password_hash, salt, is_admin) VALUES (?, ?, ?, ?)',
            (username, password_hash, salt, int(is_admin))
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Username already exists!")
        return False
    finally:
        conn.close()

def verify_user(username, password):
    """Verify user credentials"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT password_hash, salt, is_admin FROM users WHERE username = ?',
        (username,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        return False, False
    
    stored_hash, salt, is_admin = result
    input_hash = hash_password(password, salt)
    
    return (input_hash == stored_hash), bool(is_admin)

def record_login_attempt(username, success):
    """Record login attempts for security monitoring"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    if success:
        # Update last login time
        cursor.execute(
            'UPDATE users SET last_login = ? WHERE username = ?',
            (datetime.now().isoformat(), username)
        )
    else:
        # Record failed attempt
        cursor.execute(
            'INSERT INTO login_attempts (username, ip_address) VALUES (?, ?)',
            (username, get_client_ip())
        )
    
    conn.commit()
    conn.close()

def get_client_ip():
    """Get client IP address (simplified for this example)"""
    # In a real application, you'd get this from the request
    return "127.0.0.1"

def check_login_attempts(username):
    """Check if user has too many failed login attempts"""
    config = load_config()
    max_attempts = config['max_login_attempts']
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        '''SELECT COUNT(*) FROM login_attempts 
           WHERE username = ? AND attempt_time > datetime('now', '-15 minutes')''',
        (username,)
    )
    attempts = cursor.fetchone()[0]
    conn.close()
    
    return attempts >= max_attempts

# --- Caesar Cipher Core Functions (Enhanced) ---
def caesar_encrypt(text: str, shift: int, user_id=None) -> str:
    """Encrypt text with Caesar cipher and log to database"""
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    
    if user_id:
        log_operation(user_id, 'encrypt', text, encrypted_text, shift)
    
    return encrypted_text

def caesar_decrypt(text: str, shift: int, user_id=None) -> str:
    """Decrypt text with Caesar cipher and log to database"""
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    
    if user_id:
        log_operation(user_id, 'decrypt', text, decrypted_text, shift)
    
    return decrypted_text

def brute_force_caesar(text: str, user_id=None):
    """Brute-force Caesar cipher and log to database"""
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        results.append((shift, decrypted))
    
    if user_id:
        log_operation(user_id, 'brute_force', text, f"{len(results)} possibilities", None)
    
    return results

def log_operation(user_id, operation, original, result, shift):
    """Log encryption/decryption operations to database"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        '''INSERT INTO history 
           (user_id, operation, original_text, result_text, shift) 
           VALUES (?, ?, ?, ?, ?)''',
        (user_id, operation, original, result, shift)
    )
    
    # Enforce history limit
    config = load_config()
    cursor.execute(
        '''DELETE FROM history 
           WHERE user_id = ? AND id NOT IN 
           (SELECT id FROM history WHERE user_id = ? 
           ORDER BY timestamp DESC LIMIT ?)''',
        (user_id, user_id, config['history_limit'])
    )
    
    conn.commit()
    conn.close()

# --- User Interface Functions ---
def login():
    """Handle user login"""
    config = load_config()
    
    print("\n=== Login ===")
    username = input("Username: ").strip()
    
    if check_login_attempts(username):
        print("Too many failed login attempts. Please try again later.")
        return None, False
    
    password = getpass("Password: ")
    
    is_valid, is_admin = verify_user(username, password)
    if is_valid:
        record_login_attempt(username, True)
        print("Login successful!")
        
        # Get user ID
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user_id = cursor.fetchone()[0]
        conn.close()
        
        return user_id, is_admin
    else:
        record_login_attempt(username, False)
        print("Invalid username or password")
        return None, False

def register():
    """Handle new user registration"""
    config = load_config()
    
    print("\n=== Register New Account ===")
    username = input("Choose a username: ").strip()
    
    while True:
        password = getpass(f"Choose a password (min {config['password_min_length']} chars): ")
        if len(password) < config['password_min_length']:
            print(f"Password must be at least {config['password_min_length']} characters")
        else:
            confirm = getpass("Confirm password: ")
            if password == confirm:
                break
            print("Passwords don't match!")
    
    if create_user(username, password):
        print("Account created successfully! You can now login.")
    else:
        print("Failed to create account.")

def admin_menu(user_id):
    """Admin-specific menu options"""
    while True:
        print("\n=== Admin Menu ===")
        print("1. View all users")
        print("2. View login attempts")
        print("3. Reset user password")
        print("4. Back to main menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_all_users()
        elif choice == '2':
            view_login_attempts()
        elif choice == '3':
            reset_user_password()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

def view_all_users():
    """Display all registered users"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, username, is_admin, created_at, last_login FROM users')
    users = cursor.fetchall()
    conn.close()
    
    print("\n=== Registered Users ===")
    print(f"{'ID':<5}{'Username':<20}{'Admin':<8}{'Created':<25}{'Last Login':<25}")
    for user in users:
        user_id, username, is_admin, created, last_login = user
        print(f"{user_id:<5}{username:<20}{'Yes' if is_admin else 'No':<8}{created:<25}{last_login or 'Never':<25}")

def view_login_attempts():
    """Display recent login attempts"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT username, attempt_time, ip_address 
        FROM login_attempts 
        ORDER BY attempt_time DESC 
        LIMIT 50
    ''')
    attempts = cursor.fetchall()
    conn.close()
    
    print("\n=== Recent Login Attempts ===")
    print(f"{'Username':<20}{'Time':<25}{'IP Address':<15}")
    for attempt in attempts:
        username, time, ip = attempt
        print(f"{username:<20}{time:<25}{ip:<15}")

def reset_user_password():
    """Admin function to reset user password"""
    username = input("Enter username to reset password: ").strip()
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT 1 FROM users WHERE username = ?', (username,))
    if not cursor.fetchone():
        print("User not found!")
        conn.close()
        return
    
    new_password = getpass("Enter new password: ")
    confirm = getpass("Confirm new password: ")
    
    if new_password != confirm:
        print("Passwords don't match!")
        conn.close()
        return
    
    salt = generate_salt()
    password_hash = hash_password(new_password, salt)
    
    cursor.execute(
        'UPDATE users SET password_hash = ?, salt = ? WHERE username = ?',
        (password_hash, salt, username)
    )
    conn.commit()
    conn.close()
    print("Password reset successfully!")

def view_history(user_id):
    """View user's encryption/decryption history"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT operation, original_text, result_text, shift, timestamp 
        FROM history 
        WHERE user_id = ? 
        ORDER BY timestamp DESC 
        LIMIT 20
    ''', (user_id,))
    
    history = cursor.fetchall()
    conn.close()
    
    print("\n=== Your Recent Activity ===")
    print(f"{'Operation':<10}{'Original':<30}{'Result':<30}{'Shift':<6}{'Time':<20}")
    for item in history:
        op, original, result, shift, time = item
        print(f"{op:<10}{original[:28]:<30}{result[:28]:<30}{str(shift) if shift is not None else 'N/A':<6}{time:<20}")

# --- Main Application ---
def run_caesar_cipher_app():
    """Main application loop"""
    # Initialize database and config
    init_database()
    config = load_config()
    
    # Check if admin exists, create if not
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE username = ?', (config['admin_username'],))
    if not cursor.fetchone():
        admin_password = getpass(f"Create password for admin user '{config['admin_username']}': ")
        create_user(config['admin_username'], admin_password, is_admin=True)
        print("Admin account created.")
    conn.close()
    
    print("\nWelcome to the Advanced Caesar Cipher Tool!")
    print("------------------------------------------")
    
    current_user = None
    is_admin = False
    
    while True:
        if current_user is None:
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                current_user, is_admin = login()
            elif choice == '2':
                register()
            elif choice == '3':
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice")
        else:
            print("\nMain Menu:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Brute-force a message (crack)")
            print("4. View history")
            if is_admin:
                print("5. Admin Menu")
            print("6. Logout")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                message = input("Enter the message to encrypt: ")
                while True:
                    try:
                        shift = int(input("Enter the shift number (an integer, e.g., 3): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a whole number for the shift.")
                encrypted = caesar_encrypt(message, shift, current_user)
                print(f"\nYour encrypted message is: {encrypted}")
                
            elif choice == '2':
                message = input("Enter the message to decrypt: ")
                while True:
                    try:
                        shift = int(input("Enter the shift number (an integer, e.g., 3): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a whole number for the shift.")
                decrypted = caesar_decrypt(message, shift, current_user)
                print(f"\nYour decrypted message is: {decrypted}")
                
            elif choice == '3':
                message = input("Enter the message to brute-force: ")
                results = brute_force_caesar(message, current_user)
                print("\n--- Possible Decryptions ---")
                for shift, decrypted in results:
                    print(f"Shift {shift:2d}: {decrypted}")
                print("\nLook through the possible decryptions above. One of them should be the original message!")
                
            elif choice == '4':
                view_history(current_user)
                
            elif choice == '5' and is_admin:
                admin_menu(current_user)
                
            elif choice == '6':
                current_user = None
                is_admin = False
                print("Logged out successfully.")
                
            elif choice == '7':
                print("Goodbye!")
                sys.exit()
                
            else:
                print("Invalid choice")

if __name__ == "__main__":
    print
    run_caesar_cipher_app()