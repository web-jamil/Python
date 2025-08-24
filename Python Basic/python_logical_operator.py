print("--- Python Logical Operators ---")
print("------------------------------\n")

# Logical operators are used to combine conditional statements.
# They evaluate expressions and return a Boolean value (True or False).
# Python's logical operators also exhibit "short-circuiting" behavior.

# Define some variables for demonstration
x = 10
y = 5
z = 15
is_sunny = True
is_raining = False
empty_string = ""
non_empty_string = "hello"
zero_num = 0
positive_num = 100
empty_list = []
non_empty_list = [1, 2, 3]
none_val = None

print(f"Variables used:\n"
      f"  x={x}, y={y}, z={z}\n"
      f"  is_sunny={is_sunny}, is_raining={is_raining}\n"
      f"  empty_string='{empty_string}', non_empty_string='{non_empty_string}'\n"
      f"  zero_num={zero_num}, positive_num={positive_num}\n"
      f"  empty_list={empty_list}, non_empty_list={non_empty_list}\n"
      f"  none_val={none_val}\n")

# --- 1. `and` Operator ---
print("1. `and` Operator:")
# Returns True if BOTH operands are true.
# If the left operand is False, it returns the left operand immediately (short-circuits).
# Otherwise, it evaluates the right operand and returns its value.

print(f"({x} > {y}) and ({z} > {x}): { (x > y) and (z > x) }") # True and True -> True
print(f"({x} < {y}) and ({z} > {x}): { (x < y) and (z > x) }") # False and True -> False (short-circuits after (x < y))
print(f"({x} > {y}) and ({z} < {x}): { (x > y) and (z < x) }") # True and False -> False
print(f"({x} < {y}) and ({z} < {x}): { (x < y) and (z < x) }") # False and False -> False (short-circuits after (x < y))

print(f"\nShort-circuiting with 'and':")
result_and_1 = is_raining and (x / zero_num) # is_raining is False, so division is not attempted
print(f"{is_raining} and (x / zero_num) -> {result_and_1} (no ZeroDivisionError)")

result_and_2 = is_sunny and non_empty_string # is_sunny is True, evaluates non_empty_string
print(f"{is_sunny} and '{non_empty_string}' -> '{result_and_2}' (returns right operand's value)\n")


# --- 2. `or` Operator ---
print("2. `or` Operator:")
# Returns True if AT LEAST ONE of the operands is true.
# If the left operand is True, it returns the left operand immediately (short-circuits).
# Otherwise, it evaluates the right operand and returns its value.

print(f"({x} > {y}) or ({z} > {x}): { (x > y) or (z > x) }") # True or True -> True (short-circuits after (x > y))
print(f"({x} < {y}) or ({z} > {x}): { (x < y) or (z > x) }") # False or True -> True
print(f"({x} > {y}) or ({z} < {x}): { (x > y) or (z < x) }") # True or False -> True (short-circuits after (x > y))
print(f"({x} < {y}) or ({z} < {x}): { (x < y) or (z < x) }") # False or False -> False

print(f"\nShort-circuiting with 'or':")
result_or_1 = is_sunny or (x / zero_num) # is_sunny is True, so division is not attempted
print(f"{is_sunny} or (x / zero_num) -> {result_or_1} (no ZeroDivisionError)")

result_or_2 = empty_string or non_empty_list # empty_string is Falsy, evaluates non_empty_list
print(f"'{empty_string}' or {non_empty_list} -> {result_or_2} (returns right operand's value)\n")


# --- 3. `not` Operator ---
print("3. `not` Operator:")
# Reverses the logical state of its operand.
# Returns True if the operand is False.
# Returns False if the operand is True.

print(f"not {is_sunny}: { not is_sunny }") # not True -> False
print(f"not {is_raining}: { not is_raining }") # not False -> True
print(f"not ({x} == {y}): { not (x == y) }") # not False -> True
print(f"not ({x} != {y}): { not (x != y) }\n") # not True -> False


# --- Truthiness and Falsiness ---
print("--- Truthiness and Falsiness (What evaluates to True/False) ---\n")
# In Python, various values are considered "falsy" in a boolean context:
# - `False`
# - `None`
# - Numeric zero: `0`, `0.0`, `0j`
# - Empty sequences: `''` (empty string), `[]` (empty list), `()` (empty tuple)
# - Empty mappings: `{}` (empty dictionary)
# - Empty sets: `set()`

# All other values are considered "truthy".

print(f"bool(False): {bool(False)}")
print(f"bool(None): {bool(None)}")
print(f"bool(0): {bool(0)}")
print(f"bool(0.0): {bool(0.0)}")
print(f"bool(''): {bool(empty_string)}")
print(f"bool([]): {bool(empty_list)}")
print(f"bool({{}}): {bool({})}")
print(f"bool(set()): {bool(set())}\n")

print(f"bool(True): {bool(True)}")
print(f"bool(1): {bool(1)}")
print(f"bool(-5): {bool(-5)}")
print(f"bool('hi'): {bool(non_empty_string)}")
print(f"bool([1]): {bool(non_empty_list)}\n")


# --- Combining Operators ---
print("--- Combining Logical Operators (Precedence) ---\n")
# Precedence: `not` > `and` > `or`
# You can use parentheses to override the default precedence.

# Example: (A and B) or C
# (x > y and z < x) or is_sunny
# (True and False) or True
# False or True -> True
print(f"({x} > {y} and {z} < {x}) or {is_sunny}: { (x > y and z < x) or is_sunny }")

# Example: A and (B or C)
# is_sunny and (is_raining or x > y)
# True and (False or True)
# True and True -> True
print(f"{is_sunny} and ({is_raining} or {x} > {y}): { is_sunny and (is_raining or x > y) }\n")

# Practical use in conditional statements
age = 25
has_license = True
is_drunk = False

if age >= 18 and has_license and not is_drunk:
    print("Person is eligible to drive.\n")
else:
    print("Person is NOT eligible to drive.\n")

user_input = ""
if user_input or positive_num: # Checks if user_input is non-empty, otherwise uses positive_num
    print("At least one value is truthy.\n")


print("--- End of Python Logical Operators Demonstration ---")