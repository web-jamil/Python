# --- Python Dictionaries: All About Common Methods in Code ---

# Dictionaries are dynamic and come with a variety of methods to manipulate,
# access, and manage their key-value pairs.

# Let's use a sample dictionary for demonstration throughout.
user_profile = {
    "id": "user_001",
    "name": "Alice Smith",
    "email": "alice.s@example.com",
    "age": 28,
    "is_active": True,
    "roles": ["viewer", "commenter"],
    "settings": {"theme": "dark", "notifications": True}
}

print("--- 1. Methods for Accessing Elements ---")

# 1.1 `get(key, default=None)`
# - Returns the value associated with `key`.
# - If `key` is not found, it returns `default` (which is `None` if not specified).
# - Does NOT raise a KeyError.

print(f"1.1 `get()` method:")
print(f"    Email: {user_profile.get('email')}") # Key exists
print(f"    Phone (not found, returns None): {user_profile.get('phone')}")
print(f"    Address (not found, with default): {user_profile.get('address', 'Not specified')}")
print(f"    Metadata (key exists, value is None): {user_profile.get('metadata', 'Default Meta')}") # Assuming 'metadata' key is not in user_profile


# 1.2 `keys()`
# - Returns a new *view object* that displays a list of all the keys in the dictionary.
# - The view is dynamic; it reflects changes to the dictionary.

print(f"\n1.2 `keys()` method:")
all_keys = user_profile.keys()
print(f"    All keys: {all_keys}")
print(f"    Type of all_keys: {type(all_keys)}")

# Demonstrate dynamic nature:
user_profile["last_login"] = "2025-06-04"
print(f"    Keys after adding 'last_login': {all_keys}") # 'last_login' appears in the view


# 1.3 `values()`
# - Returns a new *view object* that displays a list of all the values in the dictionary.
# - The view is dynamic.

print(f"\n1.3 `values()` method:")
all_values = user_profile.values()
print(f"    All values: {all_values}")
print(f"    Type of all_values: {type(all_values)}")

# Demonstrate dynamic nature:
user_profile["age"] = 29
print(f"    Values after updating 'age': {all_values}") # 29 is reflected in the view


# 1.4 `items()`
# - Returns a new *view object* that displays a list of a dictionary's key-value tuple pairs.
# - The view is dynamic. Often used for iterating through dictionaries.

print(f"\n1.4 `items()` method:")
all_items = user_profile.items()
print(f"    All items: {all_items}")
print(f"    Type of all_items: {type(all_items)}")

# Demonstrate dynamic nature:
del user_profile["is_active"]
print(f"    Items after deleting 'is_active': {all_items}") # 'is_active' pair is removed from the view


# --- 2. Methods for Modifying Elements ---

# 2.1 `update(other_dict)`
# - Updates the dictionary with the key-value pairs from `other_dict`.
# - If a key from `other_dict` already exists, its value is overwritten.
# - If a key from `other_dict` does not exist, it's added.
# - Can also take an iterable of key-value pairs (e.g., list of tuples or keyword arguments).

print(f"\n2.1 `update()` method:")
print(f"    Before update: {user_profile}")
new_data = {
    "age": 30, # Will overwrite existing age
    "phone": "555-123-4567", # New key
    "roles": ["admin"] # Will overwrite existing roles
}
user_profile.update(new_data)
print(f"    After update with dict: {user_profile}")

# Update from a list of tuples
user_profile.update([("status", "online"), ("email", "alice@newmail.com")])
print(f"    After update with list of tuples: {user_profile}")

# Update from keyword arguments (for new keys or simple updates)
user_profile.update(last_seen="now", theme="light")
print(f"    After update with keyword args: {user_profile}")


# 2.2 `pop(key, default=None)`
# - Removes the specified `key` and returns its corresponding value.
# - If `key` is not found:
#     - If `default` is provided, `default` is returned.
#     - If `default` is NOT provided, a `KeyError` is raised.

print(f"\n2.2 `pop()` method:")
print(f"    Before pop: {user_profile}")

# Pop an existing key
removed_email = user_profile.pop("email")
print(f"    Removed email: {removed_email}")
print(f"    After pop('email'): {user_profile}")

# Pop a non-existent key with a default value
removed_address = user_profile.pop("address", "Address not found in profile")
print(f"    Removed address (not found): {removed_address}")
print(f"    Dictionary unchanged: {user_profile}") # No change as key wasn't there

# Attempt to pop a non-existent key without a default (will raise KeyError)
try:
    user_profile.pop("non_existent_key")
except KeyError as e:
    print(f"    Error: {e} - Attempted to pop non-existent key without default.")


# 2.3 `popitem()`
# - Removes and returns an arbitrary (key, value) pair.
# - In Python 3.7+, it removes and returns the *last inserted* key-value pair.
# - Raises `KeyError` if the dictionary is empty.

print(f"\n2.3 `popitem()` method:")
print(f"    Before popitem: {user_profile}")
last_entry = user_profile.popitem()
print(f"    Removed last entry: {last_entry}")
print(f"    After popitem: {user_profile}")

# Demonstrate with an empty dictionary
empty_dict = {}
try:
    empty_dict.popitem()
except KeyError as e:
    print(f"    Error: {e} - Cannot popitem from an empty dictionary.")


# 2.4 `clear()`
# - Removes all items from the dictionary, making it empty.
# - Does not return any value.

print(f"\n2.4 `clear()` method:")
data_to_clear = {"a": 1, "b": 2, "c": 3}
print(f"    Before clear(): {data_to_clear}")
data_to_clear.clear()
print(f"    After clear(): {data_to_clear}")


# 2.5 `setdefault(key, default_value=None)`
# - If `key` is in the dictionary, returns its value.
# - If `key` is *not* in the dictionary, it inserts `key` with `default_value`
#   and returns `default_value`.
# - Useful for ensuring a key exists with a default value before accessing it.

print(f"\n2.5 `setdefault()` method:")
print(f"    Before setdefault: {user_profile}")

# Key 'name' exists, so its value is returned, dictionary is unchanged
name_val = user_profile.setdefault('name', 'Guest')
print(f"    Name (key existed): {name_val}")
print(f"    Dict after setdefault (no change): {user_profile}")

# Key 'timezone' does not exist, so it's added with 'UTC' and 'UTC' is returned
timezone_val = user_profile.setdefault('timezone', 'UTC')
print(f"    Timezone (key added): {timezone_val}")
print(f"    Dict after setdefault (key added): {user_profile}")

# Using setdefault with a mutable default value (be cautious!)
# All keys will reference the *same* mutable object if created this way.
user_activity = {}
user_activity.setdefault('logs', []).append('login at 10:00')
user_activity.setdefault('logs', []).append('logout at 11:00')
print(f"    User activity logs: {user_activity}")


# --- 3. Methods for Copying Dictionaries ---

# 3.1 `copy()`
# - Returns a *shallow copy* of the dictionary.
# - A new dictionary object is created, but nested mutable objects (like lists or
#   other dictionaries) are still referenced by both the original and the copy.

print(f"\n3.1 `copy()` method (Shallow Copy):")
original_dict = {"id": 1, "data": [10, 20]}
shallow_copy_dict = original_dict.copy()
print(f"    Original: {original_dict}, Shallow Copy: {shallow_copy_dict}")

# Modify top-level item in shallow copy - does not affect original
shallow_copy_dict["id"] = 2
print(f"    Original after top-level change in copy: {original_dict}")
print(f"    Shallow Copy after top-level change: {shallow_copy_dict}")

# Modify nested mutable item in shallow copy - *does* affect original
shallow_copy_dict["data"].append(30)
print(f"    Original after nested change in copy: {original_dict}")
print(f"    Shallow Copy after nested change: {shallow_copy_dict}")

# For a *deep copy* (where nested mutable objects are also copied recursively),
# use `copy.deepcopy()` from the `copy` module.
import copy
deep_copy_dict = copy.deepcopy(original_dict)
deep_copy_dict["data"].append(40)
print(f"    Original after deep copy change: {original_dict}") # Original is unchanged
print(f"    Deep Copy after change: {deep_copy_dict}")


# --- 4. Methods for Creating Dictionaries from Keys ---

# 4.1 `fromkeys(iterable, value=None)` (Class Method)
# - Creates a new dictionary.
# - Keys are taken from `iterable`.
# - All values are set to `value` (which defaults to `None` if not specified).

print(f"\n4.1 `fromkeys()` method:")
new_users_status = dict.fromkeys(["userA", "userB", "userC"], "pending")
print(f"    New users status: {new_users_status}")

# Be cautious with mutable default values, as all keys will reference the same object.
mutable_default = dict.fromkeys(["list1", "list2"], [])
print(f"    Mutable default (initial): {mutable_default}")
mutable_default["list1"].append("item_A")
print(f"    Mutable default (after modifying list1): {mutable_default}") # list2 also modified!

# To avoid this, use a dictionary comprehension for unique mutable defaults:
safe_mutable_default = {key: [] for key in ["list3", "list4"]}
print(f"    Safe mutable default (initial): {safe_mutable_default}")
safe_mutable_default["list3"].append("item_B")
print(f"    Safe mutable default (after modifying list3): {safe_mutable_default}") # list4 is unchanged