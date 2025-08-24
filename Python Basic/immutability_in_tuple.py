# --- Python Tuples: All About Immutability in Code ---

# Immutability is a core characteristic of tuples in Python.
# Once a tuple is created, its elements cannot be changed, added, or removed.

# --- 1. What Immutability Means ---

print("--- 1. What Immutability Means ---")

# When we say a tuple is immutable, it means:
# - You cannot change the value of an existing element.
# - You cannot add new elements.
# - You cannot remove existing elements.
# - You cannot reorder elements.

my_immutable_tuple = (10, 20, 30, 40)
print(f"Original Tuple: {my_immutable_tuple}")

# 1.1 Attempting to change an element (will raise TypeError)
try:
    print("\n1.1 Attempting to change an element (e.g., my_immutable_tuple[0] = 100)...")
    my_immutable_tuple[0] = 100
except TypeError as e:
    print(f"    Error: {e} - 'tuple' object does not support item assignment.")

# 1.2 Attempting to add an element (will raise AttributeError)
try:
    print("\n1.2 Attempting to add an element (e.g., my_immutable_tuple.append(50))...")
    my_immutable_tuple.append(50)
except AttributeError as e:
    print(f"    Error: {e} - 'tuple' object has no attribute 'append'.")

# 1.3 Attempting to remove an element (will raise AttributeError)
try:
    print("\n1.3 Attempting to remove an element (e.g., my_immutable_tuple.remove(20))...")
    my_immutable_tuple.remove(20)
except AttributeError as e:
    print(f"    Error: {e} - 'tuple' object has no attribute 'remove'.")

# 1.4 Attempting to delete an element using `del` (will raise TypeError)
try:
    print("\n1.4 Attempting to delete an element using del (e.g., del my_immutable_tuple[0])...")
    del my_immutable_tuple[0]
except TypeError as e:
    print(f"    Error: {e} - 'tuple' object doesn't support item deletion.")

print(f"\nOriginal tuple remains unchanged: {my_immutable_tuple}")


# --- 2. Creating New Tuples from Existing Ones (Instead of Modifying) ---

print("\n--- 2. Creating New Tuples Instead of Modifying ---")

# Since tuples are immutable, operations that seem like "modifications" actually
# result in the creation of a *new* tuple.

# 2.1 Concatenation: Joins tuples to form a new one.
tuple_a = (1, 2)
tuple_b = (3, 4)
new_combined_tuple = tuple_a + tuple_b
print(f"2.1 tuple_a: {tuple_a}, tuple_b: {tuple_b}")
print(f"    New combined tuple: {new_combined_tuple}") # (1, 2, 3, 4)
print(f"    ID of tuple_a: {id(tuple_a)}")
print(f"    ID of new_combined_tuple: {id(new_combined_tuple)}") # Different ID

# 2.2 Repetition: Repeats elements to form a new tuple.
original_pattern = ("x", "y")
new_repeated_tuple = original_pattern * 3
print(f"2.2 Original pattern: {original_pattern}")
print(f"    New repeated tuple: {new_repeated_tuple}") # ('x', 'y', 'x', 'y', 'x', 'y')
print(f"    ID of original_pattern: {id(original_pattern)}")
print(f"    ID of new_repeated_tuple: {id(new_repeated_tuple)}") # Different ID

# 2.3 Slicing: Extracts a portion, creating a new tuple.
original_data = (10, 20, 30, 40, 50)
sliced_data = original_data[1:4]
print(f"2.3 Original data: {original_data}")
print(f"    Sliced data: {sliced_data}") # (20, 30, 40)
print(f"    ID of original_data: {id(original_data)}")
print(f"    ID of sliced_data: {id(sliced_data)}") # Different ID


# --- 3. Immutability and Mutable Elements within Tuples ---

print("\n--- 3. Immutability and Mutable Elements within Tuples ---")

# This is a crucial concept: A tuple's immutability means its *references* to objects
# cannot change. However, if those referenced objects are themselves mutable (like lists
# or dictionaries), their *contents* can still be modified.

# 3.1 Tuple containing a mutable list
mutable_list_in_tuple = (1, [2, 3], 4)
print(f"3.1 Tuple with a list: {mutable_list_in_tuple}")
print(f"    ID of the tuple: {id(mutable_list_in_tuple)}")
print(f"    ID of the list inside: {id(mutable_list_in_tuple[1])}")

# Modify the list *inside* the tuple
mutable_list_in_tuple[1].append(5)
print(f"    Tuple after modifying its internal list: {mutable_list_in_tuple}")
print(f"    ID of the tuple (unchanged): {id(mutable_list_in_tuple)}")
print(f"    ID of the list inside (unchanged): {id(mutable_list_in_tuple[1])}")
# The tuple object itself is still the same, but the object it points to at index 1 has changed.

# 3.2 Tuple containing a mutable dictionary
mutable_dict_in_tuple = ("user", {"name": "Bob", "age": 30})
print(f"\n3.2 Tuple with a dictionary: {mutable_dict_in_tuple}")
mutable_dict_in_tuple[1]["age"] = 31 # Modify the dictionary inside the tuple
print(f"    Tuple after modifying its internal dictionary: {mutable_dict_in_tuple}")

# 3.3 What you *cannot* do: Reassign the mutable element itself
try:
    print("\n3.3 Attempting to reassign the list inside the tuple...")
    mutable_list_in_tuple[1] = [6, 7] # This would be reassigning the reference at index 1
except TypeError as e:
    print(f"    Error: {e} - 'tuple' object does not support item assignment.")
# This confirms that the tuple's immutability applies to its direct elements (references).


# --- 4. Why Immutability is Useful ---

print("\n--- 4. Why Immutability is Useful ---")

# 4.1 Hashability: Tuples can be used as keys in dictionaries.
# Only immutable (hashable) objects can be dictionary keys.
# A tuple is hashable if all its elements are also hashable.
# Lists, sets, and dictionaries are mutable, so they cannot be dictionary keys.

my_data = {
    (1, 2): "Point A",
    ("red", "green", "blue"): "RGB Color"
}
print(f"4.1 Tuple as dictionary keys: {my_data}")

# Attempt to use a tuple containing a list as a dictionary key (will fail)
try:
    invalid_key_dict = {(1, [2, 3]): "Invalid Key"}
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list' (tuple containing mutable list).")

# 4.2 Data Integrity: Ensures data remains constant.
# Useful for configurations, fixed constants, or data that should not be accidentally altered.
API_ENDPOINT = ("api.example.com", "/v1/data")
# No one can accidentally change API_ENDPOINT[0] or API_ENDPOINT[1]

# 4.3 Function Arguments: Often used to return multiple values from a function.
# The returned tuple is immutable, ensuring the values are not accidentally modified by the caller.
def get_user_status(user_id):
    # Imagine fetching from a database
    return "active", "admin", "premium"

status, role, plan = get_user_status(123)
print(f"4.3 User status: {status}, role: {role}, plan: {plan}")