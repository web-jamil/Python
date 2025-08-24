# --- Python Dictionaries: All About Properties and Methods in Code ---

# Dictionaries are mutable, unordered (insertion-ordered in Python 3.7+),
# and store data as key-value pairs. They come with a rich set of built-in
# properties and methods to manage their content.

# Let's use a sample dictionary for demonstration.
user_settings = {
    "theme": "dark",
    "font_size": 14,
    "notifications_enabled": True,
    "language": "en-US",
    "last_updated": "2025-06-03"
}

print("--- 1. Dictionary Properties (Built-in Functions) ---")

# These are not methods of the dictionary object itself, but built-in Python
# functions that operate on dictionaries.

# 1.1 `len()`: Returns the number of key-value pairs (items) in the dictionary.
print(f"1.1 Number of items in user_settings: {len(user_settings)}") # Output: 5

# 1.2 `in` operator: Checks if a key exists in the dictionary.
# It checks for keys, not values.
print(f"1.2 Is 'theme' in user_settings? {'theme' in user_settings}") # Output: True
print(f"    Is 'password' in user_settings? {'password' in user_settings}") # Output: False
print(f"    Is 14 in user_settings (checks keys, not values)? {14 in user_settings}") # Output: False


print("\n--- 2. Dictionary Methods (for Accessing Elements) ---")

# These methods are used to retrieve values from the dictionary.

# 2.1 `get(key, default=None)`: Returns the value for `key` if `key` is in the dictionary,
#      else `default`. If `default` is not given, it defaults to `None`.
print(f"2.1 Get 'font_size': {user_settings.get('font_size')}") # Output: 14
print(f"    Get 'username' (not found, returns None): {user_settings.get('username')}") # Output: None
print(f"    Get 'timezone' (not found, with default): {user_settings.get('timezone', 'UTC')}") # Output: UTC

# 2.2 `keys()`: Returns a new view object that displays a list of all the keys in the dictionary.
#      This is a "view" and reflects changes to the dictionary.
all_keys = user_settings.keys()
print(f"2.2 All keys: {all_keys}") # Output: dict_keys(['theme', 'font_size', ...])
user_settings['new_setting'] = 'value'
print(f"    Keys after adding new_setting: {all_keys}") # 'new_setting' is reflected

# 2.3 `values()`: Returns a new view object that displays a list of all the values in the dictionary.
#      This is also a "view".
all_values = user_settings.values()
print(f"2.3 All values: {all_values}") # Output: dict_values(['dark', 14, ...])
user_settings['font_size'] = 16
print(f"    Values after updating font_size: {all_values}") # 16 is reflected

# 2.4 `items()`: Returns a new view object that displays a list of a dictionary's key-value tuple pairs.
#      This is also a "view".
all_items = user_settings.items()
print(f"2.4 All items: {all_items}") # Output: dict_items([('theme', 'dark'), ...])
del user_settings['last_updated']
print(f"    Items after deleting last_updated: {all_items}") # 'last_updated' is gone


print("\n--- 3. Dictionary Methods (for Modifying Elements) ---")

# These methods are used to add, update, or remove key-value pairs.

# 3.1 `update(other_dict)`: Updates the dictionary with the key-value pairs from `other_dict`,
#      overwriting existing keys. Can also take an iterable of key-value pairs.
print(f"3.1 Before update: {user_settings}")
new_settings = {"font_size": 18, "notifications_enabled": False, "username": "admin"}
user_settings.update(new_settings)
print(f"    After update with dict: {user_settings}")

# Can also update from a list of tuples
user_settings.update([("language", "fr-FR"), ("country", "France")])
print(f"    After update with list of tuples: {user_settings}")

# 3.2 `pop(key, default=None)`: Removes the specified `key` and returns its value.
#      If `key` is not found, `default` is returned. If `default` is not given and `key`
#      is not found, a `KeyError` is raised.
removed_language = user_settings.pop('language')
print(f"3.2 Removed language: {removed_language}") # Output: fr-FR
print(f"    After pop('language'): {user_settings}")

# Pop a non-existent key with a default
removed_timezone = user_settings.pop('timezone', 'Europe/Paris')
print(f"    Removed timezone (not found): {removed_timezone}") # Output: Europe/Paris

# 3.3 `popitem()`: Removes and returns an arbitrary (key, value) pair.
#      In Python 3.7+, it removes and returns the *last inserted* item.
#      Raises `KeyError` if the dictionary is empty.
last_item = user_settings.popitem()
print(f"3.3 Removed last item with popitem(): {last_item}") # e.g., ('country', 'France')
print(f"    After popitem(): {user_settings}")

# 3.4 `clear()`: Removes all items from the dictionary.
empty_dict = {"a": 1, "b": 2}
print(f"3.4 Before clear(): {empty_dict}")
empty_dict.clear()
print(f"    After clear(): {empty_dict}") # Output: {}

# 3.5 `setdefault(key, default_value=None)`: If `key` is in the dictionary, return its value.
#      If `key` is not in the dictionary, insert `key` with `default_value` and return `default_value`.
#      Useful for ensuring a key exists with a default before accessing it.
print(f"3.5 Before setdefault: {user_settings}")
# 'username' already exists, so its value is returned, no change to dict
current_username = user_settings.setdefault('username', 'guest')
print(f"    Username (key existed): {current_username}")
print(f"    Dict after setdefault (no change): {user_settings}")

# 'theme_color' does not exist, so it's added with 'blue' and 'blue' is returned
theme_color = user_settings.setdefault('theme_color', 'blue')
print(f"    Theme color (key added): {theme_color}")
print(f"    Dict after setdefault (key added): {user_settings}")


print("\n--- 4. Dictionary Methods (for Copying) ---")

# 4.1 `copy()`: Returns a shallow copy of the dictionary.
#      A shallow copy means new dictionary object, but nested mutable objects
#      (like lists or other dictionaries) are still referenced by both the original and the copy.
original_dict = {'a': 1, 'b': [2, 3]}
shallow_copy = original_dict.copy()
print(f"4.1 Original: {original_dict}, Shallow Copy: {shallow_copy}")

shallow_copy['a'] = 100 # Modifies top-level item in copy, not original
shallow_copy['b'].append(4) # Modifies nested list in copy, *does* affect original
print(f"    Original after shallow copy modification: {original_dict}")
print(f"    Shallow Copy after modification: {shallow_copy}")

# For a deep copy (where nested mutable objects are also copied), use `copy.deepcopy()`
import copy
deep_copy = copy.deepcopy(original_dict)
deep_copy['b'].append(5) # Modifies nested list in deep copy, *does NOT* affect original
print(f"    Original after deep copy modification: {original_dict}")
print(f"    Deep Copy after modification: {deep_copy}")


print("\n--- 5. Dictionary Methods (for Creation from Keys) ---")

# 5.1 `fromkeys(iterable, value=None)`: Creates a new dictionary with keys from `iterable`
#      and values set to `value` (which defaults to `None`).
new_dict_from_keys = dict.fromkeys(['name', 'age', 'city'], 'N/A')
print(f"5.1 New dict from keys: {new_dict_from_keys}") # {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}

# Important: If `value` is a mutable object (e.g., a list), all keys will reference
# the *same* mutable object.
mutable_value_dict = dict.fromkeys(['user1', 'user2'], [])
mutable_value_dict['user1'].append('task_A')
print(f"    Mutable value dict: {mutable_value_dict}") # Both user1 and user2 lists are modified!

# To avoid this, use a dictionary comprehension for mutable defaults:
safe_mutable_value_dict = {key: [] for key in ['user3', 'user4']}
safe_mutable_value_dict['user3'].append('task_B')
print(f"    Safe mutable value dict: {safe_mutable_value_dict}") # Only user3 list is modified.