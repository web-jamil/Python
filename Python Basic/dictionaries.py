# --- Python Dictionaries: All About in Code ---

# Dictionaries are one of Python's most powerful and flexible built-in data structures.
# They are used to store collections of data in key-value pairs.

# --- 1. Introduction to Dictionaries ---

# 1.1 What are Dictionaries?
# - Unordered (prior to Python 3.7, insertion order was not guaranteed; now it is).
# - Mutable: You can add, remove, and modify key-value pairs after creation.
# - Collection of key-value pairs: Each item in a dictionary consists of a key and its associated value.
# - Keys must be unique within a dictionary.
# - Keys must be immutable (e.g., strings, numbers, tuples). Lists, sets, and other dictionaries cannot be keys.
# - Values can be of any data type and can be duplicated.

# 1.2 Why use Dictionaries?
# - Fast lookups: Retrieving a value by its key is very efficient (average O(1) time complexity).
# - Flexible data storage: Ideal for representing structured data, like records or configurations.
# - Associative arrays: Map keys to values, similar to hash maps or hash tables in other languages.

print("--- 1. Introduction ---")
print("Dictionaries store data as key-value pairs.")
print("They are mutable and optimized for quick lookups by key.")


# --- 2. Creating Dictionaries ---

print("\n--- 2. Creating Dictionaries ---")

# 2.1 Empty Dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print(f"Type of empty_dict: {type(empty_dict)}")

# 2.2 Using curly braces {} with key-value pairs
# Syntax: {key1: value1, key2: value2, ...}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary 'person': {person}")

# Keys can be various immutable types:
# Strings (most common)
# Numbers (integers, floats)
# Tuples (if they contain only immutable elements)
mixed_keys_dict = {
    1: "one",
    "two": 2,
    (3, 4): "three-four tuple",
    3.14: "Pi"
}
print(f"Dictionary with mixed key types: {mixed_keys_dict}")

# Values can be of any type, including other dictionaries or lists
nested_data_dict = {
    "product_id": "P001",
    "details": {
        "name": "Laptop",
        "brand": "TechCo",
        "price": 1200.00
    },
    "tags": ["electronics", "computer", "portable"]
}
print(f"Dictionary with nested data: {nested_data_dict}")

# 2.3 Using the dict() constructor
# From keyword arguments (keys must be valid identifiers)
car = dict(make="Toyota", model="Camry", year=2023)
print(f"Dictionary 'car' (from keyword args): {car}")

# From an iterable of key-value pairs (e.g., a list of tuples)
# Each tuple must be a (key, value) pair.
fruits_list_of_tuples = [("apple", 1), ("banana", 2), ("cherry", 3)]
fruits_dict = dict(fruits_list_of_tuples)
print(f"Dictionary 'fruits_dict' (from list of tuples): {fruits_dict}")

# From another dictionary (creates a shallow copy)
copied_person = dict(person)
print(f"Copied 'person' dictionary: {copied_person}")


# --- 3. Accessing Elements ---

print("\n--- 3. Accessing Elements ---")

# 3.1 Using square brackets [] (key lookup)
# Returns the value associated with the given key.
# Raises a KeyError if the key is not found.
print(f"Person's name: {person['name']}")
print(f"Person's age: {person['age']}")

# Accessing nested values
print(f"Product name (nested): {nested_data_dict['details']['name']}")
print(f"First product tag (nested list): {nested_data_dict['tags'][0]}")

# Attempting to access a non-existent key will raise an error
try:
    print(person['address'])
except KeyError as e:
    print(f"Error accessing non-existent key: {e}")

# 3.2 Using the get() method
# - Safer way to access values as it doesn't raise a KeyError.
# - Returns None if the key is not found (default behavior).
# - Can specify a default value to return if the key is not found.
print(f"Person's city (using get()): {person.get('city')}")
print(f"Person's address (using get(), returns None): {person.get('address')}")
print(f"Person's phone (using get() with default): {person.get('phone', 'N/A')}")


# --- 4. Modifying Dictionaries ---

print("\n--- 4. Modifying Dictionaries ---")

# 4.1 Adding new key-value pairs
# If the key does not exist, a new key-value pair is added.
person["email"] = "alice@example.com"
print(f"Person after adding email: {person}")

# 4.2 Updating existing values
# If the key already exists, its value is updated.
person["age"] = 31
print(f"Person after updating age: {person}")

# 4.3 update() method
# Merges a dictionary or an iterable of key-value pairs into the current dictionary.
# Existing keys are updated, new keys are added.
additional_info = {"occupation": "Software Engineer", "city": "San Francisco"}
person.update(additional_info)
print(f"Person after update() with a dict: {person}")

# Can also update from a list of tuples
more_updates = [("age", 32), ("zip_code", "94105")]
person.update(more_updates)
print(f"Person after update() with list of tuples: {person}")


# --- 5. Removing Elements ---

print("\n--- 5. Removing Elements ---")

# 5.1 del keyword
# Deletes a specific key-value pair.
# Raises a KeyError if the key does not exist.
del person["zip_code"]
print(f"Person after deleting 'zip_code': {person}")

try:
    del person["non_existent_key"]
except KeyError as e:
    print(f"Error deleting non-existent key: {e}")

# 5.2 pop() method
# Removes the specified key and returns its value.
# Raises a KeyError if the key is not found, unless a default value is provided.
removed_city = person.pop("city")
print(f"Removed city: {removed_city}")
print(f"Person after pop('city'): {person}")

# pop() with a default value (no error if key not found)
removed_phone = person.pop("phone", "No phone found")
print(f"Removed phone (not found): {removed_phone}")

# 5.3 popitem() method (Python 3.7+ removes last inserted item)
# Removes and returns an arbitrary (key, value) pair.
# In Python 3.7+, it removes and returns the last inserted item.
# Raises KeyError if the dictionary is empty.
last_item = person.popitem()
print(f"Removed last item with popitem(): {last_item}")
print(f"Person after popitem(): {person}")

# 5.4 clear() method
# Removes all items from the dictionary, making it empty.
person.clear()
print(f"Person after clear(): {person}")


# --- 6. Dictionary Properties & Operations ---

print("\n--- 6. Dictionary Properties & Operations ---")

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# 6.1 len() - number of key-value pairs
print(f"Length of my_dict: {len(my_dict)}")

# 6.2 'in' operator - checking for key existence
# Checks if a key exists in the dictionary.
print(f"Is 'b' in my_dict? {'b' in my_dict}")
print(f"Is 'z' in my_dict? {'z' in my_dict}")

# Note: 'in' checks keys, not values directly
print(f"Is 2 in my_dict (checks keys only)? {2 in my_dict}") # False, because 2 is a value, not a key

# To check if a value exists:
print(f"Is 2 a value in my_dict? {2 in my_dict.values()}") # True

# 6.3 keys() method - returns a view object of all keys
# This is a dynamic view, reflecting changes to the dictionary.
keys_view = my_dict.keys()
print(f"Keys view: {keys_view}")
my_dict["e"] = 5 # Add a new item
print(f"Keys view after adding 'e': {keys_view}") # 'e' is automatically included

# 6.4 values() method - returns a view object of all values
# This is also a dynamic view.
values_view = my_dict.values()
print(f"Values view: {values_view}")
my_dict["a"] = 100 # Update a value
print(f"Values view after updating 'a': {values_view}") # Value for 'a' is updated

# 6.5 items() method - returns a view object of all key-value pairs (as tuples)
# This is also a dynamic view.
items_view = my_dict.items()
print(f"Items view: {items_view}")
del my_dict["b"] # Delete an item
print(f"Items view after deleting 'b': {items_view}") # 'b' is removed

# 6.6 Iterating through dictionaries
print("\nIterating through dictionaries:")

# Default iteration is over keys
print("Iterating over keys (default):")
for key in my_dict:
    print(key, end=" ")
print()

# Explicitly iterating over keys
print("Iterating over keys (explicit):")
for key in my_dict.keys():
    print(key, end=" ")
print()

# Iterating over values
print("Iterating over values:")
for value in my_dict.values():
    print(value, end=" ")
print()

# Iterating over items (most common for accessing both key and value)
print("Iterating over items:")
for key, value in my_dict.items():
    print(f"({key}: {value})", end=" ")
print()


# --- 7. Dictionary Comprehensions ---

print("\n--- 7. Dictionary Comprehensions ---")

# Concise way to create dictionaries from iterables.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Example 1: Squaring numbers
squares = {num: num**2 for num in range(5)}
print(f"Squares dictionary: {squares}") # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example 2: Filtering and transforming
even_squares = {num: num**2 for num in range(10) if num % 2 == 0}
print(f"Even squares: {even_squares}") # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Example 3: Swapping keys and values (if values are hashable)
inverted_dict = {value: key for key, value in squares.items()}
print(f"Inverted squares: {inverted_dict}") # {0: 0, 1: 1, 4: 2, 9: 3, 16: 4}


# --- 8. Nested Dictionaries ---

print("\n--- 8. Nested Dictionaries ---")

# Dictionaries can contain other dictionaries, lists, or any other data type.
students = {
    "s101": {
        "name": "John Doe",
        "age": 20,
        "courses": ["Math", "Physics"],
        "grades": {"Math": "A", "Physics": "B+"}
    },
    "s102": {
        "name": "Jane Smith",
        "age": 21,
        "courses": ["Chemistry", "Biology"],
        "grades": {"Chemistry": "A-", "Biology": "A"}
    }
}

print(f"Students data: {students}")
print(f"John Doe's age: {students['s101']['age']}")
print(f"Jane Smith's Biology grade: {students['s102']['grades']['Biology']}")
print(f"John Doe's courses: {students['s101']['courses']}")


# --- 9. Common Dictionary Methods (beyond basic CRUD) ---

print("\n--- 9. Common Dictionary Methods ---")

# 9.1 copy() - creates a shallow copy
# A shallow copy means that nested objects are still referenced, not copied.
original = {"a": 1, "b": {"c": 2}}
copied = original.copy()
print(f"Original: {original}, Copied: {copied}")
copied["a"] = 10 # Modifying top-level in copy doesn't affect original
copied["b"]["c"] = 20 # Modifying nested object in copy *does* affect original
print(f"Original after nested modification: {original}")
print(f"Copied after nested modification: {copied}")

# For a deep copy, use `import copy; copy.deepcopy(original)`

# 9.2 fromkeys(iterable, value=None) - creates a new dictionary from keys
# Creates a dictionary with keys from iterable and values set to `value` (default None).
new_dict_from_keys = dict.fromkeys(["name", "age", "city"], "unknown")
print(f"New dict from keys: {new_dict_from_keys}")

# 9.3 setdefault(key, default_value=None) - get value or set default if key missing
# If key is in dictionary, return its value.
# If key is not in dictionary, insert key with `default_value` and return `default_value`.
data = {"name": "Bob"}
city_val = data.setdefault("city", "London")
print(f"City value (newly set): {city_val}")
print(f"Data after setdefault for 'city': {data}")

name_val = data.setdefault("name", "Alice") # 'name' already exists
print(f"Name value (already exists): {name_val}")
print(f"Data after setdefault for 'name' (no change): {data}")


# --- 10. Dictionary Views (keys(), values(), items()) ---

print("\n--- 10. Dictionary Views ---")

# As mentioned earlier, keys(), values(), and items() return "view objects".
# These views provide a dynamic view of the dictionary's contents.
# They are not lists themselves, but iterable and reflect changes to the dictionary.

view_example = {"x": 10, "y": 20}
keys_view = view_example.keys()
values_view = view_example.values()
items_view = view_example.items()

print(f"Initial keys view: {keys_view}")
print(f"Initial values view: {values_view}")
print(f"Initial items view: {items_view}")

view_example["z"] = 30 # Add a new item
view_example["x"] = 100 # Update an item

print(f"Keys view after modification: {keys_view}")
print(f"Values view after modification: {values_view}")
print(f"Items view after modification: {items_view}")

# You can convert views to lists if you need a static copy:
list_of_keys = list(view_example.keys())
print(f"List of keys: {list_of_keys}")


# --- 11. Immutability of Keys ---

print("\n--- 11. Immutability of Keys ---")

# Dictionary keys must be "hashable" objects.
# Hashable means their value does not change over their lifetime, and they have a `__hash__` method.
# Immutable types are hashable: strings, numbers (int, float, complex), tuples (if all their elements are hashable).
# Mutable types are NOT hashable: lists, sets, dictionaries.

valid_keys = {
    "string_key": 1,
    123: 2,
    3.14: 3,
    (1, 2, "a"): 4 # Tuple is hashable because its elements (int, int, str) are immutable
}
print(f"Dictionary with valid keys: {valid_keys}")

# Attempting to use a mutable type as a key will raise a TypeError
try:
    invalid_keys = {[1, 2]: "list_as_key"}
except TypeError as e:
    print(f"Error using list as key: {e}")

try:
    invalid_keys = {{'a': 1}: "dict_as_key"}
except TypeError as e:
    print(f"Error using dict as key: {e}")

try:
    invalid_keys = {{1, 2}: "set_as_key"}
except TypeError as e:
    print(f"Error using set as key: {e}")


# --- 12. Dictionary vs. List vs. Set (Brief Comparison) ---

print("\n--- 12. Dictionary vs. List vs. Set ---")

# - Lists: Ordered, mutable collections of items (accessed by integer index). Best for sequences.
my_list = [10, 20, 30]
print(f"List: {my_list}, Access by index: {my_list[0]}")

# - Sets: Unordered, mutable collections of *unique* items. Best for membership testing and eliminating duplicates.
my_set = {10, 20, 30}
print(f"Set: {my_set}, Check membership: {10 in my_set}")

# - Dictionaries: Unordered (but insertion-ordered in 3.7+), mutable collections of key-value pairs.
#   Best for mapping unique keys to values, fast lookups by key.
my_dict_comp = {"itemA": 10, "itemB": 20}
print(f"Dictionary: {my_dict_comp}, Access by key: {my_dict_comp['itemA']}")


# --- 13. Python 3.7+ Order Preservation ---

print("\n--- 13. Python 3.7+ Order Preservation ---")

# Prior to Python 3.7, dictionaries were officially unordered.
# From Python 3.7 onwards, dictionaries are guaranteed to preserve insertion order.
# This means when you iterate over a dictionary, the items will be returned
# in the order they were added.

ordered_example = {}
ordered_example["first"] = 1
ordered_example["second"] = 2
ordered_example["third"] = 3
ordered_example["fourth"] = 4

print(f"Dictionary (insertion order preserved in Python 3.7+):")
for key, value in ordered_example.items():
    print(f"{key}: {value}")

# If an existing key is updated, its position in the order does not change.
ordered_example["second"] = 200
print(f"\nDictionary after updating 'second':")
for key, value in ordered_example.items():
    print(f"{key}: {value}")

# If a key is deleted and then re-added, it will appear at the end.
del ordered_example["first"]
ordered_example["first"] = 100
print(f"\nDictionary after deleting 'first' and re-adding:")
for key, value in ordered_example.items():
    print(f"{key}: {value}")