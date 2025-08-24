# ---------------------------------------------------
# Boolean Type (bool) in Python
# ---------------------------------------------------

# 1. Basic Boolean Values: True and False
#    - Booleans are a subtype of integers. True is 1, False is 0.

is_active = True
has_permission = False

print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"has_permission: {has_permission}, type: {type(has_permission)}")
print(f"True + 1 = {True + 1}")   # Output: 2
print(f"False + 1 = {False + 1}") # Output: 1

# 2. Boolean Operators
#    - and: Logical AND. Returns True if both operands are True.
#    - or:  Logical OR. Returns True if at least one operand is True.
#    - not: Logical NOT. Inverts the boolean value.

a = True
b = False
c = True

print(f"a and b: {a and b}") # False
print(f"a or b: {a or b}")   # True
print(f"not a: {not a}")     # False
print(f"a and c: {a and c}") # True

# 3. Comparisons that Yield Booleans
#    - Relational operators produce boolean results.

x = 10
y = 20

print(f"x < y: {x < y}")     # True
print(f"x > y: {x > y}")     # False
print(f"x == 10: {x == 10}") # True (Equality check, not assignment)
print(f"x != y: {x != y}")   # True
print(f"x <= 10: {x <= 10}") # True
print(f"y >= 30: {y >= 30}") # False

# 4. Boolean Contexts (Truthiness and Falsiness)
#    - In Python, various values are implicitly treated as True or False
#      when used in a boolean context (e.g., if statements, while loops).

#    - Falsy Values:
#      - None
#      - False
#      - Numeric zero of all types (0, 0.0, 0j)
#      - Empty sequences ('', [], ())
#      - Empty mappings ({}, set())

print("\n--- Falsy Values ---")
if None:
    print("None is True")
else:
    print("None is False (Falsy)")

if 0:
    print("0 is True")
else:
    print("0 is False (Falsy)")

if "":
    print("'' is True")
else:
    print("'' is False (Falsy)")

if []:
    print("[] is True")
else:
    print("[] is False (Falsy)")

if {}:
    print("{} is True")
else:
    print("{} is False (Falsy)")

#    - Truthy Values:
#      - Any value that is not Falsy is Truthy.
#      - Non-zero numbers, non-empty sequences, non-empty mappings.

print("\n--- Truthy Values ---")
if 1:
    print("1 is True (Truthy)")

if "hello":
    print("'hello' is True (Truthy)")

if [1, 2]:
    print("[1, 2] is True (Truthy)")

# 5. Using Booleans in Conditional Statements

temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a nice day for a walk.")
elif temperature > 20 and is_raining:
    print("It's warm but raining.")
else:
    print("Stay inside, it's a bit chilly.")

# 6. Boolean Conversion
#    - Use the `bool()` constructor to explicitly convert a value to a boolean.

print(f"bool(0): {bool(0)}")          # False
print(f"bool(10): {bool(10)}")        # True
print(f"bool(''): {bool('')}")        # False
print(f"bool(' '): {bool(' ')}")      # True (Space is not empty)
print(f"bool([]): {bool([])}")        # False
print(f"bool(['a']): {bool(['a'])}")  # True
print(f"bool(None): {bool(None)}")    # False

# 7. Short-circuiting Behavior of 'and' and 'or'
#    - These operators evaluate operands from left to right.
#    - 'and': If the left operand is False, the right operand is not evaluated.
#             Returns the left operand if it's Falsy, otherwise returns the right operand.
#    - 'or':  If the left operand is True, the right operand is not evaluated.
#             Returns the left operand if it's Truthy, otherwise returns the right operand.

print("\n--- Short-circuiting ---")

def my_function():
    print("my_function was called")
    return True

# 'and' short-circuits
result_and = False and my_function()
print(f"result_and (False and my_function()): {result_and}") # my_function not called

result_and_2 = True and my_function()
print(f"result_and_2 (True and my_function()): {result_and_2}") # my_function called

# 'or' short-circuits
result_or = True or my_function()
print(f"result_or (True or my_function()): {result_or}") # my_function not called

result_or_2 = False or my_function()
print(f"result_or_2 (False or my_function()): {result_or_2}") # my_function called

print(f"5 and 10: {5 and 10}")   # Returns 10 (10 is the right operand as 5 is Truthy)
print(f"0 and 10: {0 and 10}")   # Returns 0 (0 is the left operand as it's Falsy)
print(f"5 or 10: {5 or 10}")     # Returns 5 (5 is the left operand as it's Truthy)
print(f"0 or 10: {0 or 10}")     # Returns 10 (10 is the right operand as 0 is Falsy)

# 8. Type Hinting with bool

def check_status(is_online: bool) -> str:
    if is_online:
        return "User is online."
    else:
        return "User is offline."

print(check_status(True))
print(check_status(False))

# 9. Using Booleans for Flags

verbose_mode = True

if verbose_mode:
    print("\n--- Verbose Mode Enabled ---")
    print("Performing detailed operations...")
else:
    print("\nPerforming quick operations...")

# 10. `all()` and `any()` functions (related to booleans)
#     - `all(iterable)`: Returns True if all elements of the iterable are truthy.
#     - `any(iterable)`: Returns True if any element of the iterable is truthy.

print("\n--- all() and any() ---")
list1 = [True, True, True]
list2 = [True, False, True]
list3 = [0, 1, 2] # 0 is Falsy, 1 and 2 are Truthy
list4 = []        # Empty iterables return True for all(), False for any()

print(f"all({list1}): {all(list1)}")     # True
print(f"any({list1}): {any(list1)}")     # True

print(f"all({list2}): {all(list2)}")     # False
print(f"any({list2}): {any(list2)}")     # True

print(f"all({list3}): {all(list3)}")     # False
print(f"any({list3}): {any(list3)}")     # True

print(f"all({list4}): {all(list4)}")     # True (empty iterable)
print(f"any({list4}): {any(list4)}")     # False (empty iterable)