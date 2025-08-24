# --- Python Named Tuple: All About in Code ---

from collections import namedtuple

print("--- 1. Basic Named Tuple Creation ---")
print("A named tuple assigns names, as well as the numerical index, to each member.")
print("It's a subclass of tuple, meaning it's immutable like a regular tuple.")

# 1.1 Using namedtuple() function
# namedtuple('TypeName', ['field1', 'field2', ...]) or 'field1 field2 ...'
# Benefits: More readable than regular tuples, less memory than custom classes.

# Define a named tuple for a Point
Point = namedtuple('Point', ['x', 'y'])

# Create instances of the Point named tuple
p1 = Point(10, 20)
p2 = Point(x=5, y=15)
p3 = Point(25, y=30) # Can mix positional and keyword arguments

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 3: {p3}")

# Accessing elements:
# 1. By index (like a regular tuple)
print(f"p1.x (index 0): {p1[0]}")
print(f"p1.y (index 1): {p1[1]}")

# 2. By field name (more readable)
print(f"p2.x: {p2.x}")
print(f"p2.y: {p2.y}")

# Named tuples are immutable (like regular tuples)
try:
    p1.x = 100
except AttributeError as e:
    print(f"\nAttempted to modify p1.x: {e}")

try:
    p1[0] = 100
except TypeError as e:
    print(f"Attempted to modify p1[0]: {e}")


print("\n--- 2. Named Tuple Properties and Methods ---")

# 2.1 Accessing field names and arguments list
print(f"Field names of Point: {Point._fields}") # Returns a tuple of strings

# 2.2 Creating a new instance with some fields replaced (_replace)
# This creates a *new* named tuple instance.
p_new = p1._replace(x=100)
print(f"Original p1: {p1}")
print(f"New p_new (p1._replace(x=100)): {p_new}")

# 2.3 Converting to an OrderedDict (_asdict)
# Useful for serialization or converting to other dictionary-like structures.
p_dict = p1._asdict()
print(f"p1 as OrderedDict: {p_dict}")
print(f"Type of p_dict: {type(p_dict)}")

# 2.4 Getting the named tuple name
print(f"Name of the named tuple type: {Point.__name__}")

# 2.5 Using default values (Python 3.7+)
# Requires _make or passing all arguments if not using defaults.
# If not using Python 3.7+, you'd handle defaults externally or use default factory.
try:
    from collections import namedtuple as _namedtuple_default_check
    _namedtuple_default_check('Test', ['a', 'b', 'c'], defaults=(0, 0))
    supports_defaults = True
except TypeError:
    supports_defaults = False

if supports_defaults:
    print("\n--- 2.6 Named Tuple with Default Values (Python 3.7+) ---")
    Product = namedtuple('Product', ['name', 'price', 'quantity'], defaults=[1]) # quantity defaults to 1
    # Note: defaults should be an iterable. If only one default, use [default_val]

    p_item1 = Product('Laptop', 1200) # quantity takes default 1
    p_item2 = Product('Mouse', 25, 5)  # quantity is 5

    print(f"Product 1: {p_item1}")
    print(f"Product 2: {p_item2}")
    print(f"Product 1 quantity: {p_item1.quantity}")
    print(f"Product 2 quantity: {p_item2.quantity}")

    # Accessing default values defined for the named tuple type
    print(f"Product._field_defaults: {Product._field_defaults}")
else:
    print("\n--- 2.6 Named Tuple with Default Values (Requires Python 3.7+) ---")
    print("Your Python version does not directly support 'defaults' argument in namedtuple.")
    print("For older versions, you might implement defaults in a factory function.")


print("\n--- 3. Named Tuples as Dictionary Keys (Hashable) ---")
# Because named tuples are immutable, they are hashable and can be used as dictionary keys
data_points = {
    Point(1, 1): "Bottom-Left",
    Point(10, 20): "Top-Right",
    p1: "Original Point" # p1 is Point(10,20), so it will overwrite the previous entry if keys are equal
}
print(f"Data Points Dictionary: {data_points}")
print(f"Value for Point(10, 20): {data_points[Point(10, 20)]}")


print("\n--- 4. Type Hinting with Named Tuples ---")
# Improve code readability and enable static analysis (e.g., MyPy)

# Define a named tuple for a User profile
User = namedtuple('User', ['id', 'username', 'email'])

def get_user_info(user: User) -> str:
    """Returns a formatted string of user information."""
    return f"User ID: {user.id}, Username: {user.username}, Email: {user.email}"

user1 = User(id=101, username="alice_jones", email="alice@example.com")
print(get_user_info(user1))

# Benefits: Tools like MyPy can check if you're passing the correct type of object
# get_user_info({"id": 102, "username": "bob"}) # Static analysis would flag this
# print(get_user_info(user1))


print("\n--- 5. Named Tuples vs. Classes vs. Regular Tuples ---")

# 5.1 Regular Tuple
# Good for simple collections of heterogeneous data where position is sufficient.
regular_tuple = (1, 'task1', False)
print(f"Regular tuple: {regular_tuple}, Access by index: {regular_tuple[0]}")
# Less readable when many elements: what is regular_tuple[2]?

# 5.2 Named Tuple (Collections.namedtuple)
# Best when you need immutable, lightweight objects with readable field names.
# Good for "record-like" data structures.
# Lower memory footprint than a full class instance.

# 5.3 Custom Class
# Best when you need mutable objects, methods, inheritance, or complex logic.
class ProductClass:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

p_class = ProductClass("Book", 20, 2)
print(f"\nProduct Class: {p_class.name}, Total: {p_class.calculate_total()}")
p_class.quantity = 3 # Can modify attributes
print(f"Product Class (modified): {p_class.name}, Total: {p_class.calculate_total()}")


print("\n--- 6. Advanced Usage: _make() and _replace() with iterables/dicts ---")

# 6.1 _make(): Create a new named tuple instance from an iterable
# Useful for parsing data from CSV rows, database queries, etc.
CsvRow = namedtuple('CsvRow', ['header1', 'header2', 'header3'])
row_data = ['Value A', 123, True]
csv_record = CsvRow._make(row_data)
print(f"CSV Record via _make(): {csv_record}")
print(f"Accessing via name: {csv_record.header2}")

# 6.2 _replace(): Create a new instance by replacing fields from a dictionary (Python 3.8+)
# Or by passing keyword arguments.
# For older Python versions, _replace only accepts keyword arguments directly.
# Let's verify if _replace accepts dictionary directly (Python 3.8+)
try:
    import sys
    if sys.version_info >= (3, 8):
        updated_values = {'x': 50, 'y': 60}
        p_updated_dict = p1._replace(**updated_values) # Unpack dictionary
        print(f"p1._replace(**dict) for {p1}: {p_updated_dict}")
    else:
        print("Note: _replace(**dict) requires Python 3.8+.")
        p_updated_kw = p1._replace(x=50, y=60) # Traditional way
        print(f"p1._replace(kw_args) for {p1}: {p_updated_kw}")
except Exception as e:
    print(f"Error demonstrating _replace with dict: {e}")


print("\n--- 7. Use Cases for Named Tuples ---")
print("- **Database Records**: Representing rows from a database query.")
print("- **CSV/JSON Parsing**: Reading data from structured files.")
print("- **Coordinates/Points**: Simple geometric objects (as shown above).")
print("- **Configuration Objects**: Immutable settings.")
print("- **Function Return Values**: Returning multiple named values from a function.")

def analyze_data(data_list):
    # Simulate some analysis and return results
    Stats = namedtuple('Stats', ['min_val', 'max_val', 'average', 'count'])
    if not data_list:
        return Stats(None, None, None, 0)
    return Stats(min(data_list), max(data_list), sum(data_list) / len(data_list), len(data_list))

my_data = [10, 20, 5, 30, 15]
analysis_results = analyze_data(my_data)
print(f"\nAnalysis Results: {analysis_results}")
print(f"Minimum Value: {analysis_results.min_val}")
print(f"Average Value: {analysis_results.average:.2f}")