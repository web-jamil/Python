# --- Python Dictionaries: All About Accessing Elements in Code ---

# Dictionaries store data as key-value pairs, and accessing these values
# by their unique keys is one of their primary uses.

# Let's start with a sample dictionary for demonstration.
user_data = {
    "username": "coder_gal",
    "user_id": 12345,
    "email": "coder.gal@example.com",
    "is_active": True,
    "roles": ["admin", "editor"],
    "last_login": "2025-06-03 10:30:00",
    "preferences": {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    },
    "metadata": None # A key with a None value
}

print("--- 1. Accessing Elements using Square Brackets `[]` ---")

# 1.1 Basic Access: Retrieving a value by its key
# Syntax: dictionary[key]
print(f"Username: {user_data['username']}")
print(f"User ID: {user_data['user_id']}")
print(f"Is Active: {user_data['is_active']}")

# 1.2 Accessing values that are lists or other dictionaries (nested access)
print(f"First role: {user_data['roles'][0]}")
print(f"User's preferred theme: {user_data['preferences']['theme']}")
print(f"User's notification setting: {user_data['preferences']['notifications']}")

# 1.3 What happens if the key does NOT exist? (KeyError)
# Attempting to access a key that is not in the dictionary using `[]`
# will raise a KeyError. This is important to handle in your code.
try:
    print(user_data['address'])
except KeyError as e:
    print(f"Error: Attempted to access non-existent key 'address'. Details: {e}")

try:
    print(user_data['preferences']['font_size'])
except KeyError as e:
    print(f"Error: Attempted to access non-existent nested key 'font_size'. Details: {e}")


print("\n--- 2. Accessing Elements using the `get()` method ---")

# The `get()` method is a safer way to access dictionary values
# because it does not raise a KeyError if the key is not found.

# 2.1 Basic usage: Key exists
# Syntax: dictionary.get(key)
print(f"Email (using get()): {user_data.get('email')}")

# 2.2 Key does NOT exist: Returns `None` by default
# This is often preferred in situations where a missing key is not an error,
# but rather an indication that the data is optional.
print(f"Phone (using get(), key not present): {user_data.get('phone')}") # Output: None

# 2.3 Key does NOT exist: Providing a default value
# Syntax: dictionary.get(key, default_value)
# This is very useful for providing fallback values.
print(f"Address (using get() with default): {user_data.get('address', 'Not provided')}")
print(f"Subscription status (using get() with default): {user_data.get('subscription', False)}")

# 2.4 `get()` with a key whose value is `None`
# `get()` correctly returns `None` if the key exists and its value is `None`.
print(f"Metadata (using get(), value is None): {user_data.get('metadata')}")

# 2.5 `get()` vs. `[]` - When to use which?
# - Use `[]` when you are absolutely sure the key exists, and its absence
#   should be treated as an error (e.g., critical configuration parameters).
# - Use `get()` when the key might be optional, and you want to handle its absence
#   gracefully (e.g., user preferences, optional fields in data).


print("\n--- 3. Checking for Key Existence (`in` operator) ---")

# Before accessing a key, especially with `[]`, it's good practice to check
# if the key exists to prevent `KeyError`.

# 3.1 Using the `in` operator
# Syntax: key in dictionary
print(f"Is 'username' in user_data? {'username' in user_data}") # True
print(f"Is 'password' in user_data? {'password' in user_data}") # False

# 3.2 Using `if key in dictionary:` for safe access
if 'email' in user_data:
    print(f"Email found: {user_data['email']}")
else:
    print("Email not found.")

if 'phone' in user_data:
    print(f"Phone found: {user_data['phone']}")
else:
    print("Phone not found.")

# 3.3 Checking for existence in nested dictionaries
if 'preferences' in user_data and 'language' in user_data['preferences']:
    print(f"Preferred language: {user_data['preferences']['language']}")
else:
    print("Preferred language not found.")


print("\n--- 4. Accessing Keys, Values, and Items (View Objects) ---")

# Dictionaries provide methods to get "views" of their keys, values, or key-value pairs.
# These views are dynamic; they reflect changes made to the dictionary.

# 4.1 `keys()` method: Returns a view object of all keys
# Syntax: dictionary.keys()
all_keys = user_data.keys()
print(f"All keys: {all_keys}")
print(f"Type of all_keys: {type(all_keys)}") # <class 'dict_keys'>

# You can iterate over keys:
print("Iterating over keys:")
for key in user_data.keys():
    print(key, end=", ")
print()

# You can convert to a list if you need a static copy:
list_of_keys = list(user_data.keys())
print(f"List of keys: {list_of_keys}")

# 4.2 `values()` method: Returns a view object of all values
# Syntax: dictionary.values()
all_values = user_data.values()
print(f"All values: {all_values}")
print(f"Type of all_values: {type(all_values)}") # <class 'dict_values'>

# You can iterate over values:
print("Iterating over values:")
for value in user_data.values():
    print(value, end=", ")
print()

# You can convert to a list:
list_of_values = list(user_data.values())
print(f"List of values: {list_of_values}")

# 4.3 `items()` method: Returns a view object of all key-value pairs (as tuples)
# Syntax: dictionary.items()
all_items = user_data.items()
print(f"All items: {all_items}")
print(f"Type of all_items: {type(all_items)}") # <class 'dict_items'>

# This is the most common way to iterate when you need both key and value:
print("Iterating over items:")
for key, value in user_data.items():
    print(f"Key: {key}, Value: {value}")


print("\n--- 5. Using `setdefault()` for Accessing or Setting Default ---")

# The `setdefault()` method is a powerful way to access a value,
# and if the key doesn't exist, it inserts the key with a default value
# and returns that default value.

# 5.1 Key exists: Returns the existing value, no change to dictionary
theme = user_data.setdefault('theme', 'light') # 'theme' is not a top-level key
# Ah, 'theme' is nested. Let's use a simpler example.
config = {'debug': True, 'log_level': 'INFO'}
print(f"Initial config: {config}")

# Key 'debug' exists, so its value is returned
debug_setting = config.setdefault('debug', False)
print(f"Debug setting (key existed): {debug_setting}")
print(f"Config after setdefault (no change): {config}")

# 5.2 Key does NOT exist: Inserts the key with default value and returns it
port_setting = config.setdefault('port', 8080)
print(f"Port setting (key added): {port_setting}")
print(f"Config after setdefault (key added): {config}")

# 5.3 `setdefault()` for nested structures
# This is particularly useful when you want to ensure a nested dictionary or list exists
# before trying to add to it.
user_data_new = {
    "name": "New User",
    "activity": [] # Initialize with an empty list
}

# Ensure 'activity' key exists and is a list, then append to it
user_data_new.setdefault('activity', []).append("logged_in")
user_data_new.setdefault('activity', []).append("viewed_profile")
print(f"User activity: {user_data_new['activity']}")

# If you tried to do this without setdefault or checking:
# user_data_new['activity'].append("logged_in") # Would fail if 'activity' was missing


print("\n--- 6. Iterating Safely and Efficiently ---")

# When iterating and potentially modifying a dictionary, be careful.
# It's generally unsafe to modify a dictionary while iterating over it directly.
# Iterate over a copy of keys or items if you plan to delete/add elements.

# Safe iteration for deletion
data_to_clean = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"Original data to clean: {data_to_clean}")
keys_to_delete = []
for key, value in data_to_clean.items():
    if value % 2 == 0:
        keys_to_delete.append(key)

for key in keys_to_delete:
    del data_to_clean[key]
print(f"Data after cleaning even values: {data_to_clean}")

# Or using dictionary comprehension for creating a new filtered dictionary:
original_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_data = {key: value for key, value in original_data.items() if value % 2 != 0}
print(f"Filtered data (new dict): {filtered_data}")