# --- Python: All About Mutability in Data Structures in Code ---

# Mutability is a fundamental concept in Python that refers to whether
# an object's state (its value or contents) can be changed after it is created.

# --- 1. What is Mutability? ---

print("--- 1. What is Mutability? ---")

# A mutable object is one whose value can be altered in-place after it's been created.
# This means you can change its contents without creating a new object in memory.

# 1.1 Examples of Mutable Built-in Data Structures:
# - `list`
# - `dict` (dictionary)
# - `set`
# - `bytearray`

# 1.2 Examples of Immutable Built-in Data Structures:
# - `int` (integers)
# - `float` (floating-point numbers)
# - `str` (strings)
# - `tuple` (tuples, provided all their elements are also immutable)
# - `bool` (Booleans)
# - `NoneType` (None)
# - `frozenset` (immutable version of set)
# - `bytes` (immutable version of bytearray)

# We'll demonstrate mutability with lists, dictionaries, and sets.


print("\n--- 2. Mutability in Lists ---")

# Lists are mutable sequences. You can add, remove, or change elements after creation.

my_list = [1, 2, 3]
print(f"2.1 Original list: {my_list}")
print(f"    Memory address (ID) of list: {id(my_list)}")

# 2.1 Modifying an element by index
my_list[0] = 100
print(f"    After modifying element at index 0: {my_list}")
print(f"    Memory address (ID) of list (unchanged): {id(my_list)}") # Same ID

# 2.2 Adding an element (`append()`)
my_list.append(4)
print(f"    After appending 4: {my_list}")
print(f"    Memory address (ID) of list (unchanged): {id(my_list)}") # Same ID

# 2.3 Removing an element (`remove()`)
my_list.remove(2)
print(f"    After removing 2: {my_list}")
print(f"    Memory address (ID) of list (unchanged): {id(my_list)}") # Same ID

# 2.4 Modifying a slice
my_list[1:3] = [200, 300] # Replaces elements at index 1 and 2
print(f"    After modifying slice [1:3]: {my_list}")
print(f"    Memory address (ID) of list (unchanged): {id(my_list)}") # Same ID

# Contrast with immutable strings:
my_string = "hello"
print(f"\n2.5 Original string: {my_string}")
print(f"    Memory address (ID) of string: {id(my_string)}")
# my_string[0] = 'H' # This would raise a TypeError

# If you "change" a string, you're actually creating a new one:
my_string = my_string + " world"
print(f"    After 'changing' string: {my_string}")
print(f"    Memory address (ID) of new string: {id(my_string)}") # Different ID


print("\n--- 3. Mutability in Dictionaries ---")

# Dictionaries are mutable collections of key-value pairs.

my_dict = {"name": "Alice", "age": 30}
print(f"3.1 Original dictionary: {my_dict}")
print(f"    Memory address (ID) of dictionary: {id(my_dict)}")

# 3.1 Adding a new key-value pair
my_dict["city"] = "New York"
print(f"    After adding 'city': {my_dict}")
print(f"    Memory address (ID) of dictionary (unchanged): {id(my_dict)}") # Same ID

# 3.2 Updating an existing value
my_dict["age"] = 31
print(f"    After updating 'age': {my_dict}")
print(f"    Memory address (ID) of dictionary (unchanged): {id(my_dict)}") # Same ID

# 3.3 Removing a key-value pair (`del` or `pop()`)
del my_dict["city"]
print(f"    After deleting 'city': {my_dict}")
print(f"    Memory address (ID) of dictionary (unchanged): {id(my_dict)}") # Same ID


print("\n--- 4. Mutability in Sets ---")

# Sets are mutable, unordered collections of unique elements.

my_set = {1, 2, 3}
print(f"4.1 Original set: {my_set}")
print(f"    Memory address (ID) of set: {id(my_set)}")

# 4.1 Adding an element
my_set.add(4)
print(f"    After adding 4: {my_set}")
print(f"    Memory address (ID) of set (unchanged): {id(my_set)}") # Same ID

# 4.2 Removing an element
my_set.remove(2)
print(f"    After removing 2: {my_set}")
print(f"    Memory address (ID) of set (unchanged): {id(my_set)}") # Same ID


print("\n--- 5. The Concept of Immutable Objects Containing Mutable Objects ---")

# This is a common point of confusion. An immutable object (like a tuple) can
# contain references to mutable objects (like lists). The tuple itself cannot
# be changed, but the *contents* of the mutable object it refers to *can* be changed.

my_tuple_with_list = (1, [2, 3], 4)
print(f"5.1 Original tuple: {my_tuple_with_list}")
print(f"    ID of the tuple: {id(my_tuple_with_list)}")
print(f"    ID of the list inside the tuple: {id(my_tuple_with_list[1])}")

# Attempt to change an element of the tuple (will fail)
try:
    my_tuple_with_list[0] = 100
except TypeError as e:
    print(f"    Error: {e} - Tuples do not support item assignment.")

# Modify the *list itself* that is an element of the tuple (this IS allowed)
my_tuple_with_list[1].append(5)
print(f"    Tuple after modifying its internal list: {my_tuple_with_list}")
print(f"    ID of the tuple (unchanged): {id(my_tuple_with_list)}")
print(f"    ID of the list inside the tuple (unchanged): {id(my_tuple_with_list[1])}")
# The tuple object itself is still the same, but the object it refers to at index 1 has changed.


print("\n--- 6. Implications of Mutability ---")

# 6.1 In-place Modification:
# - Pros: Efficient, avoids creating new objects for every change, saving memory and CPU.
# - Cons: Can lead to unexpected side effects if multiple parts of your code
#         hold references to the same mutable object and modify it.

# Example: Shared reference
list_a = [1, 2]
list_b = list_a # list_b now refers to the SAME list object as list_a
print(f"6.1 List A: {list_a}, List B: {list_b}")
print(f"    ID of List A: {id(list_a)}, ID of List B: {id(list_b)}")

list_b.append(3) # Modifying list_b
print(f"    After list_b.append(3): List A: {list_a}, List B: {list_b}")
# Both list_a and list_b now show [1, 2, 3] because they are the same object.

# To avoid this, use `copy()` for a shallow copy or `copy.deepcopy()` for a deep copy.
import copy
list_c = list_a.copy() # Shallow copy
print(f"    List C (shallow copy of List A): {list_c}")
print(f"    ID of List C: {id(list_c)}")
list_c.append(4)
print(f"    After list_c.append(4): List A: {list_a}, List C: {list_c}") # List A is unchanged now

# 6.2 Hashing:
# - Mutable objects are generally not hashable (cannot be used as dictionary keys or set elements).
# - This is because their hash value could change if their content changes, breaking
#   the lookup mechanism of hash-based collections.
try:
    my_dict_invalid_key = {[1, 2]: "value"}
except TypeError as e:
    print(f"\n6.2 Error: {e} - Cannot use mutable list as dictionary key.")

# 6.3 Function Arguments:
# - When you pass a mutable object to a function, the function receives a reference
#   to the original object. If the function modifies the object, those changes
#   will be visible outside the function (side effect).
def modify_list_in_function(a_list):
    a_list.append("new_item")
    print(f"    Inside function: {a_list}")

my_original_list = ["item1", "item2"]
print(f"\n6.3 Before function call: {my_original_list}")
modify_list_in_function(my_original_list)
print(f"    After function call: {my_original_list}") # List was modified by the function

# If you don't want the function to modify the original list, pass a copy:
my_other_list = ["itemA", "itemB"]
print(f"    Before function call (with copy): {my_other_list}")
modify_list_in_function(my_other_list.copy()) # Pass a copy
print(f"    After function call (with copy): {my_other_list}") # Original list is unchanged