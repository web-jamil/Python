print("--- Python Comparison Operators ---")
print("----------------------------------\n")

# Define various data types for comparison
int_val1 = 10
int_val2 = 20
int_val3 = 10

float_val1 = 10.0
float_val2 = 9.99

str_val1 = "apple"
str_val2 = "banana"
str_val3 = "Apple" # Different case
str_val4 = "apple"

list_val1 = [1, 2, 3]
list_val2 = [1, 2, 3]
list_val3 = [1, 2, 4]
list_val4 = [1, 2]

tuple_val1 = (1, 2, 3)
tuple_val2 = (1, 2, 3)
tuple_val3 = (1, 2, 4)

bool_val1 = True
bool_val2 = False

none_val1 = None
none_val2 = None

print(f"Variables used:\n"
      f"  int_val1={int_val1}, int_val2={int_val2}, int_val3={int_val3}\n"
      f"  float_val1={float_val1}, float_val2={float_val2}\n"
      f"  str_val1='{str_val1}', str_val2='{str_val2}', str_val3='{str_val3}', str_val4='{str_val4}'\n"
      f"  list_val1={list_val1}, list_val2={list_val2}, list_val3={list_val3}, list_val4={list_val4}\n"
      f"  tuple_val1={tuple_val1}, tuple_val2={tuple_val2}, tuple_val3={tuple_val3}\n"
      f"  bool_val1={bool_val1}, bool_val2={bool_val2}\n"
      f"  none_val1={none_val1}, none_val2={none_val2}\n")


# 1. Equal To (==)
print("1. Equal To (==): Checks if two operands have the same value.")
print(f"{int_val1} == {int_val2}: {int_val1 == int_val2}") # False
print(f"{int_val1} == {int_val3}: {int_val1 == int_val3}") # True
print(f"{int_val1} == {float_val1}: {int_val1 == float_val1}") # True (value comparison, type conversion if needed)
print(f"'{str_val1}' == '{str_val4}': {str_val1 == str_val4}") # True
print(f"'{str_val1}' == '{str_val3}': {str_val1 == str_val3}") # False (case-sensitive)
print(f"{list_val1} == {list_val2}: {list_val1 == list_val2}") # True (element-wise and order)
print(f"{list_val1} == {list_val3}: {list_val1 == list_val3}") # False
print(f"{tuple_val1} == {tuple_val2}: {tuple_val1 == tuple_val2}") # True
print(f"{bool_val1} == {bool_val2}: {bool_val1 == bool_val2}") # False
print(f"{none_val1} == {none_val2}: {none_val1 == none_val2}\n") # True


# 2. Not Equal To (!=)
print("2. Not Equal To (!=): Checks if two operands do NOT have the same value.")
print(f"{int_val1} != {int_val2}: {int_val1 != int_val2}") # True
print(f"{int_val1} != {int_val3}: {int_val1 != int_val3}") # False
print(f"'{str_val1}' != '{str_val3}': {str_val1 != str_val3}") # True
print(f"{list_val1} != {list_val3}: {list_val1 != list_val3}\n") # True


# 3. Greater Than (>)
print("3. Greater Than (>): Checks if the left operand is greater than the right.")
print(f"{int_val2} > {int_val1}: {int_val2 > int_val1}") # True
print(f"{int_val1} > {int_val3}: {int_val1 > int_val3}") # False
print(f"{float_val1} > {float_val2}: {float_val1 > float_val2}") # True
print(f"'{str_val2}' > '{str_val1}': {str_val2 > str_val1}") # True (lexicographical comparison)
print(f"{list_val3} > {list_val1}: {list_val3 > list_val1}\n") # True (lexicographical, (1,2,4) > (1,2,3) because 4 > 3)


# 4. Less Than (<)
print("4. Less Than (<): Checks if the left operand is less than the right.")
print(f"{int_val1} < {int_val2}: {int_val1 < int_val2}") # True
print(f"{int_val1} < {int_val3}: {int_val1 < int_val3}") # False
print(f"'{str_val1}' < '{str_val2}': {str_val1 < str_val2}") # True
print(f"{list_val1} < {list_val3}: {list_val1 < list_val3}\n") # True


# 5. Greater Than or Equal To (>=)
print("5. Greater Than or Equal To (>=): Checks if the left operand is greater than or equal to the right.")
print(f"{int_val2} >= {int_val1}: {int_val2 >= int_val1}") # True
print(f"{int_val1} >= {int_val3}: {int_val1 >= int_val3}") # True
print(f"{float_val1} >= {float_val2}: {float_val1 >= float_val2}\n") # True


# 6. Less Than or Equal To (<=)
print("6. Less Than or Equal To (<=): Checks if the left operand is less than or equal to the right.")
print(f"{int_val1} <= {int_val2}: {int_val1 <= int_val2}") # True
print(f"{int_val1} <= {int_val3}: {int_val1 <= int_val3}") # True
print(f"'{str_val1}' <= '{str_val2}': {str_val1 <= str_val2}\n") # True


# --- Behavior with Different Data Types ---
print("--- Behavior with Different Data Types ---\n")

# Numeric types (int, float, complex)
# Can compare int and float directly based on their numeric value.
print(f"{int_val1} == {float_val1}: {int_val1 == float_val1}") # True
print(f"{int_val1} < {float_val2}: {int_val1 < float_val2}") # False (10 < 9.99 is False)

# Complex numbers can only be checked for equality/inequality.
# Ordering comparisons (>, <, >=, <=) are not supported for complex numbers.
complex1 = 3 + 4j
complex2 = 3 + 4j
complex3 = 2 + 5j
print(f"Complex: {complex1} == {complex2}: {complex1 == complex2}") # True
print(f"Complex: {complex1} != {complex3}: {complex1 != complex3}") # True
try:
    print(f"Complex: {complex1} < {complex3}: {complex1 < complex3}")
except TypeError as e:
    print(f"Error: {e} (Complex numbers do not support ordering comparisons).\n")


# Strings (Lexicographical Comparison)
# Compared character by character based on their Unicode (ASCII) values.
# 'A' < 'a' because ASCII of 'A' (65) is less than 'a' (97).
print(f"'{str_val3}' < '{str_val1}': {str_val3 < str_val1}") # 'Apple' < 'apple' -> True
print(f"Length does not solely determine order: 'cat' < 'dog': {'cat' < 'dog'}") # True
print(f"'cat' < 'catalog': {'cat' < 'catalog'}") # True (prefix is smaller)
print(f"'zebra' > 'apple': {'zebra' > 'apple'}\n") # True


# Lists and Tuples (Lexicographical Comparison)
# Compared element by element. If elements are equal, it moves to the next.
# If one sequence is a prefix of another, the longer one is greater.
print(f"{list_val1} < {list_val3}: {list_val1 < list_val3}") # [1,2,3] < [1,2,4] -> True (3 < 4)
print(f"{list_val4} < {list_val1}: {list_val4 < list_val1}") # [1,2] < [1,2,3] -> True (shorter prefix is smaller)
print(f"{tuple_val1} < {tuple_val3}: {tuple_val1 < tuple_val3}\n") # (1,2,3) < (1,2,4) -> True


# Sets and Dictionaries
# Sets can only be compared for equality/inequality, subset, and superset relationships.
# They do not support ordering comparisons (>, <, etc.)
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 3, 4}
print(f"Sets: {set1} == {set2}: {set1 == set2}") # True (order doesn't matter for equality)
print(f"Sets: {set1} < {set3}: {set1 < set3}")   # True (set1 is a proper subset of set3)
print(f"Sets: {set3} > {set1}: {set3 > set1}")   # True (set3 is a proper superset of set1)
try:
    print(f"Sets: {{1, 5}} < {{2, 3}}: {{1, 5}} < {{2, 3}}")
except TypeError as e:
    print(f"Error: {e} (Sets only support subset/superset comparison, not general ordering).\n")

# Dictionaries can only be compared for equality/inequality.
# They do not support ordering comparisons.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 3}
print(f"Dicts: {dict1} == {dict2}: {dict1 == dict2}") # True (order doesn't matter for equality)
print(f"Dicts: {dict1} == {dict3}: {dict1 == dict3}") # False
try:
    print(f"Dicts: {dict1} < {dict3}: {dict1 < dict3}")
except TypeError as e:
    print(f"Error: {e} (Dictionaries do not support ordering comparisons).\n")


# Identity vs. Equality (is vs. ==)
print("--- Identity vs. Equality (is vs. ==) ---")
# '==' checks for value equality.
# 'is' checks for object identity (if two variables refer to the exact same object in memory).

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}, y = {y}, z = {z}")
print(f"x == y: {x == y}") # True (same values)
print(f"x is y: {x is y}") # False (different objects in memory)
print(f"x == z: {x == z}") # True
print(f"x is z: {x is z}\n") # True (both refer to the same object)

# For small integers and short strings, Python often interned them, leading to 'is' being True
# for identical values, but don't rely on it for general objects.
a = 100
b = 100
c = 1000
d = 1000
s_a = "hello"
s_b = "hello"
s_c = "long long string" * 5
s_d = "long long string" * 5

print(f"a={a}, b={b}, c={c}, d={d}")
print(f"a is b: {a is b}") # Often True due to integer interning for small integers
print(f"c is d: {c is d}") # Often False for larger integers (implementation detail)
print(f"s_a is s_b: {s_a is s_b}") # Often True due to string interning
print(f"s_c is s_d: {s_c is s_d}\n") # Often False for longer strings (implementation detail)


print("--- End of Python Comparison Operators Demonstration ---")