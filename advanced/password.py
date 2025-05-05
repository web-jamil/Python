_github_password ="SAQxVZGcAhNgwL8JR44xW9UQcXKQTx"
python_password="2861065049jamil"


import secrets
import string

def generate_password(length=32, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    
    return ''.join(secrets.choice(chars) for _ in range(length))

# Example:
password = generate_password(32, True, True, True)
print(password)  # Output: "xK9@q#Lm2$Pv!7sZ5%fT8&Wb*Y4?nJ6"




import os
import sys
import secrets
import string
import json
import getpass
import base64
import hashlib
import hmac
import time
import pyotp
import requests
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import zxcvbn
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import Dict, List, Optional, Tuple
import webbrowser
import qrcode
from PIL import Image, ImageTk
import threading

class AdvancedPasswordManager:
    def __init__(self):
        self.key: Optional[bytes] = None
        self.master_password_hash: Optional[str] = None
        self.salt: bytes = os.urandom(16)
        self.db_file: str = "vault.db.enc"
        self.config_file: str = "config.enc"
        self.breach_api_url: str = "https://haveibeenpwned.com/api/v3/breachedaccount/"
        self.breach_api_key: str = ""  # Register at haveibeenpwned.com for API key
        self.load_config()
        
        # Password policy defaults
        self.default_policy = {
            'length': 16,
            'use_upper': True,
            'use_lower': True,
            'use_digits': True,
            'use_special': True,
            'avoid_ambiguous': True,
            'min_entropy': 80,
            'exclude_similar': True
        }

    def derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key from master password using PBKDF2"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def load_config(self) -> None:
        """Load or initialize configuration"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "rb") as f:
                    encrypted = f.read()
                    fernet = Fernet(self.derive_key(getpass.getpass("Master password: "), self.salt))
                    config = json.loads(fernet.decrypt(encrypted).decode())
                    self.master_password_hash = config['master_password_hash']
                    self.salt = base64.b64decode(config['salt'])
                    if 'breach_api_key' in config:
                        self.breach_api_key = config['breach_api_key']
                    if 'default_policy' in config:
                        self.default_policy.update(config['default_policy'])
            except Exception as e:
                print(f"Error loading config: {e}")
                sys.exit(1)

    def save_config(self) -> None:
        """Save configuration securely"""
        config = {
            'master_password_hash': self.master_password_hash,
            'salt': base64.b64encode(self.salt).decode(),
            'breach_api_key': self.breach_api_key,
            'default_policy': self.default_policy
        }
        fernet = Fernet(self.derive_key(getpass.getpass("Master password: "), self.salt))
        encrypted = fernet.encrypt(json.dumps(config).encode())
        with open(self.config_file, "wb") as f:
            f.write(encrypted)

    def initialize_vault(self) -> bool:
        """Initialize the password vault with master password"""
        if self.master_password_hash is not None:
            return True
            
        master_pw = getpass.getpass("Create master password: ")
        confirm_pw = getpass.getpass("Confirm master password: ")
        
        if master_pw != confirm_pw:
            print("Passwords don't match!")
            return False
            
        strength = zxcvbn.zxcvbn(master_pw)
        if strength['score'] < 4:
            print("Master password too weak! Score must be 4/4.")
            print(f"Suggestions: {strength['feedback']['suggestions']}")
            return False
            
        self.salt = os.urandom(16)
        self.master_password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            master_pw.encode(),
            self.salt,
            100000
        ).hex()
        
        # Initialize empty vault
        self.save_passwords([])
        self.save_config()
        return True

    def authenticate(self) -> bool:
        """Authenticate with master password"""
        attempt = getpass.getpass("Master password: ")
        attempt_hash = hashlib.pbkdf2_hmac(
            'sha256',
            attempt.encode(),
            self.salt,
            100000
        ).hex()
        return hmac.compare_digest(attempt_hash, self.master_password_hash)

    def generate_password(self, policy: Optional[Dict] = None) -> str:
        """Generate password according to policy"""
        policy = policy or self.default_policy
        length = policy['length']
        
        # Define character sets
        char_sets = []
        ambiguous = ""
        
        if policy['use_upper']:
            upper = string.ascii_uppercase
            if policy['avoid_ambiguous']:
                upper = upper.translate(str.maketrans('', '', 'IO'))
            char_sets.append(upper)
            if policy['avoid_ambiguous']:
                ambiguous += 'IO'
                
        if policy['use_lower']:
            lower = string.ascii_lowercase
            if policy['avoid_ambiguous']:
                lower = lower.translate(str.maketrans('', '', 'l'))
            char_sets.append(lower)
            if policy['avoid_ambiguous']:
                ambiguous += 'l'
                
        if policy['use_digits']:
            digits = string.digits
            if policy['avoid_ambiguous']:
                digits = digits.translate(str.maketrans('', '', '01'))
            char_sets.append(digits)
            if policy['avoid_ambiguous']:
                ambiguous += '01'
                
        if policy['use_special']:
            special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            if policy['avoid_ambiguous']:
                special = special.translate(str.maketrans('', '', '|;:\'".,'))
            char_sets.append(special)
            
        if not char_sets:
            raise ValueError("At least one character set must be enabled")
            
        # Generate password ensuring at least one from each set
        password = []
        for charset in char_sets:
            password.append(secrets.choice(charset))
            
        # Fill remaining length
        all_chars = ''.join(char_sets)
        remaining = length - len(password)
        password.extend(secrets.choice(all_chars) for _ in range(remaining))
        
        # Shuffle and check entropy
        secrets.SystemRandom().shuffle(password)
        password = ''.join(password)
        
        # Verify entropy meets requirements
        entropy = self.calculate_entropy(password)
        if entropy < policy['min_entropy']:
            return self.generate_password(policy)  # Try again
            
        return password

    def calculate_entropy(self, password: str) -> float:
        """Calculate password entropy in bits"""
        charset_size = 0
        if any(c in string.ascii_lowercase for c in password):
            charset_size += 26
        if any(c in string.ascii_uppercase for c in password):
            charset_size += 26
        if any(c in string.digits for c in password):
            charset_size += 10
        if any(c in string.punctuation for c in password):
            charset_size += 32  # Approximate common special chars
            
        length = len(password)
        return length * (math.log(charset_size) / math.log(2))

    def save_passwords(self, passwords: List[Dict]) -> None:
        """Encrypt and save passwords to file"""
        fernet = Fernet(self.derive_key(getpass.getpass("Master password: "), self.salt))
        encrypted = fernet.encrypt(json.dumps(passwords).encode())
        with open(self.db_file, "wb") as f:
            f.write(encrypted)

    def load_passwords(self) -> List[Dict]:
        """Load and decrypt passwords from file"""
        try:
            with open(self.db_file, "rb") as f:
                encrypted = f.read()
                fernet = Fernet(self.derive_key(getpass.getpass("Master password: "), self.salt))
                return json.loads(fernet.decrypt(encrypted).decode())
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        except Exception as e:
            print(f"Error loading passwords: {e}")
            return []

    def check_breaches(self, password: str) -> Tuple[bool, Optional[List[str]]]:
        """Check if password appears in known breaches using k-anonymity"""
        if not self.breach_api_key:
            return False, None
            
        # Hash the password and send first 5 chars of hash
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        
        try:
            headers = {"hibp-api-key": self.breach_api_key}
            response = requests.get(
                f"https://api.pwnedpasswords.com/range/{prefix}",
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            
            # Check if our full hash suffix appears in results
            suffix = sha1_hash[5:]
            for line in response.text.splitlines():
                if line.split(':')[0] == suffix:
                    return True, None
                    
            return False, None
        except requests.RequestException:
            return False, None

    def generate_totp_secret(self) -> str:
        """Generate a new TOTP secret"""
        return pyotp.random_base32()

    def get_totp_code(self, secret: str) -> str:
        """Generate current TOTP code"""
        return pyotp.TOTP(secret).now()

    def verify_totp(self, secret: str, code: str) -> bool:
        """Verify a TOTP code"""
        return pyotp.TOTP(secret).verify(code)

    def generate_qr_code(self, secret: str, issuer: str, account_name: str) -> Image.Image:
        """Generate QR code for TOTP setup"""
        uri = pyotp.totp.TOTP(secret).provisioning_uri(account_name, issuer_name=issuer)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")

class PasswordManagerGUI:
    def __init__(self, manager: AdvancedPasswordManager):
        self.manager = manager
        self.root = tk.Tk()
        self.root.title("Advanced Password Manager")
        self.root.geometry("900x600")
        self.setup_ui()
        
        # Check if vault needs initialization
        if self.manager.master_password_hash is None:
            self.show_setup_wizard()
            
    def setup_ui(self):
        """Setup the main user interface"""
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')
        
        # Password Vault Tab
        self.vault_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.vault_frame, text="Password Vault")
        self.setup_vault_tab()
        
        # Generator Tab
        self.generator_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.generator_frame, text="Password Generator")
        self.setup_generator_tab()
        
        # TOTP Tab
        self.totp_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.totp_frame, text="2FA Manager")
        self.setup_totp_tab()
        
        # Settings Tab
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")
        self.setup_settings_tab()
        
    def setup_vault_tab(self):
        """Setup password vault tab"""
        # Treeview for password entries
        columns = ("service", "username", "strength")
        self.vault_tree = ttk.Treeview(
            self.vault_frame, columns=columns, show="headings", selectmode='browse'
        )
        self.vault_tree.heading("service", text="Service")
        self.vault_tree.heading("username", text="Username")
        self.vault_tree.heading("strength", text="Strength")
        self.vault_tree.column("service", width=200)
        self.vault_tree.column("username", width=200)
        self.vault_tree.column("strength", width=100)
        self.vault_tree.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Buttons frame
        btn_frame = ttk.Frame(self.vault_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Add Entry", command=self.add_password_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Edit Entry", command=self.edit_password_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Delete Entry", command=self.delete_password_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_vault).pack(side='right', padx=5)
        ttk.Button(btn_frame, text="Show Password", command=self.show_password).pack(side='right', padx=5)
        
        # Bind double click to show password
        self.vault_tree.bind("<Double-1>", lambda e: self.show_password())
        
        # Load initial data
        self.refresh_vault()
        
    def setup_generator_tab(self):
        """Setup password generator tab"""
        # Password policy controls
        policy_frame = ttk.LabelFrame(self.generator_frame, text="Password Policy")
        policy_frame.pack(fill='x', padx=10, pady=5)
        
        # Length
        ttk.Label(policy_frame, text="Length:").grid(row=0, column=0, sticky='w')
        self.length_var = tk.IntVar(value=self.manager.default_policy['length'])
        ttk.Spinbox(policy_frame, from_=8, to=64, textvariable=self.length_var).grid(row=0, column=1, sticky='ew')
        
        # Character sets
        self.upper_var = tk.BooleanVar(value=self.manager.default_policy['use_upper'])
        ttk.Checkbutton(policy_frame, text="Uppercase (A-Z)", variable=self.upper_var).grid(row=1, column=0, sticky='w')
        
        self.lower_var = tk.BooleanVar(value=self.manager.default_policy['use_lower'])
        ttk.Checkbutton(policy_frame, text="Lowercase (a-z)", variable=self.lower_var).grid(row=1, column=1, sticky='w')
        
        self.digits_var = tk.BooleanVar(value=self.manager.default_policy['use_digits'])
        ttk.Checkbutton(policy_frame, text="Digits (0-9)", variable=self.digits_var).grid(row=2, column=0, sticky='w')
        
        self.special_var = tk.BooleanVar(value=self.manager.default_policy['use_special'])
        ttk.Checkbutton(policy_frame, text="Special (!@#...)", variable=self.special_var).grid(row=2, column=1, sticky='w')
        
        self.ambiguous_var = tk.BooleanVar(value=self.manager.default_policy['avoid_ambiguous'])
        ttk.Checkbutton(policy_frame, text="Avoid ambiguous chars", variable=self.ambiguous_var).grid(row=3, column=0, sticky='w')
        
        # Generate button
        ttk.Button(self.generator_frame, text="Generate Password", command=self.generate_password).pack(pady=10)
        
        # Generated password display
        self.password_var = tk.StringVar()
        ttk.Entry(self.generator_frame, textvariable=self.password_var, font=('Courier', 12), state='readonly').pack(fill='x', padx=10, pady=5)
        
        # Strength meter
        self.strength_frame = ttk.Frame(self.generator_frame)
        self.strength_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(self.strength_frame, text="Strength:").pack(side='left')
        self.strength_meter = ttk.Progressbar(self.strength_frame, maximum=4)
        self.strength_meter.pack(side='left', expand=True, fill='x', padx=5)
        self.strength_label = ttk.Label(self.strength_frame, text="")
        self.strength_label.pack(side='left')
        
        # Action buttons
        btn_frame = ttk.Frame(self.generator_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Save to Vault", command=self.save_generated_password).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Check Breaches", command=self.check_breaches).pack(side='right', padx=5)
        
    def setup_totp_tab(self):
        """Setup TOTP/2FA manager tab"""
        # Treeview for TOTP entries
        columns = ("issuer", "account")
        self.totp_tree = ttk.Treeview(
            self.totp_frame, columns=columns, show="headings", selectmode='browse'
        )
        self.totp_tree.heading("issuer", text="Issuer")
        self.totp_tree.heading("account", text="Account")
        self.totp_tree.column("issuer", width=200)
        self.totp_tree.column("account", width=300)
        self.totp_tree.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Current code frame
        code_frame = ttk.Frame(self.totp_frame)
        code_frame.pack(fill='x', padx=10, pady=5)
        
        self.totp_code_var = tk.StringVar()
        ttk.Label(code_frame, text="Current Code:").pack(side='left')
        ttk.Entry(code_frame, textvariable=self.totp_code_var, font=('Courier', 12), width=10, state='readonly').pack(side='left', padx=5)
        self.totp_timer_var = tk.StringVar()
        ttk.Label(code_frame, textvariable=self.totp_timer_var).pack(side='left')
        
        # Buttons frame
        btn_frame = ttk.Frame(self.totp_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Add TOTP", command=self.add_totp_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Delete TOTP", command=self.delete_totp_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Show QR", command=self.show_qr_code).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Copy Code", command=self.copy_totp_code).pack(side='right', padx=5)
        
        # Start TOTP refresh timer
        self.update_totp_codes()
        
    def setup_settings_tab(self):
        """Setup settings tab"""
        # Master password change
        pw_frame = ttk.LabelFrame(self.settings_frame, text="Master Password")
        pw_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(pw_frame, text="Change Master Password", command=self.change_master_password).pack(pady=5)
        
        # API settings
        api_frame = ttk.LabelFrame(self.settings_frame, text="API Settings")
        api_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(api_frame, text="HaveIBeenPwned API Key:").pack(anchor='w')
        self.api_key_var = tk.StringVar(value=self.manager.breach_api_key)
        ttk.Entry(api_frame, textvariable=self.api_key_var).pack(fill='x', pady=2)
        ttk.Button(api_frame, text="Save API Key", command=self.save_api_key).pack(pady=5)
        
        # Password policy defaults
        policy_frame = ttk.LabelFrame(self.settings_frame, text="Default Password Policy")
        policy_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(policy_frame, text="Save Current Policy as Default", command=self.save_default_policy).pack(pady=5)
        
    def show_setup_wizard(self):
        """Show initial setup wizard"""
        wizard = tk.Toplevel(self.root)
        wizard.title("Initial Setup")
        wizard.geometry("400x300")
        wizard.grab_set()
        
        ttk.Label(wizard, text="Welcome to Password Manager", font=('', 14)).pack(pady=20)
        ttk.Label(wizard, text="You need to set a master password to continue").pack(pady=10)
        
        ttk.Label(wizard, text="Master Password:").pack()
        master_pw_entry = ttk.Entry(wizard, show="*")
        master_pw_entry.pack(pady=5)
        
        ttk.Label(wizard, text="Confirm Master Password:").pack()
        confirm_pw_entry = ttk.Entry(wizard, show="*")
        confirm_pw_entry.pack(pady=5)
        
        def complete_setup():
            master_pw = master_pw_entry.get()
            confirm_pw = confirm_pw_entry.get()
            
            if master_pw != confirm_pw:
                messagebox.showerror("Error", "Passwords don't match!")
                return
                
            strength = zxcvbn.zxcvbn(master_pw)
            if strength['score'] < 4:
                messagebox.showerror("Weak Password", 
                    "Master password is too weak!\n" +
                    "\n".join(strength['feedback']['suggestions']))
                return
                
            self.manager.salt = os.urandom(16)
            self.manager.master_password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                master_pw.encode(),
                self.manager.salt,
                100000
            ).hex()
            
            # Initialize empty vault
            self.manager.save_passwords([])
            self.manager.save_config()
            wizard.destroy()
            messagebox.showinfo("Success", "Master password set successfully!")
            
        ttk.Button(wizard, text="Complete Setup", command=complete_setup).pack(pady=20)
        
    def refresh_vault(self):
        """Refresh password vault display"""
        if not self.manager.authenticate():
            messagebox.showerror("Authentication Failed", "Incorrect master password")
            return
            
        self.vault_tree.delete(*self.vault_tree.get_children())
        passwords = self.manager.load_passwords()
        
        for pwd in passwords:
            strength = pwd.get('strength', {}).get('score', 0)
            self.vault_tree.insert("", "end", values=(
                pwd['service'],
                pwd['username'],
                f"{strength}/4"
            ))
            
    def add_password_entry(self):
        """Add new password entry"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Password Entry")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Service:").pack(pady=(10, 0))
        service_entry = ttk.Entry(dialog)
        service_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Username:").pack(pady=(10, 0))
        username_entry = ttk.Entry(dialog)
        username_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Password:").pack(pady=(10, 0))
        password_entry = ttk.Entry(dialog, show="*")
        password_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Notes:").pack(pady=(10, 0))
        notes_entry = tk.Text(dialog, height=4)
        notes_entry.pack(fill='x', padx=10)
        
        def generate_password():
            password = self.manager.generate_password()
            password_entry.delete(0, 'end')
            password_entry.insert(0, password)
            
        ttk.Button(dialog, text="Generate Password", command=generate_password).pack(pady=5)
        
        def save_entry():
            service = service_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            notes = notes_entry.get("1.0", "end-1c")
            
            if not service or not password:
                messagebox.showerror("Error", "Service and password are required!")
                return
                
            passwords = self.manager.load_passwords()
            passwords.append({
                'service': service,
                'username': username,
                'password': password,
                'notes': notes,
                'strength': self.manager.evaluate_password_strength(password)
            })
            
            self.manager.save_passwords(passwords)
            self.refresh_vault()
            dialog.destroy()
            
        ttk.Button(dialog, text="Save", command=save_entry).pack(pady=10)
        
    def edit_password_entry(self):
        """Edit selected password entry"""
        selected = self.vault_tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an entry to edit")
            return
            
        item = self.vault_tree.item(selected[0])
        service = item['values'][0]
        
        passwords = self.manager.load_passwords()
        entry = next((p for p in passwords if p['service'] == service), None)
        
        if not entry:
            messagebox.showerror("Error", "Selected entry not found")
            return
            
        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Password Entry")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Service:").pack(pady=(10, 0))
        service_entry = ttk.Entry(dialog)
        service_entry.insert(0, entry['service'])
        service_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Username:").pack(pady=(10, 0))
        username_entry = ttk.Entry(dialog)
        username_entry.insert(0, entry.get('username', ''))
        username_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Password:").pack(pady=(10, 0))
        password_entry = ttk.Entry(dialog, show="*")
        password_entry.insert(0, entry['password'])
        password_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Notes:").pack(pady=(10, 0))
        notes_entry = tk.Text(dialog, height=4)
        notes_entry.insert("1.0", entry.get('notes', ''))
        notes_entry.pack(fill='x', padx=10)
        
        def generate_password():
            password = self.manager.generate_password()
            password_entry.delete(0, 'end')
            password_entry.insert(0, password)
            
        ttk.Button(dialog, text="Generate Password", command=generate_password).pack(pady=5)
        
        def save_entry():
            service = service_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            notes = notes_entry.get("1.0", "end-1c")
            
            if not service or not password:
                messagebox.showerror("Error", "Service and password are required!")
                return
                
            # Update the entry
            entry.update({
                'service': service,
                'username': username,
                'password': password,
                'notes': notes,
                'strength': self.manager.evaluate_password_strength(password)
            })
            
            self.manager.save_passwords(passwords)
            self.refresh_vault()
            dialog.destroy()
            
        ttk.Button(dialog, text="Save", command=save_entry).pack(pady=10)
        
    def delete_password_entry(self):
        """Delete selected password entry"""
        selected = self.vault_tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an entry to delete")
            return
            
        if not messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?"):
            return
            
        item = self.vault_tree.item(selected[0])
        service = item['values'][0]
        
        passwords = self.manager.load_passwords()
        passwords = [p for p in passwords if p['service'] != service]
        
        self.manager.save_passwords(passwords)
        self.refresh_vault()
        
    def show_password(self):
        """Show selected password"""
        selected = self.vault_tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an entry")
            return
            
        item = self.vault_tree.item(selected[0])
        service = item['values'][0]
        
        passwords = self.manager.load_passwords()
        entry = next((p for p in passwords if p['service'] == service), None)
        
        if not entry:
            messagebox.showerror("Error", "Selected entry not found")
            return
            
        # Show password in a dialog with copy button
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Password for {service}")
        dialog.geometry("400x200")
        
        ttk.Label(dialog, text=f"Service: {entry['service']}").pack(pady=(10, 0))
        ttk.Label(dialog, text=f"Username: {entry.get('username', '')}").pack()
        
        ttk.Label(dialog, text="Password:").pack(pady=(10, 0))
        password_entry = ttk.Entry(dialog, font=('Courier', 12), justify='center')
        password_entry.insert(0, entry['password'])
        password_entry.pack(fill='x', padx=10)
        
        if entry.get('notes'):
            ttk.Label(dialog, text="Notes:").pack(pady=(10, 0))
            notes_text = tk.Text(dialog, height=4, wrap='word')
            notes_text.insert("1.0", entry['notes'])
            notes_text.config(state='disabled')
            notes_text.pack(fill='x', padx=10)
            
        def copy_password():
            self.root.clipboard_clear()
            self.root.clipboard_append(entry['password'])
            
        ttk.Button(dialog, text="Copy Password", command=copy_password).pack(pady=10)
        
    def generate_password(self):
        """Generate password based on current settings"""
        policy = {
            'length': self.length_var.get(),
            'use_upper': self.upper_var.get(),
            'use_lower': self.lower_var.get(),
            'use_digits': self.digits_var.get(),
            'use_special': self.special_var.get(),
            'avoid_ambiguous': self.ambiguous_var.get(),
            'min_entropy': 80
        }
        
        password = self.manager.generate_password(policy)
        self.password_var.set(password)
        
        # Update strength meter
        strength = zxcvbn.zxcvbn(password)
        self.strength_meter['value'] = strength['score']
        self.strength_label.config(text=f"{strength['score']}/4")
        
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard")
            
    def save_generated_password(self):
        """Save generated password to vault"""
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("No Password", "Generate a password first")
            return
            
        dialog = tk.Toplevel(self.root)
        dialog.title("Save Password")
        dialog.geometry("300x200")
        
        ttk.Label(dialog, text="Service:").pack(pady=(10, 0))
        service_entry = ttk.Entry(dialog)
        service_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Username:").pack(pady=(10, 0))
        username_entry = ttk.Entry(dialog)
        username_entry.pack(fill='x', padx=10)
        
        def save_entry():
            service = service_entry.get()
            username = username_entry.get()
            
            if not service:
                messagebox.showerror("Error", "Service is required!")
                return
                
            passwords = self.manager.load_passwords()
            passwords.append({
                'service': service,
                'username': username,
                'password': password,
                'strength': zxcvbn.zxcvbn(password)
            })
            
            self.manager.save_passwords(passwords)
            self.refresh_vault()
            dialog.destroy()
            messagebox.showinfo("Saved", "Password saved to vault")
            
        ttk.Button(dialog, text="Save", command=save_entry).pack(pady=10)
        
    def check_breaches(self):
        """Check if generated password has been breached"""
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("No Password", "Generate a password first")
            return
            
        def do_check():
            is_breached, _ = self.manager.check_breaches(password)
            self.root.after(0, lambda: messagebox.showinfo(
                "Breach Check", 
                "Password has been breached!" if is_breached else "No breaches found"
            ))
            
        threading.Thread(target=do_check).start()
        
    def update_totp_codes(self):
        """Update TOTP codes and timer"""
        # TODO: Implement TOTP code updates
        self.root.after(1000, self.update_totp_codes)
        
    def add_totp_entry(self):
        """Add new TOTP entry"""
        # TODO: Implement TOTP entry addition
        pass
        
    def delete_totp_entry(self):
        """Delete selected TOTP entry"""
        # TODO: Implement TOTP entry deletion
        pass
        
    def show_qr_code(self):
        """Show QR code for selected TOTP entry"""
        # TODO: Implement QR code display
        pass
        
    def copy_totp_code(self):
        """Copy current TOTP code to clipboard"""
        # TODO: Implement TOTP code copying
        pass
        
    def change_master_password(self):
        """Change master password"""
        if not self.manager.authenticate():
            messagebox.showerror("Authentication Failed", "Incorrect master password")
            return
            
        dialog = tk.Toplevel(self.root)
        dialog.title("Change Master Password")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="Current Master Password:").pack(pady=(10, 0))
        current_pw_entry = ttk.Entry(dialog, show="*")
        current_pw_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="New Master Password:").pack(pady=(10, 0))
        new_pw_entry = ttk.Entry(dialog, show="*")
        new_pw_entry.pack(fill='x', padx=10)
        
        ttk.Label(dialog, text="Confirm New Master Password:").pack(pady=(10, 0))
        confirm_pw_entry = ttk.Entry(dialog, show="*")
        confirm_pw_entry.pack(fill='x', padx=10)
        
        def do_change():
            current_pw = current_pw_entry.get()
            new_pw = new_pw_entry.get()
            confirm_pw = confirm_pw_entry.get()
            
            if new_pw != confirm_pw:
                messagebox.showerror("Error", "New passwords don't match!")
                return
                
            # Verify current password
            attempt_hash = hashlib.pbkdf2_hmac(
                'sha256',
                current_pw.encode(),
                self.manager.salt,
                100000
            ).hex()
            
            if not hmac.compare_digest(attempt_hash, self.manager.master_password_hash):
                messagebox.showerror("Error", "Current password is incorrect!")
                return
                
            # Check strength
            strength = zxcvbn.zxcvbn(new_pw)
            if strength['score'] < 4:
                messagebox.showerror("Weak Password", 
                    "New password is too weak!\n" +
                    "\n".join(strength['feedback']['suggestions']))
                return
                
            # Re-encrypt all passwords with new key
            old_salt = self.manager.salt
            old_key = self.manager.derive_key(current_pw, old_salt)
            
            passwords = self.manager.load_passwords()
            
            # Change salt and hash
            self.manager.salt = os.urandom(16)
            self.manager.master_password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                new_pw.encode(),
                self.manager.salt,
                100000
            ).hex()
            
            # Save with new key
            self.manager.save_passwords(passwords)
            self.manager.save_config()
            
            dialog.destroy()
            messagebox.showinfo("Success", "Master password changed successfully!")
            
        ttk.Button(dialog, text="Change Password", command=do_change).pack(pady=10)
        
    def save_api_key(self):
        """Save HIBP API key"""
        self.manager.breach_api_key = self.api_key_var.get()
        self.manager.save_config()
        messagebox.showinfo("Saved", "API key saved")
        
    def save_default_policy(self):
        """Save current generator settings as default policy"""
        self.manager.default_policy = {
            'length': self.length_var.get(),
            'use_upper': self.upper_var.get(),
            'use_lower': self.lower_var.get(),
            'use_digits': self.digits_var.get(),
            'use_special': self.special_var.get(),
            'avoid_ambiguous': self.ambiguous_var.get(),
            'min_entropy': 80
        }
        self.manager.save_config()
        messagebox.showinfo("Saved", "Default policy updated")
        
    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    manager = AdvancedPasswordManager()
    app = PasswordManagerGUI(manager)
    app.run()