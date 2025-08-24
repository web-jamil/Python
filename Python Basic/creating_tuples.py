# --- Python Tuples: All About Creating Them in Code ---

# Tuples are ordered, immutable collections of items.
# They are defined by items separated by commas, optionally enclosed in parentheses `()`.

# --- 1. Creating Empty Tuples ---

print("--- 1. Creating Empty Tuples ---")

# 1.1 Using empty parentheses `()`: This is the most common and readable way.
empty_tuple_1 = ()
print(f"1.1 Empty tuple using (): {empty_tuple_1}")
print(f"    Type of empty_tuple_1: {type(empty_tuple_1)}")

# 1.2 Using the `tuple()` constructor without arguments:
empty_tuple_2 = tuple()
print(f"1.2 Empty tuple using tuple(): {empty_tuple_2}")
print(f"    Type of empty_tuple_2: {type(empty_tuple_2)}")

# Both methods produce the same result.


# --- 2. Creating Tuples with Multiple Elements ---

print("\n--- 2. Creating Tuples with Multiple Elements ---")

# 2.1 Using parentheses `()` with comma-separated values: (Most common syntax)
coordinates = (10.0, 20.5)
print(f"2.1 Coordinates tuple: {coordinates}")

person_info = ("Alice", 30, "New York", True)
print(f"    Person Info tuple: {person_info}")

# 2.2 Tuple Packing (without parentheses):
# Python automatically interprets comma-separated values as a tuple.
# This is often used when returning multiple values from a function.
colors = "red", "green", "blue"
print(f"2.2 Colors tuple (without parentheses): {colors}")
print(f"    Type of colors: {type(colors)}")

# 2.3 Tuple with mixed data types:
# Tuples can hold items of different data types, including other collections.
mixed_tuple = ("apple", 123, True, 3.14, [1, 2], {"key": "value"})
print(f"2.3 Mixed data types tuple: {mixed_tuple}")

# 2.4 Nested Tuples:
# Tuples can contain other tuples (or lists, dictionaries, etc.) as elements.
nested_tuple = ((1, 2), ("a", "b", "c"), (True, False))
print(f"2.4 Nested tuple: {nested_tuple}")


# --- 3. Creating Single-Element Tuples (Crucial Detail!) ---

print("\n--- 3. Creating Single-Element Tuples ---")

# This is a common pitfall for beginners. To create a tuple with only one element,
# you MUST include a trailing comma after the element.

# 3.1 Correct way: Trailing comma is essential
single_element_tuple_correct = (100,)
print(f"3.1 Correct single-element tuple: {single_element_tuple_correct}")
print(f"    Type of single_element_tuple_correct: {type(single_element_tuple_correct)}")

# 3.2 Incorrect way: Without the comma, it's just an expression in parentheses.
not_a_tuple = (100)
print(f"3.2 (100) is NOT a tuple: {not_a_tuple}, Type: {type(not_a_tuple)}")

single_string_tuple = ("hello",)
print(f"    Single-element string tuple: {single_string_tuple}")
print(f"    Type of single_string_tuple: {type(single_string_tuple)}")

# Incorrect: Just a string in parentheses
not_a_string_tuple = ("hello")
print(f"    ('hello') is NOT a tuple: {not_a_string_tuple}, Type: {type(not_a_string_tuple)}")


# --- 4. Creating Tuples from Iterables using the `tuple()` Constructor ---

print("\n--- 4. Creating Tuples from Iterables using `tuple()` ---")

# The `tuple()` constructor can convert any iterable (like lists, strings, sets,
# ranges, generators) into a new tuple.

# 4.1 From a list:
list_data = [10, 20, 30, 40]
tuple_from_list = tuple(list_data)
print(f"4.1 Tuple from a list: {tuple_from_list}")

# 4.2 From a string: Each character becomes an element.
string_data = "Python"
tuple_from_string = tuple(string_data)
print(f"4.2 Tuple from a string: {tuple_from_string}") # ('P', 'y', 't', 'h', 'o', 'n')

# 4.3 From a set: Sets are unordered, so the order of elements in the resulting
#     tuple is not guaranteed and may vary.
set_data = {5, 1, 3, 2}
tuple_from_set = tuple(set_data)
print(f"4.3 Tuple from a set (order not guaranteed): {tuple_from_set}") # e.g., (1, 2, 3, 5) or (5, 1, 2, 3)

# 4.4 From a range object:
range_data = range(1, 5) # Generates 1, 2, 3, 4
tuple_from_range = tuple(range_data)
print(f"4.4 Tuple from a range: {tuple_from_range}")

# 4.5 From a dictionary's keys, values, or items:
my_dict = {"name": "Bob", "age": 25}
tuple_from_keys = tuple(my_dict.keys())
print(f"4.5 Tuple from dictionary keys: {tuple_from_keys}") # ('name', 'age')

tuple_from_values = tuple(my_dict.values())
print(f"    Tuple from dictionary values: {tuple_from_values}") # ('Bob', 25)

tuple_from_items = tuple(my_dict.items())
print(f"    Tuple from dictionary items: {tuple_from_items}") # (('name', 'Bob'), ('age', 25))


# --- 5. Tuple Concatenation and Repetition (Creating new tuples) ---

print("\n--- 5. Tuple Concatenation and Repetition ---")

# These operations create *new* tuples, as tuples are immutable.

# 5.1 Concatenation using the `+` operator:
tuple_part1 = (1, 2, 3)
tuple_part2 = (4, 5, 6)
combined_tuple = tuple_part1 + tuple_part2
print(f"5.1 Concatenated tuple: {combined_tuple}") # (1, 2, 3, 4, 5, 6)

# 5.2 Repetition using the `*` operator:
repeated_tuple = ("hello",) * 3 # Note the comma for single-element tuple
print(f"5.2 Repeated tuple: {repeated_tuple}") # ('hello', 'hello', 'hello')

# Repetition of a multi-element tuple
pattern_tuple = (1, 0) * 4
print(f"    Repeated pattern tuple: {pattern_tuple}") # (1, 0, 1, 0, 1, 0, 1, 0)