print("--- Python None: Practice Code ---")

# --- 1. What is None? ---
print("\n--- 1. What is None? ---")
print("`None` is a special constant in Python.")
print("It represents the absence of a value or a null value.")
print("It is NOT the same as 0, an empty string (''), or False.")

# 1.1 `None` is a singleton object
# There is only one `None` object in memory.
val1 = None
val2 = None
print(f"val1: {val1}")
print(f"val2: {val2}")
print(f"val1 is val2: {val1 is val2}") # Checks if they are the exact same object in memory (True)
print(f"val1 == val2: {val1 == val2}") # Checks if their values are equal (True)


# 1.2 Type of None
print(f"Type of None: {type(None)}") # It has its own unique type: NoneType


# --- 2. Common Scenarios Where None Appears ---
print("\n--- 2. Common Scenarios Where None Appears ---")

# 2.1 Default return value of functions
# If a function doesn't explicitly return a value, it implicitly returns `None`.
def my_function_no_return():
    print("This function does not have a return statement.")

result = my_function_no_return()
print(f"Return value of my_function_no_return(): {result}")
print(f"Is result None? {result is None}")

def my_function_explicit_none():
    print("This function explicitly returns None.")
    return None

result_explicit = my_function_explicit_none()
print(f"Return value of my_function_explicit_none(): {result_explicit}")


# 2.2 Default value for function arguments (important for mutable defaults!)
print("\n2.2 Default value for function arguments:")
def add_item_to_list(item, my_list=None):
    if my_list is None: # Correct way to handle mutable default arguments
        my_list = []
    my_list.append(item)
    return my_list

list1 = add_item_to_list(1)
print(f"list1 after adding 1: {list1}")
list2 = add_item_to_list(2)
print(f"list2 after adding 2: {list2}") # list1 and list2 are separate lists

# What happens if you use a mutable default directly (BAD PRACTICE!)
def bad_add_item_to_list(item, my_bad_list=[]): # Default list created ONCE
    my_bad_list.append(item)
    return my_bad_list

bad_list1 = bad_add_item_to_list(1)
print(f"bad_list1 after adding 1: {bad_list1}")
bad_list2 = bad_add_item_to_list(2) # WARNING: This appends to the *same* default list
print(f"bad_list2 after adding 2: {bad_list2}") # Output: [1, 2] - unexpected!
# To verify they are the same object:
print(f"Are bad_list1 and bad_list2 the same object? {bad_list1 is bad_list2}") # True!

# 2.3 Initializing variables or object attributes as placeholders
user_data = None
if user_data is None:
    print("\nUser data not yet loaded.")
    user_data = {"name": "John Doe", "age": 30}
    print(f"User data loaded: {user_data}")

class User:
    def __init__(self, name):
        self.name = name
        self.email = None # Email is not set yet
        self.phone = None

user = User("Jane Smith")
print(f"Jane's email: {user.email}")
user.email = "jane@example.com"
print(f"Jane's updated email: {user.email}")


# --- 3. Checking for None ---
print("\n--- 3. Checking for None ---")
# The CORRECT way to check if a variable is None is using 'is None' or 'is not None'.

value_to_check = None
another_value = 0 # Remember 0 is falsy but not None

# Correct way: Using 'is' for identity check
if value_to_check is None:
    print("value_to_check IS None.")

if another_value is not None:
    print("another_value IS NOT None.")

# Why not use '=='?
# '==' checks for value equality, which works for None, but 'is' is preferred
# because it checks for object identity and is slightly faster/more explicit.
if value_to_check == None:
    print("value_to_check == None (This also works, but 'is' is idiomatic).")

# Pitfall: Using 'if not' (truthiness) can be misleading
# 'None' is falsy, so 'if not None' evaluates to True.
# However, many other values are also falsy (0, '', [], etc.)
if not value_to_check:
    print("value_to_check is falsy (which None is).")

if not another_value: # 0 is also falsy
    print("another_value (0) is also falsy, demonstrating why 'if not var' isn't specific to None.")


# --- 4. None and Operations ---
print("\n--- 4. None and Operations ---")

# 4.1 Arithmetic operations with None will raise TypeError
# try:
#     result = 5 + None
# except TypeError as e:
#     print(f"Caught TypeError: {e} - Cannot perform arithmetic with None.")

# 4.2 Concatenation with None will raise TypeError
# try:
#     result = "hello" + None
# except TypeError as e:
#     print(f"Caught TypeError: {e} - Cannot concatenate string with None.")

# 4.3 Calling methods on None will raise AttributeError
# try:
#     None.upper()
# except AttributeError as e:
#     print(f"Caught AttributeError: {e} - NoneType object has no 'upper' attribute.")


# --- 5. Use Cases for None ---
print("\n--- 5. Use Cases for None ---")

# 5.1 Representing an optional parameter
def greet(name, message=None):
    if message is None:
        print(f"Hello, {name}!")
    else:
        print(f"{message}, {name}!")

greet("Bob")
greet("Charlie", "Good morning")

# 5.2 Signaling an invalid state or uninitialized state
def find_item_index(items, item_to_find):
    try:
        return items.index(item_to_find)
    except ValueError:
        return None # Indicate that the item was not found

my_items = ["apple", "banana", "cherry"]
index_apple = find_item_index(my_items, "apple")
index_grape = find_item_index(my_items, "grape")

print(f"Index of 'apple': {index_apple}")
print(f"Index of 'grape': {index_grape}")

if index_grape is None:
    print("Grape was not found in the list.")


print("\n--- End of Python None Practice Code ---")