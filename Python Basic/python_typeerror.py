# --- TypeError: All About in Code ---

# A TypeError is raised when an operation or function is applied to an object
# of an inappropriate type. This means the type of the object itself prevents
# the operation from being performed.

# --- 1. Basic TypeError: Incompatible Types in Operations ---
print("--- 1. Basic TypeError: Incompatible Types in Operations ---")

# 1.1 Arithmetic operations
try:
    result = 10 + "hello" # Cannot add int and str
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Unsupported operand type(s) for +: 'int' and 'str'.")

try:
    result = "5" * "2" # Cannot multiply str by str (can multiply str by int)
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Can't multiply sequence by non-int of type 'str'.")

print("-" * 50 + "\n")


# 1.2 Comparison operations (less common, but can happen with custom objects)
# For built-in types, most comparisons are allowed, though might yield unexpected results.
# TypeError often arises when comparing custom objects without __eq__, __lt__, etc.
class CustomObject:
    def __init__(self, value):
        self.value = value

    # Uncommenting the below would allow comparison and prevent TypeError for this case
    # def __lt__(self, other):
    #     if isinstance(other, CustomObject):
    #         return self.value < other.value
    #     return NotImplemented

obj1 = CustomObject(10)
obj2 = "another_object"

try:
    print(obj1 < obj2) # Cannot compare CustomObject with str without custom __lt__
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: '<' not supported between instances of 'CustomObject' and 'str'.")

print("-" * 50 + "\n")


# --- 2. TypeError: Calling Non-Callable Objects ---
print("--- 2. TypeError: Calling Non-Callable Objects ---")

# Only functions, methods, classes, and objects with a __call__() method are callable.
my_variable = "I am a string"
my_number = 123

try:
    my_variable() # Trying to call a string as a function
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'str' object is not callable.")

try:
    my_number() # Trying to call an int as a function
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'int' object is not callable.")

print("-" * 50 + "\n")


# --- 3. TypeError: Incorrect Number/Type of Arguments to Function/Method ---
print("--- 3. TypeError: Incorrect Number/Type of Arguments ---")

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# 3.1 Too few arguments
try:
    greet("Alice") # Missing 'age' argument
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'greet()' missing 1 required positional argument: 'age'.")

# 3.2 Too many arguments
try:
    greet("Bob", 25, "extra") # Extra argument
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'greet()' takes 2 positional arguments but 3 were given.")

# 3.3 Incorrect argument types (often results in TypeError internally)
# This isn't strictly a 'TypeError on argument', but the operation inside fails due to type
def add_numbers(a, b):
    return a + b

try:
    add_numbers(10, "5") # 'b' is a string, not a number for addition
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Unsupported operand type(s) for +: 'int' and 'str' inside function.")

print("-" * 50 + "\n")


# --- 4. TypeError: Indexing/Slicing Non-Sequence Types ---
print("--- 4. TypeError: Indexing/Slicing Non-Sequence Types ---")

# Only sequence types (strings, lists, tuples) or objects implementing __getitem__
# can be indexed or sliced.

my_number = 123
my_boolean = True
my_set = {1, 2, 3} # Sets are not ordered, hence not indexable

try:
    print(my_number[0]) # Trying to index an int
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'int' object is not subscriptable.")

try:
    print(my_boolean[0]) # Trying to index a bool
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'bool' object is not subscriptable.")

try:
    print(my_set[0]) # Trying to index a set
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'set' object is not subscriptable.")

print("-" * 50 + "\n")


# --- 5. TypeError: Iterating Over Non-Iterable Objects ---
print("--- 5. TypeError: Iterating Over Non-Iterable Objects ---")

# Only iterable objects (lists, tuples, strings, dictionaries, sets, generators etc.)
# can be used in a `for` loop or with `iter()`.

my_int_for_loop = 123
my_float_for_loop = 4.56

try:
    for item in my_int_for_loop:
        print(item)
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'int' object is not iterable.")

try:
    iterator = iter(my_float_for_loop)
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'float' object is not iterable.")

print("-" * 50 + "\n")


# --- 6. TypeError in Class Methods (Incorrect `self` handling) ---
print("--- 6. TypeError in Class Methods (Incorrect `self` handling) ---")

class MyBrokenClass:
    # This method is missing 'self' as the first parameter
    def print_message():
        print("This message should be printed.")

try:
    instance = MyBrokenClass()
    instance.print_message() # Python automatically passes 'instance' as the first arg
                             # but 'print_message' expects 0 arguments.
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'print_message()' takes 0 positional arguments but 1 was given.")

class MyCorrectClass:
    def print_message_correct(self):
        print(f"Message from {self.__class__.__name__} instance.")

instance_correct = MyCorrectClass()
instance_correct.print_message_correct()

print("-" * 50 + "\n")


# --- 7. TypeError with Custom Object Conversions/Casting ---
print("--- 7. TypeError with Custom Object Conversions/Casting ---")

# If you try to cast a custom object to a built-in type (e.g., str(), int())
# without implementing the appropriate dunder methods (`__str__`, `__int__` etc.),
# it can result in a TypeError.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Uncomment to enable str() conversion and avoid TypeError
    # def __str__(self):
    #     return f"{self.name} (Price: ${self.price:.2f})"

    # Uncomment to enable int() conversion and avoid TypeError
    # def __int__(self):
    #     return int(self.price)

my_product = Product("Coffee Maker", 75.50)

try:
    print("Product as string: " + str(my_product)) # Will fail without __str__
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Can't convert Product object to str without __str__ method.")

try:
    total_price = int(my_product) + 10 # Will fail without __int__
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Can't convert Product object to int without __int__ method.")

print("-" * 50 + "\n")


# --- 8. TypeError with List/Tuple Packing and Unpacking ---
print("--- 8. TypeError with List/Tuple Packing and Unpacking ---")

# Unpacking requires the number of variables to match the number of elements in the iterable.

data_tuple = (10, 20)

try:
    a, b, c = data_tuple # Too many variables for unpacking
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Cannot unpack non-iterable int object (too many values to unpack).")
    # The error message is a bit misleading here. It means the `data_tuple`
    # *could not* provide 3 values because it only has 2.
    # A more common error message is "not enough values to unpack (expected 3, got 2)".

# Correct unpacking
x, y = data_tuple
print(f"Correct unpacking: x={x}, y={y}")

print("-" * 50 + "\n")


# --- 9. TypeError with Incorrect Use of `None` ---
print("--- 9. TypeError with Incorrect Use of `None` ---")

# `None` is an object of type `NoneType`. Operations on `NoneType` are very limited.
# Often, an `AttributeError` for `NoneType` methods can precede a `TypeError`
# if the problematic `None` is then passed to a function expecting a different type.

def process_data(data):
    if data is None:
        print("Received None data, skipping processing.")
        return
    try:
        # If 'data' is not a list, this will cause a TypeError
        for item in data:
            print(f"Processing item: {item}")
    except TypeError as e:
        print(f"Caught TypeError inside process_data (expected): {e}")
        print("Reason: 'data' is not iterable (e.g., it's an int, or None).")

process_data([1, 2, 3]) # OK
process_data(None)      # Handled by `if data is None`

value_from_api = None # Simulate an API returning None
# value_from_api = "some_string" # Uncomment to see it pass
# value_from_api = 123 # Uncomment to see TypeError

print("\nCalling process_data with potentially problematic values:")
process_data(value_from_api)

print("-" * 50 + "\n")

print("--- End of TypeError demonstration ---")




# --- TypeError: More Examples (Continued) ---

# This section delves into further scenarios where TypeError can arise,
# including more nuanced interactions with object types and built-in functions.

# --- 10. TypeError with Type Hints (Runtime Behavior) ---
print("--- 10. TypeError with Type Hints (Runtime Behavior) ---")

# Type hints are for static analysis (linters, IDEs) and don't enforce types at runtime
# by default. A TypeError will still occur if incompatible types are used.

def add_numbers_with_hints(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

print(f"Adding 5 + 3 (correct types): {add_numbers_with_hints(5, 3)}")

try:
    # This will still raise a TypeError at runtime, despite the type hints
    result = add_numbers_with_hints(10, "5")
except TypeError as e:
    print(f"Caught TypeError (expected, type hints not enforced at runtime): {e}")
    print("Reason: Still unsupported operand type(s) for +: 'int' and 'str'.")

# Note: Libraries like `mypy` perform static type checking and would flag this
# as an error *before* runtime. For runtime type enforcement, libraries like
# `typeguard` or custom decorators are needed.

print("-" * 50 + "\n")


# --- 11. TypeError with Immutable Objects (e.g., Tuples, Strings) ---
print("--- 11. TypeError with Immutable Objects ---")

# Immutable objects cannot be changed after creation. Attempting to modify them
# in-place (like appending to a tuple) will result in a TypeError.

my_tuple = (1, 2, 3)
my_string = "hello"

try:
    my_tuple[0] = 10 # Tuples do not support item assignment
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'tuple' object does not support item assignment.")

try:
    my_tuple.append(4) # Tuples do not have an append method
except AttributeError as e: # This is AttributeError, not TypeError, for missing method
    print(f"Caught AttributeError (expected for .append() on tuple): {e}")
    print("Reason: 'tuple' object has no attribute 'append'.")


try:
    my_string[0] = 'H' # Strings do not support item assignment
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'str' object does not support item assignment.")

# Correct way to "modify" immutable objects: create a new one
new_tuple = my_tuple + (4,)
print(f"New tuple: {new_tuple}")

new_string = 'H' + my_string[1:]
print(f"New string: {new_string}")

print("-" * 50 + "\n")


# --- 12. TypeError with Set Operations ---
print("--- 12. TypeError with Set Operations ---")

# Set operations (union, intersection, difference) generally require iterable arguments.
# Attempting to use non-hashable types as set elements, or incorrect arguments for methods,
# can lead to TypeErrors.

my_set = {1, 2, 3}

try:
    my_set.add([4, 5]) # Lists are unhashable and cannot be added to a set
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Unhashable type: 'list'.")

another_set = {3, 4, 5}
try:
    union_set = my_set.union(10) # 10 is not an iterable
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'int' object is not iterable.")

# Correct union
union_set_correct = my_set.union(another_set)
print(f"Correct union: {union_set_correct}")

print("-" * 50 + "\n")


# --- 13. TypeError with F-strings (Complex Objects) ---
print("--- 13. TypeError with F-strings (Complex Objects) ---")

# While f-strings are powerful, if an object doesn't have a suitable __str__ or __repr__
# method, or if an operation within the f-string curly braces is invalid, TypeError can occur.

class NoStringRepresentation:
    def __init__(self, data):
        self.data = data

# If an object doesn't define __str__ or __repr__, it defaults to a less friendly representation.
# It doesn't typically cause a TypeError *just* for being put in an f-string,
# but an operation *on* the object within the f-string can.

obj_no_repr = NoStringRepresentation(123)
print(f"Object with no __str__/__repr__: {obj_no_repr}") # This prints default repr, not TypeError

try:
    # Attempting an operation on obj_no_repr that its type doesn't support
    # (e.g., if it was expected to be a number)
    print(f"Result: {obj_no_repr + 10}")
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: Unsupported operand type for + with custom object and int.")

print("-" * 50 + "\n")


# --- 14. TypeError from Built-in Functions/Constructors ---
print("--- 14. TypeError from Built-in Functions/Constructors ---")

# Many built-in functions and class constructors expect specific types.

# 14.1 `int()`, `float()`, `str()`, `bool()`
try:
    int_from_list = int([1, 2]) # Cannot convert list to int
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: int() argument must be a string, a bytes-like object or a real number, not 'list'.")

try:
    bool_from_invalid = bool(None) # None correctly evaluates to False, not a TypeError
    # bool(0) is also False, no TypeError
    # bool([]) is also False, no TypeError
    # TypeError here would be rare unless you pass a custom object without __bool__ or __len__
    class NoBoolOrLen: pass
    bool(NoBoolOrLen()) # This usually works unless some other issue.
except Exception as e:
    print(f"Caught unexpected error for bool(): {e}") # Rarely TypeError for bool()

# 14.2 `range()`
try:
    list(range(10.5)) # Range arguments must be integers
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: 'float' object cannot be interpreted as an integer.")

# 14.3 `len()`
try:
    length = len(123) # int has no length
except TypeError as e:
    print(f"Caught TypeError (expected): {e}")
    print("Reason: object of type 'int' has no len().")

print("-" * 50 + "\n")


# --- 15. TypeError in Deserialization (json, pickle) ---
print("--- 15. TypeError in Deserialization (json, pickle) ---")

# When using serialization libraries, providing a non-string/bytes object to load/loads
# functions, or trying to serialize non-serializable objects, can lead to TypeError.
import json
import pickle

# json.loads() expects a string or bytes-like object
try:
    json_object = json.loads(123) # int is not a valid JSON string
except TypeError as e:
    print(f"Caught TypeError (expected for json.loads(int)): {e}")
    print("Reason: the JSON object must be str, bytes or bytearray, not int.")

# json.dumps() can raise TypeError for non-serializable objects (handled in previous examples)
class NonSerializable:
    pass

try:
    json.dumps(NonSerializable())
except TypeError as e:
    print(f"Caught TypeError (expected for json.dumps(NonSerializable)): {e}")
    print("Reason: Object of type 'NonSerializable' is not JSON serializable.")


# pickle.loads() expects bytes-like object
try:
    pickle_object = pickle.loads("hello") # string is not a valid pickle bytes
except TypeError as e:
    print(f"Caught TypeError (expected for pickle.loads(str)): {e}")
    print("Reason: a bytes-like object is required, not 'str'.")
except pickle.UnpicklingError as e: # This might also be UnpicklingError if it's not valid pickle format
    print(f"Caught UnpicklingError (expected for invalid pickle str): {e}")


print("-" * 50 + "\n")

print("--- End of More TypeError Examples ---")
