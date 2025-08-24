print("--- Python Tuples: Practice Code ---")

# --- 1. Creating Tuples ---
print("\n--- 1. Creating Tuples ---")

# 1.1 Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
print(f"Type of empty_tuple: {type(empty_tuple)}")

# 1.2 Tuple with elements
my_tuple = (1, 2, 3, 4, 5)
print(f"Tuple with numbers: {my_tuple}")

# 1.3 Tuple without parentheses (tuple packing) - common!
another_tuple = 10, 20, 30
print(f"Tuple without parentheses: {another_tuple}")
print(f"Type of another_tuple: {type(another_tuple)}")

# 1.4 Single-element tuple (needs a comma!)
# Without the comma, it's just an integer in parentheses.
single_element_tuple = (42,)
print(f"Single-element tuple: {single_element_tuple}")
print(f"Type of single_element_tuple: {type(single_element_tuple)}")

not_a_tuple = (42) # This is just an integer
print(f"Not a tuple (just an integer): {not_a_tuple}")
print(f"Type of not_a_tuple: {type(not_a_tuple)}")

# 1.5 Tuple from an iterable (using tuple() constructor)
tuple_from_list = tuple([1, 2, 3])
print(f"Tuple from list: {tuple_from_list}")

tuple_from_string = tuple("hello")
print(f"Tuple from string: {tuple_from_string}")

tuple_from_range = tuple(range(5))
print(f"Tuple from range: {tuple_from_range}")

# 1.6 Nested tuples
nested_tuple = ((1, 2), (3, 4, 5))
print(f"Nested tuple: {nested_tuple}")

# 1.7 Mixed data types
mixed_tuple = (1, "apple", True, 3.14)
print(f"Mixed tuple: {mixed_tuple}")


print("\n--- 2. Accessing Elements ---")

my_data = ("Alice", 30, "Engineer", "New York")

# 2.1 By index (0-based)
print(f"First element: {my_data[0]}")
print(f"Third element: {my_data[2]}")

# 2.2 Negative indexing (from the end)
print(f"Last element: {my_data[-1]}")
print(f"Second to last element: {my_data[-2]}")

# 2.3 Accessing elements in nested tuples
nested_access = ((10, 11), (20, 21))
print(f"Element from nested tuple: {nested_access[1][0]}") # Accesses 20


print("\n--- 3. Slicing Tuples ---")
# Syntax: tuple[start:end:step]
# 'end' index is exclusive. 'step' is optional, default is 1.

alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# 3.1 Slice from start to index (exclusive)
print(f"Elements from index 0 to 3 (exclusive): {alphabet_tuple[0:4]}")
print(f"Same as above (default start is 0): {alphabet_tuple[:4]}")

# 3.2 Slice from index to end
print(f"Elements from index 3 to end: {alphabet_tuple[3:]}")

# 3.3 Slice the entire tuple (creates a copy)
print(f"Copy of the tuple: {alphabet_tuple[:]}")

# 3.4 Slice with step
print(f"Every second element: {alphabet_tuple[::2]}")
print(f"Elements from index 1 to 6, every third: {alphabet_tuple[1:7:3]}")

# 3.5 Reverse a tuple using slicing
print(f"Reversed tuple: {alphabet_tuple[::-1]}")


print("\n--- 4. Tuple Operations and Methods ---")

tuple1 = (10, 20, 30)
tuple2 = (40, 50)

# 4.1 Concatenation using + operator (creates new tuple)
combined_tuple = tuple1 + tuple2
print(f"Combined tuple using +: {combined_tuple}")

# 4.2 Repetition using * operator
repeated_tuple = ('x',) * 3 # Note the comma for single-element tuple repetition
print(f"Repeated tuple using *: {repeated_tuple}")

# 4.3 Length of a tuple: len()
print(f"Length of combined_tuple: {len(combined_tuple)}")

# 4.4 Check if element exists: 'in' operator
print(f"Is 'banana' in ('apple', 'banana')? {'banana' in ('apple', 'banana')}")
print(f"Is 20 in combined_tuple? {20 in combined_tuple}")

# 4.5 Finding an element's index: .index()
# Note: Raises ValueError if item is not found
print(f"Index of 30 in combined_tuple: {combined_tuple.index(30)}")

# 4.6 Counting elements: .count()
my_data_tuple = (1, 2, 2, 3, 2, 4)
print(f"Count of 2 in my_data_tuple: {my_data_tuple.count(2)}")

# 4.7 Min, Max, Sum of numeric tuples
num_tuple = (10, 5, 25, 12, 8)
print(f"Min of num_tuple: {min(num_tuple)}")
print(f"Max of num_tuple: {max(num_tuple)}")
print(f"Sum of num_tuple: {sum(num_tuple)}")


print("\n--- 5. Immutability of Tuples ---")
# Tuples are immutable, meaning their elements cannot be changed, added, or removed after creation.

immutable_tuple = (1, 2, 3)
print(f"Original immutable_tuple: {immutable_tuple}")

# immutable_tuple[0] = 99 # This would raise a TypeError: 'tuple' object does not support item assignment
# immutable_tuple.append(4) # This would raise an AttributeError: 'tuple' object has no attribute 'append'

# However, if a tuple contains mutable elements (like lists), those mutable elements CAN be changed.
tuple_with_list = (1, [2, 3], 4)
print(f"Tuple with a mutable list: {tuple_with_list}")
tuple_with_list[1].append(5) # Modifying the list inside the tuple is allowed
print(f"After modifying the nested list: {tuple_with_list}")


print("\n--- 6. Iterating Through Tuples ---")

planets = ("Mercury", "Venus", "Earth", "Mars")

# 6.1 Basic for loop
print("Basic for loop:")
for planet in planets:
    print(planet)

# 6.2 Iterating with index using enumerate()
print("\nIterating with index using enumerate():")
for index, planet in enumerate(planets):
    print(f"Index {index}: {planet}")


print("\n--- 7. Tuple Unpacking (Assignment) ---")
# Very common and useful feature!

# 7.1 Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: x={x}, y={y}")

# 7.2 Unpacking in a loop
points = [(1, 1), (2, 4), (3, 9)]
print("\nUnpacking in a loop:")
for p_x, p_y in points:
    print(f"Point X: {p_x}, Point Y: {p_y}")

# 7.3 Swapping variables (classic use case)
a = 5
b = 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a # This works because the right side creates a tuple (10, 5), then unpacks it.
print(f"After swap: a={a}, b={b}")

# 7.4 Using * to catch multiple elements (Python 3+)
# This is called "extended iterable unpacking"
names = ("Alice", "Bob", "Charlie", "David", "Eve")
first, *middle, last = names
print(f"\nFirst: {first}, Middle: {middle}, Last: {last}")

# When no middle elements, middle becomes an empty list
single_name_tuple = ("Zoe",)
only_one, *rest = single_name_tuple
print(f"Only one: {only_one}, Rest: {rest}")


print("\n--- 8. Common Tuple Use Cases ---")

# 8.1 Function Return Values
# Functions often return multiple values as a tuple, which can then be unpacked.
def get_user_info():
    return "John Doe", 45, "Developer"

name, age, job = get_user_info()
print(f"\nUser Info: Name={name}, Age={age}, Job={job}")

# 8.2 Dictionary Keys (since tuples are immutable, they can be dictionary keys)
# Lists cannot be dictionary keys because they are mutable.
location_data = {
    (40.71, -74.00): "New York City",
    (34.05, -118.24): "Los Angeles"
}
print(f"\nCity at (40.71, -74.00): {location_data[(40.71, -74.00)]}")

# 8.3 Named Tuples (from collections module - more like lightweight objects)
# Provides readable access to elements by name instead of just index.
from collections import namedtuple

# Define a namedtuple type
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=10, y=20)
print(f"\nNamed Tuple Point: {p1}")
print(f"Accessing by name: {p1.x}, {p1.y}")
print(f"Accessing by index: {p1[0]}, {p1[1]}")

# 8.4 As immutable records
# Tuples are good for fixed collections of heterogeneous items, like a database record.
# Example: (person_id, name, date_of_birth, is_active)
record1 = (101, "Maria", "1990-05-15", True)
record2 = (102, "Luiz", "1988-11-20", False)
print(f"\nRecord 1: {record1}")
print(f"Is Record 2 active? {record2[3]}") # Accessing directly by index

print("\n--- End of Python Tuples Practice Code ---")