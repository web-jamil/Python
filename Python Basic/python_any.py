print("--- Python any() Function: Practice Code ---")

# --- 1. What is any()? ---
print("\n--- 1. What is any()? ---")
print("The `any()` function returns `True` if any element of an iterable is true.")
print("If the iterable is empty, it returns `False`.")
print("It's a built-in function, part of Python's standard library.")


# --- 2. Syntax of any() ---
print("\n--- 2. Syntax of any() ---")
print("Syntax: any(iterable)")

# `iterable`: Any iterable (list, tuple, set, string, dictionary, generator, etc.)
#             whose elements will be evaluated for truthiness.


# --- 3. How any() Works (Truthiness) ---
print("\n--- 3. How any() Works (Truthiness) ---")
print("`any()` evaluates the truthiness of each element in the iterable.")
print("It stops and returns `True` as soon as it finds the first truthy element (short-circuiting).")
print("If it iterates through all elements and finds no truthy ones, it returns `False`.")

# Remember common Falsy values in Python:
# - `False`
# - `None`
# - `0` (integer, float)
# - Empty sequences: `''`, `[]`, `()`, `{}`
# - Empty ranges: `range(0)`

# All other values are generally Truthy.

# Example 1: Basic True/False values
print(f"any([True, False, False]): {any([True, False, False])}") # True (stops at first True)
print(f"any([False, False, False]): {any([False, False, False])}") # False
print(f"any([True, True, True]): {any([True, True, True])}")     # True (stops at first True)

# Example 2: Numbers
print(f"any([0, 1, 2]): {any([0, 1, 2])}")     # True (1 is truthy)
print(f"any([0, 0.0, False]): {any([0, 0.0, False])}") # False (all are falsy)

# Example 3: Strings and Empty Sequences
print(f"any(['', 'hello', 'world']): {any(['', 'hello', 'world'])}") # True ('hello' is truthy)
print(f"any(['', [], {}, 0]): {any(['', [], {}, 0])}") # False (all are falsy)
print(f"any([' ']): {any([' '])}") # True (a space is a truthy string)

# Example 4: Empty Iterable
print(f"any([]): {any([])}") # False
print(f"any(()): {any(())}") # False
print(f"any({}): {any({})}") # False
print(f"any(''): {any('')}") # False


# --- 4. Short-Circuiting Behavior ---
print("\n--- 4. Short-Circuiting Behavior ---")
print("`any()` is efficient because it stops processing as soon as a `True` condition is met.")

def check_truthy(value):
    print(f"Checking: {value}")
    return bool(value)

print("\nDemonstrating short-circuiting with any():")
result_short_circuit = any([False, 0, 'hello', True, 5])
print(f"Result: {result_short_circuit}")
# Output will show "Checking: False", "Checking: 0", "Checking: hello", then stop and return True.


# --- 5. Common Use Cases for any() ---
print("\n--- 5. Common Use Cases for any() ---")

# 5.1 Checking if any element in a list meets a condition
print("\n5.1 Checking if any element meets a condition:")
scores = [55, 60, 72, 45, 80]
# Is any score greater than 90?
any_over_90 = any(score > 90 for score in scores) # Using a generator expression
print(f"Scores: {scores}")
print(f"Is any score > 90? {any_over_90}")

# Is any score less than 50?
any_under_50 = any(score < 50 for score in scores)
print(f"Is any score < 50? {any_under_50}")

# 5.2 Validating user input (e.g., if any field is empty)
print("\n5.2 Validating user input:")
user_fields = ["John Doe", "", "john.doe@example.com"]
if any(not field for field in user_fields): # Checks if any field is empty/falsy
    print("Warning: One or more user fields are empty.")
else:
    print("All user fields are filled.")

user_fields_filled = ["Jane Doe", "jane@example.com"]
if any(not field for field in user_fields_filled):
    print("Warning: One or more user fields are empty.")
else:
    print("All user fields are filled.")

# 5.3 Checking for existence of specific properties in objects
print("\n5.3 Checking for existence of specific properties in objects:")
products = [
    {'name': 'Laptop', 'in_stock': False},
    {'name': 'Mouse', 'in_stock': True},
    {'name': 'Keyboard', 'in_stock': False}
]
# Is any product in stock?
any_product_in_stock = any(product['in_stock'] for product in products)
print(f"Products: {products}")
print(f"Is any product in stock? {any_product_in_stock}")

# 5.4 With dictionaries (checks truthiness of keys by default)
print("\n5.4 With dictionaries:")
my_dict = {'a': 1, 'b': 0, 'c': False}
print(f"any({my_dict}) (checks keys): {any(my_dict)}") # True ('a' is truthy)

# To check values, use .values()
print(f"any({my_dict.values()}) (checks values): {any(my_dict.values())}") # True (1 is truthy)

# To check items (tuples of key-value pairs)
print(f"any({my_dict.items()}) (checks items): {any(my_dict.items())}") # True (('a',1) is truthy)

# 5.5 Checking for presence of a specific character in a string
word = "banana"
has_z = any(char == 'z' for char in word)
print(f"Does '{word}' contain 'z'? {has_z}")
has_a = any(char == 'a' for char in word)
print(f"Does '{word}' contain 'a'? {has_a}")


# --- 6. Comparison with `all()` ---
print("\n--- 6. Comparison with `all()` ---")
print("`any()` returns True if *at least one* element is true.")
print("`all()` returns True if *all* elements are true (or if the iterable is empty).")

bool_list_1 = [True, False, True]
bool_list_2 = [True, True, True]
bool_list_3 = [False, False]

print(f"any({bool_list_1}): {any(bool_list_1)}, all({bool_list_1}): {all(bool_list_1)}")
print(f"any({bool_list_2}): {any(bool_list_2)}, all({bool_list_2}): {all(bool_list_2)}")
print(f"any({bool_list_3}): {any(bool_list_3)}, all({bool_list_3}): {all(bool_list_3)}")

print(f"any([]): {any([])}, all([]): {all([])}") # all([]) is True, any([]) is False


print("\n--- End of Python any() Function Practice Code ---")