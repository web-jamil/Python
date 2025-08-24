# ---------------------------------------------------
# issubclass() in Python
# ---------------------------------------------------

# The issubclass() built-in function is used to check if a class is a subclass
# (direct or indirect) of another class.

# Syntax: issubclass(class, classinfo)
#   - class: The class to be checked.
#   - classinfo: A class, type, or a tuple of classes and types.

# 1. Basic Usage: Checking against a single parent class

class Animal:
    pass

class Dog(Animal):
    pass

class GoldenRetriever(Dog):
    pass

class Cat(Animal):
    pass

class Vehicle:
    pass

print("--- Basic Class Checks ---")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")               # True (Dog is a direct subclass of Animal)
print(f"issubclass(GoldenRetriever, Dog): {issubclass(GoldenRetriever, Dog)}") # True
print(f"issubclass(GoldenRetriever, Animal): {issubclass(GoldenRetriever, Animal)}") # True (GoldenRetriever is an indirect subclass of Animal)
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")               # True
print(f"issubclass(Animal, Dog): {issubclass(Animal, Dog)}")               # False (Animal is a superclass, not a subclass of Dog)
print(f"issubclass(Dog, Cat): {issubclass(Dog, Cat)}")                     # False (No inheritance relationship)
print(f"issubclass(Dog, Dog): {issubclass(Dog, Dog)}")                     # True (A class is considered a subclass of itself)
print(f"issubclass(Animal, object): {issubclass(Animal, object)}")         # True (All classes implicitly inherit from 'object')
print(f"issubclass(int, object): {issubclass(int, object)}")               # True (Built-in types also inherit from 'object')

# 2. Checking against a tuple of classes (OR logic)
#    - If `classinfo` is a tuple, `issubclass()` returns True if `class` is a
#      subclass of any of the classes/types in the tuple.

print("\n--- Checking Against a Tuple of Classes ---")
print(f"issubclass(Dog, (Animal, Vehicle)): {issubclass(Dog, (Animal, Vehicle))}")       # True (Dog is a subclass of Animal)
print(f"issubclass(Vehicle, (Animal, Vehicle)): {issubclass(Vehicle, (Animal, Vehicle))}") # True (Vehicle is a subclass of Vehicle itself)
print(f"issubclass(int, (float, str, int)): {issubclass(int, (float, str, int))}")       # True
print(f"issubclass(list, (tuple, dict)): {issubclass(list, (tuple, dict))}")           # False

# 3. Checking with Built-in Types

print("\n--- Checking with Built-in Types ---")
print(f"issubclass(bool, int): {issubclass(bool, int)}")             # True (bool is a subclass of int)
print(f"issubclass(int, bool): {issubclass(int, bool)}")             # False
print(f"issubclass(list, object): {issubclass(list, object)}")       # True
print(f"issubclass(dict, object): {issubclass(dict, object)}")       # True
print(f"issubclass(str, object): {issubclass(str, object)}")         # True

# 4. Using issubclass() with Type Hinting (informal use case, not direct `issubclass` feature)
#    - While `issubclass` directly checks classes, type hints help convey
#      inheritance relationships in code for static analysis.

from typing import Type

def register_animal_type(animal_type: Type[Animal]):
    """Registers a new animal type, ensuring it's a subclass of Animal."""
    if not issubclass(animal_type, Animal):
        raise TypeError(f"{animal_type.__name__} must be a subclass of Animal.")
    print(f"Registered animal type: {animal_type.__name__}")

print("\n--- Using issubclass() for Type Validation (Example) ---")
register_animal_type(Dog)
register_animal_type(GoldenRetriever)

try:
    register_animal_type(Vehicle) # This will raise an error
except TypeError as e:
    print(f"Error registering Vehicle: {e}")

# 5. Comparing issubclass() with isinstance()
#    - `issubclass()` checks the relationship between CLASSES.
#    - `isinstance()` checks if an OBJECT is an instance of a CLASS (or its subclass).

print("\n--- issubclass() vs isinstance() ---")
my_dog_instance = Dog()

print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")           # True (Class Dog is a subclass of Class Animal)
print(f"isinstance(my_dog_instance, Animal): {isinstance(my_dog_instance, Animal)}") # True (Object my_dog_instance is an instance of Class Animal)

print(f"issubclass(my_dog_instance, Animal): {issubclass(my_dog_instance, Animal)}") # TypeError: arg 1 must be a class
# The above line would cause a TypeError because `issubclass` expects a class as its first argument, not an instance.

# 6. Abstract Base Classes (ABCs) and issubclass()
#    - issubclass() works well with ABCs, allowing you to check if a class
#      implements an interface defined by an ABC.
#    - A class can be registered as a "virtual subclass" of an ABC using `ABC.register()`,
#      making `issubclass()` return True even without explicit inheritance.

from collections.abc import Sized, Iterable
import abc

class MyCustomContainer:
    def __init__(self, data):
        self._data = data
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data)

class AnotherContainer:
    pass

print("\n--- Using issubclass() with ABCs ---")
print(f"issubclass(MyCustomContainer, Sized): {issubclass(MyCustomContainer, Sized)}") # True (MyCustomContainer implements __len__)
print(f"issubclass(MyCustomContainer, Iterable): {issubclass(MyCustomContainer, Iterable)}") # True (MyCustomContainer implements __iter__)
print(f"issubclass(AnotherContainer, Sized): {issubclass(AnotherContainer, Sized)}")   # False

# Example of `register` (for more advanced ABC usage)
class CustomListABC(abc.ABC):
    @abc.abstractmethod
    def add(self, item):
        pass

@CustomListABC.register
class MyNonInheritingList:
    def __init__(self):
        self.data = []
    def add(self, item):
        self.data.append(item)

print(f"issubclass(MyNonInheritingList, CustomListABC): {issubclass(MyNonInheritingList, CustomListABC)}") # True (due to register)

# 7. Metaclasses and issubclass() (Advanced)
#    - issubclass() works correctly with classes created via metaclasses.

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubClass(MyClass):
    pass

print("\n--- Metaclasses and issubclass() ---")
print(f"issubclass(MySubClass, MyClass): {issubclass(MySubClass, MyClass)}") # True