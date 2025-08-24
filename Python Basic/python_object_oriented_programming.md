# **Python OOP – From Basic to Advanced** 🚀  

Python supports **Object-Oriented Programming (OOP)**, a paradigm that models real-world entities using **classes** and **objects**.  

---

## **1️⃣ What is Object-Oriented Programming?**
OOP focuses on **creating objects** that contain both **data (attributes)** and **behavior (methods)**.  
### **Key OOP Concepts:**
- **Class** → A blueprint for creating objects.
- **Object** → An instance of a class.
- **Encapsulation** → Hiding data to protect it from unauthorized access.
- **Abstraction** → Hiding implementation details and showing only relevant information.
- **Inheritance** → Allows a class to inherit properties from another class.
- **Polymorphism** → Objects of different classes can be treated as instances of the same class.

---

# **🔹 BASIC OOP IN PYTHON**
## **2️⃣ Creating a Simple Class and Object**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object (instance)
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla
```
📌 **Explanation:**  
- `__init__()` → Constructor method that initializes attributes.  
- `self` → Refers to the current instance of the class.

---

## **3️⃣ Instance Variables vs. Class Variables**
```python
class Person:
    species = "Human"  # Class variable (shared by all instances)

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

# Creating objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.species)  # Output: Human
print(p2.name)  # Output: Bob
```
📌 **Class variables** are **shared** across all instances, while **instance variables** are **unique** to each object.

---

## **4️⃣ Encapsulation (Data Hiding)**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

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
📌 **Encapsulation** protects data by using **private variables (`__variable`)**.

---

## **5️⃣ Property Decorators – Getters and Setters**
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
📌 **`@property`** → Makes a method act like an **attribute**.  
📌 **Setter (`@property_name.setter`)** → Controls how a value is set.

---

## **6️⃣ Inheritance (Code Reusability)**
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
📌 **Inheritance allows a class to inherit methods and attributes from another class.**  

---

## **7️⃣ Multiple Inheritance**
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

## **8️⃣ Method Overriding (Polymorphism)**
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

## **9️⃣ Operator Overloading (Magic Methods)**
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
📌 **Operator overloading** allows us to **define custom behavior** for operators like `+`, `-`, `*`, etc.

---

## **🔟 Abstract Classes (Hiding Implementation)**
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

## **1️⃣1️⃣ Class vs Static Methods**
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

## **1️⃣2️⃣ Metaclasses (Advanced)**
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

## **🎯 OOP Best Practices**
✅ Use **encapsulation** to protect data.  
✅ Prefer **composition over inheritance** to avoid deep inheritance chains.  
✅ Use **abstract classes and interfaces** for structured design.  
✅ **Follow naming conventions** (`CamelCase` for classes, `snake_case` for variables).  

---

## **📌 Summary**
| Concept | Description |
|---------|------------|
| Class & Object | Blueprint and instance |
| Encapsulation | Hiding data (`private` variables) |
| Inheritance | Reusing code from another class |
| Polymorphism | Overriding methods |
| Abstraction | Hiding implementation details |
| Static & Class Methods | Methods independent of an instance |
| Operator Overloading | Custom behavior for operators |

🚀 **Mastering OOP in Python will help you write cleaner, reusable, and scalable code!** 🚀


Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects**, which are instances of **classes**. Python is an object-oriented language, and OOP is a fundamental concept in Python programming. Below is a comprehensive guide to Python OOP, starting from basic concepts and progressing to advanced topics.

---

## **1. Basic Concepts of OOP**

### **1.1 Classes and Objects**
- A **class** is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects will have.
- An **object** is an instance of a class.

#### **Example: Creating a Class and Object**
```python
# Define a class
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

# Create an object (instance of the class)
my_dog = Dog("Buddy", 3)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Buddy says woof!
```

---

### **1.2 Attributes and Methods**
- **Attributes**: Variables that belong to an object or class.
  - **Instance attributes**: Unique to each object.
  - **Class attributes**: Shared by all instances of the class.
- **Methods**: Functions that belong to an object or class.

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

### **1.3 The `self` Keyword**
- `self` refers to the current instance of the class. It is used to access instance attributes and methods.

#### **Example: Using `self`**
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

## **2. Intermediate Concepts**

### **2.1 Inheritance**
- Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
- It promotes code reuse and establishes a relationship between classes.

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
- It is achieved through method overriding and duck typing.

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



Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects, which are instances of classes. In Python, OOP is one of the most widely used paradigms, allowing developers to create modular, reusable, and maintainable code. Let’s explore Python's OOP concepts from basic to advanced.

### 1. **Basic Concepts of OOP**

#### **Class and Object**

- **Class**: A blueprint for creating objects (a particular data structure), defining methods (functions) and attributes (variables).
- **Object**: An instance of a class.

#### Example of Class and Object:

```python
# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def bark(self):
        print(f"{self.name} says woof!")

# Create an object of the class Dog
my_dog = Dog("Buddy", 5)

# Accessing object's methods and attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
my_dog.bark()       # Output: Buddy says woof!
```

#### **Constructor (`__init__` method)**

The `__init__()` method is called when an object is instantiated. It initializes the object's attributes.

#### Example:

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.brand)  # Output: Toyota
```

### 2. **Attributes and Methods**

- **Instance Attributes**: Variables that belong to a specific object.
- **Instance Methods**: Functions that belong to the object and can access the instance’s attributes.

#### Example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create an object
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

### 3. **Encapsulation**

Encapsulation is the concept of restricting access to certain details of an object and exposing only the necessary parts. This is done using **private** and **public** access modifiers.

- **Public Attributes**: Attributes that can be accessed directly.
- **Private Attributes**: Attributes that are not directly accessible outside the class (denoted by a leading underscore `_` or double underscore `__`).

#### Example:

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = Account("John", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# Direct access to __balance will raise an error
# print(account.__balance)  # AttributeError
```

- **Public Method**: `get_balance()` is used to access the private attribute `__balance`.

### 4. **Inheritance**

Inheritance allows a class to inherit methods and attributes from another class. This helps in code reuse and creating hierarchies.

- **Base Class (Parent Class)**: The class being inherited from.
- **Derived Class (Child Class)**: The class that inherits from the base class.

#### Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

In this example, `Dog` and `Cat` are derived classes that inherit from the base class `Animal`. Both override the `speak` method.

### 5. **Polymorphism**

Polymorphism allows different classes to be treated as instances of the same class through inheritance. It refers to the ability of a method to behave differently depending on the object it is acting on.

#### Example:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()
```

Output:
```
Woof!
Meow!
Animal speaks
```

Each class has its own version of the `speak()` method, but all can be treated as `Animal`.

### 6. **Abstraction**

Abstraction is the process of hiding the implementation details and showing only the essential features. This is typically done using **abstract classes** and **abstract methods**.

- **Abstract Class**: A class that cannot be instantiated and is designed to be inherited by other classes.
- **Abstract Method**: A method that is declared but does not have an implementation in the abstract class. Subclasses must implement this method.

To use abstraction in Python, you can use the `ABC` module.

#### Example:

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

Here, the `Shape` class is abstract, and the `Circle` class must implement the `area()` method.

### 7. **Class Methods and Static Methods**

- **Class Methods**: Methods that take the class as the first argument (`cls`) and can access class attributes.
- **Static Methods**: Methods that do not take any special first argument and don’t access or modify class or instance attributes.

#### Example:

```python
class MyClass:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        print(f"Class method accessed {cls.class_variable}")

    @staticmethod
    def static_method():
        print("Static method accessed")

# Calling class method
MyClass.class_method()  # Output: Class method accessed Hello

# Calling static method
MyClass.static_method()  # Output: Static method accessed
```

### 8. **Operator Overloading**

Operator overloading allows you to define the behavior of operators for objects of a class. This is done by defining special methods in the class.

#### Example: Overloading `+` Operator

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(result)  # Output: Point(6, 8)
```

The `__add__` method is used to overload the `+` operator to add two `Point` objects.

### 9. **Mixins**

A **mixin** is a class that provides methods to other classes but is not intended to be instantiated on its own. Mixins are often used to add specific functionality to classes.

#### Example: Mixin for Logging

```python
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class MyClass(LoggerMixin):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        self.log(f"{self.name} says Hello!")
        print(f"Hello from {self.name}")

obj = MyClass("Alice")
obj.say_hello()  
```

Output:
```
[LOG]: Alice says Hello!
Hello from Alice
```

### 10. **Advanced Concepts in OOP**

#### **Multiple Inheritance**
In Python, a class can inherit from multiple classes, which can introduce complexities like the **diamond problem**. Python handles this using the **Method Resolution Order (MRO)**.

```python
class A:
    def do_something(self):
        print("A doing something")

class B(A):
    def do_something(self):
        print("B doing something")

class C(A):
    def do_something(self):
        print("C doing something")

class D(B, C):
    pass

d = D()
d.do_something()  # Output: B doing something (based on MRO)
```

#### **Descriptors**

Descriptors are objects that define how attributes are accessed and modified. They are used to manage attributes in classes more efficiently.

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Accessing attribute!"

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Output: Accessing attribute!
```

### Conclusion:

Object-Oriented Programming (OOP) in Python is a powerful paradigm that promotes code reuse, modularity, and organization. By understanding basic concepts like classes and objects, and advancing to more complex topics like inheritance, polymorphism, encapsulation, and abstraction, you can write clean, scalable, and maintainable code.

From creating simple classes and objects to more advanced concepts such as multiple inheritance, mixins, operator overloading, and descriptors, Python’s OOP capabilities are both flexible and robust, enabling developers to solve complex problems efficiently.


Alright, let's dive into Object-Oriented Programming (OOP) in Python, covering everything from the basics to more advanced concepts.

**1. Core Concepts**

OOP is a programming paradigm that revolves around "objects," which are self-contained entities that encapsulate data (attributes) and behavior (methods).

*   **Class:** A blueprint or template for creating objects. It defines the attributes and methods that objects of that class will have. Think of it as a cookie cutter.
*   **Object (Instance):** A specific realization of a class. It's a concrete entity created from the class blueprint. Think of it as the actual cookie created using the cutter.
*   **Attribute:** A variable associated with an object. It stores data about the object.  Also known as "properties."
*   **Method:** A function associated with an object. It defines the actions an object can perform.
*   **Encapsulation:** Bundling data (attributes) and methods that operate on that data within a class. It helps hide internal implementation details and protect data from unauthorized access.
*   **Abstraction:**  Presenting only essential information to the user and hiding complex implementation details. It simplifies the interaction with objects.
*   **Inheritance:**  A mechanism where a new class (subclass/derived class) inherits attributes and methods from an existing class (superclass/base class). It promotes code reuse and establishes "is-a" relationships.
*   **Polymorphism:**  The ability of an object to take on many forms. It allows objects of different classes to respond to the same method call in their own way.

**2. Creating Classes and Objects**

```python
# Define a class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer) - called when an object is created
    def __init__(self, name, breed):
        # Instance attributes (unique to each object)
        self.name = name
        self.breed = breed
        self.is_sleeping = False  # Default state

    # Instance method (operates on the object's data)
    def bark(self):
        return "Woof!"

    def sleep(self):
        self.is_sleeping = True
        return f"{self.name} is now sleeping."

    def wake_up(self):
        self.is_sleeping = False
        return f"{self.name} has woken up!"

# Create objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Poodle")

# Access attributes
print(my_dog.name)  # Output: Buddy
print(your_dog.breed) # Output: Poodle
print(Dog.species)  # Output: Canis familiaris (accessing class attribute)

# Call methods
print(my_dog.bark())  # Output: Woof!
print(your_dog.sleep()) # Output: Buddy is now sleeping.
print(your_dog.wake_up()) # Output: Lucy has woken up!
```

Key points:

*   `class` keyword defines a class.
*   `__init__()` is the constructor (initializer). It's automatically called when you create an object.  The `self` parameter refers to the object being created.
*   `self` is used to access instance attributes and methods within the class.
*   Class attributes are shared by all instances of the class. Instance attributes are unique to each object.
*   Methods are functions defined within a class.

**3. Inheritance**

```python
# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

# Derived class (Child class) inheriting from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        # Call the parent class's constructor
        super().__init__(name)  # Use super() to call the parent's __init__
        self.breed = breed

    # Override the speak() method
    def speak(self):
        return "Meow!"

    def purr(self):
        return "Purrrr..."

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self): #overriding
        return "Woof!"


# Create objects
my_cat = Cat("Whiskers", "Siamese")
my_dog = Dog("Rover")

print(my_cat.name)  # Output: Whiskers (inherited from Animal)
print(my_cat.breed) # Output: Siamese
print(my_cat.speak()) # Output: Meow! (overridden method)
print(my_cat.purr())  # Output: Purrrr... (Cat-specific method)
print(my_dog.speak()) # Output: Woof!
```

Key points:

*   Use parentheses `()` after the class name to indicate inheritance: `class Cat(Animal):`
*   `super()` is used to call methods from the parent class. This is important for initializing the parent's attributes.
*   **Method overriding:**  A subclass can provide its own implementation of a method that is already defined in the superclass. This allows subclasses to customize behavior.

**4. Polymorphism**

Polymorphism means "many forms." In OOP, it allows objects of different classes to respond to the same method call in their own way.

*   **Duck Typing:**  A form of polymorphism where the type of an object is less important than whether it has the methods and attributes required. "If it walks like a duck and quacks like a duck, then it must be a duck."
*   **Method Overriding (as seen in Inheritance):** Different subclasses can provide different implementations of the same method.

```python
# Example of polymorphism

animals = [Cat("Whiskers", "Siamese"), Dog("Rover"), Animal("Generic")]

for animal in animals:
    print(animal.speak())  # Each object responds differently to the speak() method
# Output:
# Meow!
# Woof!
# Generic animal sound
```

**5. Encapsulation and Data Hiding**

Encapsulation involves bundling data and methods together and controlling access to the data.  Python doesn't have strict private variables like some other languages, but it uses naming conventions to suggest privacy.

*   **Naming Conventions:**
    *   `_variable`:  A single underscore indicates a "protected" member. It suggests that the variable should not be accessed directly from outside the class, but it's still possible.
    *   `__variable`: A double underscore indicates a "private" member. Python uses name mangling to make it harder (but not impossible) to access these variables directly from outside the class.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self): #Getter Method
        return self.__balance

    def get_account_number(self):
        return self._account_number

my_account = BankAccount("1234567890", 1000)

# Accessing protected attribute (discouraged but possible)
print(my_account._account_number)  # Output: 1234567890

# Attempting to access private attribute (name mangling)
# print(my_account.__balance)  # This will raise an AttributeError

print(my_account.get_balance()) # Output 1000

my_account.deposit(500)
print(my_account.get_balance()) # Output 1500

my_account.withdraw(200)
print(my_account.get_balance()) # Output 1300
```

Key points:

*   The single and double underscore conventions are *suggestions* to other developers.  Python doesn't enforce strict privacy.
*   Name mangling changes the name of `__balance` to something like `_BankAccount__balance`, making it less obvious to access directly.
*   **Getter and Setter Methods:** Provide controlled access to attributes. Getter methods retrieve the value of an attribute, and setter methods modify the value (often with validation).  This is a more robust way to encapsulate data.

**6. Abstraction**

Abstraction focuses on hiding complex implementation details and presenting a simplified interface to the user. Abstract base classes (ABCs) are a way to enforce abstraction in Python.

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method (must be implemented by subclasses)

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing the Shape ABC
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Concrete class implementing the Shape ABC
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# You cannot create an instance of the abstract class Shape:
# my_shape = Shape()  # This will raise a TypeError

my_rectangle = Rectangle(5, 10)
print(my_rectangle.area())  # Output: 50

my_circle = Circle(3)
print(my_circle.area())  # Output: 28.27431
```

Key points:

*   `abc` module provides support for abstract base classes.
*   `ABC` is the base class for creating abstract classes.
*   `@abstractmethod` decorator marks a method as abstract. Subclasses *must* implement these methods.
*   You cannot create instances of abstract classes directly. They serve as blueprints for concrete subclasses.

**7. Advanced OOP Concepts**

*   **Multiple Inheritance:** A class can inherit from multiple base classes.  This can lead to complex inheritance hierarchies and potential conflicts (the "diamond problem"). Use with caution.

    ```python
    class A:
        def method(self):
            print("Method from A")

    class B:
        def method(self):
            print("Method from B")

    class C(A, B):  # Inherits from both A and B
        pass

    obj = C()
    obj.method()  # Output: Method from A (due to method resolution order)

    print(C.mro()) #Method Resolution Order - tells you how python will resolve method calls
    # Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
    ```

*   **Mixins:**  Small classes that provide specific functionality to other classes through multiple inheritance.  Often used to add features without creating deep inheritance hierarchies.

    ```python
    class Printable:
        def print_me(self):
            print(f"Printing: {self.__dict__}")

    class MyClass(Printable):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    obj = MyClass(10, 20)
    obj.print_me()  # Output: Printing: {'x': 10, 'y': 20}
    ```

*   **Data Classes (Python 3.7+):**  Classes that are primarily used to store data. The `dataclasses` module automatically generates methods like `__init__`, `__repr__`, `__eq__`, etc.

    ```python
    from dataclasses import dataclass

    @dataclass
    class Point:
        x: int
        y: int

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)  # Output: Point(x=1, y=2)
    print(p1 == p2) # Output: True (automatically generates __eq__)
    ```

*   **Metaclasses:**  Classes that create classes. They allow you to control the creation process of classes, modify class behavior, or enforce certain patterns. This is a very advanced topic.

*   **Properties:** A way to define getter, setter, and deleter methods for class attributes, allowing you to control access and modification.

    ```python
    class Celsius:
        def __init__(self, temperature=0):
            self._temperature = temperature

        def to_fahrenheit(self


Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects**, which are instances of **classes**. Python is an object-oriented language, and OOP is one of its core features. This guide will take you from the **basics** to **advanced concepts** of OOP in Python.

---

## **1. Basics of OOP**

### **1.1 What is OOP?**
- OOP is a programming paradigm that uses **objects** and **classes** to structure code.
- It focuses on **encapsulation**, **inheritance**, **polymorphism**, and **abstraction**.
- Objects are instances of classes, and classes are blueprints for creating objects.

---

### **1.2 Key Concepts**
1. **Class**: A blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) of the objects.
2. **Object**: An instance of a class.
3. **Attribute**: A variable that belongs to an object or class.
4. **Method**: A function that belongs to an object or class.

---

### **1.3 Creating a Class and Object**
```python
# Define a class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method (called when an object is created)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

# Create an object (instance of the Dog class)
my_dog = Dog("Buddy", 5)

# Access attributes and methods
print(my_dog.name)          # Output: Buddy
print(my_dog.age)           # Output: 5
print(my_dog.species)       # Output: Canis familiaris
print(my_dog.bark())        # Output: Buddy says woof!
```

---

### **1.4 The `self` Keyword**
- `self` refers to the instance of the class.
- It is used to access attributes and methods within the class.
- Python automatically passes the instance as the first argument to methods.

---

### **1.5 Class and Instance Attributes**
- **Class attributes**: Shared by all instances of the class.
- **Instance attributes**: Unique to each instance.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Access class attribute
print(Dog.species)  # Output: Canis familiaris

# Create instances
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Access instance attributes
print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max
```

---

## **2. Intermediate OOP Concepts**

### **2.1 Inheritance**
- Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
- It promotes code reuse and modularity.

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

# Create an instance of the child class
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says woof!
```

---

### **2.2 Method Overriding**
- A child class can override a method defined in the parent class.

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

```python
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # Call the parent class constructor
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says chirp!"

bird = Bird("Tweety", True)
print(bird.speak())  # Output: Tweety says chirp!
```

---

### **2.4 Multiple Inheritance**
- A class can inherit from multiple parent classes.

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
print(obj.greet())  # Output: Hello from A (A's method is called first)
```

---

### **2.5 Encapsulation**
- Encapsulation restricts access to certain attributes and methods.
- Use **private attributes** (prefixed with `_` or `__`) to control access.

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

## **3. Advanced OOP Concepts**

### **3.1 Polymorphism**
- Polymorphism allows objects of different classes to be treated as objects of a common superclass.
- It can be achieved through **method overriding** and **duck typing**.

```python
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

def animal_sound(animal):
    return animal.speak()

cat = Cat()
dog = Dog()

print(animal_sound(cat))  # Output: Meow!
print(animal_sound(dog))  # Output: Woof!
```

---

### **3.2 Abstract Base Classes (ABCs)**
- ABCs define a blueprint for other classes. They cannot be instantiated directly.
- Use the `abc` module to create abstract classes.

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

# shape = Shape()  # Error: Cannot instantiate abstract class
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

### **3.3 Magic Methods (Dunder Methods)**
- Magic methods are special methods with double underscores (`__`) that allow custom behavior for built-in operations.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Addition of two objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

---

### **3.4 Class Methods and Static Methods**
- **Class methods**: Methods that operate on the class itself, not the instance. Use `@classmethod`.
- **Static methods**: Methods that do not depend on the instance or class. Use `@staticmethod`.

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

### **3.5 Property Decorators**
- Use `@property` to define getter, setter, and deleter methods for attributes.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)  # Output: 25
temp.celsius = 30
print(temp.celsius)  # Output: 30
```

---

## **4. Best Practices**
1. Use meaningful names for classes, methods, and attributes.
2. Follow the **Single Responsibility Principle** (a class should have only one reason to change).
3. Use inheritance sparingly; prefer composition over inheritance.
4. Encapsulate data and expose only necessary methods.
5. Use abstract classes to define interfaces.

---

By mastering these concepts, you can write clean, modular, and reusable code using Python's OOP features!