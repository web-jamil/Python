# ---------------------------------------------------
# isinstance() in Python
# ---------------------------------------------------

# The isinstance() built-in function is used to check if an object is an instance
# of a specified class or of a subclass thereof.

# Syntax: isinstance(object, classinfo)
#   - object: The object to be checked.
#   - classinfo: A class, type, or a tuple of classes and types.

# 1. Basic Usage: Checking against a single type

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

my_dog = Dog()
my_cat = Cat()
my_animal = Animal()
my_list = [1, 2, 3]
my_int = 5
my_str = "hello"

print("--- Basic Type Checks ---")
print(f"isinstance(my_dog, Dog): {isinstance(my_dog, Dog)}")           # True
print(f"isinstance(my_cat, Cat): {isinstance(my_cat, Cat)}")           # True
print(f"isinstance(my_dog, Animal): {isinstance(my_dog, Animal)}")     # True (Dog is a subclass of Animal)
print(f"isinstance(my_animal, Animal): {isinstance(my_animal, Animal)}") # True
print(f"isinstance(my_dog, Cat): {isinstance(my_dog, Cat)}")           # False
print(f"isinstance(my_list, list): {isinstance(my_list, list)}")       # True
print(f"isinstance(my_int, int): {isinstance(my_int, int)}")           # True
print(f"isinstance(my_str, str): {isinstance(my_str, str)}")           # True
print(f"isinstance(my_str, int): {isinstance(my_str, int)}")           # False


# 2. Checking against a tuple of types (OR logic)
#    - If `classinfo` is a tuple, `isinstance()` returns True if `object` is an
#      instance of any of the classes/types in the tuple.

print("\n--- Checking Against a Tuple of Types ---")
print(f"isinstance(my_dog, (Dog, Cat)): {isinstance(my_dog, (Dog, Cat))}")       # True
print(f"isinstance(my_cat, (Dog, Cat)): {isinstance(my_cat, (Dog, Cat))}")       # True
print(f"isinstance(my_animal, (Dog, Cat)): {isinstance(my_animal, (Dog, Cat))}") # False
print(f"isinstance(my_int, (int, float)): {isinstance(my_int, (int, float))}")   # True
print(f"isinstance(3.14, (int, float)): {isinstance(3.14, (int, float))}")       # True
print(f"isinstance(my_str, (int, float, str)): {isinstance(my_str, (int, float, str))}") # True

# 3. Inheritance and Polymorphism with isinstance()
#    - isinstance() correctly handles inheritance. An instance of a subclass
#      is also considered an instance of its superclass(es).

print("\n--- Inheritance and Polymorphism ---")
class Vehicle:
    pass

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

my_electric_car = ElectricCar()

print(f"isinstance(my_electric_car, ElectricCar): {isinstance(my_electric_car, ElectricCar)}") # True
print(f"isinstance(my_electric_car, Car): {isinstance(my_electric_car, Car)}")               # True
print(f"isinstance(my_electric_car, Vehicle): {isinstance(my_electric_car, Vehicle)}")         # True
print(f"isinstance(my_electric_car, object): {isinstance(my_electric_car, object)}")         # True (All classes inherit from object)

# 4. Checking against Built-in Types

print("\n--- Checking Against Built-in Types ---")
print(f"isinstance(123, int): {isinstance(123, int)}")         # True
print(f"isinstance(3.14, float): {isinstance(3.14, float)}")     # True
print(f"isinstance('hello', str): {isinstance('hello', str)}")   # True
print(f"isinstance([1, 2], list): {isinstance([1, 2], list)}")   # True
print(f"isinstance((1, 2), tuple): {isinstance((1, 2), tuple)}") # True
print(f"isinstance({'a': 1}, dict): {isinstance({'a': 1}, dict)}") # True
print(f"isinstance({1, 2}, set): {isinstance({1, 2}, set)}")     # True
print(f"isinstance(True, bool): {isinstance(True, bool)}")       # True
print(f"isinstance(True, int): {isinstance(True, int)}")         # True (bool is a subclass of int)
print(f"isinstance(None, type(None)): {isinstance(None, type(None))}") # True

# 5. When to use isinstance() vs type()
#    - `isinstance()` is generally preferred over `type()` for type checking
#      because it accounts for inheritance.
#    - `type()` checks for exact type match, while `isinstance()` checks for
#      instance of class or a subclass.

print("\n--- isinstance() vs type() ---")
print(f"type(my_electric_car) == ElectricCar: {type(my_electric_car) == ElectricCar}") # True
print(f"type(my_electric_car) == Car: {type(my_electric_car) == Car}")               # False (Exact type mismatch)
print(f"isinstance(my_electric_car, Car): {isinstance(my_electric_car, Car)}")       # True (Handles inheritance)

# 6. Practical Use Cases

# Example 1: Function argument validation
def process_data(data):
    if isinstance(data, list):
        print("Processing list data:", data)
        for item in data:
            print(f"  Item: {item}")
    elif isinstance(data, dict):
        print("Processing dictionary data:", data)
        for key, value in data.items():
            print(f"  Key: {key}, Value: {value}")
    else:
        print(f"Unsupported data type: {type(data)}")

print("\n--- Practical Use Cases: Argument Validation ---")
process_data([10, 20, 30])
process_data({'name': 'Alice', 'age': 30})
process_data("hello world")

# Example 2: Conditional logic based on type
def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14159 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    else:
        raise TypeError("Unknown shape type")

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

print("\n--- Practical Use Cases: Conditional Logic ---")
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of circle: {calculate_area(circle)}")
print(f"Area of rectangle: {calculate_area(rectangle)}")

try:
    calculate_area("triangle")
except TypeError as e:
    print(f"Error: {e}")

# 7. Caveats: Mutable vs. Immutable Types for isinstance()
#    - isinstance() works consistently for both. The nature of the object
#      (mutable/immutable) doesn't change how isinstance() behaves.

print("\n--- isinstance() with Mutable/Immutable Types ---")
mutable_list = [1, 2]
immutable_tuple = (1, 2)
print(f"isinstance(mutable_list, list): {isinstance(mutable_list, list)}") # True
print(f"isinstance(immutable_tuple, tuple): {isinstance(immutable_tuple, tuple)}") # True

# 8. Abstract Base Classes (ABCs) with isinstance()
#    - isinstance() is commonly used with ABCs to check if an object implements
#      a certain interface, regardless of its concrete class hierarchy.

from collections.abc import Sequence, Mapping, Set

print("\n--- Using isinstance() with ABCs ---")
my_list_abc = [1, 2, 3]
my_dict_abc = {'a': 1, 'b': 2}
my_set_abc = {1, 2, 3}
my_str_abc = "abc"

print(f"isinstance(my_list_abc, Sequence): {isinstance(my_list_abc, Sequence)}") # True (list is a Sequence)
print(f"isinstance(my_dict_abc, Mapping): {isinstance(my_dict_abc, Mapping)}")   # True (dict is a Mapping)
print(f"isinstance(my_set_abc, Set): {isinstance(my_set_abc, Set)}")             # True (set is a Set)
print(f"isinstance(my_str_abc, Sequence): {isinstance(my_str_abc, Sequence)}")   # True (str is a Sequence)
print(f"isinstance(my_str_abc, Mapping): {isinstance(my_str_abc, Mapping)}")     # False

# End of isinstance() examples