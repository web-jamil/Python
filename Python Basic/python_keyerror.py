# --- KeyError: All About in Code ---

# A KeyError is raised when you try to access a dictionary key that does not exist.
# It's one of the most common errors when working with dictionaries.

# --- 1. Basic KeyError: Accessing a Non-Existent Key ---
print("--- 1. Basic KeyError: Accessing a Non-Existent Key ---")

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing an existing key (OK)
print(f"Accessing existing key 'name': {my_dict['name']}")

# Attempting to access a key that does not exist (causes KeyError)
try:
    print(my_dict['country'])
except KeyError as e:
    print(f"Caught KeyError (expected): {e}")
    print("Reason: Key 'country' does not exist in the dictionary.")

print("-" * 50 + "\n")


# --- 2. KeyError when Modifying/Deleting Non-Existent Key ---
print("--- 2. KeyError when Modifying/Deleting Non-Existent Key ---")

# Attempting to assign to a non-existent key will *create* it, not raise an error.
my_dict['job'] = "Engineer"
print(f"After assigning to 'job': {my_dict}")

# Attempting to delete a non-existent key (causes KeyError)
try:
    del my_dict['zip_code']
except KeyError as e:
    print(f"Caught KeyError (expected): {e}")
    print("Reason: Key 'zip_code' does not exist in the dictionary and cannot be deleted.")

print("-" * 50 + "\n")


# --- 3. Preventing KeyError: Using `get()` Method ---
print("--- 3. Preventing KeyError: Using `get()` Method ---")

# The `get(key, default_value)` method is the safest way to access dictionary values
# if you're unsure if a key exists. It returns `None` or `default_value` if the key is not found.

existing_value = my_dict.get('name')
print(f"Using .get() for existing key 'name': {existing_value}")

non_existent_value_none = my_dict.get('country') # Default is None if key not found
print(f"Using .get() for non-existent key 'country' (default None): {non_existent_value_none}")

non_existent_value_default = my_dict.get('country', 'Unknown') # Provide a custom default
print(f"Using .get() for non-existent key 'country' (custom default): {non_existent_value_default}")

print("-" * 50 + "\n")


# --- 4. Preventing KeyError: Using `in` Operator ---
print("--- 4. Preventing KeyError: Using `in` Operator ---")

# The `in` operator checks for the existence of a key in a dictionary and returns a boolean.

if 'age' in my_dict:
    print(f"Key 'age' exists: {my_dict['age']}")
else:
    print("Key 'age' does not exist.")

if 'state' in my_dict:
    print(f"Key 'state' exists: {my_dict['state']}")
else:
    print("Key 'state' does not exist.")

# Combine with else to provide a default or alternative action
if 'zip_code' in my_dict:
    print(f"Zip code: {my_dict['zip_code']}")
else:
    print("Zip code not available.")

print("-" * 50 + "\n")


# --- 5. Preventing KeyError: Using `setdefault()` Method ---
print("--- 5. Preventing KeyError: Using `setdefault()` Method ---")

# `setdefault(key, default_value)` inserts the key with `default_value` if the key
# is not present, and returns the value (either the existing one or the newly set one).
# Useful for ensuring a key exists before using it.

user_settings = {'theme': 'dark'}

# Key 'language' does not exist, so it's added with default 'en'
current_lang = user_settings.setdefault('language', 'en')
print(f"Language after setdefault (new key): {current_lang}")
print(f"Updated settings: {user_settings}")

# Key 'theme' already exists, its value is returned, and it's not changed
current_theme = user_settings.setdefault('theme', 'light')
print(f"Theme after setdefault (existing key): {current_theme}")
print(f"Updated settings: {user_settings} (theme unchanged)")

print("-" * 50 + "\n")


# --- 6. KeyError in Loops and Iteration ---
print("--- 6. KeyError in Loops and Iteration ---")

# Iterating over dictionary keys directly using `for key in dict:`
# is safe because it only iterates over *existing* keys.
scores = {'math': 90, 'science': 85, 'english': 92}
print("Iterating over scores:")
for subject in scores:
    print(f"{subject}: {scores[subject]}")

# However, if you try to access a non-existent key *inside* the loop based on external data:
student_grades = {'Alice': {'math': 88, 'science': 92}, 'Bob': {'math': 75}}
students = ['Alice', 'Bob', 'Charlie'] # Charlie is not in student_grades

print("\nAccessing grades for students:")
for student in students:
    try:
        # This will cause a KeyError when student is 'Charlie'
        math_grade = student_grades[student]['math']
        print(f"{student}'s math grade: {math_grade}")
    except KeyError as e:
        print(f"Caught KeyError for student '{student}': {e}")
        print(f"Reason: Student '{student}' or their 'math' grade not found.")

print("-" * 50 + "\n")


# --- 7. KeyError with Nested Dictionaries ---
print("--- 7. KeyError with Nested Dictionaries ---")

nested_data = {
    "user": {
        "id": "abc123",
        "profile": {
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
    },
    "preferences": {}
}

# Accessing existing nested keys (OK)
print(f"User email: {nested_data['user']['profile']['email']}")

# Attempting to access a non-existent nested key
try:
    print(nested_data['user']['address']['street']) # 'address' does not exist under 'user'
except KeyError as e:
    print(f"Caught KeyError (expected, nested): {e}")
    print("Reason: Key 'address' does not exist in 'user' dictionary.")

try:
    print(nested_data['preferences']['notification_sound']) # 'notification_sound' does not exist
except KeyError as e:
    print(f"Caught KeyError (expected, nested): {e}")
    print("Reason: Key 'notification_sound' does not exist in 'preferences' dictionary.")


# Safer way to access nested keys using `get()` and chaining
# Note: `get()` chaining works well, but if an intermediate step returns `None`,
# trying to call `.get()` on `None` will raise an AttributeError.
# Always check intermediate results if there's a possibility of `None`.

user_profile = nested_data.get('user', {}).get('profile', {})
print(f"User profile (using chained .get()): {user_profile.get('name', 'N/A')}")

# If 'address' might be missing at 'user' level, or 'street' at 'address' level
address_info = nested_data.get('user', {}).get('address', {}) # .get('address', {}) ensures it's a dict or empty dict
street = address_info.get('street', 'Address Not Found')
print(f"User street (using chained .get() with checks): {street}")

print("-" * 50 + "\n")


# --- 8. KeyError when using `dict.keys()`, `dict.values()`, `dict.items()` ---
print("--- 8. KeyError when using `dict.keys()`, `dict.values()`, `dict.items()` ---")

# These methods return dictionary view objects, which are safe for iteration.
# The KeyError occurs if you try to use a key from an external source that's not in the view.

product_info = {'id': 'P001', 'name': 'Laptop', 'price': 1200}

# Iterating over keys view (safe)
print("Keys in product_info:")
for key in product_info.keys():
    print(key)

# Iterating over items view (safe)
print("\nItems in product_info:")
for key, value in product_info.items():
    print(f"{key}: {value}")

# Still, accessing a non-existent key using [] after getting a key list can fail
missing_key_list = ['id', 'name', 'stock']
print("\nAccessing using a list of keys (potential KeyError):")
for key in missing_key_list:
    try:
        print(f"{key}: {product_info[key]}")
    except KeyError as e:
        print(f"Caught KeyError for '{key}': {e}")

print("-" * 50 + "\n")


# --- 9. KeyError in Dictionary Comprehensions ---
print("--- 9. KeyError in Dictionary Comprehensions ---")

# If the source data for the comprehension is inconsistent, it can lead to KeyError.

list_of_dicts = [
    {'item': 'Apple', 'color': 'Red'},
    {'item': 'Banana', 'color': 'Yellow'},
    {'item': 'Grape'} # Missing 'color' key
]

try:
    # This will cause a KeyError for the 'Grape' dictionary
    item_colors = {d['item']: d['color'] for d in list_of_dicts}
    print(item_colors)
except KeyError as e:
    print(f"Caught KeyError in dict comprehension (expected): {e}")
    print("Reason: 'color' key was missing in one of the dictionaries.")

# Corrected comprehension using .get() to handle missing keys
item_colors_safe = {d['item']: d.get('color', 'Unknown') for d in list_of_dicts}
print(f"Corrected comprehension: {item_colors_safe}")

print("-" * 50 + "\n")

# --- 10. `collections.defaultdict` as an Alternative to Avoid KeyError ---
print("--- 10. `collections.defaultdict` as an Alternative ---")

# `defaultdict` allows you to specify a default factory function for missing keys.
# When a missing key is accessed, the default factory is called to provide a default value.
from collections import defaultdict

# Example: Counting occurrences of items
word_counts = defaultdict(int) # Default value for missing key is int() which is 0
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

for word in words:
    word_counts[word] += 1 # No need to check if word exists, int() provides initial 0
print(f"Word counts (defaultdict int): {word_counts}")

# Example: Grouping items into lists
grouped_items = defaultdict(list) # Default value for missing key is list() which is []
data_points = [('fruit', 'apple'), ('color', 'red'), ('fruit', 'banana'), ('color', 'blue')]

for category, value in data_points:
    grouped_items[category].append(value) # Appends to existing list or a new empty list
print(f"Grouped items (defaultdict list): {grouped_items}")

print("-" * 50 + "\n")

print("--- End of KeyError demonstration ---")



# --- KeyError: More Examples and Practice ---

# This section provides additional scenarios for KeyError, focusing on common pitfalls,
# practical applications, and more advanced ways to handle missing keys.

# --- 11. KeyError in Function Parameters (Keyword Arguments) ---
print("--- 11. KeyError in Function Parameters (Keyword Arguments) ---")

# When a function expects specific keyword arguments, passing a dictionary
# that's missing a required key can lead to a KeyError if not handled.

def process_user_data(user_info):
    """Processes user data, expecting 'name', 'email', and 'id'."""
    try:
        user_name = user_info['name']
        user_email = user_info['email']
        user_id = user_info['id'] # This is the potentially missing key
        print(f"Processing user: ID={user_id}, Name={user_name}, Email={user_email}")
    except KeyError as e:
        print(f"Error: Missing required key in user_info: {e}")

# Valid data
valid_user = {'name': 'Alice', 'email': 'alice@example.com', 'id': 'A101'}
process_user_data(valid_user)

# Data missing 'id'
invalid_user_no_id = {'name': 'Bob', 'email': 'bob@example.com'}
process_user_data(invalid_user_no_id)

# Data missing 'email'
invalid_user_no_email = {'name': 'Charlie', 'id': 'C103'}
process_user_data(invalid_user_no_email)

print("-" * 50 + "\n")


# --- 12. KeyError with `dict.pop()` Method ---
print("--- 12. KeyError with `dict.pop()` Method ---")

# `dict.pop(key[, default])` removes the specified key and returns its value.
# If the key is not found and a `default` value is not provided, it raises a KeyError.

inventory = {'apple': 100, 'banana': 150, 'orange': 75}

# Pop an existing item (OK)
sold_apples = inventory.pop('apple')
print(f"Sold apples: {sold_apples}, Remaining inventory: {inventory}")

# Pop a non-existent item without a default (causes KeyError)
try:
    sold_grapes = inventory.pop('grape')
except KeyError as e:
    print(f"Caught KeyError (expected): {e}")
    print("Reason: Key 'grape' does not exist and no default was provided.")

# Pop a non-existent item with a default (OK, returns default)
sold_mangoes = inventory.pop('mango', 0) # Returns 0 if 'mango' not found
print(f"Sold mangoes: {sold_mangoes}, Remaining inventory: {inventory}")

print("-" * 50 + "\n")


# --- 13. KeyError due to Case Sensitivity ---
print("--- 13. KeyError due to Case Sensitivity ---")

# Dictionary keys are case-sensitive. 'Name' is different from 'name'.

user_profile = {"Name": "David", "AGE": 40, "email": "david@example.com"}

print(f"Accessing 'Name' (correct case): {user_profile['Name']}")

try:
    print(user_profile['name']) # Incorrect case
except KeyError as e:
    print(f"Caught KeyError (expected): {e}")
    print("Reason: Key 'name' (lowercase) does not exist, only 'Name' (uppercase N).")

# Common solution: Normalize keys (e.g., to lowercase) if case consistency is an issue.
normalized_profile = {k.lower(): v for k, v in user_profile.items()}
print(f"Normalized profile: {normalized_profile}")
print(f"Accessing 'name' (after normalization): {normalized_profile['name']}")

print("-" * 50 + "\n")


# --- 14. KeyError when Using F-strings with Direct Dictionary Access ---
print("--- 14. KeyError when Using F-strings with Direct Dictionary Access ---")

# F-strings evaluate expressions inside curly braces. If the expression includes
# a dictionary access with a non-existent key, it will raise a KeyError.

employee = {'first_name': 'Sarah', 'last_name': 'Connor'}

# Correct access in f-string (OK)
print(f"Employee: {employee['first_name']} {employee['last_name']}")

# Incorrect access (causes KeyError)
try:
    # Attempting to access 'department' which doesn't exist
    print(f"Employee: {employee['first_name']} from {employee['department']}")
except KeyError as e:
    print(f"Caught KeyError (expected): {e}")
    print("Reason: 'department' key is missing when f-string tries to format.")

# Safer f-string usage with .get()
# Note: You can't use .get() directly *inside* f-string curly braces
# if you want a default if the key is missing *and* the default itself is part of the output.
# You need to prepare the value outside or use a more complex expression.

employee_department = employee.get('department', 'Unknown Department')
print(f"Employee (safer with .get()): {employee['first_name']} from {employee_department}")

print("-" * 50 + "\n")


# --- 15. KeyError in Data Processing Pipelines (JSON/API Data) ---
print("--- 15. KeyError in Data Processing Pipelines (JSON/API Data) ---")

# This is a very common scenario: working with external data (e.g., from APIs, JSON files)
# where the structure might not always be guaranteed.

import json

json_data_1 = '{"status": "success", "data": {"id": "U001", "username": "alpha"}}'
json_data_2 = '{"status": "error", "message": "User not found"}'
json_data_3 = '{"status": "success", "data": {"id": "U002"}}' # Missing username

def parse_api_response(response_str):
    """Parses API response and extracts user information."""
    try:
        data = json.loads(response_str)
        if data['status'] == 'success':
            # This can cause KeyError if 'data' or 'username' is missing
            user_id = data['data']['id']
            username = data['data']['username'] # Potential KeyError here
            print(f"API Success: User ID={user_id}, Username={username}")
        else:
            print(f"API Error: {data.get('message', 'Unknown Error')}")
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")
    except KeyError as e:
        print(f"Data Structure Error: Missing key in API response: {e}")

print("Processing API Response 1 (Success, complete data):")
parse_api_response(json_data_1)

print("\nProcessing API Response 2 (Error):")
parse_api_response(json_data_2)

print("\nProcessing API Response 3 (Success, but missing 'username' in data):")
parse_api_response(json_data_3)

print("\nProcessing Malformed JSON:")
parse_api_response('{"key": "value"') # Malformed JSON

# Best practice for robust parsing of external data:
def parse_api_response_robust(response_str):
    """Parses API response robustly using .get() and checks."""
    try:
        data = json.loads(response_str)
        status = data.get('status')

        if status == 'success':
            user_data = data.get('data', {}) # Get 'data' dict, or an empty dict if missing
            user_id = user_data.get('id', 'N/A')
            username = user_data.get('username', 'Anonymous')
            print(f"API Success (Robust): User ID={user_id}, Username={username}")
        elif status == 'error':
            message = data.get('message', 'Unknown Error')
            print(f"API Error (Robust): {message}")
        else:
            print(f"API Response (Robust): Unexpected status or missing 'status' key.")
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error (Robust): {e}")
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred (Robust): {e}")

print("\n--- Robust API Response Parsing ---")
print("Processing API Response 1 (Success, complete data):")
parse_api_response_robust(json_data_1)

print("\nProcessing API Response 2 (Error):")
parse_api_response_robust(json_data_2)

print("\nProcessing API Response 3 (Success, but missing 'username' in data):")
parse_api_response_robust(json_data_3)

print("\nProcessing Malformed JSON:")
parse_api_response_robust('{"key": "value"')

print("-" * 50 + "\n")


# --- 16. Using `try-except` for Dictionary Lookup with Fallback ---
print("--- 16. Using `try-except` for Dictionary Lookup with Fallback ---")

# While `.get()` is good for simple fallbacks, `try-except` can be more
# explicit or handle more complex fallback logic.

product_details = {'id': 'PROD005', 'name': 'Smart Watch'}

# Scenario: Try to get 'description', if not found, use a default
# If that's not available, generate a generic one.
try:
    description = product_details['description']
    print(f"Product Description: {description}")
except KeyError:
    print("Description not found, trying default.")
    try:
        # Fallback 1: Default from another source or a global constant
        description = "A versatile electronic device for daily use."
        print(f"Using default description: {description}")
    except NameError: # If 'default_description' itself wasn't defined
        print("Default description source also missing, generating generic.")
        description = f"Generic description for {product_details.get('name', 'product')}."
        print(f"Using generic description: {description}")

print("-" * 50 + "\n")


print("--- End of KeyError (More Examples and Practice) ---")
