# --- Python Tuples: All About Accessing Elements in Code ---

# Tuples are ordered collections, meaning the elements have a defined sequence.
# This allows access to elements using indexing and slicing, similar to lists and strings.

# Let's define a sample tuple for demonstration.
my_tuple = ("apple", "banana", "cherry", "date", "elderberry", "fig")

print("--- 1. Accessing Elements using Indexing ---")

# Indexing allows you to retrieve a single element from the tuple.
# Python uses zero-based indexing, meaning the first element is at index 0.

# 1.1 Positive Indexing (from the beginning)
# Syntax: tuple[index]
print(f"1.1 First element (index 0): {my_tuple[0]}")     # Output: apple
print(f"    Third element (index 2): {my_tuple[2]}")     # Output: cherry
print(f"    Last element (index 5): {my_tuple[5]}")      # Output: fig

# 1.2 Negative Indexing (from the end)
# Negative indexing starts from -1 for the last element.
print(f"1.2 Last element (index -1): {my_tuple[-1]}")    # Output: fig
print(f"    Second to last element (index -2): {my_tuple[-2]}") # Output: elderberry
print(f"    Third element from end (index -4): {my_tuple[-4]}") # Output: cherry

# 1.3 Accessing elements in nested tuples
nested_tuple = ((1, 2), ("a", "b", "c"), (True, False))
print(f"1.3 Accessing element in nested tuple:")
print(f"    First nested tuple: {nested_tuple[0]}")         # Output: (1, 2)
print(f"    First element of the first nested tuple: {nested_tuple[0][0]}") # Output: 1
print(f"    Second element of the second nested tuple: {nested_tuple[1][1]}") # Output: b

# 1.4 What happens if the index is out of range? (IndexError)
# Attempting to access an index that does not exist will raise an IndexError.
try:
    print(my_tuple[10]) # Tuple only has 6 elements (indices 0-5)
except IndexError as e:
    print(f"1.4 Error: {e} - Index 10 is out of range.")

try:
    print(my_tuple[-7]) # Tuple only has 6 elements (indices -1 to -6)
except IndexError as e:
    print(f"    Error: {e} - Index -7 is out of range.")


print("\n--- 2. Accessing Elements using Slicing ---")

# Slicing allows you to extract a sub-tuple (a portion) from an existing tuple.
# Syntax: tuple[start:end:step]
# - `start`: The starting index (inclusive). Default is 0.
# - `end`: The ending index (exclusive). Default is the end of the tuple.
# - `step`: The increment between indices. Default is 1.

# 2.1 Basic Slicing: `tuple[start:end]`
# Extracts elements from `start` up to (but not including) `end`.
print(f"2.1 Slice from index 1 to 4 (exclusive): {my_tuple[1:4]}") # Output: ('banana', 'cherry', 'date')
print(f"    Slice from index 0 to 3 (exclusive): {my_tuple[0:3]}") # Output: ('apple', 'banana', 'cherry')

# 2.2 Slicing with omitted `start` or `end`
print(f"2.2 Slice from beginning to index 3 (exclusive): {my_tuple[:3]}") # Output: ('apple', 'banana', 'cherry')
print(f"    Slice from index 3 to end: {my_tuple[3:]}") # Output: ('date', 'elderberry', 'fig')
print(f"    Slice the entire tuple (creates a shallow copy): {my_tuple[:]}") # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig')

# 2.3 Slicing with `step`
# Extracts elements by skipping `step - 1` elements.
print(f"2.3 Slice with step 2: {my_tuple[::2]}") # Output: ('apple', 'cherry', 'elderberry')
print(f"    Slice from index 1 with step 2: {my_tuple[1::2]}") # Output: ('banana', 'date', 'fig')

# 2.4 Reverse a tuple using slicing
print(f"2.4 Reverse the tuple: {my_tuple[::-1]}") # Output: ('fig', 'elderberry', 'date', 'cherry', 'banana', 'apple')

# 2.5 Slicing with negative indices
print(f"2.5 Slice from -4 to -1 (exclusive): {my_tuple[-4:-1]}") # Output: ('cherry', 'date', 'elderberry')
print(f"    Slice from beginning to -2 (exclusive): {my_tuple[:-2]}") # Output: ('apple', 'banana', 'cherry', 'date')


print("\n--- 3. Iterating Through Tuples ---")

# You can access each element of a tuple by iterating over it using a `for` loop.

# 3.1 Basic iteration
print("3.1 Iterating through a tuple:")
for item in my_tuple:
    print(item)

# 3.2 Iterating with `enumerate()` to get both index and value
print("\n3.2 Iterating with enumerate():")
for index, value in enumerate(my_tuple):
    print(f"Index {index}: {value}")


print("\n--- 4. Unpacking Tuples (Sequence Unpacking) ---")

# Tuple unpacking allows you to assign elements of a tuple directly to multiple variables.
# The number of variables on the left-hand side must match the number of elements in the tuple.

# 4.1 Basic unpacking
coordinates = (100, 200)
x, y = coordinates
print(f"4.1 Unpacked coordinates: x={x}, y={y}")

# 4.2 Unpacking with different data types
person = ("Bob", 25, "Engineer")
name, age, profession = person
print(f"    Unpacked person data: Name={name}, Age={age}, Profession={profession}")

# 4.3 Unpacking return values from functions
def get_dimensions():
    return 800, 600 # Python automatically packs these into a tuple

width, height = get_dimensions()
print(f"    Unpacked dimensions from function: Width={width}, Height={height}")

# 4.4 Swapping variables using tuple unpacking
a = 5
b = 10
print(f"    Before swap: a={a}, b={b}")
a, b = b, a # This creates a temporary tuple (10, 5) and unpacks it.
print(f"    After swap: a={a}, b={b}")

# 4.5 Extended Unpacking (Python 3.0+)
# Use the `*` operator to capture multiple elements into a list.
# Only one starred expression is allowed in an assignment.
long_data = (1, 2, 3, 4, 5, 6, 7, 8)
first, second, *middle, last = long_data
print(f"4.5 Extended unpack: First={first}, Second={second}, Middle={middle}, Last={last}")
# Output: First=1, Second=2, Middle=[3, 4, 5, 6, 7], Last=8

# If the starred variable captures no elements, it will be an empty list.
short_data = (10, 20)
start, *rest, end = short_data
print(f"    Extended unpack (rest is empty): Start={start}, Rest={rest}, End={end}")
# Output: Start=10, Rest=[], End=20

# Using `*_` to ignore intermediate elements (common convention)
header, *_, footer = ("ID", "Name", "Age", "City", "Country", "Timestamp")
print(f"    Extended unpack (ignoring middle with *_): Header={header}, Footer={footer}")

# 4.6 What happens if the number of variables doesn't match in basic unpacking? (ValueError)
try:
    x, y, z = (10, 20) # Too few values to unpack
except ValueError as e:
    print(f"4.6 Error: {e} - Mismatch in number of variables for unpacking.")

try:
    a, b = (1, 2, 3) # Too many values to unpack
except ValueError as e:
    print(f"    Error: {e} - Mismatch in number of variables for unpacking.")