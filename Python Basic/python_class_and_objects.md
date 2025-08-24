In Python, **classes** and **objects** are the foundation of Object-Oriented Programming (OOP). A **class** is a blueprint for creating objects, and an **object** is an instance of a class. This guide will cover everything about classes and objects, from **basic concepts** to **advanced features**.

---

## Table of Contents
1. **Basic Concepts**
   - Defining a Class
   - Creating Objects
   - Attributes and Methods
   - The `__init__` Method (Constructor)
   - The `self` Parameter
2. **Intermediate Concepts**
   - Class Attributes vs Instance Attributes
   - Class Methods and Static Methods
   - Encapsulation (Private and Protected Members)
3. **Advanced Concepts**
   - Inheritance
   - Method Overriding
   - Polymorphism
   - Magic Methods (Dunder Methods)
   - Properties and Descriptors
   - Abstract Base Classes (ABCs)
4. **Best Practices**
   - Composition over Inheritance
   - SOLID Principles
   - Design Patterns

---

## 1. Basic Concepts

### **Defining a Class**
- A class is defined using the `class` keyword.
- It can contain attributes (variables) and methods (functions).

```python
class Dog:
    pass
```

---

### **Creating Objects**
- An object is an instance of a class. You can create an object by calling the class.

```python
my_dog = Dog()
```

---

### **Attributes and Methods**
- **Attributes** are variables that belong to an object.
- **Methods** are functions that belong to an object.

```python
class Dog:
    # Attribute
    species = "Canis familiaris"

    # Method
    def bark(self):
        print("Woof!")

# Create an object
my_dog = Dog()

# Access attribute
print(my_dog.species)  # Output: Canis familiaris

# Call method
my_dog.bark()  # Output: Woof!
```

---

### **The `__init__` Method (Constructor)**
- The `__init__` method is called when an object is created. It initializes the object's attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object with attributes
my_dog = Dog("Buddy", 5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
```

---

### **The `self` Parameter**
- The `self` parameter refers to the instance of the class. It is used to access attributes and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

my_dog = Dog("Buddy")
my_dog.greet()  # Output: Hello, my name is Buddy
```

---

## 2. Intermediate Concepts

### **Class Attributes vs Instance Attributes**
- **Class attributes** are shared by all instances of the class.
- **Instance attributes** are specific to each instance.

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name):
        # Instance attribute
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max
```

---

### **Class Methods and Static Methods**
- **Class methods** are bound to the class and not the instance. They use the `@classmethod` decorator.
- **Static methods** are utility methods that don't depend on the instance or class. They use the `@staticmethod` decorator.

```python
class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.add(2, 3))        # Output: 5
print(Math.multiply(2, 3))   # Output: 6
```

---

### **Encapsulation**
- Encapsulation restricts access to certain attributes and methods.
- Use `_` for **protected** members and `__` for **private** members.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Error: AttributeError
```

---

## 3. Advanced Concepts

### **Inheritance**
- Inheritance allows a class to inherit attributes and methods from another class.

```python
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.speak()  # Output: Animal speaks
my_dog.bark()   # Output: Woof!
```

---

### **Method Overriding**
- A child class can override a method from the parent class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

my_dog = Dog()
my_dog.speak()  # Output: Dog barks
```

---

### **Polymorphism**
- Polymorphism allows objects of different classes to be treated as objects of a common superclass.

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def animal_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Woof
```

---

### **Magic Methods (Dunder Methods)**
- Magic methods are special methods with double underscores (`__`) that allow you to define behavior for built-in operations.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

---

### **Properties and Descriptors**
- Properties allow you to add behavior to attribute access.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(0)
print(temp.fahrenheit)  # Output: 32.0
temp.fahrenheit = 100
print(temp.celsius)     # Output: 37.777...
```

---

### **Abstract Base Classes (ABCs)**
- ABCs define a blueprint for other classes. They cannot be instantiated directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

## 4. Best Practices

### **Composition over Inheritance**
- Prefer composition (using objects as attributes) over inheritance for better flexibility.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()
car.start()  # Output: Engine started
```

---

### **SOLID Principles**
- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

---

### **Design Patterns**
- Common design patterns like Singleton, Factory, and Observer can be implemented in Python.

```python
# Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # Output: True
```

---

## Conclusion
Classes and objects are the building blocks of Python's OOP paradigm. By mastering these concepts, you can write clean, reusable, and maintainable code. Practice is key to understanding and applying these principles effectively!



# **Python Classes and Objects – From Basic to Advanced**

Object-Oriented Programming (OOP) in Python revolves around **classes** and **objects**. A **class** is a blueprint for creating **objects**, and an **object** is an instance of a class with its own attributes and behaviors.

---

## **1. Creating a Simple Class and Object**
### **Defining a Class**
```python
class Car:
    def __init__(self, brand, model):  # Constructor
        self.brand = brand  # Instance Variable
        self.model = model  # Instance Variable

    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}")

# Creating an Object
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla
```
---

## **2. Class Attributes vs Instance Attributes**
- **Instance Attributes**: Unique to each object (e.g., `self.brand`, `self.model`).
- **Class Attributes**: Shared across all instances of a class.

### **Example:**
```python
class Employee:
    company = "TechCorp"  # Class Variable

    def __init__(self, name, salary):
        self.name = name  # Instance Variable
        self.salary = salary  # Instance Variable

emp1 = Employee("John", 5000)
emp2 = Employee("Emma", 7000)

print(emp1.company)  # Output: TechCorp
print(emp2.company)  # Output: TechCorp

# Changing the class attribute affects all objects
Employee.company = "NewCorp"
print(emp1.company)  # Output: NewCorp
```
---

## **3. Instance Methods, Class Methods, and Static Methods**
Python provides three types of methods inside a class:

1. **Instance Methods**: Operate on instance variables.
2. **Class Methods**: Operate on class variables using `@classmethod`.
3. **Static Methods**: Independent methods using `@staticmethod`.

### **Example**
```python
class Example:
    class_variable = "Class Level"

    def __init__(self, value):
        self.instance_variable = value

    def instance_method(self):
        return f"Instance Method: {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"Class Method: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "Static Method: No instance or class variables used"

obj = Example("Instance Level")
print(obj.instance_method())  # Output: Instance Method: Instance Level
print(Example.class_method()) # Output: Class Method: Class Level
print(Example.static_method())# Output: Static Method: No instance or class variables used
```
---

## **4. Encapsulation (Data Hiding)**
Encapsulation restricts access to certain attributes:
- **Public Attributes**: `self.name`
- **Protected Attributes**: `_name`
- **Private Attributes**: `__name`

### **Example**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Trying to access private attribute directly will cause an error
# print(account.__balance)  # AttributeError
```
---

## **5. Inheritance (Reusability of Code)**
Inheritance allows one class to acquire properties and methods of another class.

### **Types of Inheritance**
1. **Single Inheritance**: One class inherits from another.
2. **Multiple Inheritance**: A class inherits from multiple classes.
3. **Multilevel Inheritance**: A class inherits from a derived class.
4. **Hierarchical Inheritance**: Multiple child classes inherit from a single parent.

### **Example: Single Inheritance**
```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

dog = Dog()
print(dog.make_sound())  # Output: Bark!
```
---

## **6. Method Overriding (Polymorphism)**
Method overriding allows a subclass to provide a specific implementation of a method.

```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Output:
# Bark!
# Meow!
```
---

## **7. Abstract Classes (Abstraction)**
Abstraction hides implementation details and only shows relevant parts. Python achieves this using the `abc` module.

### **Example**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())  # Output: 78.5
```
---

## **8. Operator Overloading**
Python allows operators like `+`, `-`, `*` to be overloaded using special methods.

### **Example: Overloading the `+` Operator**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
result = v1 + v2
print(result)  # Output: Vector(6, 8)
```
---

## **9. Properties (`@property` Decorator)**
Python allows defining **getter and setter methods** using the `@property` decorator.

### **Example**
```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected variable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Name cannot be empty!")

p = Person("Alice")
print(p.name)  # Output: Alice
p.name = "Bob"
print(p.name)  # Output: Bob
```
---

## **10. Class vs Static Methods in Detail**
### **Example**
```python
class MathOperations:
    @classmethod
    def class_method(cls):
        return "This is a class method"

    @staticmethod
    def static_method():
        return "This is a static method"

print(MathOperations.class_method())  # Output: This is a class method
print(MathOperations.static_method())  # Output: This is a static method
```
---

## **11. Metaclasses (Advanced)**
Metaclasses control class creation. They allow modifying class behavior before instantiation.

### **Example**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Output: Creating class MyClass
```
---

## **12. Design Patterns in OOP (Advanced)**
Some common design patterns in OOP:
1. **Singleton Pattern** (Ensures a class has only one instance).
2. **Factory Pattern** (Encapsulates object creation).
3. **Observer Pattern** (Allows event-driven programming).

---

# **Conclusion**
- **Classes and Objects** form the foundation of OOP.
- **Encapsulation, Inheritance, Polymorphism, and Abstraction** help in structuring and organizing code.
- **Advanced concepts** like `@property`, operator overloading, metaclasses, and design patterns enhance flexibility.

In Python, **classes** and **objects** are fundamental concepts in **Object-Oriented Programming (OOP)**. They allow for the creation of reusable and modular code, making it easier to model real-world scenarios. Let's explore **classes**, **objects**, and their associated **functions** from basic to advanced topics.

---

## 1. **Basic Concepts: Class and Object**

### **Class**:
A class is a blueprint for creating objects. It defines the structure and behavior (attributes and methods) that the objects will have.

### **Object**:
An object is an instance of a class. When you create an object, you are creating a concrete instance of the class with the data and functionality defined within the class.

### **Example: Basic Class and Object**

```python
# Define a class
class Dog:
    # Constructor method to initialize object attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Method to simulate barking
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object (instance of the Dog class)
my_dog = Dog("Buddy", 3)

# Accessing object attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Calling an object method
my_dog.bark()  # Output: Buddy says Woof!
```

In the example above:
- **`__init__`** is the constructor method, initializing the object with the attributes `name` and `age`.
- **`bark()`** is a method that operates on the object’s attributes.

---

## 2. **Class Attributes vs Instance Attributes**

- **Instance Attributes**: These belong to a specific instance of the class and are defined using `self`.
- **Class Attributes**: These are shared among all instances of the class. They are defined directly within the class, not using `self`.

### Example:

```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4 (Class attribute shared by all instances)
print(car2.wheels)  # Output: 4
```

---

## 3. **Methods: Instance, Class, and Static**

### **Instance Method**:
An instance method operates on the instance data (attributes). It has access to the `self` parameter, which refers to the instance.

### **Class Method**:
A class method operates on the class itself and is marked with the `@classmethod` decorator. It takes `cls` as the first argument, referring to the class, not the instance.

### **Static Method**:
A static method does not operate on instance or class data. It is independent and is marked with the `@staticmethod` decorator.

### Example:

```python
class Person:
    species = "Homo sapiens"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name}.")

    # Class method
    @classmethod
    def species_info(cls):
        print(f"Species: {cls.species}")

    # Static method
    @staticmethod
    def info():
        print("Humans are the only species of the genus Homo.")

# Create an object
person1 = Person("John", 30)

# Calling an instance method
person1.greet()  # Output: Hello, my name is John.

# Calling a class method
person1.species_info()  # Output: Species: Homo sapiens

# Calling a static method
person1.info()  # Output: Humans are the only species of the genus Homo.
```

---

## 4. **Inheritance**

Inheritance allows one class to inherit attributes and methods from another class. This facilitates code reuse and creating more complex classes by building on simpler ones.

### Example:

```python
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

# Create an object of the Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # Output: Buddy barks
```

In this example:
- `Dog` inherits from the `Animal` class and overrides the `speak()` method to provide its own behavior.
- The `super()` function allows calling methods from the base class.

---

## 5. **Method Overriding**

Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its superclass.

### Example:

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating objects and calling overridden method
a = Animal()
a.speak()  # Output: Animal makes a sound

d = Dog()
d.speak()  # Output: Dog barks
```

---

## 6. **Polymorphism**

Polymorphism allows different classes to be treated as instances of the same class, especially when they share the same method names. Each subclass can provide its own implementation of methods, but the calling code doesn’t need to know the specific type of object.

### Example:

```python
class Cat:
    def speak(self):
        print("Cat meows")

class Dog:
    def speak(self):
        print("Dog barks")

def animal_sound(animal):
    animal.speak()

# Calling the same function with different objects
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows
```

In this case, even though `animal_sound` is calling `speak()`, the actual behavior depends on the object passed.

---

## 7. **Encapsulation and Getter/Setter Methods**

Encapsulation refers to the practice of hiding the internal state of an object and only exposing methods to modify or retrieve that state. Python does not have explicit access modifiers like `private` or `protected`, but it uses naming conventions to indicate private attributes (using a leading underscore `_` or double underscore `__`).

### Example with Getter and Setter Methods:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000

# Setting new balance
account.set_balance(2000)
print(account.get_balance())  # Output: 2000
```

In this example:
- `__balance` is a private attribute.
- `get_balance()` is a getter method to access it.
- `set_balance()` is a setter method to modify it.

---

## 8. **Multiple Inheritance**

Multiple inheritance allows a class to inherit from more than one class. In this case, the class inherits methods and attributes from all its parent classes.

### Example:

```python
class A:
    def speak(self):
        print("Class A speaks")

class B:
    def speak(self):
        print("Class B speaks")

class C(A, B):
    pass

# Creating an object of class C
obj = C()
obj.speak()  # Output: Class A speaks
```

In this case, `C` inherits from both `A` and `B`, and it follows the **Method Resolution Order (MRO)** to determine which method to call.

---

## 9. **Operator Overloading**

Operator overloading allows you to define custom behavior for operators like `+`, `-`, `*`, etc., for objects of a class.

### Example: Overloading the `+` Operator

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Adding two Point objects using overloaded + operator
result = p1 + p2
print(result)  # Output: Point(4, 6)
```

Here, the `__add__` method is used to define the behavior of the `+` operator when applied to `Point` objects.

---

## 10. **Advanced: Descriptors and Metaclasses**

- **Descriptors** are objects that control the behavior of attribute access, assignment, and deletion in Python classes.
  
  **Example:**

  ```python
  class MyDescriptor:
      def __get__(self, instance, owner):
          return "Accessing value"

  class MyClass:
      attribute = MyDescriptor()

  obj = MyClass()
  print(obj.attribute)  # Output: Accessing value
  ```

- **Metaclasses** are classes of classes. They define the behavior of a class itself, allowing you to modify how classes are created.

---

## Conclusion

Understanding **classes** and **objects** in Python is fundamental to writing efficient, maintainable, and scalable code using **Object-Oriented Programming** (OOP). From basic concepts like creating classes and objects to more advanced topics such as **inheritance**, **polymorphism**, **encapsulation**, **multiple inheritance**, **operator overloading**, and more, Python provides a wide array of features to help you model and manage complex systems effectively.

Okay, let's break down Python classes, objects, and functions, covering everything from the fundamental concepts to more advanced techniques.

**1. Classes and Objects: The Foundation**

*   **Class Definition:** A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (behavior) that objects of that class will possess.

    ```python
    class Dog:  # Class name (convention: PascalCase)
        # Class attribute (shared by all Dog objects)
        species = "Canis familiaris"

        # Constructor (initializer) - called when an object is created
        def __init__(self, name, breed, age):
            # Instance attributes (unique to each Dog object)
            self.name = name
            self.breed = breed
            self.age = age
            self.is_sleeping = False

        # Instance method (operates on the object's data)
        def bark(self):
            return "Woof!"

        def describe(self):
            return f"{self.name} is a {self.age}-year-old {self.breed}."

        def sleep(self):
            self.is_sleeping = True
            return f"{self.name} is now sleeping."

        def wake_up(self):
            self.is_sleeping = False
            return f"{self.name} has woken up!"
    ```

*   **Object Creation (Instantiation):** Creating an object (also called an instance) from a class.

    ```python
    my_dog = Dog("Buddy", "Golden Retriever", 3)  # Creating a Dog object
    your_dog = Dog("Lucy", "Poodle", 5)  # Creating another Dog object
    ```

*   **Accessing Attributes and Calling Methods:**

    ```python
    print(my_dog.name)  # Output: Buddy (accessing an attribute)
    print(your_dog.breed) # Output: Poodle
    print(my_dog.bark())  # Output: Woof! (calling a method)
    print(my_dog.describe()) # Output: Buddy is a 3-year-old Golden Retriever.
    ```

**2. Class Attributes vs. Instance Attributes**

*   **Class Attributes:** Shared by all instances of the class.  Defined directly within the class but outside of any method.

    ```python
    class Dog:
        species = "Canis familiaris"  # Class attribute
        def __init__(self, name):
            self.name = name

    dog1 = Dog("Fido")
    dog2 = Dog("Rex")

    print(dog1.species)  # Output: Canis familiaris
    print(dog2.species)  # Output: Canis familiaris

    Dog.species = "New Value"  # Modifying the class attribute

    print(dog1.species)  # Output: New Value (affected for all instances)
    ```

*   **Instance Attributes:** Unique to each object.  Defined within the `__init__()` method using `self.attribute_name`.

    ```python
    class Dog:
        species = "Canis familiaris"
        def __init__(self, name):
            self.name = name #instance attribute

    dog1 = Dog("Fido")
    dog2 = Dog("Rex")

    print(dog1.name) #output: Fido
    print(dog2.name) #output: Rex

    dog1.name = "Charlie"
    print(dog1.name) # Output: Charlie
    print(dog2.name) # Output: Rex (dog2 is unaffected)
    ```

**3. Methods: Defining Behavior**

*   **Instance Methods:**  Operate on the data of a specific object.  They have `self` as the first parameter, which refers to the object itself.

    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self): #Instance Method
            return "Woof!"

        def rename(self, new_name):
            self.name = new_name # Modifying the object's attribute
            return f"Name changed to {self.name}"


    my_dog = Dog("Buddy")
    print(my_dog.bark())  # Output: Woof!
    print(my_dog.rename("Max")) #Output: Name changed to Max
    print(my_dog.name) # Output: Max
    ```

*   **Class Methods:**  Bound to the class itself, not to an instance.  They receive the class (`cls`) as the first parameter.  Use the `@classmethod` decorator.  Often used for factory methods (creating instances in a specific way).

    ```python
    class Dog:
        species = "Canis familiaris"
        num_dogs = 0 # Class attribute to track the number of dogs

        def __init__(self, name):
            self.name = name
            Dog.num_dogs += 1 #increment the count upon instantiation

        @classmethod
        def get_species(cls):
            return cls.species

        @classmethod
        def create_generic_dog(cls):
            #Factory Method
            return cls("Generic Dog") # Creates a Dog object with a default name


    print(Dog.get_species())  # Output: Canis familiaris
    generic_dog = Dog.create_generic_dog()
    print(generic_dog.name) # Output: Generic Dog
    print(Dog.num_dogs) #Output: 1
    ```

*   **Static Methods:**  Neither bound to the class nor to an instance. They are essentially regular functions that happen to be defined within the class. They don't receive `self` or `cls` as implicit arguments. Use the `@staticmethod` decorator.  Often used for utility functions related to the class.

    ```python
    class Dog:
        @staticmethod
        def is_mammal():
            return True

    print(Dog.is_mammal())  # Output: True
    ```

**4. The `__init__()` Method (Constructor)**

*   The `__init__()` method is a special method called the *constructor* or *initializer*. It's automatically called when you create a new object of the class.
*   Its primary purpose is to initialize the object's attributes.
*   The `self` parameter refers to the object being created.

    ```python
    class Dog:
        def __init__(self, name, breed, age):
            self.name = name
            self.breed = breed
            self.age = age
            self.is_sleeping = False  # Default value
    ```

**5. Inheritance and Polymorphism**

*   **Inheritance:** Creating new classes (subclasses) based on existing classes (superclasses).  Subclasses inherit attributes and methods from the superclass.

    ```python
    class Animal:  # Superclass
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "Generic animal sound"

    class Dog(Animal):  # Subclass inheriting from Animal
        def __init__(self, name, breed):
            super().__init__(name)  # Call the parent's constructor
            self.breed = breed

        def speak(self):  # Method overriding
            return "Woof!"

        def wag_tail(self):
            return "Tail wagging!"

    my_dog = Dog("Buddy", "Golden Retriever")
    print(my_dog.name)   # Output: Buddy (inherited from Animal)
    print(my_dog.speak())  # Output: Woof! (overridden method)
    print(my_dog.wag_tail()) # Output: Tail wagging!
    ```

*   **Polymorphism:** The ability of objects of different classes to respond to the same method call in their own way (method overriding).  Also achieved through duck typing (if it walks like a duck and quacks like a duck...).

    ```python
    animals = [Animal("Generic"), Dog("Buddy", "Golden Retriever")]

    for animal in animals:
        print(animal.speak())  # Different output based on the object's class
    # Output:
    # Generic animal sound
    # Woof!
    ```

**6. Encapsulation and Data Hiding**

*   Encapsulation: Bundling data (attributes) and methods that operate on that data within a class.
*   Data Hiding: Limiting direct access to internal data (attributes) to protect it from accidental modification. Python uses naming conventions to suggest privacy:
    *   `_variable`:  Protected (shouldn't be accessed directly from outside)
    *   `__variable`: Private (name mangling makes it harder to access directly)

    ```python
    class BankAccount:
        def __init__(self, account_number, balance):
            self._account_number = account_number  # Protected
            self.__balance = balance  # Private (name mangled)

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds")

        def get_balance(self):
            return self.__balance  # Getter method


    my_account = BankAccount("12345", 1000)
    print(my_account._account_number)  # Accessing protected (still possible)
    #print(my_account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
    print(my_account.get_balance()) # Output: 1000 (using the getter)
    ```

**7. Properties**

*   Properties provide a way to control access to attributes using getter, setter, and deleter methods. They allow you to add logic (validation, calculations) when getting or setting attribute values.

    ```python
    class Celsius:
        def __init__(self, temperature=0):
            self._temperature = temperature

        def to_fahrenheit(self):
            return (self._temperature * 9/5) + 32

        #Getter
        def get_temperature(self):
            print("Getting value")
            return self._temperature

        #Setter
        def set_temperature(self, value):
            if value < -273.15:
                raise ValueError("Temperature below absolute zero")
            print("Setting value")
            self._temperature = value

        temperature = property(get_temperature, set_temperature)

    c = Celsius()
    c.temperature = 37 # Setting value
    print(c.temperature) # Getting value # Output: 37
    print(c.to_fahrenheit()) # Output: 98.6
    ```

    *   **Using the `@property` decorator (more modern):**

        ```python
        class Celsius:
            def __init__(self, temperature=0):
                self._temperature = temperature

            @property
            def temperature(self):
                print("Getting value")
                return self._temperature

            @temperature.setter
            def temperature(self, value):
                if value < -273.15:
                    raise ValueError("Temperature below absolute zero")
                print("Setting value")
                self._temperature = value

            def to_fahrenheit(self):
                return (self._temperature * 9/5) + 32


        c = Celsius()
        c.temperature = 37  # Setting value
        print(c.temperature)  # Getting value # Output: 37
        print(c.to_fahrenheit())
        ```

**8. Special Methods (Magic Methods / Dunder Methods)**

*   Methods with double underscores (`__`) at the beginning and end of their names. They provide special behavior to your classes.

    *   `__init__(self, ...)`: Constructor (initializer)
    *   `__str__(self)`:  Returns a string representation of the object (for `print()` and `str()`)
    *   `__repr__(self)`: Returns a string representation of the object (for debugging, more technical)
    *   `__len__(self)`: Returns the length of the object (for `len()`)
    *   `__add__(self, other)`: Defines addition behavior (for `+` operator)
    *   `__eq__(self, other)`: Defines equality comparison (for `==` operator)
    *   `__lt__(self, other)`: Defines less-than comparison (for `<` operator)
    *   And many more...

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Point({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __eq__(self, other):
            return self.x == other.x and self
# **Python Classes and Objects – From Basic to Advanced** 🚀

## **🔹 What are Classes and Objects?**
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.
- **Attributes**: Variables inside a class.
- **Methods**: Functions inside a class.

---

# **🔹 1️⃣ Creating a Simple Class and Object**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance Variable
        self.model = model  # Instance Variable

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object (instance)
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla
```
📌 **Explanation:**  
- `__init__()` is the **constructor** that initializes the object.  
- `self` represents the instance of the class.  

---

# **🔹 2️⃣ Instance Variables vs. Class Variables**
```python
class Person:
    species = "Human"  # Class Variable (Shared)

    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age  # Instance Variable

# Creating objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.species)  # Output: Human
print(p2.name)  # Output: Bob
```
📌 **Class variables** are **shared**, while **instance variables** are **unique** to each object.

---

# **🔹 3️⃣ Encapsulation (Data Hiding)**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# print(account.__balance)  # ❌ Error! Private variable
```
📌 **Encapsulation** protects data using **private variables (`__variable`)**.

---

# **🔹 4️⃣ Property Decorators (Getters and Setters)**
```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):  # Getter
        return self.__salary

    @salary.setter
    def salary(self, amount):  # Setter
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be positive!")

emp = Employee(5000)
print(emp.salary)  # Output: 5000
emp.salary = 6000  # Updates salary
print(emp.salary)  # Output: 6000
```
📌 **`@property`** makes a method **act like an attribute**.

---

# **🔹 5️⃣ Inheritance (Code Reusability)**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
```
📌 **Inheritance** allows a class to **reuse attributes and methods** from another class.

---

# **🔹 6️⃣ Multiple Inheritance**
```python
class A:
    def method_A(self):
        return "Method from A"

class B:
    def method_B(self):
        return "Method from B"

class C(A, B):  # Multiple Inheritance
    pass

obj = C()
print(obj.method_A())  # Output: Method from A
print(obj.method_B())  # Output: Method from B
```
📌 **Python supports multiple inheritance**, meaning a class can inherit from multiple parents.

---

# **🔹 7️⃣ Method Overriding (Polymorphism)**
```python
class Bird:
    def fly(self):
        return "Bird is flying"

class Penguin(Bird):
    def fly(self):  # Overriding parent method
        return "Penguins can't fly"

penguin = Penguin()
print(penguin.fly())  # Output: Penguins can't fly
```
📌 **Overriding** allows a subclass to **change the behavior** of a parent class method.

---

# **🔹 8️⃣ Operator Overloading (Magic Methods)**
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python", 300)
book2 = Book("Java", 400)

print(book1 + book2)  # Output: 700
```
📌 **Operator overloading** allows custom behavior for operators like `+`, `-`, `*`, etc.

---

# **🔹 9️⃣ Abstract Classes (Hiding Implementation)**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```
📌 **Abstract classes** (`ABC`) **cannot be instantiated** and must be **implemented in child classes**.

---

# **🔟 Class vs Static Methods**
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.multiply(5, 3))  # Output: 15
```
📌 **`@staticmethod`** → Doesn't use `self` or `cls`, behaves like a normal function.  
📌 **`@classmethod`** → Uses `cls` and can modify class-level attributes.

---

# **🔹 1️⃣1️⃣ Metaclasses (Advanced)**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct["created_by"] = "Metaclass"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.created_by)  # Output: Metaclass
```
📌 **Metaclasses** control the creation of classes.

---

# **🎯 Best Practices**
✅ Use **encapsulation** to protect data.  
✅ Prefer **composition over inheritance** to avoid deep inheritance chains.  
✅ Use **abstract classes and interfaces** for structured design.  
✅ **Follow naming conventions** (`CamelCase` for classes, `snake_case` for variables).  

---

# **📌 Summary**
| Concept | Description |
|---------|------------|
| Class & Object | Blueprint and instance |
| Encapsulation | Hiding data (`private` variables) |
| Inheritance | Reusing code from another class |
| Polymorphism | Overriding methods |
| Abstraction | Hiding implementation details |
| Static & Class Methods | Methods independent of an instance |
| Operator Overloading | Custom behavior for operators |

🚀 **Mastering Classes & Objects in Python will help you write cleaner, reusable, and scalable code!** 🚀

In Python, **classes** and **objects** are the foundation of Object-Oriented Programming (OOP). A **class** is a blueprint for creating objects, and an **object** is an instance of a class. Classes encapsulate data (attributes) and behavior (methods) into a single entity.

Below is a comprehensive guide to Python classes and objects, starting from basic concepts and progressing to advanced topics.

---

## **1. Basic Concepts**

### **1.1 Defining a Class**
- Use the `class` keyword to define a class.
- Classes can have attributes (variables) and methods (functions).

#### **Example: Simple Class**
```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
```

---

### **1.2 Creating Objects**
- Objects are instances of a class.
- Use the class name followed by parentheses to create an object.

#### **Example: Creating an Object**
```python
# Create an object
my_dog = Dog("Buddy", 3)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Buddy says woof!
```

---

### **1.3 The `__init__` Method**
- The `__init__` method is called when an object is created.
- It is used to initialize instance attributes.

#### **Example: Using `__init__`**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)
print(person.introduce())  # Output: My name is Alice and I am 25 years old.
```

---

### **1.4 Class and Instance Attributes**
- **Class attributes**: Shared by all instances of the class.
- **Instance attributes**: Unique to each instance.

#### **Example: Class and Instance Attributes**
```python
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Output: Toyota
print(car2.wheels)  # Output: 4 (class attribute)
```

---

### **1.5 The `self` Keyword**
- `self` refers to the current instance of the class.
- It is used to access instance attributes and methods.

#### **Example: Using `self`**
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

## **2. Intermediate Concepts**

### **2.1 Inheritance**
- Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

#### **Example: Inheritance**
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

# Create objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())     # Output: Buddy says woof!
```

---

### **2.2 Method Overriding**
- A child class can override a method defined in the parent class.

#### **Example: Method Overriding**
```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says meow!
```

---

### **2.3 The `super()` Function**
- `super()` is used to call a method from the parent class.

#### **Example: Using `super()`**
```python
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Call the parent class's __init__ method
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says chirp!"

bird = Bird("Tweety", True)
print(bird.speak())  # Output: Tweety says chirp!
```

---

### **2.4 Encapsulation**
- Encapsulation is the concept of restricting access to certain attributes or methods.
- Use **private attributes** (prefixed with `_` or `__`) to achieve encapsulation.

#### **Example: Encapsulation**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Error: AttributeError
```

---

### **2.5 Polymorphism**
- Polymorphism allows objects of different classes to be treated as objects of a common superclass.

#### **Example: Polymorphism**
```python
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog("Buddy"))  # Output: Buddy says woof!
animal_sound(Cat("Whiskers"))  # Output: Whiskers says meow!
```

---

## **3. Advanced Concepts**

### **3.1 Class Methods and Static Methods**
- **Class methods**: Methods that operate on the class itself, not on instances. Use the `@classmethod` decorator.
- **Static methods**: Methods that do not depend on the class or instance. Use the `@staticmethod` decorator.

#### **Example: Class and Static Methods**
```python
class Math:
    # Class method
    @classmethod
    def add(cls, a, b):
        return a + b

    # Static method
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.add(2, 3))  # Output: 5
print(Math.multiply(2, 3))  # Output: 6
```

---

### **3.2 Magic (Dunder) Methods**
- Magic methods (e.g., `__init__`, `__str__`, `__add__`) allow you to define how objects behave with operators and built-in functions.

#### **Example: Magic Methods**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

---

### **3.3 Multiple Inheritance**
- A class can inherit from multiple parent classes.

#### **Example: Multiple Inheritance**
```python
class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):
    pass

obj = C()
print(obj.greet())  # Output: Hello from A (due to method resolution order)
```

---

### **3.4 Abstract Base Classes (ABCs)**
- ABCs define a blueprint for other classes. They cannot be instantiated directly.

#### **Example: Abstract Base Class**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

### **3.5 Composition over Inheritance**
- Composition is an alternative to inheritance where a class contains objects of other classes.

#### **Example: Composition**
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Output: Engine started
```

---

## **4. Best Practices**
1. Use meaningful class and method names.
2. Follow the **Single Responsibility Principle** (a class should have only one reason to change).
3. Prefer composition over inheritance when possible.
4. Use encapsulation to protect data.
5. Write docstrings to document your classes and methods.

---

## **5. Summary**
- **Classes** are blueprints for creating objects.
- **Objects** are instances of classes.
- **Inheritance** allows code reuse and establishes relationships between classes.
- **Encapsulation** protects data by restricting access.
- **Polymorphism** allows objects of different classes to be treated uniformly.
- Advanced concepts include **magic methods**, **ABCs**, and **composition**.

By mastering these concepts, you can write clean, reusable, and maintainable Python code using OOP principles.


Let's dive into the fundamentals of Object-Oriented Programming (OOP) in Python, focusing on classes, objects, attributes, methods, the `__init__` method, and the crucial `self` parameter.

---

### Theory: Understanding Classes and Objects

**1. Defining a Class**

* **Theory:** A class is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from this class will have. Think of it like a cookie cutter: the cutter itself is the class, defining the shape and characteristics of the cookies. It doesn't represent an actual cookie, but rather how cookies *can be* made.
* **Purpose:** Classes allow us to logically group data and functions that operate on that data. This promotes code organization, reusability, and modularity.

**2. Creating Objects (Instantiating a Class)**

* **Theory:** An object (also called an instance) is a concrete realization of a class. It's a specific entity created based on the class's blueprint. Following the cookie analogy, if the class is the cookie cutter, an object is an actual cookie made using that cutter. You can make many cookies from one cutter, and each cookie is a distinct object, even if they share the same shape.
* **Process:** Creating an object is called "instantiation." When you instantiate a class, Python allocates memory for that specific object and sets up its attributes and methods according to the class definition.

**3. Attributes and Methods**

* **Theory:**
    * **Attributes:** These are variables that belong to a class or an object. They represent the characteristics or data associated with the object.
        * **Class Attributes:** Belong to the class itself and are shared by all instances of that class. They are defined directly within the class body, outside of any methods.
        * **Instance Attributes:** Belong to a specific object (instance) and hold unique data for that object. They are typically defined within methods (most commonly `__init__`) using the `self` keyword.
    * **Methods:** These are functions defined inside a class that perform actions or operations on the object's data (attributes). They define the behavior of an object.
* **Analogy:** For a `Car` class:
    * **Attributes:** `color`, `brand`, `speed`, `num_wheels`
    * **Methods:** `start_engine()`, `accelerate()`, `brake()`, `turn_on_lights()`

**4. The `__init__` Method (Constructor)**

* **Theory:** The `__init__` method is a special method in Python classes. It's automatically called whenever a new object (instance) of the class is created. Its primary purpose is to initialize the attributes of the newly created object.
* **"Constructor":** Although Python doesn't have a strict "constructor" in the same way some other languages do, `__init__` serves the role of a constructor because it's responsible for setting up the initial state of an object.
* **Parameters:** It takes `self` as its first parameter (which refers to the newly created instance), followed by any other parameters needed to set the initial state of the object (e.g., `name`, `age` for a `Person` object).

**5. The `self` Parameter**

* **Theory:** `self` is a convention (not a keyword, but universally adopted) used as the very first parameter in instance methods (including `__init__`). It is a reference to the instance (object) that the method is being called on.
* **Why `self`?** When you call a method on an object (e.g., `my_dog.bark()`), Python automatically passes the `my_dog` object itself as the first argument to the `bark` method. Inside `bark`, this object is referred to by the parameter `self`.
* **Purpose:** `self` allows you to access and modify the instance's attributes and call other instance methods from within the class's methods. Without `self`, a method wouldn't know which specific object's data it should be operating on.

---

### Code: Practical Demonstration

```python
# ---------------------------------------------------
# 1. Defining a Class
# ---------------------------------------------------

# Class names typically follow PascalCase (e.g., MyClass, CarEngine).
# A docstring (triple quotes) immediately after the class definition is good practice
# to describe what the class does.

class Dog:
    """
    A class to represent a dog.
    This class demonstrates basic OOP concepts: attributes, methods, and the __init__ constructor.
    """

    # ---------------------------------------------------
    # 3. Class Attributes
    #    - Shared by all instances of the class.
    # ---------------------------------------------------
    species = "Canis familiaris" # All dogs belong to this species

    # ---------------------------------------------------
    # 4. The __init__ Method (Constructor)
    # ---------------------------------------------------
    # - This method is automatically called when a new object (instance) is created.
    # - It initializes the instance's attributes.
    # - 'self' is the first parameter and refers to the newly created instance itself.
    def __init__(self, name, breed, age):
        """
        Initializes a new Dog object.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
            age (int): The age of the dog in years.
        """
        # ---------------------------------------------------
        # 3. Instance Attributes
        #    - Unique to each object/instance.
        #    - Defined using 'self.attribute_name = value'.
        # ---------------------------------------------------
        self.name = name  # Instance attribute: the dog's name
        self.breed = breed # Instance attribute: the dog's breed
        self.age = age    # Instance attribute: the dog's age
        self.is_hungry = True # Default state for a new dog

    # ---------------------------------------------------
    # 3. Methods
    #    - Functions that belong to the class and operate on its instances.
    #    - 'self' is always the first parameter of an instance method.
    # ---------------------------------------------------

    def bark(self):
        """
        Makes the dog bark.
        Accesses the 'name' instance attribute using 'self.name'.
        """
        print(f"{self.name} says Woof! Woof!")

    def eat(self, food):
        """
        Simulates the dog eating food.
        Changes an instance attribute 'is_hungry' and prints a message.
        """
        if self.is_hungry:
            print(f"{self.name} is eating {food}.")
            self.is_hungry = False # Dog is no longer hungry after eating
        else:
            print(f"{self.name} is not hungry right now.")

    def get_info(self):
        """
        Returns a string containing information about the dog.
        Accesses multiple instance attributes and a class attribute.
        """
        return f"{self.name} is a {self.age}-year-old {self.breed} ({self.species})."


# ---------------------------------------------------
# 2. Creating Objects (Instantiating the Class)
# ---------------------------------------------------

# To create an object, you call the class name like a function,
# passing arguments that correspond to the parameters of the __init__ method
# (excluding 'self', which is passed automatically).

print("--- Creating Objects ---")
my_dog = Dog("Buddy", "Golden Retriever", 3)  # Creating an instance named 'my_dog'
your_dog = Dog("Lucy", "Labrador", 5)       # Creating another instance named 'your_dog'
stray_dog = Dog("Max", "Mixed Breed", 2)    # Yet another instance

print(f"Type of my_dog: {type(my_dog)}")
print(f"my_dog is an instance of Dog: {isinstance(my_dog, Dog)}")

# ---------------------------------------------------
# 3. Accessing Attributes and Calling Methods
# ---------------------------------------------------

print("\n--- Accessing Attributes ---")

# Accessing instance attributes using dot notation: object.attribute_name
print(f"My dog's name: {my_dog.name}")
print(f"Your dog's breed: {your_dog.breed}")
print(f"Stray dog's age: {stray_dog.age}")
print(f"My dog is hungry (initial state): {my_dog.is_hungry}")

# Accessing class attributes using either class name or object name
print(f"Dog species (via class): {Dog.species}")
print(f"My dog's species (via instance): {my_dog.species}")
# If you try to modify a class attribute via an instance, it often creates
# an instance attribute with the same name, rather than changing the class attribute.
# Dog.species = "Other" # This would change for all instances
# my_dog.species = "New Species" # This creates a new instance attribute for my_dog only.

print("\n--- Calling Methods ---")

# Calling methods using dot notation: object.method_name()
my_dog.bark()
your_dog.bark()

my_dog.eat("kibble") # Buddy eats and is no longer hungry
print(f"My dog is hungry (after eating): {my_dog.is_hungry}")
my_dog.eat("more kibble") # Buddy is not hungry

your_dog.eat("chicken") # Lucy eats

# Using the get_info method
print(my_dog.get_info())
print(your_dog.get_info())
print(stray_dog.get_info())

# ---------------------------------------------------
# Understanding 'self' in more detail
# ---------------------------------------------------
print("\n--- Understanding 'self' ---")

# When you call my_dog.bark(), Python internally translates it to:
# Dog.bark(my_dog)

# Let's verify the `id` (memory address) of 'self' inside the method
# and the object outside.

class SelfDemo:
    def __init__(self, value):
        self.value = value
        print(f"Inside __init__: self is {id(self)}")

    def show_self_id(self):
        print(f"Inside show_self_id: self is {id(self)}")
        print(f"Self's value: {self.value}")

my_demo_obj = SelfDemo(100)
print(f"Outside: my_demo_obj is {id(my_demo_obj)}")

my_demo_obj.show_self_id() # When this is called, my_demo_obj is automatically passed as 'self'


# When calling a method from another method within the same class:
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        print(f"Count incremented to {self.count}")

    def reset(self):
        # We use self.count to access the instance attribute
        # We use self.increment() to call another instance method
        print("Resetting counter...")
        self.count = 0
        self.increment() # This will call increment on *this* instance

my_counter = Counter()
my_counter.increment() # Count 1
my_counter.increment() # Count 2
my_counter.reset()     # Resets to 0, then increments to 1

```

Sure, let's dive into Python classes, covering all essential syntaxes, theoretical concepts, and practical code examples.

### Python Classes: All About with Theory and Code

#### 1. What are Classes and Objects?

In object-oriented programming (OOP), a **class** is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have. Think of it like a cookie cutter – the cutter itself is the class, and the cookies you make with it are the objects.

An **object** is an instance of a class. When you create an object, you are essentially creating a concrete entity based on the class's blueprint. Each object has its own unique set of data, but it shares the methods defined in the class.

**Key Concepts:**
* **Encapsulation:** Bundling data (attributes) and methods (functions) that operate on the data into a single unit (the class). This hides the internal implementation details from the outside world.
* **Abstraction:** Showing only essential information and hiding the complex implementation details. Classes provide a level of abstraction by allowing you to interact with objects without knowing their intricate inner workings.
* **Inheritance:** A mechanism where a new class (subclass/child class) can inherit properties and behaviors from an existing class (superclass/parent class). This promotes code reusability.
* **Polymorphism:** The ability of an object to take on many forms. In Python, this often refers to method overriding (subclasses providing their own implementation of a method defined in the superclass) and method overloading (though Python doesn't support true method overloading in the traditional sense, it can be simulated).

#### 2. Defining a Class

You define a class using the `class` keyword, followed by the class name (conventionally capitalized using CamelCase) and a colon.

**Syntax:**

```python
class ClassName:
    # Class body
    # Attributes and methods
```

**Example:**

```python
class Dog:
    pass # 'pass' is a placeholder, meaning "do nothing"
```

#### 3. Class Attributes (Variables)

Class attributes are variables that are shared by all instances (objects) of a class. They are defined directly within the class body, outside of any method.

**Syntax:**

```python
class ClassName:
    class_attribute = value
```

**Example:**

```python
class Dog:
    species = "Canis familiaris" # Class attribute

dog1 = Dog()
dog2 = Dog()

print(dog1.species)
print(dog2.species)
```

**Theory:** Class attributes are useful for storing data that is common to all objects of that class, such as constants or default values.

#### 4. The `__init__` Method (Constructor)

The `__init__` method is a special method called a constructor. It's automatically called when you create a new instance (object) of the class. It's used to initialize the object's attributes.

**Syntax:**

```python
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        # ...
```

**Theory:**
* `self`: The first parameter of any method in a class is always `self`. It's a convention and refers to the instance of the class itself. It allows you to access the instance's attributes and methods.
* The `__init__` method sets up the initial state of the object.

**Example:**

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating objects (instances) of the Dog class
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(my_dog.name)
print(my_dog.age)
print(your_dog.name)
print(your_dog.age)
```

#### 5. Instance Attributes

Instance attributes are variables that are unique to each instance (object) of a class. They are typically defined within the `__init__` method using `self.attribute_name`.

**Theory:** Instance attributes store data that varies from object to object.

**Example (already seen in `__init__` example):**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
```

#### 6. Instance Methods

Instance methods are functions defined within a class that operate on the instance's data. They always take `self` as their first parameter.

**Syntax:**

```python
class ClassName:
    def instance_method(self, parameter1, ...):
        # Method body
        # Access instance attributes using self.attribute_name
```

**Theory:** Instance methods allow objects to perform actions or manipulate their own data.

**Example:**

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.get_info())
```

#### 7. Class Methods

Class methods are methods that are bound to the class itself, not to an instance of the class. They take `cls` (conventionally) as their first parameter, which refers to the class itself. They are defined using the `@classmethod` decorator.

**Syntax:**

```python
class ClassName:
    @classmethod
    def class_method(cls, parameter1, ...):
        # Method body
        # Access class attributes using cls.class_attribute
```

**Theory:**
* Class methods are often used as alternative constructors (e.g., creating an instance from a different data format).
* They can access and modify class-level attributes.

**Example:**

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025 # Assuming current year for calculation
        age = current_year - birth_year
        return cls(name, age) # Create and return a new Dog instance

dog_from_year = Dog.from_birth_year("Max", 2022)
print(f"{dog_from_year.name} is {dog_from_year.age} years old and is a {dog_from_year.species}.")
```

#### 8. Static Methods

Static methods are methods that belong to the class but do not operate on either the instance or the class itself. They don't take `self` or `cls` as their first parameter. They are defined using the `@staticmethod` decorator.

**Syntax:**

```python
class ClassName:
    @staticmethod
    def static_method(parameter1, ...):
        # Method body
        # Does not access instance or class attributes
```

**Theory:**
* Static methods are utility functions that have a logical connection to the class but don't need any class or instance-specific data.
* They are like regular functions but are grouped within the class for organizational purposes.

**Example:**

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathOperations.add(5, 3))
print(MathOperations.multiply(4, 2))
```

#### 9. Inheritance

Inheritance allows a new class (child/derived class) to inherit attributes and methods from an existing class (parent/base class).

**Syntax:**

```python
class ParentClass:
    # ...

class ChildClass(ParentClass):
    # ...
```

**Theory:**
* **Code Reusability:** Avoids duplicating code by allowing common functionalities to be defined in a parent class and reused by child classes.
* **IS-A Relationship:** If `ChildClass` inherits from `ParentClass`, it means `ChildClass` "is a" `ParentClass`. (e.g., A `Car` is a `Vehicle`).

**Example:**

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"The {self.brand} is driving."

class Car(Vehicle): # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand) # Call the parent class's constructor
        self.model = model

    def honk(self):
        return f"The {self.brand} {self.model} honks!"

my_car = Car("Toyota", "Camry")
print(my_car.drive())
print(my_car.honk())

# Demonstrating polymorphism
class Bicycle(Vehicle):
    def ride(self):
        return "The bicycle is being ridden."

my_bicycle = Bicycle("Giant")
print(my_bicycle.drive()) # Bicycle can also drive (from Vehicle)
print(my_bicycle.ride())
```

**`super().__init__(...)`:** This is crucial in inheritance. It calls the `__init__` method of the parent class, ensuring that the parent's attributes are properly initialized in the child class instance.

#### 10. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that is already defined in its parent class.

**Syntax:**

```python
class ParentClass:
    def common_method(self):
        # Parent's implementation

class ChildClass(ParentClass):
    def common_method(self):
        # Child's specific implementation
```

**Theory:** Allows subclasses to provide specialized behavior for methods inherited from their superclass.

**Example:**

```python
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self): # Overriding make_sound
        return "Woof!"

class Cat(Animal):
    def make_sound(self): # Overriding make_sound
        return "Meow!"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.make_sound())
print(dog.make_sound())
print(cat.make_sound())
```

#### 11. Polymorphism

Polymorphism ("many forms") in Python refers to the ability of different objects to respond to the same method call in their own specific ways. This is often achieved through method overriding.

**Theory:** Enables writing generic code that can work with objects of different types, as long as they adhere to a common interface (i.e., they have the same method names).

**Example (demonstrated through method overriding):**

```python
def make_animal_sound(animal):
    print(animal.make_sound())

make_animal_sound(Animal())
make_animal_sound(Dog())
make_animal_sound(Cat())
```

In this example, `make_animal_sound` works with any object that has a `make_sound` method, regardless of its specific class.

#### 12. Special Methods (Dunder Methods)

Python classes have many special methods (also known as "dunder" methods because their names start and end with double underscores). These methods allow you to define how your objects behave in certain situations, such as when they are printed, compared, or used in arithmetic operations.

Some common dunder methods:

* `__str__(self)`: Called by `str()` and `print()`. Should return a human-readable string representation of the object.
* `__repr__(self)`: Called by `repr()`. Should return an "official" string representation that could be used to recreate the object.
* `__len__(self)`: Called by `len()`. Should return the length of the object.
* `__add__(self, other)`: Called by the `+` operator.
* `__eq__(self, other)`: Called by the `==` operator.

**Example:**

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 193)
book2 = Book("Pride and Prejudice", "Jane Austen", 279)
book3 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 193)

print(book1) # Uses __str__
print(repr(book1)) # Uses __repr__
print(len(book1)) # Uses __len__

print(book1 == book2) # Uses __eq__
print(book1 == book3) # Uses __eq__
```

#### 13. Access Modifiers (Convention)

Python doesn't have strict access modifiers like `public`, `private`, or `protected` as found in some other languages (e.g., Java, C++). However, it uses conventions to indicate the intended visibility of attributes and methods:

* **Public:** Attributes/methods without any leading underscores are considered public and can be accessed from anywhere. (Default)
* **Protected (Convention):** Attributes/methods starting with a single underscore (`_attribute_name`) are conventionally considered "protected." This indicates that they are intended for internal use within the class and its subclasses, but they can still be accessed from outside.
* **Private (Strong Convention/Name Mangling):** Attributes/methods starting with double underscores (`__attribute_name`) trigger "name mangling." This makes them harder (but not impossible) to access directly from outside the class. The interpreter renames them to `_ClassName__attribute_name`. This is intended to prevent accidental overriding in subclasses and to signal that they are strictly for internal use.

**Example:**

```python
class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected (by convention)"
        self.__private_var = "I am private (name mangled)"

    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method (by convention).")

    def __private_method(self):
        print("This is a private method (name mangled).")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()

obj = MyClass()
print(obj.public_var)
obj.public_method()

print(obj._protected_var) # Can be accessed, but convention suggests not directly
obj._protected_method()   # Can be called, but convention suggests not directly

# print(obj.__private_var) # This will raise an AttributeError
# obj.__private_method()   # This will raise an AttributeError

obj.access_private() # Accessing private members through a public method

# Accessing private member using name mangling (not recommended practice)
print(obj._MyClass__private_var)
```

#### 14. Property Decorator (`@property`)

The `@property` decorator allows you to define methods that can be accessed like attributes. It's often used to create "getters," "setters," and "deleters" for attributes, providing more control over how attributes are accessed and modified.

**Syntax:**

```python
class ClassName:
    def __init__(self, value):
        self._value = value # Using a private-like variable to store the actual data

    @property
    def value(self):
        # Getter method
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter method
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @value.deleter
    def value(self):
        # Deleter method
        del self._value
```

**Theory:**
* Provides an interface to access and modify attributes without directly exposing the underlying data.
* Allows you to add validation, logging, or other logic when an attribute is accessed or changed.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self._name = name # Stored internally as _name
        self._age = age   # Stored internally as _age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = new_age

    @age.deleter
    def age(self):
        print("Age deleted!")
        del self._age

person = Person("Alice", 30)
print(person.name) # Accessing like an attribute (calls the getter)
print(person.age)

person.name = "Bob" # Setting like an attribute (calls the setter)
person.age = 25

print(person.name)
print(person.age)

try:
    person.age = -5 # This will raise a ValueError due to setter validation
except ValueError as e:
    print(e)

del person.age # Calls the deleter
# print(person.age) # This would raise an AttributeError as age is deleted
```

#### 15. Abstract Base Classes (ABCs)

Abstract Base Classes provide a way to define interfaces. They cannot be instantiated directly, and their abstract methods must be implemented by concrete subclasses.

**Syntax:**

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Implementation of abstract method"
```

**Theory:**
* Enforce that subclasses implement specific methods, ensuring a common interface.
* Used for defining contracts that subclasses must adhere to.

**Example:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape() # This would raise a TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
```

#### 16. Multiple Inheritance

Python supports multiple inheritance, where a class can inherit from multiple parent classes.

**Syntax:**

```python
class ParentClass1:
    # ...

class ParentClass2:
    # ...

class ChildClass(ParentClass1, ParentClass2):
    # ...
```

**Theory:**
* Allows a class to combine features from multiple sources.
* Can lead to the "diamond problem" (Method Resolution Order - MRO) if not handled carefully. Python uses a C3 linearization algorithm for MRO.

**Example:**

```python
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())
```

**Method Resolution Order (MRO):** When using multiple inheritance, Python needs a way to resolve which method to call if a method exists in multiple parent classes. You can see the MRO using `ClassName.mro()` or `help(ClassName)`.

```python
print(Duck.mro())
# Output: [<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>]
```

This order dictates the search path for methods and attributes.

#### 17. Class Variables vs. Instance Variables (Revisited)

It's crucial to understand the distinction:

* **Class Variables:** Shared among all instances of a class. Changes to a class variable affect all instances.
* **Instance Variables:** Unique to each instance of a class. Changes to an instance variable only affect that specific instance.

**Example:**

```python
class Counter:
    total_instances = 0 # Class variable

    def __init__(self, name):
        self.name = name # Instance variable
        Counter.total_instances += 1 # Increment class variable

c1 = Counter("First")
c2 = Counter("Second")

print(f"C1 name: {c1.name}")
print(f"C2 name: {c2.name}")
print(f"Total instances: {Counter.total_instances}") # Access class variable via class name

c1.name = "Renamed First"
print(f"C1 name after rename: {c1.name}")
print(f"Total instances (still same for all): {Counter.total_instances}")
```

#### Conclusion

This comprehensive overview covers the core syntaxes and theoretical aspects of Python classes. Understanding these concepts is fundamental to writing organized, reusable, and maintainable object-oriented code in Python. Practice building your own classes and experimenting with these features to solidify your understanding.