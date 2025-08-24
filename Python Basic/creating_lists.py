# --- Python Lists: All About Creating Them in Code ---

# Lists are fundamental, ordered, and mutable collections in Python.
# They are incredibly versatile for storing sequences of items.

# --- 1. Creating Empty Lists ---

print("--- 1. Creating Empty Lists ---")

# 1.1 Using empty square brackets `[]`: This is the most common and Pythonic way.
empty_list_1 = []
print(f"1.1 Empty list using []: {empty_list_1}")
print(f"    Type of empty_list_1: {type(empty_list_1)}")

# 1.2 Using the `list()` constructor without arguments:
empty_list_2 = list()
print(f"1.2 Empty list using list(): {empty_list_2}")
print(f"    Type of empty_list_2: {type(empty_list_2)}")

# Both methods produce an identical empty list.


# --- 2. Creating Lists with Initial Elements (Literal Syntax) ---

print("\n--- 2. Creating Lists with Initial Elements ---")

# This is the most common and readable way when you know the elements
# at the time of creation. Elements are separated by commas and enclosed in `[]`.

# 2.1 Basic list of numbers
numbers = [1, 2, 3, 4, 5]
print(f"2.1 List of numbers: {numbers}")

# 2.2 Basic list of strings
fruits = ["apple", "banana", "cherry"]
print(f"2.2 List of strings: {fruits}")

# 2.3 List with mixed data types
# Lists can hold elements of different types, including other lists, tuples, or dictionaries.
mixed_list = ["hello", 123, True, 3.14, None, (1, 2), {"key": "value"}]
print(f"2.3 List with mixed data types: {mixed_list}")

# 2.4 Nested Lists
# Lists can contain other lists, creating multi-dimensional structures.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"2.4 Nested list (matrix): {matrix}")


# --- 3. Creating Lists from Iterables using the `list()` Constructor ---

print("\n--- 3. Creating Lists from Iterables using `list()` ---")

# The `list()` constructor can convert any iterable (like strings, tuples, sets,
# ranges, generators) into a new list.

# 3.1 From a string: Each character becomes an element.
string_data = "Python"
list_from_string = list(string_data)
print(f"3.1 List from a string: {list_from_string}") # ['P', 'y', 't', 'h', 'o', 'n']

# 3.2 From a tuple:
tuple_data = (10, 20, 30)
list_from_tuple = list(tuple_data)
print(f"3.2 List from a tuple: {list_from_tuple}")

# 3.3 From a set: Sets are unordered, so the order of elements in the resulting
#     list is not guaranteed and may vary.
set_data = {"red", "green", "blue"}
list_from_set = list(set_data)
print(f"3.3 List from a set (order not guaranteed): {list_from_set}")

# 3.4 From a range object:
range_data = range(1, 6) # Generates numbers from 1 up to (but not including) 6
list_from_range = list(range_data)
print(f"3.4 List from a range: {list_from_range}") # [1, 2, 3, 4, 5]

# 3.5 From a dictionary's keys, values, or items:
my_dict = {"name": "Bob", "age": 25, "city": "London"}
list_from_keys = list(my_dict.keys())
print(f"3.5 List from dictionary keys: {list_from_keys}") # ['name', 'age', 'city']

list_from_values = list(my_dict.values())
print(f"    List from dictionary values: {list_from_values}") # ['Bob', 25, 'London']

list_from_items = list(my_dict.items())
print(f"    List from dictionary items: {list_from_items}") # [('name', 'Bob'), ('age', 25), ('city', 'London')]


# --- 4. Creating Lists using List Comprehensions ---

print("\n--- 4. Creating Lists using List Comprehensions ---")

# List comprehensions provide a concise and efficient way to create lists
# based on existing iterables, often with transformations or filtering.
# Syntax: `[expression for item in iterable if condition]`

# 4.1 Basic comprehension: squaring numbers
squares = [num**2 for num in range(1, 6)]
print(f"4.1 Squares list: {squares}") # [1, 4, 9, 16, 25]

# 4.2 Comprehension with conditional filtering: only even numbers
even_numbers = [num for num in range(10) if num % 2 == 0]
print(f"4.2 Even numbers list: {even_numbers}") # [0, 2, 4, 6, 8]

# 4.3 Comprehension with transformation and filtering
# Create a list of uppercase words longer than 5 characters.
words = ["apple", "banana", "cherry", "date", "fig"]
long_uppercase_words = [word.upper() for word in words if len(word) > 5]
print(f"4.3 Long uppercase words: {long_uppercase_words}") # ['BANANA', 'CHERRY']

# 4.4 Nested list comprehensions (for creating nested lists)
# Create a 3x3 matrix where each element is i*j
nested_comp_matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"4.4 Nested comprehension matrix: {nested_comp_matrix}")
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# --- 5. Creating Lists by Concatenation and Repetition ---

print("\n--- 5. Creating Lists by Concatenation and Repetition ---")

# These operations create *new* lists.

# 5.1 Concatenation using the `+` operator:
list_part1 = [1, 2, 3]
list_part2 = [4, 5, 6]
combined_list = list_part1 + list_part2
print(f"5.1 Concatenated list: {combined_list}") # [1, 2, 3, 4, 5, 6]

# 5.2 Repetition using the `*` operator:
repeated_list = ["a", "b"] * 3
print(f"5.2 Repeated list: {repeated_list}") # ['a', 'b', 'a', 'b', 'a', 'b']

# 5.3 Using `*` with `list()` for initialization (less common, but possible)
# This creates a list with N copies of the same object. Be careful with mutable objects.
# For mutable objects, all elements will refer to the *same* object.
list_with_same_objects = [[]] * 3
print(f"5.3 List with same mutable objects: {list_with_same_objects}")
list_with_same_objects[0].append(10)
print(f"    After modifying one: {list_with_same_objects}") # All sublists are modified!

# To create a list of *distinct* mutable objects, use a list comprehension:
list_with_distinct_objects = [[] for _ in range(3)]
print(f"    List with distinct mutable objects (initial): {list_with_distinct_objects}")
list_with_distinct_objects[0].append(10)
print(f"    After modifying one: {list_with_distinct_objects}") # Only the first sublist is modified.