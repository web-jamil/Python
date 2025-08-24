print("--- Python all() Function: Practice Code ---")

# --- 1. What is all()? ---
print("\n--- 1. What is all()? ---")
print("The `all()` function returns `True` if all elements of an iterable are true (or if the iterable is empty).")
print("It's a built-in function, part of Python's standard library.")


# --- 2. Syntax of all() ---
print("\n--- 2. Syntax of all() ---")
print("Syntax: all(iterable)")

# `iterable`: Any iterable (list, tuple, set, string, dictionary, generator, etc.)
#             whose elements will be evaluated for truthiness.


# --- 3. How all() Works (Truthiness) ---
print("\n--- 3. How all() Works (Truthiness) ---")
print("`all()` evaluates the truthiness of each element in the iterable.")
print("It stops and returns `False` as soon as it finds the first falsy element (short-circuiting).")
print("If it iterates through all elements and all are truthy, or if the iterable is empty, it returns `True`.")

# Remember common Falsy values in Python:
# - `False`
# - `None`
# - `0` (integer, float)
# - Empty sequences: `''`, `[]`, `()`, `{}`
# - Empty ranges: `range(0)`

# All other values are generally Truthy.

# Example 1: Basic True/False values
print(f"all([True, True, True]): {all([True, True, True])}")     # True
print(f"all([True, False, True]): {all([True, False, True])}")   # False (stops at False)
print(f"all([False, False, False]): {all([False, False, False])}") # False

# Example 2: Numbers
print(f"all([1, 2, 3]): {all([1, 2, 3])}")     # True (all are truthy)
print(f"all([1, 0, 3]): {all([1, 0, 3])}")     # False (0 is falsy)
print(f"all([-1, -2, -3]): {all([-1, -2, -3])}") # True (non-zero numbers are truthy)

# Example 3: Strings and Empty Sequences
print(f"all(['hello', 'world']): {all(['hello', 'world'])}") # True (both are truthy)
print(f"all(['hello', '', 'world']): {all(['hello', '', 'world'])}") # False (empty string is falsy)
print(f"all([' ']): {all([' '])}") # True (a space is a truthy string)

# Example 4: Empty Iterable - IMPORTANT BEHAVIOR
print(f"all([]): {all([])}") # True (This is a common interview question)
print(f"all(()): {all(())}") # True
print(f"all({}): {all({})}") # True
print(f"all(''): {all('')}") # True
print("Rule: `all()` returns True for an empty iterable because 'all' of its elements (which are none) satisfy the condition.")


# --- 4. Short-Circuiting Behavior ---
print("\n--- 4. Short-Circuiting Behavior ---")
print("`all()` is efficient because it stops processing as soon as a `False` condition is met.")

def check_truthy(value):
    print(f"Checking: {value}")
    return bool(value)

print("\nDemonstrating short-circuiting with all():")
result_short_circuit = all([True, 1, '', "hello", True])
print(f"Result: {result_short_circuit}")
# Output will show "Checking: True", "Checking: 1", "Checking: ", then stop and return False.


# --- 5. Common Use Cases for all() ---
print("\n--- 5. Common Use Cases for all() ---")

# 5.1 Checking if all elements in a list meet a condition
print("\n5.1 Checking if all elements meet a condition:")
scores = [75, 80, 92, 65, 88]
# Are all scores greater than 60?
all_pass = all(score > 60 for score in scores) # Using a generator expression
print(f"Scores: {scores}")
print(f"Are all scores > 60? {all_pass}")

scores_strict = [95, 88, 92]
all_pass_strict = all(score > 90 for score in scores_strict)
print(f"Scores (strict): {scores_strict}")
print(f"Are all scores > 90? {all_pass_strict}")

# 5.2 Validating user input (e.g., if all fields are non-empty)
print("\n5.2 Validating user input:")
user_data_incomplete = ["John Doe", "", "john.doe@example.com"]
if all(user_data_incomplete): # Checks if all elements are truthy (non-empty)
    print("All user data is complete.")
else:
    print("Error: Some user data is missing.")

user_data_complete = ["Jane Doe", "30", "jane@example.com"]
if all(user_data_complete):
    print("All user data is complete.")
else:
    print("Error: Some user data is missing.")

# 5.3 Checking for specific properties across objects
print("\n5.3 Checking for specific properties across objects:")
products = [
    {'name': 'Laptop', 'available': True},
    {'name': 'Mouse', 'available': True},
    {'name': 'Keyboard', 'available': False}
]
# Are all products available?
all_products_available = all(product['available'] for product in products)
print(f"Products: {products}")
print(f"Are all products available? {all_products_available}")

# 5.4 With dictionaries (checks truthiness of keys by default)
print("\n5.4 With dictionaries:")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"all({my_dict}) (checks keys): {all(my_dict)}") # True ('a', 'b', 'c' are truthy)

my_dict_falsy_key = {'a': 1, '': 2}
print(f"all({my_dict_falsy_key}) (checks keys): {all(my_dict_falsy_key)}") # False ('' is falsy)

# To check values, use .values()
print(f"all({my_dict.values()}) (checks values): {all(my_dict.values())}") # True (1, 2, 3 are truthy)

my_dict_falsy_value = {'a': 1, 'b': 0}
print(f"all({my_dict_falsy_value.values()}) (checks values): {all(my_dict_falsy_value.values())}") # False (0 is falsy)


# 5.5 Ensuring all characters in a string are digits
pin = "12345"
is_digit_pin = all(char.isdigit() for char in pin)
print(f"Is '{pin}' all digits? {is_digit_pin}")

pin_invalid = "123a5"
is_digit_pin_invalid = all(char.isdigit() for char in pin_invalid)
print(f"Is '{pin_invalid}' all digits? {is_digit_pin_invalid}")


# --- 6. Comparison with `any()` ---
print("\n--- 6. Comparison with `any()` ---")
print("`all()` returns True if *all* elements are true (or if the iterable is empty).")
print("`any()` returns True if *at least one* element is true (or if the iterable is not empty and has truthy values).")

bool_list_1 = [True, False, True]
bool_list_2 = [True, True, True]
bool_list_3 = [False, False]

print(f"all({bool_list_1}): {all(bool_list_1)}, any({bool_list_1}): {any(bool_list_1)}")
print(f"all({bool_list_2}): {all(bool_list_2)}, any({bool_list_2}): {any(bool_list_2)}")
print(f"all({bool_list_3}): {all(bool_list_3)}, any({bool_list_3}): {any(bool_list_3)}")

print(f"all([]): {all([])}, any([]): {any([])}")


print("\n--- End of Python all() Function Practice Code ---")