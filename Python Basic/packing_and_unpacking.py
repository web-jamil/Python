# --- Python: All About Packing and Unpacking in Code ---

# Packing and unpacking are fundamental concepts in Python that allow you to
# group multiple values into a single variable (packing) or extract values
# from a sequence into distinct variables (unpacking).

# --- 1. Packing (Creating a Sequence from Multiple Values) ---

print("--- 1. Packing ---")

# Packing occurs when you assign multiple values, separated by commas, to a single variable.
# Python automatically collects these values into a tuple.

# 1.1 Basic Tuple Packing
# Values on the right are packed into a tuple on the left.
packed_data = 10, "hello", True
print(f"1.1 Packed data: {packed_data}")
print(f"    Type of packed_data: {type(packed_data)}") # Output: <class 'tuple'>

# 1.2 Packing with different data types
user_record = "Alice", 30, "alice@example.com", ["admin", "user"]
print(f"1.2 User record: {user_record}")

# 1.3 Packing with parentheses (explicit tuple creation)
# While not strictly "packing" in the sense of the comma operator,
# it's the explicit way to create a tuple, which is the result of packing.
explicit_tuple = (1, 2, 3)
print(f"1.3 Explicit tuple: {explicit_tuple}")


# --- 2. Unpacking (Assigning Sequence Elements to Multiple Variables) ---

print("\n--- 2. Unpacking ---")

# Unpacking occurs when you assign an iterable (like a tuple, list, or string)
# to multiple variables on the left-hand side of an assignment operator.
# The number of variables must match the number of elements in the iterable.

# 2.1 Basic Tuple Unpacking
coordinates = (100, 200)
x, y = coordinates # Unpacking the tuple (100, 200) into x and y
print(f"2.1 Unpacked coordinates: x={x}, y={y}")

# 2.2 Unpacking with different data types
person_details = ("Bob", 25, "Engineer")
name, age, profession = person_details
print(f"2.2 Unpacked person details: Name={name}, Age={age}, Profession={profession}")

# 2.3 Unpacking values returned by a function
# This is a very common use case.
def get_product_info():
    return "Laptop", 1200.50, 50 # This implicitly packs into a tuple

product_name, product_price, product_stock = get_product_info()
print(f"2.3 Unpacked product info: Name={product_name}, Price=${product_price:.2f}, Stock={product_stock}")

# 2.4 Swapping variable values (a classic Pythonic trick)
a = 5
b = 10
print(f"2.4 Before swap: a={a}, b={b}")
a, b = b, a # Python packs (b, a) into a tuple (10, 5), then unpacks it into a and b.
print(f"    After swap: a={a}, b={b}")

# 2.5 Unpacking from other iterables (lists, strings, etc.)
# List unpacking
my_list = [10, 20, 30]
val1, val2, val3 = my_list
print(f"2.5 Unpacked from list: {val1}, {val2}, {val3}")

# String unpacking (each character)
my_string = "XYZ"
char1, char2, char3 = my_string
print(f"    Unpacked from string: {char1}, {char2}, {char3}")

# 2.6 What happens if the number of variables doesn't match? (ValueError)
try:
    too_few_vars = (1, 2, 3)
    v1, v2 = too_few_vars # Expected 3 elements, got 2 variables
except ValueError as e:
    print(f"\n2.6 Error (Too few variables): {e}")

try:
    too_many_vars = (10, 20)
    x, y, z = too_many_vars # Expected 2 elements, got 3 variables
except ValueError as e:
    print(f"    Error (Too many variables): {e}")


print("\n--- 3. Extended Unpacking (Starred Assignment) ---")

# Introduced in Python 3.0 (PEP 3132), extended unpacking allows you to
# capture multiple elements into a single list using the `*` (asterisk) operator.
# Only one starred expression is allowed on the left-hand side.

# 3.1 Catch-all at the end: `first, *rest = iterable`
data_sequence = (1, 2, 3, 4, 5, 6, 7)
first_item, second_item, *remaining_items = data_sequence
print(f"3.1 Catch-all at end: First={first_item}, Second={second_item}, Remaining={remaining_items}")
# Output: First=1, Second=2, Remaining=[3, 4, 5, 6, 7]
print(f"    Type of 'remaining_items': {type(remaining_items)}") # Always a list

# 3.2 Catch-all at the beginning: `*beginning, last = iterable`
*initial_items, last_item = data_sequence
print(f"3.2 Catch-all at beginning: Initial={initial_items}, Last={last_item}")
# Output: Initial=[1, 2, 3, 4, 5, 6], Last=7

# 3.3 Catch-all in the middle: `first, *middle, last = iterable`
start_item, *middle_items, end_item = data_sequence
print(f"3.3 Catch-all in middle: Start={start_item}, Middle={middle_items}, End={end_item}")
# Output: Start=1, Middle=[2, 3, 4, 5, 6], End=7

# 3.4 What if the starred variable captures zero or one element?
# It will still be a list.
short_seq = (10, 20)
s1, *s_rest, s2 = short_seq
print(f"3.4 Starred captures zero: s1={s1}, s_rest={s_rest}, s2={s2}")
# Output: s1=10, s_rest=[], s2=20 (s_rest is an empty list)

single_element_seq = (50,)
*single_list, = single_element_seq # Note the comma after `*single_list` is crucial for single-element iterable
print(f"    Starred captures one: single_list={single_list}")
# Output: single_list=[50] (still a list)

# 3.5 Using `*_` to ignore captured elements
# It's a common convention to use `_` as a variable name for values you don't intend to use.
header, *_, footer = ("ID", "Name", "Age", "City", "Country", "Timestamp")
print(f"3.5 Ignoring elements with `*_`: Header={header}, Footer={footer}")
# Output: Header=ID, Footer=Timestamp


print("\n--- 4. Packing and Unpacking in Function Arguments ---")

# The `*` and `**` operators are also used for packing/unpacking arguments
# when defining or calling functions.

# 4.1 `*args` (Packing Positional Arguments in Definition)
# Collects an arbitrary number of positional arguments into a tuple.
def sum_all_numbers(*numbers): # `numbers` will be a tuple
    print(f"4.1 sum_all_numbers received: {numbers}, type: {type(numbers)}")
    return sum(numbers)

print(f"    Sum of 1, 2, 3: {sum_all_numbers(1, 2, 3)}")
print(f"    Sum of 10, 20: {sum_all_numbers(10, 20)}")

# 4.2 `**kwargs` (Packing Keyword Arguments in Definition)
# Collects an arbitrary number of keyword arguments into a dictionary.
def process_user_data(user_id, **details): # `details` will be a dictionary
    print(f"4.2 process_user_data received user_id: {user_id}, details: {details}, type: {type(details)}")
    if "name" in details:
        print(f"    User Name: {details['name']}")

process_user_data("U001", name="Alice", age=30, city="London")
process_user_data("U002", status="active")

# 4.3 `*iterable` (Unpacking Positional Arguments in Call)
# Unpacks an iterable (list, tuple, etc.) into separate positional arguments.
def display_coords(x, y, z):
    print(f"4.3 Coordinates: x={x}, y={y}, z={z}")

coords_list = [10, 20, 30]
display_coords(*coords_list) # Unpacks [10, 20, 30] into 10, 20, 30

coords_tuple = (1.5, 2.5, 3.5)
display_coords(*coords_tuple) # Unpacks (1.5, 2.5, 3.5) into 1.5, 2.5, 3.5

# 4.4 `**dictionary` (Unpacking Keyword Arguments in Call)
# Unpacks a dictionary into separate keyword arguments.
def configure_printer(model, dpi, color_mode="CMYK"):
    print(f"4.4 Printer Config: Model={model}, DPI={dpi}, Color Mode={color_mode}")

printer_settings = {"model": "HP LaserJet", "dpi": 600, "color_mode": "RGB"}
configure_printer(**printer_settings) # Unpacks dict into model='HP LaserJet', dpi=600, color_mode='RGB'

# Overriding a default value
default_settings = {"dpi": 300}
configure_printer(model="Epson Inkjet", **default_settings, color_mode="Grayscale")