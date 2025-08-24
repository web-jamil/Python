# --- Python: All About Mutability in Code ---

# Mutability is a core concept in Python that determines whether an object's
# state (its value or contents) can be changed after it has been created.
# Understanding mutability is crucial for writing correct and predictable Python code,
# especially when dealing with assignments, function arguments, and data structures.

# --- 1. What is Mutability? ---

print("--- 1. What is Mutability? ---")

# An object is **mutable** if its internal state can be changed.
# This means you can modify its contents without creating a new object in memory.

# An object is **immutable** if its internal state cannot be changed after creation.
# Any "modification" to an immutable object actually results in the creation of a new object.

# We can check an object's memory address using `id()` to see if it's the same object.

# 1.1 Examples of Mutable Built-in Types:
# - `list`
# - `dict` (dictionary)
# - `set`
# - `bytearray`

# 1.2 Examples of Immutable Built-in Types:
# - `int` (integers)
# - `float` (floating-point numbers)
# - `str` (strings)
# - `tuple` (tuples, provided all their elements are also immutable)
# - `bool` (Booleans)
# - `NoneType` (None)
# - `frozenset` (immutable version of set)
# - `bytes` (immutable version of bytearray)

print("Mutability determines if an object's state can change after creation.")
print("Check object ID with `id()` to see if it's the same object.")


print("\n--- 2. Demonstrating Mutability (Lists, Dictionaries, Sets) ---")

# 2.1 Lists (Mutable)
my_list = [1, 2, 3]
print(f"2.1 Original list: {my_list}")
print(f"    ID of list: {id(my_list)}")

my_list.append(4) # Modifying the list in-place
print(f"    After append(4): {my_list}")
print(f"    ID of list (unchanged): {id(my_list)}") # The ID remains the same

my_list[0] = 100 # Modifying an element in-place
print(f"    After my_list[0] = 100: {my_list}")
print(f"    ID of list (unchanged): {id(my_list)}") # The ID remains the same


# 2.2 Dictionaries (Mutable)
my_dict = {"name": "Alice", "age": 30}
print(f"\n2.2 Original dictionary: {my_dict}")
print(f"    ID of dictionary: {id(my_dict)}")

my_dict["city"] = "New York" # Adding a new key-value pair
print(f"    After adding 'city': {my_dict}")
print(f"    ID of dictionary (unchanged): {id(my_dict)}") # The ID remains the same

my_dict["age"] = 31 # Updating an existing value
print(f"    After updating 'age': {my_dict}")
print(f"    ID of dictionary (unchanged): {id(my_dict)}") # The ID remains the same


# 2.3 Sets (Mutable)
my_set = {1, 2, 3}
print(f"\n2.3 Original set: {my_set}")
print(f"    ID of set: {id(my_set)}")

my_set.add(4) # Adding an element
print(f"    After add(4): {my_set}")
print(f"    ID of set (unchanged): {id(my_set)}") # The ID remains the same

my_set.remove(2) # Removing an element
print(f"    After remove(2): {my_set}")
print(f"    ID of set (unchanged): {id(my_set)}") # The ID remains the same


print("\n--- 3. Demonstrating Immutability (Integers, Strings, Tuples) ---")

# 3.1 Integers (Immutable)
my_int = 10
print(f"3.1 Original integer: {my_int}")
print(f"    ID of integer: {id(my_int)}")

my_int = my_int + 5 # This operation creates a NEW integer object
print(f"    After my_int = my_int + 5: {my_int}")
print(f"    ID of new integer: {id(my_int)}") # The ID CHANGES

# 3.2 Strings (Immutable)
my_string = "hello"
print(f"\n3.2 Original string: {my_string}")
print(f"    ID of string: {id(my_string)}")

# Attempting to modify a character (will raise TypeError)
try:
    my_string[0] = 'H'
except TypeError as e:
    print(f"    Error: {e} - 'str' object does not support item assignment.")

my_string = my_string + " world" # This operation creates a NEW string object
print(f"    After my_string = my_string + ' world': {my_string}")
print(f"    ID of new string: {id(my_string)}") # The ID CHANGES

# 3.3 Tuples (Immutable)
# A tuple's immutability means its *references* to objects cannot change.
# However, if those referenced objects are themselves mutable, their *contents* can change.
my_tuple = (1, 2, [3, 4]) # Tuple contains a mutable list
print(f"\n3.3 Original tuple: {my_tuple}")
print(f"    ID of tuple: {id(my_tuple)}")
print(f"    ID of list inside tuple: {id(my_tuple[2])}")

# Attempt to change an element of the tuple (will raise TypeError)
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"    Error: {e} - 'tuple' object does not support item assignment.")

# Modify the *list itself* that is an element of the tuple (this IS allowed)
my_tuple[2].append(5)
print(f"    Tuple after modifying its internal list: {my_tuple}")
print(f"    ID of tuple (unchanged): {id(my_tuple)}") # The ID remains the same
print(f"    ID of list inside tuple (unchanged): {id(my_tuple[2])}") # The ID of the list remains the same


print("\n--- 4. Implications of Mutability ---")

# Understanding mutability is critical for several reasons:

# 4.1 Shared References (Aliasing):
# When you assign one variable to another that refers to a mutable object,
# both variables point to the *same* object in memory. Modifying one affects the other.
list_a = [1, 2]
list_b = list_a # list_b now refers to the SAME list object as list_a
print(f"4.1 List A: {list_a}, List B: {list_b}")
print(f"    ID of List A: {id(list_a)}, ID of List B: {id(list_b)}")

list_b.append(3) # Modifying list_b
print(f"    After list_b.append(3): List A: {list_a}, List B: {list_b}")
# Both list_a and list_b now show [1, 2, 3] because they are the same object.

# To create an independent copy, use `list.copy()` (shallow copy) or `copy.deepcopy()`.
import copy
list_c = list_a.copy() # Creates a shallow copy
print(f"    List C (shallow copy of List A): {list_c}")
print(f"    ID of List C: {id(list_c)}")
list_c.append(4)
print(f"    After list_c.append(4): List A: {list_a}, List C: {list_c}") # List A is now unaffected

# 4.2 Function Arguments:
# When you pass a mutable object to a function, the function receives a reference
# to the original object. If the function modifies the object, those changes
# will be visible outside the function (a "side effect").
def modify_list_in_function(a_list):
    a_list.append("new_item")
    print(f"    Inside function: {a_list}")

my_original_list = ["item1", "item2"]
print(f"\n4.2 Before function call: {my_original_list}")
modify_list_in_function(my_original_list)
print(f"    After function call: {my_original_list}") # List was modified by the function

# If you don't want the function to modify the original list, pass a copy:
my_other_list = ["itemA", "itemB"]
print(f"    Before function call (with copy): {my_other_list}")
modify_list_in_function(my_other_list.copy()) # Pass a shallow copy
print(f"    After function call (with copy): {my_other_list}") # Original list is unchanged

# 4.3 Hashing (Dictionary Keys and Set Elements):
# - Mutable objects are generally NOT hashable. This means they cannot be used
#   as keys in dictionaries or as elements in sets.
# - This is because their hash value could change if their content changes,
#   which would break the efficient lookup mechanism of hash-based collections.
try:
    my_dict_invalid_key = {[1, 2]: "value"}
except TypeError as e:
    print(f"\n4.3 Error: {e} - Cannot use mutable list as dictionary key.")

# 4.4 Default Arguments in Functions:
# Using mutable objects as default arguments in function definitions can lead
# to unexpected behavior because the default object is created only once.
def add_to_list(item, my_list_arg=[]): # DANGER: my_list_arg is created once
    my_list_arg.append(item)
    return my_list_arg

print(f"\n4.4 Dangerous mutable default argument:")
print(add_to_list(1)) # [1]
print(add_to_list(2)) # [1, 2] - Unexpected! The same list object is reused.
print(add_to_list(3, [])) # [3] - This creates a new list for this call

# Correct way to handle mutable default arguments:
def add_to_list_safe(item, my_list_arg=None):
    if my_list_arg is None:
        my_list_arg = [] # Create a new list each time if not provided
    my_list_arg.append(item)
    return my_list_arg

print(f"\n    Safe mutable default argument:")
print(add_to_list_safe(1)) # [1]
print(add_to_list_safe(2)) # [2] - Correct behavior
print(add_to_list_safe(3, [])) # [3]


print("\n--- 7. Conclusion ---")
print("Mutability is a core concept that affects how objects behave,")
print("especially with assignments, function calls, and data structures.")
print("Be mindful of whether an object is mutable or immutable to write robust Python code.")