# The 'string' module in Python provides a collection of useful string constants.
# It was more commonly used in older Python versions (Python 2.x) for string
# manipulation functions that are now primarily available as methods of string objects.
# In modern Python (Python 3.x), it's mainly used for its constants.

# --- 1. Constants provided by the 'string' module ---

import string

# string.ascii_lowercase: All lowercase ASCII letters
print(f"string.ascii_lowercase: {string.ascii_lowercase}")

# string.ascii_uppercase: All uppercase ASCII letters
print(f"string.ascii_uppercase: {string.ascii_uppercase}")

# string.ascii_letters: Concatenation of ascii_lowercase and ascii_uppercase
print(f"string.ascii_letters: {string.ascii_letters}")

# string.digits: The string '0123456789'
print(f"string.digits: {string.digits}")

# string.hexdigits: The string '0123456789abcdefABCDEF'
print(f"string.hexdigits: {string.hexdigits}")

# string.octdigits: The string '01234567'
print(f"string.octdigits: {string.octdigits}")

# string.punctuation: String of ASCII characters which are considered punctuation characters
print(f"string.punctuation: {string.punctuation}")

# string.printable: String of characters which are considered printable (digits, letters, punctuation, whitespace)
print(f"string.printable: {string.printable}")

# string.whitespace: A string containing all ASCII whitespace characters (space, tab, linefeed, return, formfeed, vertical tab)
print(f"string.whitespace: {string.whitespace.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')}")

# --- 2. Template Strings (string.Template) ---
# Template Strings provide a simpler syntax for string interpolation,
# especially useful when values are user-supplied and might contain
# problematic characters for f-strings or str.format().

from string import Template

# Basic usage
s = Template('$who likes $what')
print(f"\nTemplate string basic usage: {s.substitute(who='John', what='Python')}")

# Using a dictionary for values
data = {'who': 'Jane', 'what': 'reading'}
print(f"Template string with dictionary: {s.substitute(data)}")

# Handling missing placeholders (KeyError if not safe_substitute)
try:
    s = Template('The color is $color and size is $size')
    s.substitute(color='red') # Missing 'size' will raise KeyError
except KeyError as e:
    print(f"Template string KeyError: {e}")

# safe_substitute() does not raise an error for missing placeholders;
# instead, it leaves the placeholder in the string.
s = Template('The color is $color and size is $size')
print(f"Template string safe_substitute: {s.safe_substitute(color='blue')}")

# Escaping the dollar sign
s = Template('$$ dollar sign, not a variable')
print(f"Template string escaping dollar sign: {s.substitute()}")

# --- 3. Old String Functions (less common in modern Python) ---
# Historically, the `string` module contained functions like `capwords`,
# `maketrans`, and `translate`. In Python 3, `maketrans` and `translate`
# are primarily methods of string objects. `capwords` is still available
# but `str.title()` often suffices.

# string.capwords(): Capitalize words in a string.
# (Note: str.title() is often preferred for simpler cases)
text = "hello world, how are you?"
print(f"\nstring.capwords: {string.capwords(text)}")
print(f"str.title(): {text.title()}") # Differs slightly (e.g., apostrophes)

# Demonstration of str.maketrans and str.translate (more common than string.maketrans/translate)
# creating a translation table
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

my_string = "This is a string with vowels."
translated_string = my_string.translate(trantab)
print(f"Original string: {my_string}")
print(f"Translated string (vowels to digits): {translated_string}")

# Removing characters using translate
# To remove characters, map them to None
remove_chars_table = str.maketrans('', '', 'abc') # third argument is chars to delete
new_string = "abracadabra".translate(remove_chars_table)
print(f"String with 'a', 'b', 'c' removed: {new_string}")





import string

# --- Constants provided by the 'string' module ---
# These are pre-defined strings that are useful for various string operations,
# especially when you need to categorize or validate characters.

print("--- string.ascii_lowercase ---")
# Contains all lowercase ASCII letters.
# Equivalent to 'abcdefghijklmnopqrstuvwxyz'.
print(f"Value: '{string.ascii_lowercase}'")
print(f"Length: {len(string.ascii_lowercase)}")
print("-" * 30)

print("--- string.ascii_uppercase ---")
# Contains all uppercase ASCII letters.
# Equivalent to 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
print(f"Value: '{string.ascii_uppercase}'")
print(f"Length: {len(string.ascii_uppercase)}")
print("-" * 30)

print("--- string.ascii_letters ---")
# Concatenation of string.ascii_lowercase and string.ascii_uppercase.
# Equivalent to 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
print(f"Value: '{string.ascii_letters}'")
print(f"Length: {len(string.ascii_letters)}")
print("-" * 30)

print("--- string.digits ---")
# Contains the string '0123456789'.
# Useful for checking if a character is a digit.
print(f"Value: '{string.digits}'")
print(f"Length: {len(string.digits)}")
print("-" * 30)

print("--- string.hexdigits ---")
# Contains the string '0123456789abcdefABCDEF'.
# Represents all valid hexadecimal digits.
print(f"Value: '{string.hexdigits}'")
print(f"Length: {len(string.hexdigits)}")
print("-" * 30)

print("--- string.octdigits ---")
# Contains the string '01234567'.
# Represents all valid octal digits.
print(f"Value: '{string.octdigits}'")
print(f"Length: {len(string.octdigits)}")
print("-" * 30)

print("--- string.punctuation ---")
# Contains ASCII characters that are considered punctuation characters.
# The exact set can vary slightly depending on the locale, but for ASCII,
# it generally includes symbols like !, ", #, $, %, &, ', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, ~.
print(f"Value: '{string.punctuation}'")
print(f"Length: {len(string.punctuation)}")
print("-" * 30)

print("--- string.printable ---")
# Contains a string of characters which are considered printable.
# This includes digits, letters, punctuation, and whitespace.
# It excludes non-printable control characters.
# For demonstration, we replace special whitespace chars for clear output.
print(f"Value (first 50 chars): '{string.printable[:50].replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')}'...")
print(f"Length: {len(string.printable)}")
print("-" * 30)

print("--- string.whitespace ---")
# Contains all ASCII whitespace characters.
# This includes:
# - Space (' ')
# - Tab ('\t')
# - Linefeed ('\n')
# - Return ('\r')
# - Formfeed ('\f')
# - Vertical tab ('\v')
# For clear output, we replace special characters.
print(f"Value: '{string.whitespace.replace(' ', '[SPACE]').replace('\t', '[TAB]').replace('\n', '[LF]').replace('\r', '[CR]').replace('\f', '[FF]').replace('\v', '[VT]')}'")
print(f"Length: {len(string.whitespace)}")
print("-" * 30)


# --- Practical Use Cases ---

# Example 1: Checking if a character is an uppercase letter
char = 'A'
if char in string.ascii_uppercase:
    print(f"'{char}' is an uppercase letter.")

# Example 2: Filtering out non-digit characters from a string
phone_number = "123-456-7890 (ext. 12)"
digits_only = "".join(c for c in phone_number if c in string.digits)
print(f"Original: '{phone_number}', Digits only: '{digits_only}'")

# Example 3: Validating a password to contain at least one digit and one punctuation
password = "MyStrongPassword123!"
has_digit = any(c in string.digits for c in password)
has_punctuation = any(c in string.punctuation for c in password)
if has_digit and has_punctuation:
    print(f"Password '{password}' has digits and punctuation.")

# Example 4: Creating a random string of a specific type (e.g., lowercase letters and digits)
import random
random_chars = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
print(f"Random string (lowercase + digits): {random_chars}")



# The 'string.Template' class provides a simpler way to perform string substitutions.
# It is particularly useful when dealing with user-supplied strings, as it does not
# support arbitrary Python expressions and is therefore safer than f-strings or
# str.format() when the template or substitution values come from untrusted sources.

from string import Template

print("--- 1. Basic Substitution ---")
# Placeholders are indicated by a '$' followed by a valid Python identifier.
# Or, if the identifier is immediately followed by more alphanumeric characters,
# it must be enclosed in curly braces: ${identifier}.

t = Template('Hello, $name! Welcome to $place.')
result_basic = t.substitute(name='Alice', place='Wonderland')
print(f"Basic substitution: {result_basic}")

# Using a dictionary for substitutions
data = {'name': 'Bob', 'place': 'the Matrix'}
result_dict = t.substitute(data)
print(f"Substitution with dictionary: {result_dict}")
print("-" * 30)

print("--- 2. Escaping the Dollar Sign ---")
# To include a literal dollar sign in the output, use '$$'.

t_escape = Template('The price is $amount$$ today.')
result_escape = t_escape.substitute(amount='10.50')
print(f"Escaping dollar sign: {result_escape}")
print("-" * 30)

print("--- 3. Using Curly Braces for Identifiers ---")
# Curly braces are necessary when the placeholder name is immediately followed
# by characters that are part of the word but not part of the identifier.

t_curly = Template('It is ${hour}AM and the temperature is ${temp}C.')
result_curly = t_curly.substitute(hour='09', temp='25')
print(f"Using curly braces: {result_curly}")
print("-" * 30)

print("--- 4. Handling Missing Placeholders with .substitute() ---")
# If a placeholder specified in the template is not provided in the substitution
# arguments (either keywords or dictionary), .substitute() will raise a KeyError.

t_missing = Template('Product: $item, Quantity: $qty, Price: $price.')
try:
    # 'price' is missing
    t_missing.substitute(item='Laptop', qty=2)
except KeyError as e:
    print(f"Error with missing placeholder (substitute): {e}")
print("-" * 30)

print("--- 5. Handling Missing Placeholders with .safe_substitute() ---")
# The .safe_substitute() method handles missing placeholders by leaving
# them unchanged in the output string. This is safer for user-supplied templates.

t_safe = Template('Product: $item, Quantity: $qty, Price: $price.')
result_safe = t_safe.safe_substitute(item='Keyboard', qty=5)
print(f"Safe substitution (missing 'price'): {result_safe}")

# If some placeholders are provided, they are substituted normally.
result_safe_partial = t_safe.safe_substitute(item='Mouse', price='15.99')
print(f"Safe substitution (missing 'qty'): {result_safe_partial}")
print("-" * 30)

print("--- 6. Custom Delimiter for Placeholders ---")
# You can customize the delimiter by overriding the 'delimiter' and 'idpattern'
# attributes in a subclass of Template. The 'idpattern' is a regular expression
# that defines what constitutes a valid identifier.

class MyTemplate(Template):
    delimiter = '%'  # Change from '$' to '%'

class CustomIdTemplate(Template):
    delimiter = '%'
    # Allow identifiers to start with a number (not recommended for general use, just for demo)
    idpattern = r'[a-zA-Z0-9_]+'

t_custom_delimiter = MyTemplate('Hello, %name! Your %city is lovely.')
result_custom = t_custom_delimiter.substitute(name='Charlie', city='New York')
print(f"Custom delimiter (%): {result_custom}")

t_custom_id = CustomIdTemplate('Value is %123test.')
result_custom_id = t_custom_id.substitute(**{'123test': 'Success!'})
print(f"Custom ID pattern (starts with number): {result_custom_id}")
print("-" * 30)

print("--- 7. Common Use Cases ---")

# a) Generating dynamic messages where parts might be optional or unknown
message_template = Template("Reminder: $event at $time in $location. $notes_optional")
print(f"Event 1: {message_template.safe_substitute(event='Meeting', time='10 AM', location='Office', notes_optional='Bring presentation.')}")
print(f"Event 2: {message_template.safe_substitute(event='Lunch', time='1 PM', location='Cafeteria')}") # notes_optional is left as is

# b) Safely constructing SQL queries or shell commands (though prepared statements are usually better for SQL)
# This is a conceptual example; always prefer proper parameter binding for SQL to prevent SQL injection.
# query_template = Template("SELECT * FROM users WHERE username = '$username'")
# user_input = "admin' OR '1'='1" # Malicious input
# print(f"Potentially unsafe query: {query_template.substitute(username=user_input)}")

# c) Simple templating for configuration files or basic text generation
config_template = Template("""
[SERVER]
host = $hostname
port = $port
debug = $debug_mode
""")
config_data = {
    'hostname': 'localhost',
    'port': '8080',
    'debug_mode': 'True'
}
print("\nGenerated Configuration:")
print(config_template.substitute(config_data))
print("-" * 30)



import string
import random
import re # Often used with string manipulation, though not directly part of the string module

print("--- 6. Character Set Manipulation and Filtering ---")

# a) Filtering out non-alphanumeric characters
def filter_alphanumeric(text):
    return ''.join(c for c in text if c in string.ascii_letters or c in string.digits)

mixed_string = "Hello World! 123 @#$ Bye."
filtered = filter_alphanumeric(mixed_string)
print(f"Original: '{mixed_string}'")
print(f"Alphanumeric only: '{filtered}'")

# b) Creating a custom character set for validation
# Imagine a system only allows specific symbols
allowed_symbols = string.ascii_letters + string.digits + "_-." # Alphanumeric plus underscore, hyphen, dot

def is_valid_username(username):
    return all(char in allowed_symbols for char in username)

print(f"Is 'my_user.name123' valid? {is_valid_username('my_user.name123')}")
print(f"Is 'bad!name' valid? {is_valid_username('bad!name')}")
print("-" * 30)

print("--- 7. Advanced Password Generation (with string module constants) ---")

# Ensure complexity requirements are met using string constants
def generate_complex_password(length=14):
    if length < 8:
        raise ValueError("Password length must be at least 8 for complexity.")

    # Define character pools using string constants
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    all_chars = lower + upper + digits + punctuation

    password = []
    # Ensure at least one of each required character type
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(digits))
    password.append(random.choice(punctuation))

    # Fill the rest of the password length randomly
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    random.shuffle(password) # Shuffle to randomize the position of mandatory characters
    return "".join(password)

print(f"Complex Password (14 chars): {generate_complex_password()}")
print(f"Complex Password (20 chars): {generate_complex_password(20)}")
try:
    generate_complex_password(5)
except ValueError as e:
    print(f"Error generating short password: {e}")
print("-" * 30)


print("--- 8. Template Strings for Code Generation/Configuration Files ---")

# Imagine generating a Python script snippet or a configuration file
script_template = Template("""
# auto_generated_script.py
import os
import sys

def run_task_$task_id():
    print("Running task $task_id...")
    # Add custom logic here for task $task_id
    # Log directory: $log_dir
    if not os.path.exists('$log_dir'):
        os.makedirs('$log_dir')
    with open(os.path.join('$log_dir', 'task_$task_id.log'), 'w') as f:
        f.write("Task $task_id started successfully.\\n")

if __name__ == "__main__":
    run_task_$task_id()
""")

task_config = {
    'task_id': '42',
    'log_dir': '/var/log/my_app_tasks'
}

generated_script = script_template.substitute(task_config)
print("\n--- Generated Python Script Snippet ---")
print(generated_script)

# Save to a dummy file (optional)
# with open("auto_generated_script_42.py", "w") as f:
#     f.write(generated_script)
# print("\n(Script saved to auto_generated_script_42.py)")
print("-" * 30)

print("--- 9. Using string.capwords with Specific Scenarios ---")

# How capwords handles numbers and hyphens (compared to str.title())
text_hyphenated = "north-east-south-west"
text_with_numbers = "the year 2024 is awesome"

print(f"Original: '{text_hyphenated}'")
print(f"string.capwords: '{string.capwords(text_hyphenated)}'")
print(f"str.title(): '{text_hyphenated.title()}'") # Note: title() doesn't split on hyphens by default

print(f"\nOriginal: '{text_with_numbers}'")
print(f"string.capwords: '{string.capwords(text_with_numbers)}'")
print(f"str.title(): '{text_with_numbers.title()}'") # Note: title() capitalizes 'Is' as 'Is', capwords as 'is' if not a new word

# capwords implicitly cleans up multiple spaces between words
text_messy = "  hello   world   how are you  "
print(f"\nOriginal messy: '{text_messy}'")
print(f"string.capwords(messy): '{string.capwords(text_messy)}'")
print("-" * 30)

print("--- 10. Simple Character-Based Encryption/Decryption (Concept) ---")

# This is a very basic example, NOT for security!
# Using str.maketrans and str.translate for a simple Caesar cipher-like shift.

def caesar_cipher_encrypt(text, shift):
    # Create shifted alphabet
    lower_shifted = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    upper_shifted = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]

    # Create translation table for lowercase and uppercase letters
    # map original letters to shifted letters
    trans_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        lower_shifted + upper_shifted
    )
    return text.translate(trans_table)

def caesar_cipher_decrypt(text, shift):
    # To decrypt, shift back by 26 - shift (for a 26-letter alphabet)
    return caesar_cipher_encrypt(text, 26 - (shift % 26))


original_message = "Hello, World! 123"
encrypted_message = caesar_cipher_encrypt(original_message, 3)
decrypted_message = caesar_cipher_decrypt(encrypted_message, 3)

print(f"Original: '{original_message}'")
print(f"Encrypted (shift 3): '{encrypted_message}'")
print(f"Decrypted: '{decrypted_message}'")
print("-" * 30)


import pyjokes
import json
import getpass
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import random
from colorama import Fore, Style, init
from abc import ABC, abstractmethod
import textwrap
import time

# Initialize colorama
init(autoreset=True)

class DatabaseManager:
    """Handles all JSON file operations"""
    def __init__(self):
        self.users_file = "users.json"
        self.joke_history_file = "joke_history.json"
        self.stats_file = "joke_stats.json"
        self.initialize_files()

    def initialize_files(self):
        """Create required files if they don't exist"""
        files = {
            self.users_file: {"admin": {"password": "admin123", "role": "admin"}},
            self.joke_history_file: {},
            self.stats_file: {"total_jokes_told": 0, "popular_jokes": {}}
        }

        for file, default_data in files.items():
            if not Path(file).exists():
                self.write_file(file, default_data)

    def read_file(self, filename):
        """Read JSON file"""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def write_file(self, filename, data):
        """Write to JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

class UserManager:
    """Handles user authentication and registration"""
    def __init__(self, db_manager):
        self.db = db_manager

    def register_user(self):
        """Register a new user"""
        username = input(Fore.CYAN + "Enter new username: " + Style.RESET_ALL)
        users = self.db.read_file(self.db.users_file)

        if username in users:
            print(Fore.RED + "Username already exists!")
            return None

        password = getpass.getpass(Fore.CYAN + "Enter password: " + Style.RESET_ALL)
        confirm = getpass.getpass(Fore.CYAN + "Confirm password: " + Style.RESET_ALL)

        if password != confirm:
            print(Fore.RED + "Passwords don't match!")
            return None

        users[username] = {
            "password": password, 
            "role": "user", 
            "created_at": str(datetime.now())
        }
        self.db.write_file(self.db.users_file, users)

        print(Fore.GREEN + "Registration successful!")
        return {"username": username, "role": "user"}

    def authenticate(self):
        """Authenticate existing user"""
        username = input(Fore.CYAN + "Username: " + Style.RESET_ALL)
        password = getpass.getpass(Fore.CYAN + "Password: " + Style.RESET_ALL)

        users = self.db.read_file(self.db.users_file)

        if username not in users or users[username]["password"] != password:
            print(Fore.RED + "Invalid credentials!")
            return None

        print(Fore.GREEN + f"\nWelcome back, {username}!")
        return {"username": username, "role": users[username]["role"]}
     
    def change_password(self, username):
        """Change password for existing user"""
        users = self.db.read_file(self.db.users_file)
        
        if username not in users:
            print(Fore.RED + "User not found!")
            return False

        current = getpass.getpass(Fore.CYAN + "Current password: " + Style.RESET_ALL)
        if users[username]["password"] != current:
            print(Fore.RED + "Incorrect current password!")
            return False

        new_pass = getpass.getpass(Fore.CYAN + "New password: " + Style.RESET_ALL)
        
        if new_pass == current:
            print(Fore.RED + "New password must be different from current password!")
            return False
            
        if len(new_pass) < 8:
            print(Fore.RED + "Password must be at least 8 characters!")
            return False

        confirm = getpass.getpass(Fore.CYAN + "Confirm new password: " + Style.RESET_ALL)

        if new_pass != confirm:
            print(Fore.RED + "Passwords don't match!")
            return False

        users[username]["password"] = new_pass
        users[username]["last_password_change"] = str(datetime.now())
        self.db.write_file(self.db.users_file, users)
        print(Fore.GREEN + "Password changed successfully!")
        return True

    def reset_password(self, admin_username):
        """Admin password reset for other users"""
        users = self.db.read_file(self.db.users_file)
        
        if users.get(admin_username, {}).get("role") != "admin":
            print(Fore.RED + "Admin privileges required!")
            return False

        target = input(Fore.CYAN + "Enter username to reset: " + Style.RESET_ALL)
        if target not in users:
            print(Fore.RED + "User not found!")
            return False

        new_pass = getpass.getpass(Fore.CYAN + f"New password for {target}: " + Style.RESET_ALL)
        
        if len(new_pass) < 8:
            print(Fore.RED + "Password must be at least 8 characters!")
            return False

        confirm = getpass.getpass(Fore.CYAN + "Confirm new password: " + Style.RESET_ALL)

        if new_pass != confirm:
            print(Fore.RED + "Passwords don't match!")
            return False

        users[target]["password"] = new_pass
        users[target]["last_password_change"] = str(datetime.now())
        users[target]["reset_by_admin"] = admin_username
        self.db.write_file(self.db.users_file, users)
        print(Fore.GREEN + f"Password for {target} reset successfully!")
        return True

class JokeTeller:
    """Core joke telling functionality"""
    SUPPORTED_LANGUAGES = ['en', 'de', 'es', 'fr', 'gl', 'eu']
    SUPPORTED_CATEGORIES = ['neutral', 'chuck', 'all']
    MAX_JOKE_LENGTH = 120  # For formatting

    def __init__(self, db_manager):
        self.db = db_manager

    def tell_joke(self, language='en', category='neutral'):
        """Get a joke with specified language and category"""
        try:
            joke = pyjokes.get_joke(language=language, category=category)
            return self._format_joke(joke)
        except Exception as e:
            print(Fore.YELLOW + f"Joke error: {str(e)}")
            return None

    def tell_multiple_jokes(self, count=1, language='en', category='neutral'):
        """Get multiple jokes"""
        jokes = []
        for _ in range(min(10, max(1, count))):
            joke = self.tell_joke(language, category)
            if joke:
                jokes.append(joke)
        return jokes

    def _format_joke(self, joke):
        """Format long jokes with text wrapping"""
        if len(joke) > self.MAX_JOKE_LENGTH:
            return textwrap.fill(joke, width=self.MAX_JOKE_LENGTH)
        return joke

class JokeHistoryManager:
    """Manages joke history and statistics"""
    def __init__(self, db_manager):
        self.db = db_manager

    def log_joke(self, username, joke, language, category, rating=None):
        """Record a joke in history"""
        history = self.db.read_file(self.db.joke_history_file)
        stats = self.db.read_file(self.db.stats_file)

        if username not in history:
            history[username] = []

        joke_entry = {
            "joke": joke,
            "language": language,
            "category": category,
            "timestamp": str(datetime.now()),
            "rating": rating
        }
        history[username].append(joke_entry)
        
        # Update statistics
        stats["total_jokes_told"] = stats.get("total_jokes_told", 0) + 1
        if joke in stats.get("popular_jokes", {}):
            stats["popular_jokes"][joke] += 1
        else:
            stats["popular_jokes"][joke] = 1

        self.db.write_file(self.db.joke_history_file, history)
        self.db.write_file(self.db.stats_file, stats)

    def get_user_history(self, username, limit=5):
        """Get user's joke history"""
        history = self.db.read_file(self.db.joke_history_file)
        user_history = history.get(username, [])
        return user_history[-limit:] if limit else user_history

    def get_user_favorite_language(self, username):
        """Determine user's preferred joke language"""
        history = self.db.read_file(self.db.joke_history_file)
        if username not in history or not history[username]:
            return None

        lang_counts = defaultdict(int)
        for entry in history[username]:
            lang_counts[entry["language"]] += 1

        return max(lang_counts.items(), key=lambda x: x[1])[0]

    def get_global_stats(self):
        """Get global joke statistics"""
        return self.db.read_file(self.db.stats_file)

class UserInterface(ABC):
    """Abstract base class for UI components"""
    @abstractmethod
    def display(self):
        pass

class MainMenu(UserInterface):
    """Main menu interface"""
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def display(self):
        print(Fore.BLUE + "\n=== JOKE TELLER GAME ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        while True:
            option = input(Fore.CYAN + "\nSelect option (1-3): " + Style.RESET_ALL)

            if option == '1':
                return self.user_manager.authenticate()
            elif option == '2':
                user = self.user_manager.register_user()
                if user:
                    return user
            elif option == '3':
                print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
                exit()
            else:
                print(Fore.RED + "Invalid option!" + Style.RESET_ALL)

class JokeMenu(UserInterface):
    """Joke telling menu"""
    def __init__(self, username, role, joke_teller, history_manager, user_manager):
        self.username = username
        self.role = role
        self.joke_teller = joke_teller
        self.history = history_manager
        self.user_manager = user_manager
        
    def display(self):
        while True:
            print(Fore.BLUE + "\nJOKE TELLER MENU")
            print("1. Random joke")
            print("2. Chuck Norris joke")
            print("3. Joke in specific language")
            print("4. Multiple jokes")
            print("5. Personalized joke")
            print("6. Rate last joke")
            print("7. View joke history")
            print("8. Change password")
            if self.role == "admin":
                print("9. Admin Panel")
            print("0. Exit")

            choice = input(Fore.CYAN + "\nEnter choice: " + Style.RESET_ALL)

            if choice == '1':
                self._handle_random_joke()
            elif choice == '2':
                self._handle_chuck_joke()
            elif choice == '3':
                self._handle_language_joke()
            elif choice == '4':
                self._handle_multiple_jokes()
            elif choice == '5':
                self._handle_personalized_joke()
            elif choice == '6':
                self._handle_rating()
            elif choice == '7':
                self._show_history()
            elif choice == '8':
                result = self._handle_password_change()
                if result == "logout":
                    return "logout"
            elif choice == '9' and self.role == "admin":
                AdminPanel(self.username, self.history, self.user_manager).display()
            elif choice == '0':
                print(Fore.YELLOW + "Thanks for playing!" + Style.RESET_ALL)
                return
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)

    def _handle_random_joke(self):
        joke = self.joke_teller.tell_joke()
        if joke:
            print(Fore.GREEN + f"\n{joke}")
            self.history.log_joke(self.username, joke, 'en', 'neutral')
        else:
            print(Fore.RED + "Failed to get joke!")

    def _handle_chuck_joke(self):
        joke = self.joke_teller.tell_joke(category='chuck')
        if joke:
            print(Fore.GREEN + f"\n{joke}")
            self.history.log_joke(self.username, joke, 'en', 'chuck')
        else:
            print(Fore.RED + "Failed to get Chuck joke!")

    def _handle_language_joke(self):
        lang = input(Fore.CYAN + f"Choose language ({'/'.join(JokeTeller.SUPPORTED_LANGUAGES)}): ")
        if lang in JokeTeller.SUPPORTED_LANGUAGES:
            joke = self.joke_teller.tell_joke(language=lang)
            if joke:
                print(Fore.GREEN + f"\n{joke}")
                self.history.log_joke(self.username, joke, lang, 'neutral')
            else:
                print(Fore.RED + "Failed to get joke in this language!")
        else:
            print(Fore.RED + "Unsupported language!")

    def _handle_multiple_jokes(self):
        try:
            count = int(input(Fore.CYAN + "How many jokes? (1-10): "))
            count = max(1, min(10, count))
            jokes = self.joke_teller.tell_multiple_jokes(count)
            for i, joke in enumerate(jokes, 1):
                print(Fore.GREEN + f"\n{i}. {joke}")
                self.history.log_joke(self.username, joke, 'en', 'neutral')
        except ValueError:
            print(Fore.RED + "Invalid number!")

    def _handle_personalized_joke(self):
        fav_lang = self.history.get_user_favorite_language(self.username) or 'en'
        joke = self.joke_teller.tell_joke(language=fav_lang)
        if joke:
            print(Fore.GREEN + f"\nPersonalized joke ({fav_lang}):\n{joke}")
            self.history.log_joke(self.username, joke, fav_lang, 'neutral')
        else:
            print(Fore.RED + "Failed to get personalized joke!")

    def _handle_rating(self):
        history = self.history.get_user_history(self.username, 1)
        if not history:
            print(Fore.YELLOW + "No jokes to rate yet!")
            return

        last_joke = history[0]
        print(Fore.CYAN + f"\nLast joke: {last_joke['joke']}")

        try:
            rating = int(input(Fore.CYAN + "Rate (1-5): "))
            if 1 <= rating <= 5:
                last_joke["rating"] = rating
                self.history.log_joke(
                    self.username,
                    last_joke["joke"],
                    last_joke["language"],
                    last_joke["category"],
                    rating
                )
                print(Fore.GREEN + "Thanks for rating!")
            else:
                print(Fore.RED + "Rating must be between 1-5!")
        except ValueError:
            print(Fore.RED + "Invalid input!")

    def _show_history(self):
        history = self.history.get_user_history(self.username, 5)
        if not history:
            print(Fore.YELLOW + "No joke history yet!")
            return

        print(Fore.MAGENTA + "\nYOUR RECENT JOKES:")
        for i, entry in enumerate(reversed(history), 1):
            print(f"\n{i}. {entry['joke']}")
            print(f"   Language: {entry['language']}, Category: {entry['category']}")
            print(f"   Date: {entry['timestamp'].split('.')[0]}")
            if entry.get('rating'):
                print(f"   Your rating: {entry['rating']}/5")

    def _handle_password_change(self):
        """Handle password change for current user"""
        if self.user_manager.change_password(self.username):
            print(Fore.GREEN + "Password changed successfully! Please login again.")
            return "logout"  # Signal to logout
        return None

class AdminPanel(UserInterface):
    """Admin control panel"""
    def __init__(self, username, history_manager, user_manager):
        self.username = username
        self.history = history_manager
        self.user_manager = user_manager

    def display(self):
        while True:
            print(Fore.MAGENTA + "\nADMIN PANEL")
            print("1. View all users")
            print("2. View joke history")
            print("3. View statistics")
            print("4. Reset user password")
            print("5. Back to main menu")

            choice = input(Fore.CYAN + "\nEnter choice (1-5): " + Style.RESET_ALL)

            if choice == '1':
                self._show_users()
            elif choice == '2':
                self._show_all_history()
            elif choice == '3':
                self._show_stats()
            elif choice == '4':
                self.user_manager.reset_password(self.username)
            elif choice == '5':
                return
            else:
                print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)

    def _show_users(self):
        db = DatabaseManager()
        users = db.read_file(db.users_file)
        print(Fore.YELLOW + "\nREGISTERED USERS:")
        for user, data in users.items():
            print(f"\nUsername: {user}")
            print(f"Role: {data['role']}")
            print(f"Created: {data.get('created_at', 'N/A')}")

    def _show_all_history(self):
        history = self.history.get_user_history(self.username, None)  # Get all
        if not history:
            print(Fore.YELLOW + "No joke history yet!")
            return

        print(Fore.YELLOW + "\nALL JOKE HISTORY:")
        for entry in history:
            print(f"\n- {entry['joke']}")
            print(f"  User: {self.username}, Language: {entry['language']}")
            print(f"  Date: {entry['timestamp'].split('.')[0]}")

    def _show_stats(self):
        stats = self.history.get_global_stats()
        print(Fore.YELLOW + "\nGLOBAL STATISTICS:")
        print(f"\nTotal jokes told: {stats.get('total_jokes_told', 0)}")
        
        if stats.get("popular_jokes"):
            top_joke = max(stats["popular_jokes"].items(), key=lambda x: x[1])
            print(f"\nMost popular joke (told {top_joke[1]} times):")
            print(f"{top_joke[0]}")

class JokeGame:
    """Main application controller"""
    def __init__(self):
        self.db = DatabaseManager()
        self.user_manager = UserManager(self.db)
        self.joke_teller = JokeTeller(self.db)
        self.history_manager = JokeHistoryManager(self.db)

    def run(self):
        """Run the application"""
        print(Fore.BLUE + "=== JOKE TELLER APPLICATION ===" + Style.RESET_ALL)

        while True:
            # Show main menu
            user_data = MainMenu(self.user_manager).display()
            
            if user_data:
                # Show joke menu for authenticated users
                result = JokeMenu(
                    user_data["username"],
                    user_data["role"],
                    self.joke_teller,
                    self.history_manager,
                    self.user_manager
                ).display()
                
                if result == "logout":
                    continue  # Force re-login after password change

if __name__ == "__main__":
    try:
        game = JokeGame()
        game.run()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProgram terminated by user")
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {str(e)}")