# --- Python Dictionaries: All About Removing Elements in Code ---

# Dictionaries are mutable, meaning you can add, modify, and remove elements
# (key-value pairs) after the dictionary has been created.

# Let's start with a sample dictionary for demonstration.
student_info = {
    "id": "S001",
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["CS101", "MA201", "PH101"],
    "is_enrolled": True
}

print("--- 1. Removing Elements using `del` keyword ---")

# The `del` keyword is used to delete a specific key-value pair from the dictionary.
# If the key does not exist, it will raise a KeyError.

# 1.1 Deleting an existing key-value pair
print(f"1.1 Before deleting 'gpa': {student_info}")
del student_info["gpa"]
print(f"    After deleting 'gpa': {student_info}")

# 1.2 Attempting to delete a non-existent key (raises KeyError)
try:
    print("\n1.2 Attempting to delete 'address' (non-existent key)...")
    del student_info["address"]
except KeyError as e:
    print(f"    Error: {e} - Key 'address' not found.")

# 1.3 Deleting nested dictionary elements
# You can use `del` to remove items from nested dictionaries as well.
course_grades = {
    "math": {"quiz1": 85, "quiz2": 90, "final": 92},
    "physics": {"quiz1": 70, "quiz2": 75, "final": 80}
}
print(f"\n1.3 Before deleting 'quiz2' from 'math': {course_grades}")
del course_grades["math"]["quiz2"]
print(f"    After deleting 'quiz2' from 'math': {course_grades}")


print("\n--- 2. Removing Elements using `pop()` method ---")

# The `pop()` method removes the specified key and returns its corresponding value.
# This is useful when you need the value of the removed item.

# 2.1 Removing an existing key and retrieving its value
# Syntax: dictionary.pop(key)
print(f"2.1 Before pop('major'): {student_info}")
removed_major = student_info.pop("major")
print(f"    Removed major: {removed_major}")
print(f"    After pop('major'): {student_info}")

# 2.2 Removing a non-existent key (raises KeyError by default)
try:
    print("\n2.2 Attempting to pop 'phone' (non-existent key)...")
    student_info.pop("phone")
except KeyError as e:
    print(f"    Error: {e} - Key 'phone' not found.")

# 2.3 Removing a non-existent key with a default return value
# Syntax: dictionary.pop(key, default_value)
# If the key is not found, it returns the `default_value` instead of raising an error.
print("\n2.3 Attempting to pop 'address' with a default value...")
removed_address = student_info.pop("address", "Address not found")
print(f"    Removed address: {removed_address}")
print(f"    Dictionary remains unchanged: {student_info}") # No change as key wasn't there

# 2.4 Pop from nested dictionaries
# You can use pop on nested dictionaries.
removed_final_grade = course_grades["physics"].pop("final")
print(f"\n2.4 Removed final grade from physics: {removed_final_grade}")
print(f"    Course grades after pop: {course_grades}")


print("\n--- 3. Removing Elements using `popitem()` method ---")

# The `popitem()` method removes and returns an arbitrary key-value pair.
# In Python 3.7+, it guarantees to remove and return the *last inserted* key-value pair.
# It raises a KeyError if the dictionary is empty.

# Let's create a new dictionary to demonstrate popitem's order (Python 3.7+ behavior)
order_dict = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4
}
print(f"\n3.1 Before popitem(): {order_dict}")

# Remove the last inserted item
last_item_removed = order_dict.popitem()
print(f"    Removed item with popitem(): {last_item_removed}")
print(f"    After first popitem(): {order_dict}")

# Remove another item
another_item_removed = order_dict.popitem()
print(f"    Removed item with popitem(): {another_item_removed}")
print(f"    After second popitem(): {order_dict}")

# Attempting to popitem from an empty dictionary
empty_dict = {}
try:
    print("\n3.2 Attempting to popitem from an empty dictionary...")
    empty_dict.popitem()
except KeyError as e:
    print(f"    Error: {e} - Cannot pop from an empty dictionary.")


print("\n--- 4. Removing All Elements using `clear()` method ---")

# The `clear()` method removes all key-value pairs from the dictionary,
# making it empty. It does not return any value.

# Create a dictionary to clear
data_to_clear = {
    "item1": 10,
    "item2": 20,
    "item3": 30
}
print(f"4.1 Before clear(): {data_to_clear}")

data_to_clear.clear()
print(f"    After clear(): {data_to_clear}")


print("\n--- 5. Deleting the Entire Dictionary Object ---")

# While not strictly "removing elements from a dictionary," you can delete
# the dictionary variable itself from memory using `del`.

# Create a dictionary to delete
my_config = {
    "host": "localhost",
    "port": 8000
}
print(f"5.1 Before deleting the variable: {my_config}")

del my_config # Deletes the variable `my_config`

# Attempting to access the deleted variable will result in a NameError
try:
    print(my_config)
except NameError as e:
    print(f"    Error: {e} - The dictionary variable 'my_config' no longer exists.")


print("\n--- 6. Iterating and Removing (Important Considerations) ---")

# It's generally unsafe to modify a dictionary (add/remove items)
# while you are iterating over it directly. This can lead to unexpected behavior
# or runtime errors (e.g., `RuntimeError: dictionary changed size during iteration`).

# 6.1 Unsafe way (will likely cause RuntimeError)
# This code is commented out because it's problematic.
# my_collection = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# try:
#     for key, value in my_collection.items():
#         if value % 2 == 0:
#             del my_collection[key] # Modifying during iteration
# except RuntimeError as e:
#     print(f"\n6.1 UNSAFE: Caught expected RuntimeError: {e}")
# print(f"    Result of unsafe operation: {my_collection}")

# 6.2 Safe way 1: Iterate over a copy of keys or items
# Create a list of keys to iterate over, then modify the original dictionary.
my_collection_safe = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"\n6.2 SAFE Way 1: Original: {my_collection_safe}")
keys_to_remove = [key for key, value in my_collection_safe.items() if value % 2 == 0]
for key in keys_to_remove:
    del my_collection_safe[key]
print(f"    After safe removal: {my_collection_safe}")

# 6.3 Safe way 2: Create a new dictionary with desired elements
# This is often the most Pythonic and safest approach for filtering.
original_data = {'itemX': 100, 'itemY': 200, 'itemZ': 300}
print(f"\n6.3 SAFE Way 2: Original: {original_data}")
filtered_data = {key: value for key, value in original_data.items() if value < 250}
print(f"    New dictionary with filtered elements: {filtered_data}")