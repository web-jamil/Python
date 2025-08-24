# --- Python Dictionaries: Positional Arguments in Code ---

# The phrase "dictionary positional arguments" can be a bit confusing because
# dictionaries themselves are inherently *unordered* collections of key-value pairs
# (though insertion-ordered since Python 3.7). They don't have "positions" in the
# same way lists or tuples do.

# However, there are two main contexts where dictionaries interact with "positional"
# concepts in Python:

# 1.  **Creating Dictionaries from Positional Data:** Using the `dict()` constructor
#     with an iterable of key-value pairs (e.g., a list of tuples).
# 2.  **Passing Dictionaries as Keyword Arguments to Functions:** Using the `**`
#     (double-asterisk) operator to unpack a dictionary into keyword arguments in a
#     function call. While these are *keyword* arguments, their origin from a
#     dictionary can be seen as a form of "positional" data if the dictionary
#     itself was constructed from ordered inputs.

# Let's explore both scenarios.

print("--- 1. Creating Dictionaries from Positional Data ---")

# The `dict()` constructor can take a single positional argument: an iterable
# where each element is a 2-item sequence (like a tuple or list) representing
# a `(key, value)` pair. The *order* of these pairs in the iterable matters
# for the resulting dictionary's insertion order (Python 3.7+).

# 1.1 From a list of tuples (common use case)
# Each tuple `(key, value)` is a "positional argument" to the dictionary creation.
list_of_tuples = [
    ("name", "Alice"),
    ("age", 30),
    ("city", "New York")
]
person_dict_from_tuples = dict(list_of_tuples)
print(f"1.1 Dictionary from list of tuples: {person_dict_from_tuples}")
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 1.2 From a list of lists (also works)
list_of_lists = [
    ["product_id", "P001"],
    ["price", 120.50],
    ["in_stock", True]
]
product_dict_from_lists = dict(list_of_lists)
print(f"1.2 Dictionary from list of lists: {product_dict_from_lists}")

# 1.3 Using `zip()` to combine two iterables into key-value pairs
# `zip()` creates an iterable of tuples, which `dict()` can consume.
keys = ["fruit", "color", "taste"]
values = ["apple", "red", "sweet"]
fruit_details = dict(zip(keys, values))
print(f"1.3 Dictionary from zip(keys, values): {fruit_details}")

# 1.4 What happens if the inner sequence is not 2 items? (ValueError)
try:
    invalid_input = [("key1", "value1", "extra"), ("key2", "value2")]
    dict(invalid_input)
except ValueError as e:
    print(f"\n1.4 Error: {e} - Inner sequence must have exactly 2 items.")

# 1.5 What happens if keys are duplicated?
# The last occurrence of the key will overwrite previous ones.
duplicate_keys_input = [
    ("item", "pen"),
    ("color", "blue"),
    ("item", "pencil") # 'item' is duplicated
]
dict_with_duplicates = dict(duplicate_keys_input)
print(f"\n1.5 Dictionary with duplicate keys (last one wins): {dict_with_duplicates}")
# Output: {'item': 'pencil', 'color': 'blue'}


print("\n--- 2. Passing Dictionaries as Keyword Arguments to Functions (`**kwargs`) ---")

# This is where dictionaries often interact with function arguments.
# The `**` operator unpacks a dictionary into keyword arguments when calling a function.
# While the arguments are keyword-based, the values come from the dictionary's "positions"
# (its key-value pairs).

# 2.1 Basic unpacking into keyword arguments
def greet_user(name, age, city):
    print(f"2.1 Hello, {name}! You are {age} years old and live in {city}.")

user_info_dict = {
    "name": "Bob",
    "age": 25,
    "city": "London"
}

# The `**` unpacks `user_info_dict` into `name='Bob', age=25, city='London'`
greet_user(**user_info_dict)

# 2.2 What if dictionary keys don't match function parameters? (TypeError)
def create_profile(username, email):
    print(f"2.2 Profile created for {username} with email {email}.")

# Missing 'email' key
missing_key_dict = {"username": "charlie"}
try:
    create_profile(**missing_key_dict)
except TypeError as e:
    print(f"\n2.2 Error: {e} - Missing required argument 'email'.")

# Extra key 'phone'
extra_key_dict = {"username": "david", "email": "david@example.com", "phone": "123-456"}
try:
    create_profile(**extra_key_dict)
except TypeError as e:
    print(f"    Error: {e} - Got an unexpected keyword argument 'phone'.")

# 2.3 Combining with positional and other keyword arguments
def configure_app(host, port=80, debug=False, **extra_settings):
    print(f"\n2.3 App Configuration:")
    print(f"    Host: {host}")
    print(f"    Port: {port}")
    print(f"    Debug: {debug}")
    print(f"    Extra Settings: {extra_settings}")

# `host` is a positional argument
# `port` is a keyword argument explicitly passed
# `**db_settings` unpacks into `user='admin', password='123'`
db_settings = {"user": "admin", "password": "123"}
configure_app("localhost", port=8080, **db_settings)

# Example with a mix, including overriding a default
other_settings = {"debug": True, "timeout": 30}
configure_app("remote.server", **other_settings)


print("\n--- 3. `dict()` constructor with mixed arguments ---")

# The `dict()` constructor can also take a mix of positional iterable and keyword arguments.
# Keyword arguments always take precedence if keys overlap.

# 3.1 Mixing iterable and keyword arguments
mixed_creation = dict([("color", "red"), ("size", "M")], material="cotton", color="blue")
print(f"3.1 Mixed dictionary creation: {mixed_creation}")
# Output: {'color': 'blue', 'size': 'M', 'material': 'cotton'}
# 'color' from keyword argument 'color="blue"' overwrites 'color' from iterable.

# 3.2 Order preservation (Python 3.7+)
# The order of elements from the iterable is preserved, followed by the order of keyword arguments.
ordered_mixed = dict([("first", 1), ("second", 2)], third=3, fourth=4)
print(f"3.2 Ordered mixed creation: {ordered_mixed}")
# Output: {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}