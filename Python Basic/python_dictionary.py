import random

print("--- Python Dictionary: All Methods in Practice Code ---")

# --- 1. Creating Dictionaries ---
print("\n--- 1. Creating Dictionaries ---")

# 1.1 Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# 1.2 Dictionary with key-value pairs
# Keys must be immutable (strings, numbers, tuples). Values can be any type.
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72
}
print(f"Student scores: {student_scores}")

# 1.3 Using dict() constructor with keyword arguments
employee_roles = dict(John="Manager", Jane="Developer", Mike="Designer")
print(f"Employee roles (dict() with kwargs): {employee_roles}")

# 1.4 Using dict() with a list of key-value tuples
product_prices = dict([
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 75)
])
print(f"Product prices (dict() with list of tuples): {product_prices}")




print("--- Dictionary Updating, Accessing, and Deleting Code ---")

# --- 1. Initial Dictionary Setup ---
print("\n--- 1. Initial Dictionary Setup ---")

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "email": "alice@example.com"
}
print(f"Original dictionary: {my_dict}")


# --- 2. Accessing Elements ---
print("\n--- 2. Accessing Elements ---")

# 2.1 Using square brackets [] (most common)
# If the key doesn't exist, this will raise a KeyError.
print(f"Accessing 'name': {my_dict['name']}")
print(f"Accessing 'age': {my_dict['age']}")

# Example of KeyError if you try to access a non-existent key:
# try:
#     print(my_dict['country'])
# except KeyError as e:
#     print(f"Caught KeyError: {e} - 'country' key does not exist.")

# 2.2 Using the .get() method (safer, returns None or a default value)
# If the key exists, it returns its value.
print(f"Accessing 'city' using .get(): {my_dict.get('city')}")

# If the key doesn't exist, .get() returns None by default.
print(f"Accessing 'country' using .get() (default None): {my_dict.get('country')}")

# You can provide a custom default value if the key is not found.
print(f"Accessing 'zip_code' using .get() (custom default 'N/A'): {my_dict.get('zip_code', 'N/A')}")

# 2.3 Accessing all keys, values, or items (key-value pairs)
print(f"All keys: {list(my_dict.keys())}")
print(f"All values: {list(my_dict.values())}")
print(f"All items (key-value pairs): {list(my_dict.items())}")


# --- 3. Updating Elements ---
print("\n--- 3. Updating Elements ---")

# 3.1 Modifying an existing value
# Simply assign a new value to an existing key.
my_dict["age"] = 31
print(f"After updating 'age': {my_dict}")

# 3.2 Adding a new key-value pair
# If the key doesn't exist, it's added.
my_dict["has_car"] = True
print(f"After adding 'has_car': {my_dict}")

# 3.3 Using the .update() method
# Merges another dictionary or iterable of key-value pairs into the current dictionary.
# Existing keys are updated, new keys are added.
additional_info = {
    "city": "London",        # Updates existing 'city'
    "phone": "123-456-7890", # Adds new 'phone'
    "occupation": "Software Engineer" # Updates existing 'occupation'
}
my_dict.update(additional_info)
print(f"After updating with 'additional_info': {my_dict}")

# You can also update with a list of tuples:
my_dict.update([("email", "alice.london@example.com"), ("status", "active")])
print(f"After updating with list of tuples: {my_dict}")


# --- 4. Deleting Elements ---
print("\n--- 4. Deleting Elements ---")

# 4.1 Using the `del` keyword
# Deletes a specific key-value pair. Raises KeyError if the key doesn't exist.
del my_dict["email"]
print(f"After deleting 'email' with del: {my_dict}")

# Example of KeyError if you try to delete a non-existent key:
# try:
#     del my_dict['non_existent_key']
# except KeyError as e:
#     print(f"Caught KeyError: {e} - 'non_existent_key' cannot be deleted.")

# 4.2 Using the .pop() method
# Removes the specified key and returns its value. Raises KeyError if key not found (unless a default is provided).
removed_occupation = my_dict.pop("occupation")
print(f"After popping 'occupation' ({removed_occupation}): {my_dict}")

# .pop() with a default value:
# If the key doesn't exist, it returns the default value instead of raising an error.
result_pop_safe = my_dict.pop("gender", "Not specified")
print(f"Attempted to pop 'gender' (not found), result: {result_pop_safe}, dict: {my_dict}")

# 4.3 Using the .popitem() method
# Removes and returns an arbitrary key-value pair as a tuple.
# In Python 3.7+, it removes and returns the last inserted key-value pair (LIFO order).
# Raises KeyError if the dictionary is empty.
if my_dict: # Check if dictionary is not empty before popping
    removed_item_key, removed_item_value = my_dict.popitem()
    print(f"After popping an item ({removed_item_key}: {removed_item_value}): {my_dict}")
else:
    print("Dictionary is empty, cannot popitem.")

# 4.4 Using the .clear() method
# Removes all items from the dictionary, making it empty.
my_dict.clear()
print(f"After clearing the dictionary: {my_dict}")


print("\n--- End of Dictionary Operations Code ---")




# 1.5 Using dict.fromkeys() to create a dictionary with default values
# Useful for initializing a dictionary with a list of keys
default_value = 0
inventory_items = ["Apple", "Banana", "Cherry"]
initial_inventory = dict.fromkeys(inventory_items, default_value)
print(f"Initial inventory (dict.fromkeys()): {initial_inventory}")

# 1.6 Dictionary comprehension (similar to list comprehension)
square_map = {x: x*x for x in range(1, 6)}
print(f"Square map (dictionary comprehension): {square_map}")


print("\n--- 2. Accessing Dictionary Elements ---")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# 2.1 Using square brackets (most common)
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")

# 2.2 Using .get() method (safer, returns None or a default value if key not found)
print(f"City: {my_dict.get('city')}")
print(f"Country (not present, returns None): {my_dict.get('country')}")
print(f"Zip Code (not present, returns 'N/A'): {my_dict.get('zip', 'N/A')}")

# 2.3 Accessing all keys: .keys() method
all_keys = my_dict.keys()
print(f"All keys: {list(all_keys)}") # Convert to list for display

# 2.4 Accessing all values: .values() method
all_values = my_dict.values()
print(f"All values: {list(all_values)}") # Convert to list for display

# 2.5 Accessing all key-value pairs: .items() method
all_items = my_dict.items()
print(f"All items: {list(all_items)}") # Convert to list for display


print("\n--- 3. Modifying Dictionaries ---")

config = {"theme": "dark", "font_size": 14, "notifications": True}
print(f"Original config: {config}")

# 3.1 Adding a new key-value pair
config["language"] = "en"
print(f"After adding 'language': {config}")

# 3.2 Updating an existing value
config["font_size"] = 16
print(f"After updating 'font_size': {config}")

# 3.3 Using .update() method to merge dictionaries or add/update multiple items
# It takes another dictionary or an iterable of key-value pairs.
new_settings = {"notifications": False, "theme": "light", "debug_mode": True}
config.update(new_settings)
print(f"After updating with new_settings: {config}")

# 3.4 Removing elements: .pop() (removes key and returns its value)
removed_font_size = config.pop("font_size")
print(f"After popping 'font_size' ({removed_font_size}): {config}")
# .pop() with a default value if key not found
removed_non_existent = config.pop("non_existent_key", "Key not found")
print(f"After popping non-existent key: {config}, Result: {removed_non_existent}")

# 3.5 Removing elements: .popitem() (removes and returns an arbitrary (last in Python 3.7+) key-value pair)
key_removed, value_removed = config.popitem()
print(f"After popping an item ({key_removed}: {value_removed}): {config}")

# 3.6 Removing elements: del keyword (deletes a key-value pair)
del config["language"]
print(f"After deleting 'language' with del: {config}")

# 3.7 Clearing all elements: .clear()
config.clear()
print(f"After clearing the dictionary: {config}")


print("\n--- 4. Dictionary Operations and Utilities ---")

student_grades = {"Alice": 90, "Bob": 75, "Charlie": 85, "David": 92}

# 4.1 Length of a dictionary: len()
print(f"Length of student_grades: {len(student_grades)}")

# 4.2 Check if a key exists: 'in' operator
print(f"Is 'Bob' in student_grades? {'Bob' in student_grades}")
print(f"Is 'Eve' in student_grades? {'Eve' in student_grades}")

# 4.3 Copying a dictionary (important for avoiding side effects)
original_dict = {"a": 1, "b": 2}
copy_method = original_dict.copy() # Recommended for shallow copy
copy_constructor = dict(original_dict) # Also creates a shallow copy

original_dict["a"] = 99
print(f"Original dictionary after modification: {original_dict}")
print(f"Copy created by .copy(): {copy_method} (remains unchanged)")
print(f"Copy created by dict(): {copy_constructor} (remains unchanged)")

# 4.4 Merging dictionaries (Python 3.5+ using **, Python 3.9+ using |)
dict1 = {"A": 1, "B": 2}
dict2 = {"B": 3, "C": 4} # B will be overwritten by dict2's B

# Using ** (merge operator for dictionaries, creates a new dict)
merged_dict_star = {**dict1, **dict2}
print(f"Merged dict (using **): {merged_dict_star}")

# Using | (union operator for dictionaries, Python 3.9+, creates a new dict)
merged_dict_pipe = dict1 | dict2
print(f"Merged dict (using |): {merged_dict_pipe}")


# 4.5 Iterating through dictionaries
print("\nIterating through student_grades:")
# Default iteration is over keys
for student in student_grades:
    print(f"Student: {student}")

# Iterate over keys explicitly
for student_name in student_grades.keys():
    print(f"Key: {student_name}")

# Iterate over values explicitly
for grade in student_grades.values():
    print(f"Grade: {grade}")

# Iterate over key-value pairs (most common)
for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")


print("\n--- 5. Practical Use Cases / Advanced Topics ---")

# 5.1 Using .setdefault()
# If key exists, returns its value. If not, inserts key with default value and returns it.
user_settings = {"theme": "dark", "language": "en"}
print(f"Initial user_settings: {user_settings}")

# Key 'language' exists, returns its value
lang = user_settings.setdefault("language", "fr")
print(f"Language (key existed): {lang}, dict: {user_settings}")

# Key 'notifications' does not exist, adds it with default value
notif = user_settings.setdefault("notifications", True)
print(f"Notifications (key added): {notif}, dict: {user_settings}")

# 5.2 Ordered Dictionaries (since Python 3.7, standard dicts preserve insertion order)
ordered_data = {"first": 1, "second": 2, "third": 3}
print(f"\nOrdered dictionary (insertion order preserved in Python 3.7+): {ordered_data}")
# You can verify by iterating, it will always be in the order of insertion.

# 5.3 Nested Dictionaries
user_profile = {
    "id": 101,
    "name": "Eve",
    "contact": {
        "email": "eve@example.com",
        "phone": "555-1234"
    },
    "preferences": {
        "notifications": {"email": True, "sms": False},
        "theme": "light"
    }
}
print(f"\nNested Dictionary:\n{user_profile}")
print(f"Eve's email: {user_profile['contact']['email']}")
user_profile['preferences']['notifications']['sms'] = True
print(f"Updated SMS notification: {user_profile['preferences']['notifications']['sms']}")

# 5.4 Using dictionaries for counting/frequency mapping
word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}
for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1
print(f"\nWord counts: {word_counts}")

# Or using collections.Counter for more advanced counting
from collections import Counter
word_counts_counter = Counter(word_list)
print(f"Word counts (using Counter): {word_counts_counter}")

# 5.5 Inverting a dictionary (swapping keys and values) - careful with non-unique values!
# This assumes values are unique, otherwise information is lost.
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for key, value in original.items()}
print(f"\nOriginal dict: {original}, Inverted dict: {inverted}")

# What happens if values are not unique?
original_with_dupes = {'a': 1, 'b': 2, 'c': 1}
inverted_dupes = {value: key for key, value in original_with_dupes.items()}
print(f"Original with dupes: {original_with_dupes}, Inverted (note loss of 'a'): {inverted_dupes}")


print("\n--- End of Python Dictionary Practice Code ---")