print("--- Python Comparison Operators: Practice Code ---")

# --- 1. Introduction to Comparison Operators ---
print("\n--- 1. Introduction to Comparison Operators ---")
print("Comparison operators are used to compare two values.")
print("They always return a Boolean value: True or False.")

# --- 2. Equality Operator (==) ---
print("\n--- 2. Equality Operator (==) ---")
print("Checks if the values of two operands are equal.")

# 2.1 Comparing numbers
num1 = 10
num2 = 20
num3 = 10
print(f"num1 ({num1}) == num2 ({num2}): {num1 == num2}") # False
print(f"num1 ({num1}) == num3 ({num3}): {num1 == num3}") # True

# 2.2 Comparing different numeric types (value is compared)
num_int = 10
num_float = 10.0
print(f"num_int ({num_int}) == num_float ({num_float}): {num_int == num_float}") # True

# 2.3 Comparing strings (case-sensitive)
str1 = "Hello"
str2 = "hello"
str3 = "Hello"
print(f"str1 ('{str1}') == str2 ('{str2}'): {str1 == str2}") # False
print(f"str1 ('{str1}') == str3 ('{str3}'): {str1 == str3}") # True

# 2.4 Comparing lists, tuples, sets, dictionaries (content comparison)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
print(f"list1 ({list1}) == list2 ({list2}): {list1 == list2}") # True
print(f"list1 ({list1}) == list3 ({list3}): {list1 == list3}") # False (order matters for lists/tuples)

set1 = {1, 2, 3}
set2 = {3, 2, 1} # Order doesn't matter for sets
print(f"set1 ({set1}) == set2 ({set2}): {set1 == set2}") # True

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1} # Order doesn't matter for dictionaries
print(f"dict1 ({dict1}) == dict2 ({dict2}): {dict1 == dict2}") # True


# --- 3. Inequality Operator (!=) ---
print("\n--- 3. Inequality Operator (!=) ---")
print("Checks if the values of two operands are NOT equal.")

print(f"num1 ({num1}) != num2 ({num2}): {num1 != num2}") # True
print(f"str1 ('{str1}') != str2 ('{str2}'): {str1 != str2}") # True
print(f"list1 ({list1}) != list3 ({list3}): {list1 != list3}") # True


# --- 4. Greater Than Operator (>) ---
print("\n--- 4. Greater Than Operator (>) ---")
print("Checks if the left operand's value is greater than the right operand's value.")

print(f"num2 ({num2}) > num1 ({num1}): {num2 > num1}") # True
print(f"5 > 5: {5 > 5}") # False
print(f"3.14 > 3.0: {3.14 > 3.0}") # True

# Comparing strings (lexicographical comparison based on ASCII/Unicode values)
print(f"'banana' > 'apple': {'banana' > 'apple'}") # True
print(f"'Zebra' > 'apple': {'Zebra' > 'apple'}") # False (Z comes after a in ASCII/Unicode)


# --- 5. Less Than Operator (<) ---
print("\n--- 5. Less Than Operator (<) ---")
print("Checks if the left operand's value is less than the right operand's value.")

print(f"num1 ({num1}) < num2 ({num2}): {num1 < num2}") # True
print(f"5 < 5: {5 < 5}") # False
print(f"'apple' < 'banana': {'apple' < 'banana'}") # True


# --- 6. Greater Than or Equal To Operator (>=) ---
print("\n--- 6. Greater Than or Equal To Operator (>=) ---")
print("Checks if the left operand's value is greater than or equal to the right operand's value.")

print(f"num1 ({num1}) >= num3 ({num3}): {num1 >= num3}") # True (equal)
print(f"num2 ({num2}) >= num1 ({num1}): {num2 >= num1}") # True (greater)
print(f"5 >= 6: {5 >= 6}") # False


# --- 7. Less Than or Equal To Operator (<=) ---
print("\n--- 7. Less Than or Equal To Operator (<=) ---")
print("Checks if the left operand's value is less than or equal to the right operand's value.")

print(f"num1 ({num1}) <= num3 ({num3}): {num1 <= num3}") # True (equal)
print(f"num1 ({num1}) <= num2 ({num2}): {num1 <= num2}") # True (less)
print(f"6 <= 5: {6 <= 5}") # False


# --- 8. Chained Comparisons (Pythonic Way) ---
print("\n--- 8. Chained Comparisons ---")
print("Python allows chaining comparison operators for conciseness.")

score = 85
print(f"Score: {score}")
print(f"60 < score < 90: {60 < score < 90}") # Equivalent to (60 < score) and (score < 90)
print(f"score >= 80 and score <= 90: {score >= 80 and score <= 90}") # Traditional way

temp = 25
print(f"Temperature: {temp}")
if 20 <= temp <= 30: # Check if temp is between 20 and 30 (inclusive)
    print("Temperature is in the comfortable range.")
else:
    print("Temperature is outside the comfortable range.")


# --- 9. Identity Operator vs. Equality Operator (is vs. ==) ---
print("\n--- 9. Identity Operator (is) vs. Equality Operator (==) ---")
print("'==' checks for value equality.")
print("'is' checks if two variables refer to the *exact same object* in memory.")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a # list_c now refers to the same object as list_a

print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print(f"list_c: {list_c}")

print(f"list_a == list_b: {list_a == list_b}") # True (values are equal)
print(f"list_a is list_b: {list_a is list_b}") # False (different objects, even if content is same)

print(f"list_a == list_c: {list_a == list_c}") # True (values are equal)
print(f"list_a is list_c: {list_a is list_c}") # True (they refer to the same object)

# For None, it is *always* recommended to use 'is'
none_var = None
print(f"none_var is None: {none_var is None}") # Recommended
print(f"none_var == None: {none_var == None}") # Also works, but 'is' is idiomatic


# --- 10. Membership Operator (in / not in) ---
print("\n--- 10. Membership Operators (in / not in) ---")
print("Checks if a value exists within a sequence (string, list, tuple, set, dictionary keys).")

my_list = [10, 20, 30, 40]
print(f"Is 20 in {my_list}? {20 in my_list}") # True
print(f"Is 50 in {my_list}? {50 in my_list}") # False

my_string = "Hello Python"
print(f"Is 'Python' in '{my_string}'? {'Python' in my_string}") # True
print(f"Is 'java' not in '{my_string}'? {'java' not in my_string}") # True

my_dict = {'name': 'Alice', 'age': 30}
print(f"Is 'name' in {my_dict} (keys)? {'name' in my_dict}") # True
print(f"Is 30 in {my_dict} (values)? {30 in my_dict.values()}") # True (must check .values())


print("\n--- End of Python Comparison Operators Practice Code ---")