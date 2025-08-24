print("--- Python Classes: Practice Code ---")

# --- 1. What is a Class? ---
print("\n--- 1. What is a Class? ---")
print("A class is a blueprint or a template for creating objects (instances).")
print("It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.")
print("Think of it like a cookie cutter: the class is the cutter, and the cookies are the objects (instances).")

# --- 2. Defining a Simple Class ---
print("\n--- 2. Defining a Simple Class ---")

class Dog:
    # Class attribute: Shared by all instances of the class
    species = "Canis familiaris"

    def __init__(self, name, age):
        """
        The constructor method. It's called automatically when a new object is created.
        'self' refers to the instance of the class being created.
        'name' and 'age' are instance attributes, specific to each dog object.
        """
        self.name = name
        self.age = age
        print(f"A new dog named {self.name} has been created!")

    def bark(self):
        """
        An instance method. It operates on the specific instance (self).
        """
        return f"{self.name} says Woof!"

    def human_age(self):
        """
        Another instance method that calculates a derived attribute.
        """
        return self.age * 7

# --- 3. Creating Objects (Instances) of a Class ---
print("\n--- 3. Creating Objects (Instances) of a Class ---")

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"\nType of dog1: {type(dog1)}")
print(f"Is dog1 an instance of Dog? {isinstance(dog1, Dog)}")


# --- 4. Accessing Attributes and Calling Methods ---
print("\n--- 4. Accessing Attributes and Calling Methods ---")

# Accessing instance attributes
print(f"\nDog 1's name: {dog1.name}")
print(f"Dog 1's age: {dog1.age}")
print(f"Dog 2's name: {dog2.name}")

# Accessing class attributes (can be accessed via instance or class itself)
print(f"Dog 1's species: {dog1.species}")
print(f"Dog 2's species: {dog2.species}")
print(f"Class species: {Dog.species}")

# Calling instance methods
print(f"{dog1.name} barks: {dog1.bark()}")
print(f"{dog2.name} barks: {dog2.bark()}")
print(f"{dog1.name}'s human age: {dog1.human_age()} years")


# --- 5. `self` Explained ---
print("\n--- 5. `self` Explained ---")
print("`self` is a convention (but strongly adhered to) in Python for the first parameter of instance methods.")
print("It refers to the instance of the class on which the method is called.")
print("When you do `dog1.bark()`, Python internally translates it to `Dog.bark(dog1)`.")
print("This `self` allows the method to access and modify the instance's specific attributes (`self.name`, `self.age`).")


# --- 6. Class Attributes vs. Instance Attributes ---
print("\n--- 6. Class Attributes vs. Instance Attributes ---")

# Class attribute `species` is shared
print(f"\nInitial Dog.species: {Dog.species}")
dog3 = Dog("Max", 2)
print(f"dog3.species: {dog3.species}")

# Modifying a class attribute via the class affects all instances
Dog.species = "Canis lupus familiaris"
print(f"\nAfter changing Dog.species:")
print(f"Dog.species: {Dog.species}")
print(f"dog1.species: {dog1.species}") # Refers to the changed class attribute
print(f"dog2.species: {dog2.species}")
print(f"dog3.species: {dog3.species}")

# Modifying an attribute via an instance creates an *instance-specific* attribute
# It *shadows* the class attribute for that instance.
dog1.species = "Canis domesticus"
print(f"\nAfter changing dog1.species:")
print(f"dog1.species: {dog1.species} (now an instance attribute)")
print(f"dog2.species: {dog2.species} (still refers to class attribute)")
print(f"Dog.species: {Dog.species} (class attribute remains)")


# --- 7. Inheritance: Building on Existing Classes ---
print("\n--- 7. Inheritance: Building on Existing Classes ---")
print("Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).")
print("This promotes code reusability and creates a hierarchical relationship.")

class Labrador(Dog): # Labrador inherits from Dog
    def __init__(self, name, age, color):
        # Call the parent class's constructor
        super().__init__(name, age) # Equivalent to Dog.__init__(self, name, age)
        self.color = color
        print(f"A new Labrador named {self.name} ({self.color}) has been created!")

    def bark(self): # Method Overriding: Labradors bark differently
        return f"{self.name} says Woof woof! (more enthusiastic)"

    def retrieve(self, item):
        return f"{self.name} retrieved the {item}!"

my_lab = Labrador("Goldie", 4, "golden")
print(f"\nLabrador's name: {my_lab.name}")
print(f"Labrador's age: {my_lab.age}")
print(f"Labrador's color: {my_lab.color}")
print(f"Labrador's species: {my_lab.species}") # Inherited from Dog
print(f"Labrador barks: {my_lab.bark()}") # Overridden method
print(f"Labrador retrieves: {my_lab.retrieve('ball')}")


# --- 8. Method Types: Instance, Class, and Static Methods ---
print("\n--- 8. Method Types: Instance, Class, and Static Methods ---")

class Animal:
    planet = "Earth" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

    def describe(self): # Instance method: takes 'self'
        return f"{self.name} is an animal on {self.planet}."

    @classmethod # Class method: takes 'cls' (the class itself)
    def from_string(cls, animal_string):
        # Can access/modify class attributes or create instances of the class
        name_part = animal_string.split(" ")[0]
        return cls(name_part) # Creates an instance of the class (Animal or its subclass)

    @staticmethod # Static method: takes no special first argument (neither self nor cls)
    def get_info():
        # Behaves like a regular function but is logically part of the class.
        # Cannot access instance or class specific attributes/methods directly.
        return "This is a general animal utility function."

# Instance method usage
animal1 = Animal("Leo")
print(f"\nInstance method: {animal1.describe()}")

# Class method usage
# Can be called on the class or an instance, but `cls` refers to the class.
animal2 = Animal.from_string("Zebra stripes")
print(f"Class method created: {animal2.name}")

class Bird(Animal):
    pass # Bird inherits from Animal

bird1 = Bird.from_string("Sparrow bird") # `cls` here will be Bird
print(f"Class method (subclass): {bird1.name}, Type: {type(bird1)}")

# Static method usage
print(f"Static method (via class): {Animal.get_info()}")
print(f"Static method (via instance): {animal1.get_info()}")


# --- 9. Encapsulation (Public, Protected, Private attributes - by convention) ---
print("\n--- 9. Encapsulation ---")
print("Python doesn't have strict 'private' keywords like Java or C++.")
print("It uses naming conventions to suggest visibility:")
print(" - `public_attribute`: Accessible from anywhere (default).")
print(" - `_protected_attribute`: Single leading underscore. Conventionally, don't access directly from outside the class or its subclasses.")
print(" - `__private_attribute`: Double leading underscore (name mangling). Python renames it to `_ClassName__private_attribute` to make it harder to access directly.")

class MyClass:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected (by convention)"
        self.__private = "I'm private (name mangled)"

    def get_private(self):
        return self.__private # Accessible within the class

obj = MyClass()
print(f"\nPublic: {obj.public}")
print(f"Protected: {obj._protected}") # Still accessible, but "don't touch"
# print(obj.__private) # This would raise AttributeError
print(f"Private (via method): {obj.get_private()}")
# How to access mangled name (not recommended for general use)
print(f"Private (via mangled name): {obj._MyClass__private}")


# --- 10. Polymorphism ---
print("\n--- 10. Polymorphism ---")
print("Polymorphism means 'many forms'. In OOP, it refers to the ability of objects of different classes")
print("to respond to the same method call in different ways (often through inheritance and method overriding).")

def make_sound(animal):
    print(animal.bark()) # Assumes the object has a 'bark' method

class Cat:
    def __init__(self, name):
        self.name = name
    def bark(self): # Even though it's a cat, we'll give it a 'bark' method for demonstration
        return f"{self.name} says Meow!"

print("\nPolymorphism in action:")
dog_instance = Dog("Pupper", 1)
cat_instance = Cat("Whiskers")
lab_instance = Labrador("Rex", 3, "black")

make_sound(dog_instance)
make_sound(cat_instance) # Calls Cat's bark method
make_sound(lab_instance) # Calls Labrador's overridden bark method


print("\n--- End of Python Classes Practice Code ---")