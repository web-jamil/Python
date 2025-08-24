In Python, variable-length arguments allow you to pass a varying number of arguments to a function. This is useful when you don't know in advance how many arguments will be passed. There are two types of variable-length arguments in Python:

1. **\*args (Non-Keyword Arguments)**
2. **\*\*kwargs (Keyword Arguments)**

Let's explore both in detail, from basic to advanced usage.

---

### 1. **\*args (Non-Keyword Arguments)**

`*args` allows you to pass a variable number of **non-keyword arguments** to a function. The arguments are collected into a **tuple**.

#### Basic Usage:
```python
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```
**Output:**
```
1
2
3
```

- Here, `*args` collects all the positional arguments into a tuple.

#### Combining with Regular Arguments:
```python
def my_function(a, b, *args):
    print("a:", a)
    print("b:", b)
    print("args:", args)

my_function(1, 2, 3, 4, 5)
```
**Output:**
```
a: 1
b: 2
args: (3, 4, 5)
```

- `a` and `b` are regular arguments, while `*args` collects the remaining arguments.

#### Advanced Usage:
You can use `*args` to unpack a list or tuple when calling a function:
```python
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)  # Unpacks the list into arguments
```
**Output:**
```
1 2 3
```

---

### 2. **\*\*kwargs (Keyword Arguments)**

`**kwargs` allows you to pass a variable number of **keyword arguments** to a function. The arguments are collected into a **dictionary**.

#### Basic Usage:
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
```
**Output:**
```
name: Alice
age: 30
city: New York
```

- Here, `**kwargs` collects all the keyword arguments into a dictionary.

#### Combining with Regular Arguments and `*args`:
```python
def my_function(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

my_function(1, 2, 3, 4, 5, name="Alice", age=30)
```
**Output:**
```
a: 1
b: 2
args: (3, 4, 5)
kwargs: {'name': 'Alice', 'age': 30}
```

- `a` and `b` are regular arguments.
- `*args` collects additional positional arguments.
- `**kwargs` collects additional keyword arguments.

#### Advanced Usage:
You can use `**kwargs` to unpack a dictionary when calling a function:
```python
def my_function(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_function(**my_dict)  # Unpacks the dictionary into keyword arguments
```
**Output:**
```
Alice is 30 years old and lives in New York.
```

---

### 3. **Combining `*args` and `**kwargs`**

You can use both `*args` and `**kwargs` in the same function to handle a mix of positional and keyword arguments.

#### Example:
```python
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, name="Alice", age=30)
```
**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
```

---

### 4. **Order of Arguments**

When defining a function, the order of arguments must follow this sequence:
1. Regular positional arguments
2. `*args`
3. Keyword-only arguments (if any)
4. `**kwargs`

#### Example:
```python
def my_function(a, b, *args, c=10, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)

my_function(1, 2, 3, 4, c=20, name="Alice", age=30)
```
**Output:**
```
a: 1
b: 2
args: (3, 4)
c: 20
kwargs: {'name': 'Alice', 'age': 30}
```

---

### 5. **Practical Use Cases**

#### a) **Mathematical Operations**
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

#### b) **Function Wrapping**
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))  # Output: Calling add with args: (3, 5), kwargs: {}
```

#### c) **Dynamic Function Arguments**
```python
def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

print(create_profile(name="Alice", age=30, city="New York"))
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

---

### 6. **Best Practices**

1. Use `*args` and `**kwargs` when the number of arguments is unknown or can vary.
2. Avoid overusing them, as they can make the function signature less clear.
3. Always document the expected arguments when using `*args` and `**kwargs`.

---

By mastering `*args` and `**kwargs`, you can write more flexible and reusable functions in Python! Let me know if you have further questions. 🚀


# **Python Variable-Length Arguments – From Basic to Advanced** 🚀

In Python, **variable-length arguments** allow functions to accept an arbitrary number of arguments. There are **two types**:
1. **`*args` (Non-keyword arguments)** – Allows passing multiple positional arguments.
2. **`**kwargs` (Keyword arguments)** – Allows passing multiple keyword arguments.

---

## **🔹 1️⃣ `*args` – Variable-Length Positional Arguments**
- `*args` collects **multiple arguments into a tuple**.
- It allows a function to accept an **arbitrary number** of positional arguments.

### **🔸 1.1 Basic Example**
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3, 5))  # Output: 10
print(add_numbers(1, 2, 3, 4, 5, 6))  # Output: 21
```
📌 Here, `args` is a **tuple** containing all the values passed to the function.

### **🔸 1.2 Looping Through `*args`**
```python
def print_names(*args):
    for name in args:
        print(name)

print_names("Alice", "Bob", "Charlie")
```
**Output:**
```
Alice
Bob
Charlie
```

### **🔸 1.3 Using `*args` with Other Parameters**
- You can mix `*args` with **regular parameters**.
- Regular parameters must come **before** `*args`.

```python
def greet(message, *names):
    for name in names:
        print(f"{message}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
```
**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### **🔸 1.4 Unpacking Arguments**
- You can pass a **list or tuple** to a function using `*`.

```python
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

numbers = [2, 3, 4]
print(multiply(*numbers))  # Output: 24
```
📌 The `*numbers` **unpacks** the list into separate arguments.

---

## **🔹 2️⃣ `**kwargs` – Variable-Length Keyword Arguments**
- `**kwargs` collects **multiple keyword arguments into a dictionary**.
- This is useful when you don't know how many named arguments will be passed.

### **🔸 2.1 Basic Example**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```
**Output:**
```
name: Alice
age: 25
city: New York
```
📌 Here, `kwargs` is a **dictionary** containing all the named arguments.

### **🔸 2.2 Using `**kwargs` with Other Parameters**
- Regular parameters must come **before** `**kwargs`.

```python
def profile(name, **details):
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")

profile("Alice", age=25, city="New York", job="Engineer")
```
**Output:**
```
Name: Alice
age: 25
city: New York
job: Engineer
```

### **🔸 2.3 Unpacking `**kwargs`**
- You can pass a **dictionary** using `**`.

```python
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person = {"name": "Alice", "age": 25, "city": "New York"}
display_info(**person)
```
📌 The `**person` **unpacks** the dictionary into keyword arguments.

---

## **🔹 3️⃣ Combining `*args` and `**kwargs`**
- You can use **both `*args` and `**kwargs`** in the same function.

```python
def full_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

full_info("Alice", "Bob", age=25, city="New York")
```
**Output:**
```
Positional arguments: ('Alice', 'Bob')
Keyword arguments: {'age': 25, 'city': 'New York'}
```

📌 Order of parameters when using `*args` and `**kwargs`:
1. Regular parameters
2. `*args`
3. `**kwargs`

```python
def demo(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")

demo(1, 2, 3, 4, 5, c=20, x=100, y=200)
```
**Output:**
```
a: 1, b: 2, args: (3, 4, 5), c: 20, kwargs: {'x': 100, 'y': 200}
```

---

## **🔹 4️⃣ Advanced Uses of `*args` and `**kwargs`**
### **🔸 4.1 Passing `*args` and `**kwargs` to Another Function**
```python
def func1(*args, **kwargs):
    print("Func1:", args, kwargs)

def func2(*args, **kwargs):
    func1(*args, **kwargs)

func2(1, 2, 3, name="Alice", age=25)
```
📌 `func2` forwards the arguments to `func1`.

---

### **🔸 4.2 Using `*args` and `**kwargs` in Class Methods**
```python
class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.details = kwargs  # Store extra info as a dictionary

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Details: {self.details}")

p = Person("Alice", 25, city="New York", job="Engineer")
p.show_info()
```
**Output:**
```
Name: Alice, Age: 25, Details: {'city': 'New York', 'job': 'Engineer'}
```

---

## **🔹 5️⃣ Summary – When to Use `*args` and `**kwargs`**
| Scenario | Use |
|----------|-----|
| When function arguments are **unknown** | Use `*args` |
| When function arguments include **named values** | Use `**kwargs` |
| When you need to **forward arguments** to another function | Use `*args` and `**kwargs` together |
| When working with **OOP (classes, methods)** | Use `**kwargs` for additional attributes |

🚀 **`*args` and `**kwargs` make Python functions more flexible, reusable, and scalable!**


# **Python Variable-Length Arguments (`*args` and `**kwargs`) – From Basic to Advanced**

In Python, **variable-length arguments** allow functions to accept an arbitrary number of arguments. This is useful when you don't know in advance how many arguments will be passed to a function.

---

## **1. Understanding `*args` (Non-Keyword Arguments)**

- `*args` allows a function to accept **any number of positional arguments**.
- Inside the function, `args` is **treated as a tuple**.

### **Basic Example**
```python
def add_numbers(*args):
    total = sum(args)
    print(f"Sum: {total}")

add_numbers(1, 2, 3)  # Output: Sum: 6
add_numbers(5, 10, 15, 20)  # Output: Sum: 50
```
- The function `add_numbers()` can accept **any number of arguments**.
- The arguments are packed into a **tuple** named `args`.

### **Example: Iterating Over `*args`**
```python
def display_elements(*args):
    for item in args:
        print(item)

display_elements("Apple", "Banana", "Cherry")
```
**Output:**
```
Apple
Banana
Cherry
```

---

## **2. Understanding `**kwargs` (Keyword Arguments)**

- `**kwargs` allows a function to accept **any number of keyword arguments**.
- Inside the function, `kwargs` is treated as a **dictionary**.

### **Basic Example**
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
```
**Output:**
```
name: Alice
age: 25
city: New York
```
- The function can accept **any number of keyword arguments**.
- The arguments are packed into a **dictionary** named `kwargs`.

---

## **3. Using `*args` and `**kwargs` Together**
- `*args` must come **before** `**kwargs` in the function definition.
- This allows the function to accept both positional and keyword arguments.

### **Example**
```python
def employee_details(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

employee_details("John", "Developer", age=30, department="IT")
```
**Output:**
```
Positional arguments (args): ('John', 'Developer')
Keyword arguments (kwargs): {'age': 30, 'department': 'IT'}
```

---

## **4. Using `*args` to Pass Arguments to Another Function**
You can use `*args` to pass arguments from one function to another.

### **Example**
```python
def multiply(a, b):
    return a * b

def calculate(*args):
    result = multiply(*args)  # Unpacking args into multiply()
    print("Result:", result)

calculate(3, 4)  # Output: Result: 12
```
- The `calculate()` function takes **any number of arguments**.
- It passes them to `multiply()` using `*args`.

---

## **5. Using `**kwargs` to Pass Dictionary Arguments**
You can use `**kwargs` to pass dictionary values into a function.

### **Example**
```python
def print_person(name, age):
    print(f"Name: {name}, Age: {age}")

person_dict = {"name": "Emma", "age": 28}
print_person(**person_dict)  # Unpacking dictionary into function
```
**Output:**
```
Name: Emma, Age: 28
```
- The `**person_dict` syntax **unpacks dictionary values** into function arguments.

---

## **6. Mixing Positional, `*args`, Default, and `**kwargs`**
You can combine different types of function arguments:
```python
def mixed_args(pos1, pos2, *args, kw1="default", kw2="default", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Additional Positional (*args): {args}")
    print(f"Default keyword arguments: kw1={kw1}, kw2={kw2}")
    print(f"Additional Keyword Arguments (**kwargs): {kwargs}")

mixed_args("A", "B", "C", "D", kw1="X", key1="Value1", key2="Value2")
```
**Output:**
```
Positional: A, B
Additional Positional (*args): ('C', 'D')
Default keyword arguments: kw1=X, kw2=default
Additional Keyword Arguments (**kwargs): {'key1': 'Value1', 'key2': 'Value2'}
```
### **Order of Arguments**
The correct order for function parameters is:
1. **Regular Positional Arguments**
2. **`*args` (Variable Positional Arguments)**
3. **Default Parameters**
4. **`**kwargs` (Variable Keyword Arguments)**

---

## **7. Unpacking Arguments Using `*args` and `**kwargs`**
- You can **unpack lists and dictionaries** when calling functions.

### **Example: Unpacking a List with `*args`**
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = ["Alice", 30]
greet(*person_info)  # Unpacking list
```
**Output:**
```
Hello Alice, you are 30 years old.
```

### **Example: Unpacking a Dictionary with `**kwargs`**
```python
person_info = {"name": "Bob", "age": 40}
greet(**person_info)  # Unpacking dictionary
```
**Output:**
```
Hello Bob, you are 40 years old.
```

---

## **8. Using `*args` and `**kwargs` in Class Methods**
### **Example**
```python
class Employee:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.extra_info = kwargs  # Store extra info in a dictionary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        for key, value in self.extra_info.items():
            print(f"{key}: {value}")

emp = Employee("John", 30, department="HR", salary=5000)
emp.display()
```
**Output:**
```
Name: John, Age: 30
department: HR
salary: 5000
```
- Any additional information is stored in the `extra_info` dictionary.

---

## **9. Advanced Use Case: Passing `*args` and `**kwargs` to Parent Class**
```python
class Parent:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)  # Passing kwargs to the next class

class Child(Parent):
    def __init__(self, name, age, **kwargs):
        self.age = age
        super().__init__(name, **kwargs)

child = Child("Emma", 10, school="XYZ School", grade="5th")
print(child.__dict__)  # {'age': 10, 'name': 'Emma', 'school': 'XYZ School', 'grade': '5th'}
```
- This method allows passing arguments through multiple **inheritance levels**.

---

## **Conclusion**
- **`*args`** is used for **variable-length positional arguments** (stored as a **tuple**).
- **`**kwargs`** is used for **variable-length keyword arguments** (stored as a **dictionary**).
- You can use `*args` and `**kwargs` **together**.
- They are useful in **flexible function definitions**, **class inheritance**, and **dynamic argument passing**.

In Python, **variable-length arguments** allow you to pass a variable number of arguments to a function. This is useful when you don't know how many arguments will be passed to the function in advance. Python provides two ways to handle variable-length arguments:

1. **`*args`**: For passing a variable number of **non-keyword (positional) arguments**.
2. **`**kwargs`**: For passing a variable number of **keyword arguments**.

Let's explore both concepts in detail, from basic to advanced usage.

---

## 1. **`*args` (Variable-Length Non-Keyword Arguments)**

### Basic Usage
- `*args` allows you to pass a variable number of **positional arguments** to a function.
- Inside the function, `args` is treated as a **tuple**.

#### Example:
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))          # Output: 6
print(sum_numbers(10, 20, 30, 40))   # Output: 100
```

- Here, `*args` collects all the positional arguments into a tuple.

---

### Combining `*args` with Regular Arguments
You can combine `*args` with regular arguments. However, `*args` must come after the regular arguments.

#### Example:
```python
def greet(name, *args):
    print(f"Hello, {name}!")
    print("Additional arguments:", args)

greet("Alice")                        # Output: Hello, Alice! Additional arguments: ()
greet("Bob", "How are you?", 123)     # Output: Hello, Bob! Additional arguments: ('How are you?', 123)
```

---

### Unpacking with `*args`
You can use `*args` to unpack a list or tuple when calling a function.

#### Example:
```python
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
print(multiply(*numbers))  # Output: 24 (equivalent to multiply(2, 3, 4))
```

---

### Advanced: Using `*args` with Default Arguments
You can combine `*args` with default arguments.

#### Example:
```python
def func(a, b=10, *args):
    print(f"a: {a}, b: {b}, args: {args}")

func(1)                  # Output: a: 1, b: 10, args: ()
func(1, 2, 3, 4)         # Output: a: 1, b: 2, args: (3, 4)
```

---

## 2. **`**kwargs` (Variable-Length Keyword Arguments)**

### Basic Usage
- `**kwargs` allows you to pass a variable number of **keyword arguments** to a function.
- Inside the function, `kwargs` is treated as a **dictionary**.

#### Example:
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

---

### Combining `**kwargs` with Regular Arguments
You can combine `**kwargs` with regular arguments and `*args`. The order must be:
1. Regular arguments
2. `*args`
3. `**kwargs`

#### Example:
```python
def func(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, kwargs: {kwargs}")

func(1, 2, 3, 4, name="Alice", age=30)
# Output:
# a: 1, b: 2, args: (3, 4), kwargs: {'name': 'Alice', 'age': 30}
```

---

### Unpacking with `**kwargs`
You can use `**kwargs` to unpack a dictionary when calling a function.

#### Example:
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

info = {"name": "Alice", "age": 30}
greet(**info)  # Output: Hello, Alice! You are 30 years old.
```

---

### Advanced: Using `**kwargs` with Default Arguments
You can combine `**kwargs` with default arguments.

#### Example:
```python
def func(a, b=10, **kwargs):
    print(f"a: {a}, b: {b}, kwargs: {kwargs}")

func(1)                  # Output: a: 1, b: 10, kwargs: {}
func(1, 2, name="Alice") # Output: a: 1, b: 2, kwargs: {'name': 'Alice'}
```

---

## 3. **Combining `*args` and `**kwargs`**

You can use both `*args` and `**kwargs` in the same function to handle a variable number of positional and keyword arguments.

#### Example:
```python
def func(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")

func(1, 2, 3, name="Alice", age=30)
# Output:
# args: (1, 2, 3), kwargs: {'name': 'Alice', 'age': 30}
```

---

## 4. **Practical Use Cases**

### Use Case 1: Flexible Function for Calculations
```python
def calculate(*args, operation="sum"):
    if operation == "sum":
        return sum(args)
    elif operation == "product":
        result = 1
        for num in args:
            result *= num
        return result

print(calculate(1, 2, 3, operation="sum"))      # Output: 6
print(calculate(2, 3, 4, operation="product"))  # Output: 24
```

---

### Use Case 2: Wrapper Functions
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)  # Output: Calling add with args: (3, 5), kwargs: {}
           #         add returned: 8
```

---

### Use Case 3: Configuring Objects
```python
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make", "Unknown")
        self.model = kwargs.get("model", "Unknown")
        self.year = kwargs.get("year", 2023)

car = Car(make="Toyota", model="Corolla")
print(car.make)   # Output: Toyota
print(car.model)  # Output: Corolla
print(car.year)   # Output: 2023
```

---

## 5. **Key Points to Remember**




1. **Order of Arguments**:
   - Regular arguments → `*args` → `**kwargs`.
   - Example: `def func(a, b, *args, **kwargs)`.

2. **`*args`**:
   - Collects extra positional arguments into a **tuple**.

3. **`**kwargs`**:
   - Collects extra keyword arguments into a **dictionary**.

4. **Unpacking**:
   - Use `*` to unpack a list/tuple for `*args`.
   - Use `**` to unpack a dictionary for `**kwargs`.

5. **Flexibility**:
   - `*args` and `**kwargs` make functions highly flexible and reusable.

---

By mastering `*args` and `**kwargs`, you can write more dynamic and flexible Python functions that can handle a wide range of use cases!


In Python, **variable-length arguments** allow you to pass a variable number of arguments to a function. This is useful when you don't know beforehand how many arguments will be passed to the function. There are two main types of variable-length arguments in Python:

1. **Arbitrary Positional Arguments (`*args`)**
2. **Arbitrary Keyword Arguments (`**kwargs`)**

Let’s explore these concepts from basic to advanced.

---

## 1. **Arbitrary Positional Arguments (`*args`)**

### **What is `*args`?**
- The `*args` syntax is used to pass a variable number of positional arguments to a function.
- Inside the function, `args` will be a tuple that contains all the arguments passed to the function.

### **Basic Example**:

```python
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

In this example:
- The function `greet` accepts any number of positional arguments using `*names`.
- The argument `names` inside the function is a tuple containing all the passed arguments.

### **Using `*args` in Functions with Regular Arguments**:

```python
def multiply(factor, *numbers):
    result = factor
    for number in numbers:
        result *= number
    return result

print(multiply(2, 3, 4, 5))  # Output: 120
```

Here:
- `factor` is a regular argument.
- `*numbers` accepts a variable number of additional positional arguments.
- The function multiplies the `factor` by each number in `numbers`.

---

## 2. **Arbitrary Keyword Arguments (`**kwargs`)**

### **What is `**kwargs`?**
- The `**kwargs` syntax is used to pass a variable number of keyword arguments to a function.
- Inside the function, `kwargs` will be a dictionary where the keys are the argument names and the values are the corresponding argument values.

### **Basic Example**:

```python
def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, profession="Engineer")
# Output:
# name: Alice
# age: 25
# profession: Engineer
```

In this example:
- The function `print_details` accepts any number of keyword arguments using `**details`.
- `details` inside the function is a dictionary containing the key-value pairs of the passed arguments.

### **Using `**kwargs` with Regular Arguments**:

```python
def create_profile(name, age, **extra_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in extra_info.items():
        print(f"{key}: {value}")

create_profile("Alice", 25, profession="Engineer", country="USA")
# Output:
# Name: Alice
# Age: 25
# profession: Engineer
# country: USA
```

Here:
- `name` and `age` are regular arguments.
- `**extra_info` accepts additional keyword arguments.
- The function prints out the basic details and any extra information passed as keyword arguments.

---

## 3. **Combining `*args` and `**kwargs`**

You can combine both `*args` and `**kwargs` in a single function. However, **`*args`** must always come before **`**kwargs`**.

### **Example:**

```python
def mixed_example(arg1, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

mixed_example(1, 2, 3, 4, kwarg1="specified", extra1="value1", extra2="value2")
# Output:
# arg1: 1
# args: (2, 3, 4)
# kwarg1: specified
# kwargs: {'extra1': 'value1', 'extra2': 'value2'}
```

In this case:
- `arg1` is a regular argument.
- `*args` collects the additional positional arguments (2, 3, 4).
- `kwarg1` is a keyword argument with a default value ("specified" overrides the default).
- `**kwargs` collects the remaining keyword arguments into a dictionary.

---

## 4. **Use Cases and Best Practices**

### **Use Case 1: Handling Dynamic Number of Arguments**

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))        # Output: 6
print(sum_numbers(10, 20, 30, 40)) # Output: 100
```
- This function can sum any number of arguments, making it versatile for different cases.

### **Use Case 2: Flexible Function Signature**

```python
def configure_settings(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

configure_settings(volume=80, brightness=50, contrast=70)
# Output:
# volume: 80
# brightness: 50
# contrast: 70
```
- This allows the user to configure various settings dynamically without having to define all possible settings explicitly.

### **Use Case 3: Overriding Default Behavior with `**kwargs`**

```python
def greet(message="Hello", **kwargs):
    name = kwargs.get('name', 'Guest')
    print(f"{message}, {name}!")

greet(name="Alice")            # Output: Hello, Alice!
greet(message="Goodbye")       # Output: Goodbye, Guest!
greet(message="Hi", name="Bob") # Output: Hi, Bob!
```
- Here, you can override the `message` parameter and pass additional keyword arguments dynamically.

---

## 5. **Advanced Topics**

### **Unpacking Arguments with `*` and `**`**

- You can **unpack** arguments into functions using `*` and `**` syntax when calling functions.

#### **Unpacking Positional Arguments:**

```python
def add(a, b, c):
    return a + b + c

args = (1, 2, 3)
print(add(*args))  # Output: 6
```

- The `*args` syntax is used to unpack a tuple into positional arguments.

#### **Unpacking Keyword Arguments:**

```python
def display(name, age):
    print(f"Name: {name}, Age: {age}")

kwargs = {"name": "Alice", "age": 25}
display(**kwargs)  # Output: Name: Alice, Age: 25
```

- The `**kwargs` syntax is used to unpack a dictionary into keyword arguments.

### **Variable-Length Arguments in Lambda Functions**

You can also use `*args` and `**kwargs` in **lambda functions**.

#### Example with `*args` in Lambda:

```python
sum_numbers = lambda *args: sum(args)
print(sum_numbers(1, 2, 3, 4))  # Output: 10
```

#### Example with `**kwargs` in Lambda:

```python
greet = lambda **kwargs: f"Hello, {kwargs.get('name', 'Guest')}!"
print(greet(name="Alice"))  # Output: Hello, Alice!
print(greet())  # Output: Hello, Guest!
```

### **Using `*args` and `**kwargs` in Inheritance**

In class methods, `*args` and `**kwargs` can be passed when calling parent class methods.

```python
class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_values(self):
        print(f"a: {self.a}, b: {self.b}")

class Derived(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)  # Call the parent class constructor
        self.c = c

    def print_all(self):
        super().print_values()  # Call the parent class method
        print(f"c: {self.c}")

obj = Derived(1, 2, 3)
obj.print_all()
# Output:
# a: 1, b: 2
# c: 3
```

---

## 6. **Summary of `*args` and `**kwargs`**

- **`*args`**: Allows you to pass a variable number of positional arguments to a function. Inside the function, these arguments are accessible as a tuple.
- **`**kwargs`**: Allows you to pass a variable number of keyword arguments to a function. Inside the function, these arguments are accessible as a dictionary.
- Both `*args` and `**kwargs` provide flexibility in function signatures, enabling you to create functions that can handle an arbitrary number of arguments.

---

## Conclusion

Python’s variable-length arguments (`*args` and `**kwargs`) are powerful tools that allow you to write more flexible and dynamic functions. Whether dealing with an unknown number of arguments or varying keyword arguments, these techniques help create more adaptable and reusable code.

By understanding how to use these arguments in combination, unpack them, and apply them in different scenarios like inheritance and lambda functions, you can significantly improve the flexibility of your Python code.


In Python, **variable-length arguments** allow you to pass a variable number of arguments to a function. This is useful when you don't know in advance how many arguments will be passed. Python provides two ways to handle variable-length arguments:

1. **`*args`**: For passing a variable number of **non-keyword arguments**.
2. **`**kwargs`**: For passing a variable number of **keyword arguments**.

This guide will cover everything about variable-length arguments, from **basic** to **advanced** usage.

---

## **1. Basics of Variable-Length Arguments**

### **1.1 `*args` (Non-Keyword Arguments)**
- `*args` allows you to pass a variable number of non-keyword arguments to a function.
- The arguments are collected into a **tuple**.

#### Syntax:
```python
def function_name(*args):
    # Function body
```

#### Example:
```python
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3))          # Output: 6
print(add(1, 2, 3, 4, 5))    # Output: 15
```

---

### **1.2 `**kwargs` (Keyword Arguments)**
- `**kwargs` allows you to pass a variable number of keyword arguments to a function.
- The arguments are collected into a **dictionary**.

#### Syntax:
```python
def function_name(**kwargs):
    # Function body
```

#### Example:
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

---

### **1.3 Combining `*args` and `**kwargs`**
You can use both `*args` and `**kwargs` in the same function.

#### Example:
```python
def func(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

---

## **2. Intermediate Concepts**

### **2.1 Unpacking Arguments**
You can use `*` and `**` to unpack arguments when calling a function.

#### Example:
```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Output: 6

info = {'a': 1, 'b': 2, 'c': 3}
print(add(**info))    # Output: 6
```

---

### **2.2 Default Arguments with `*args` and `**kwargs`**
You can combine default arguments with `*args` and `**kwargs`.

#### Example:
```python
def func(a, b=2, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

func(1, 3, 4, 5, name="Alice", age=25)
# Output:
# a: 1
# b: 3
# args: (4, 5)
# kwargs: {'name': 'Alice', 'age': 25}
```

---

### **2.3 Using `*args` and `**kwargs` in Class Methods**
You can use `*args` and `**kwargs` in class methods.

#### Example:
```python
class MyClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def display(self):
        print("Positional arguments:", self.args)
        print("Keyword arguments:", self.kwargs)

obj = MyClass(1, 2, 3, name="Alice", age=25)
obj.display()
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

---

## **3. Advanced Concepts**

### **3.1 Decorators with `*args` and `**kwargs`**
You can use `*args` and `**kwargs` in decorators to make them work with any function.

#### Example:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Before function call
# Hello, Alice!
# After function call
```

---

### **3.2 Using `*args` and `**kwargs` with Inheritance**
You can use `*args` and `**kwargs` to pass arguments to parent class constructors.

#### Example:
```python
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

child = Child(name="Alice", age=25)
print(child.name)  # Output: Alice
print(child.age)   # Output: 25
```

---

### **3.3 Using `*args` and `**kwargs` with `functools.partial`**
You can use `*args` and `**kwargs` with `functools.partial` to create partial functions.

#### Example:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # Output: 25
```

---

## **4. Best Practices**
1. Use `*args` for variable-length positional arguments.
2. Use `**kwargs` for variable-length keyword arguments.
3. Combine `*args` and `**kwargs` when you need both.
4. Use unpacking (`*` and `**`) to pass arguments dynamically.
5. Document your functions clearly when using `*args` and `**kwargs`.

---

By mastering variable-length arguments, you can write more flexible and reusable functions in Python!