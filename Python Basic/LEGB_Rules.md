The **LEGB Rule** is an essential concept in Python that defines the order in which Python looks for a variable when you reference it in your code. It stands for:

- **L**: Local
- **E**: Enclosing
- **G**: Global
- **B**: Built-in

### Overview of LEGB Rule:

When Python encounters a variable in your code, it searches for it in the following order:

1. **Local (L)**: The innermost scope, which includes variables that are locally defined in the current function or method.
2. **Enclosing (E)**: The next outer scope, where Python looks for variables in enclosing functions (e.g., functions that are nested).
3. **Global (G)**: The global scope, which includes variables defined at the top level of the module or script.
4. **Built-in (B)**: The outermost scope, where Python looks for variables that are built-in to the Python language, such as `print()`, `len()`, `sum()`, etc.

If Python does not find the variable in one scope, it moves on to the next one in the LEGB order until it either finds the variable or raises an error (if the variable is not found at all).

### Detailed Breakdown:

#### 1. **Local (L)**

- The **local scope** refers to the variables defined within the current function or method.
- Python first looks for the variable in the **local scope** (the innermost scope). This includes parameters, variables declared in the function, and variables within loops or comprehensions inside that function.

#### Example of Local Scope:

```python
def my_function():
    x = 10  # Local variable
    print(x)  # This will use the local 'x'

my_function()  # Output: 10
```

Here, `x` is defined inside `my_function`, and Python will first look for `x` in the local scope of the function.

#### 2. **Enclosing (E)**

- If the variable is not found in the local scope, Python checks the **enclosing scope**. This is the scope of any functions that enclose the current function.
- The **enclosing scope** applies in nested functions, where the outer function defines a variable that can be accessed by inner functions.

#### Example of Enclosing Scope:

```python
def outer():
    x = 20  # Variable in the enclosing function

    def inner():
        print(x)  # This will use 'x' from the enclosing scope

    inner()

outer()  # Output: 20
```

Here, `inner()` does not have its own `x`, so Python looks to the enclosing `outer()` function to find it.

#### 3. **Global (G)**

- If the variable is not found in the local or enclosing scopes, Python checks the **global scope**. This refers to variables that are defined outside of any function or method, typically at the top level of your script or module.

#### Example of Global Scope:

```python
x = 30  # Global variable

def my_function():
    print(x)  # This will use the global 'x'

my_function()  # Output: 30
```

Here, Python finds the variable `x` in the global scope, since it is not defined locally in the function.

#### 4. **Built-in (B)**

- If Python still hasn’t found the variable, it will look in the **built-in scope**, which contains the built-in names that are always available in Python, such as functions like `print()`, `len()`, `abs()`, and more.

#### Example of Built-in Scope:

```python
def my_function():
    x = len([1, 2, 3])  # Using the built-in function 'len'
    print(x)

my_function()  # Output: 3
```

Here, `len` is a built-in function, so Python will refer to the built-in scope to resolve it.

---

### LEGB Rule in Action with Examples:

#### Example 1: Simple Variable Lookup

```python
x = 50  # Global variable

def outer():
    x = 100  # Enclosing variable

    def inner():
        x = 200  # Local variable
        print(x)  # Prints local 'x'

    inner()
    print(x)  # Prints enclosing 'x'

outer()
print(x)  # Prints global 'x'
```

**Output**:

```
200  # From the local scope of 'inner'
100  # From the enclosing scope of 'outer'
50   # From the global scope
```

- In `inner()`, Python finds the **local** `x = 200`, so it prints `200`.
- In `outer()`, after `inner()` finishes, Python finds the **enclosing** `x = 100` and prints it.
- Outside `outer()`, Python finds the **global** `x = 50` and prints it.

#### Example 2: Nested Functions and Enclosing Variables

```python
def outer():
    x = 10  # Enclosing variable

    def inner():
        print(x)  # Refers to the enclosing 'x'

    inner()

outer()  # Output: 10
```

Here:

- The variable `x` is found in the enclosing scope of `outer()` when `inner()` tries to access it.

#### Example 3: Global and Built-in Variable Lookup

```python
x = 5  # Global variable

def func():
    print(x)  # This will refer to the global 'x'
    print(len)  # This will refer to the built-in function 'len'

func()
```

**Output**:

```
5   # From the global scope
<built-in function len>  # Refers to the built-in 'len' function
```

Here:

- The `x` is found in the **global** scope.
- The `len` function is found in the **built-in** scope.

---

### Key Points to Remember:

1. **Order of Lookup**: Python looks for variables in the following order:
   - Local
   - Enclosing
   - Global
   - Built-in
2. **Local Variables**: Always searched first and found in the innermost scope.
3. **Enclosing Variables**: Searched next, in functions that enclose the current function.
4. **Global Variables**: Searched after enclosing, for variables defined at the top level.
5. **Built-in Variables**: The last resort, where built-in functions and objects are found.

### Special Cases:

- **Variable Shadowing**: Local variables can **shadow** variables in enclosing, global, or built-in scopes. This means that a variable with the same name in a local scope will be used over the variable in an enclosing, global, or built-in scope.

  Example of shadowing:

  ```python
  x = 10  # Global x

  def func():
      x = 20  # Local x, shadows global x
      print(x)  # Prints local x

  func()
  print(x)  # Prints global x
  ```

  **Output**:

  ```
  20  # From the local scope
  10  # From the global scope
  ```

- **`global` Keyword**: If you want to modify a global variable inside a function, you need to use the `global` keyword to tell Python that you want to use the global variable instead of creating a new local variable.

  Example with `global`:

  ```python
  x = 5  # Global variable

  def modify():
      global x  # Refers to global 'x'
      x = 10  # Modify the global x

  modify()
  print(x)  # Output: 10
  ```

- **`nonlocal` Keyword**: When dealing with nested functions, the `nonlocal` keyword allows you to modify a variable in an enclosing (non-global) scope.

  Example with `nonlocal`:

  ```python
  def outer():
      x = 5  # Enclosing variable

      def inner():
          nonlocal x  # Refers to 'x' in the enclosing scope (outer)
          x = 10  # Modify the enclosing 'x'

      inner()
      print(x)  # Output: 10

  outer()
  ```

---

### Conclusion

The **LEGB Rule** provides a structured way to understand how Python resolves variable references in different scopes. By understanding the LEGB rule, you can predict how variables are looked up and avoid confusion when working with nested functions, global variables, and built-in functions. This rule helps in avoiding conflicts and allows for cleaner, more efficient code by managing scope effectively.
The **LEGB Rule** in Python governs how the interpreter looks up variables and resolves names. It stands for:

- **L**: **Local** – The innermost scope, such as variables defined within a function or method.
- **E**: **Enclosing** – The scope of any enclosing function (when a function is nested inside another).
- **G**: **Global** – The module-level scope, or the scope of variables defined at the top-level of a script or module.
- **B**: **Built-in** – The outermost scope, which includes Python's built-in functions and objects.

Understanding this rule is critical for effective variable management in Python, especially when working with nested functions, modules, and closures. The Python interpreter follows the LEGB order to search for variables when they are accessed. Below is a deep dive into each part of the LEGB rule, with explanations, nuances, and examples.

---

### 1. **Local Scope (L)**

- **Local** scope refers to the **innermost** namespace, which consists of the current function's arguments and any variables that are defined within that function.
- The local scope only exists while the function is executing. Once the function call ends, its local scope and variables are discarded.

#### Characteristics:

- Variables defined inside a function (including arguments) belong to the local scope.
- Python looks for the variable first in the **local** scope before moving on to any outer scopes.

#### Example:

```python
def add_numbers(a, b):
    result = a + b  # Local variable 'result'
    return result

print(add_numbers(3, 4))  # Output: 7
```

Here, `a`, `b`, and `result` are local to the `add_numbers()` function. Python looks for `result` in the local scope and returns it.

#### Limitations:

- Local variables are destroyed once the function finishes executing.
- If a variable is redefined inside the function, it will **shadow** the variable in the enclosing or global scope.

---

### 2. **Enclosing Scope (E)**

- **Enclosing** scope refers to the scope of any **outer functions** that enclose the current function. In other words, when a function is nested inside another function, the outer function's variables are part of the enclosing scope for the inner function.
- Enclosing scopes are not the same as the global scope. They are only accessible to the inner function.

#### Characteristics:

- Python first checks the local scope (innermost), and if it doesn’t find the variable there, it checks the enclosing scope.
- The enclosing scope is only applicable to **nested functions**, where a function is defined inside another function.

#### Example:

```python
def outer():
    x = 5  # Enclosing variable

    def inner():
        print(x)  # Uses variable from the enclosing scope (outer)

    inner()

outer()  # Output: 5
```

Here, `x` is defined in `outer()`, and when `inner()` accesses `x`, it uses the **enclosing scope** of `outer()`.

#### Key Points:

- If there are multiple enclosing functions, Python looks for the variable in the outermost enclosing function’s scope.
- Enclosing scopes can be modified with the `nonlocal` keyword.

---

### 3. **Global Scope (G)**

- **Global** scope refers to the scope at the **top-level** of a Python script or module. Any variable declared outside of a function, class, or other function definitions will reside in the global scope.
- Python checks the **global** scope after checking the local and enclosing scopes.

#### Characteristics:

- Variables defined at the top level of the script or module are global.
- Global variables are accessible to all functions and methods unless they are shadowed by a variable in a local or enclosing scope.
- To modify a global variable inside a function, you must use the `global` keyword.

#### Example:

```python
x = 10  # Global variable

def print_global():
    print(x)  # Accesses the global 'x'

print_global()  # Output: 10
```

Here, `x` is defined at the global level and accessed by the function `print_global()`.

#### Modifying Global Variables:

If you want to modify a global variable inside a function, use the `global` keyword.

```python
x = 10  # Global variable

def modify_global():
    global x  # Tells Python to use the global variable 'x'
    x = 20  # Modify the global 'x'

modify_global()
print(x)  # Output: 20
```

Without `global`, Python would create a new **local** variable `x` inside the function, leaving the global variable unchanged.

---

### 4. **Built-in Scope (B)**

- **Built-in** scope refers to the scope where Python stores all the built-in functions and objects that are available by default, such as `print()`, `len()`, `max()`, `abs()`, and so on.
- This scope is always available and Python checks this scope last when looking for a variable.

#### Characteristics:

- Built-in variables and functions (like `sum`, `str`, `int`) are always available.
- These functions are part of Python's built-in namespace and are accessible from anywhere in the Python environment.

#### Example:

```python
print(len([1, 2, 3]))  # Output: 3 (Built-in function 'len')
```

If a variable name conflicts with a built-in name, Python will refer to the most specific scope (i.e., Local > Enclosing > Global) and will not use the built-in version unless explicitly called.

---

### LEGB Rule in Action: Combining Scopes

Let's break down an example where Python looks for a variable across multiple scopes:

```python
x = 5  # Global variable

def outer():
    x = 10  # Enclosing variable

    def inner():
        x = 20  # Local variable
        print(x)  # Prints local 'x'

    inner()
    print(x)  # Prints enclosing 'x'

outer()
print(x)  # Prints global 'x'
```

**Output**:

```
20  # From the local scope of 'inner'
10  # From the enclosing scope of 'outer'
5   # From the global scope
```

Here's the flow:

1. **`inner()`** looks for `x` and finds the **local variable** `x = 20`, so it prints `20`.
2. After `inner()` finishes, **`outer()`** looks for `x` and finds the **enclosing variable** `x = 10`, so it prints `10`.
3. Finally, outside the functions, Python looks for `x` and finds the **global variable** `x = 5`, so it prints `5`.

---

### Special Cases in LEGB:

#### 1. **Shadowing and Overriding Variables**

- If a variable in a local scope has the same name as a variable in an enclosing or global scope, it will **shadow** that variable.

  Example of shadowing:

  ```python
  x = 30  # Global variable

  def func():
      x = 20  # Local variable shadows global variable
      print(x)  # Prints local 'x'

  func()  # Output: 20
  print(x)  # Output: 30 (Global variable is not changed)
  ```

In this case, `x` inside `func()` shadows the global `x`. The local `x` is used when printing within the function.

#### 2. **`nonlocal` Keyword in Enclosing Scopes**

- The `nonlocal` keyword allows you to modify a variable in an enclosing scope (but not the global scope). This is useful in nested functions, where you want the inner function to modify a variable in an outer function.

  Example of `nonlocal`:

  ```python
  def outer():
      x = 5  # Enclosing variable

      def inner():
          nonlocal x  # Refers to 'x' in the enclosing scope
          x = 10  # Modify the enclosing 'x'

      inner()
      print(x)  # Output: 10

  outer()
  ```

Here, the `nonlocal` keyword allows `inner()` to modify the `x` in `outer()`'s scope.

#### 3. **`global` Keyword for Global Variables**

- The `global` keyword is used when you want to modify a variable in the **global scope** from within a function. This avoids creating a new local variable and changes the global one.

  Example with `global`:

  ```python
  x = 10  # Global variable

  def modify_global():
      global x  # Tells Python to use the global variable 'x'
      x = 20  # Modify the global 'x'

  modify_global()
  print(x)  # Output: 20
  ```

Here, the `global` keyword allows `modify_global()` to modify the global variable `x`.

---

### Advanced Considerations:

- **Dynamic Scope Resolution**: Python’s scope resolution is **static** and follows the LEGB rule at the time of code execution, not dynamically as the program runs.
- **Function Objects and Closures**: In a closure, Python remembers the enclosing scope even after the outer function finishes executing, allowing inner functions to access variables from their enclosing scope.
- **Mutable vs Immutable**: Modifying mutable objects (like lists or dictionaries) in a local or enclosing scope can affect those objects in the global scope, but reassigning variables themselves does not affect variables in other scopes.

---

### Conclusion:

The **LEGB Rule** is crucial for understanding how Python resolves variable names across different scopes. It helps programmers write more efficient and predictable code by being aware of how Python looks for variables in local, enclosing, global, and built-in scopes. By mastering the LEGB Rule, you can avoid variable name conflicts, correctly manage global and local states, and use nested functions, closures, and decorators effectively.

The **LEGB Rule** in Python is a structured framework that the Python interpreter uses to resolve variable names. By mastering its details, you gain a deeper understanding of variable scope, shadowing, and how Python handles nested functions, closures, and global namespaces.

Here’s a comprehensive explanation with advanced insights and examples:

---

## **LEGB Rule Breakdown**

### 1. **Local Scope (L)**

This is the **innermost scope**, comprising variables defined within the current function or block of code.

#### Characteristics:

- Variables in the local scope exist only during the execution of the function or block.
- Local variables are created when the function is called and destroyed when the function ends.
- Includes function arguments, loop variables, and any variables defined in comprehensions.

#### Advanced Example:

```python
def calculate_area(length, width):
    area = length * width  # 'area' is local
    print(f"Area: {area}")

calculate_area(5, 10)  # Output: Area: 50
```

Here, `length`, `width`, and `area` are local variables specific to the `calculate_area` function.

#### Shadowing Example:

```python
x = 100  # Global variable

def example():
    x = 50  # Local variable shadows the global 'x'
    print(x)

example()  # Output: 50
print(x)    # Output: 100
```

In this case, the local `x` within `example()` shadows the global `x`.

---

### 2. **Enclosing Scope (E)**

This is the scope of an **outer function** that contains a nested (inner) function. Variables in the enclosing function’s scope are accessible to the inner function unless overridden locally.

#### Characteristics:

- Applies only to nested functions.
- The enclosing scope persists as long as the inner function can access it, enabling **closures**.
- Variables from the enclosing scope are read-only in the inner function unless explicitly declared with the `nonlocal` keyword.

#### Nested Function Example:

```python
def outer_function():
    message = "Hello from outer"  # Enclosing variable

    def inner_function():
        print(message)  # Accesses enclosing variable

    inner_function()

outer_function()
```

#### Modifying Enclosing Variables:

Use the `nonlocal` keyword to modify variables in the enclosing scope.

```python
def outer_function():
    count = 0  # Enclosing variable

    def inner_function():
        nonlocal count  # Modifies the enclosing 'count'
        count += 1
        print(count)

    inner_function()
    inner_function()

outer_function()
```

**Output**:

```
1
2
```

---

### 3. **Global Scope (G)**

Variables in the global scope are defined at the **module level**, outside of any function or class.

#### Characteristics:

- Global variables are accessible throughout the module unless shadowed by a local variable.
- Global variables persist for the duration of the program.

#### Accessing Global Variables:

```python
global_var = "I am global"  # Global variable

def show_global():
    print(global_var)

show_global()  # Output: I am global
```

#### Modifying Global Variables:

To modify a global variable within a function, use the `global` keyword.

```python
counter = 0  # Global variable

def increment():
    global counter  # Refers to the global 'counter'
    counter += 1

increment()
print(counter)  # Output: 1
```

---

### 4. **Built-in Scope (B)**

This is the outermost scope containing all of Python’s built-in functions, constants, and exceptions, such as `print()`, `len()`, `max()`, etc.

#### Characteristics:

- Python automatically provides access to built-in names.
- Built-in names can be overridden, but this is generally discouraged.

#### Accessing Built-in Functions:

```python
print(len([1, 2, 3]))  # Output: 3
```

#### Overriding Built-ins (Not Recommended):

```python
len = 10  # Overrides built-in 'len'

# Using 'len' now refers to the integer 10
print(len)  # Output: 10
```

To avoid issues like this, avoid naming variables after built-in functions or objects.

---

## **LEGB in Action: Resolution Process**

When Python encounters a variable, it resolves it using the LEGB order:

1. **Local Scope**: Looks for the variable in the current function.
2. **Enclosing Scope**: If not found locally, checks any enclosing functions.
3. **Global Scope**: If still not found, looks for a global variable.
4. **Built-in Scope**: Finally, checks the built-in namespace.

---

## **Advanced Concepts in LEGB**

### 1. **Closures**

Closures allow an inner function to retain access to the enclosing function's variables, even after the enclosing function has finished executing.

#### Closure Example:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' is retained in closure
    return multiply

double = make_multiplier(2)
print(double(5))  # Output: 10
```

Here, the `factor` variable is retained by the `multiply` function, forming a closure.

---

### 2. **The `global` Keyword**

Use `global` to explicitly state that a variable belongs to the global scope.

#### When to Use `global`:

- To modify a global variable inside a function.
- Avoid unnecessary use; instead, pass variables explicitly for better clarity.

```python
counter = 0

def increment():
    global counter
    counter += 1
```

---

### 3. **The `nonlocal` Keyword**

The `nonlocal` keyword modifies variables in an enclosing scope that are neither local nor global.

#### Nonlocal Example:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        print(x)

    inner()
    print(x)

outer()
```

**Output**:

```
15
15
```

---

### 4. **Mutable vs Immutable in LEGB**

Variables referring to **mutable objects** (e.g., lists, dictionaries) can be modified without re-declaring the variable, but reassigning them creates a new local variable.

#### Example with Mutable Objects:

```python
x = [1, 2, 3]  # Global variable

def modify_list():
    x.append(4)  # Modifies global 'x'

modify_list()
print(x)  # Output: [1, 2, 3, 4]
```

---

## **Common Pitfalls with LEGB**

### Shadowing

Local variables with the same name as global or enclosing variables can unintentionally shadow them, leading to bugs.

#### Example of Shadowing:

```python
x = 10

def func():
    x = 20
    print(x)  # Prints 20 (local)

func()
print(x)  # Prints 10 (global)
```

### Name Errors

Accessing variables before they are defined in the proper scope leads to `NameError`.

#### Example:

```python
def func():
    print(x)  # Error: 'x' is not defined locally
    x = 5

func()
```

---

## **LEGB Rules Summary**

| **Scope**         | **Description**                                          | **When It Exists**                    | **Keywords for Modification** |
| ----------------- | -------------------------------------------------------- | ------------------------------------- | ----------------------------- |
| **Local (L)**     | Variables defined in the current function or block.      | During function execution.            | N/A                           |
| **Enclosing (E)** | Variables in enclosing functions (nested functions).     | As long as the inner function exists. | `nonlocal`                    |
| **Global (G)**    | Variables defined at the module level.                   | Throughout the program’s runtime.     | `global`                      |
| **Built-in (B)**  | Python’s built-in functions and objects (e.g., `len()`). | Always available.                     | Cannot be modified directly.  |

By understanding and applying the LEGB rule, you can better control variable resolution, avoid naming conflicts, and write efficient, error-free Python code.

Here are additional **details, examples, and advanced considerations** about the **LEGB rule** in Python. We'll dive deeper into edge cases, practical use, and theoretical foundations.

---

### **Detailed Explanation of Each Scope**

#### **Local Scope (L)**

- The **local scope** is the innermost level, specifically for variables defined inside a function or comprehension.
- **Unique Behavior**: A new local scope is created each time a function is called, even if the same function is invoked multiple times.

#### **Key Characteristics**:

- Local variables cannot be accessed outside their function.
- Local scope variables are destroyed when the function ends unless explicitly returned or referenced by a closure.

#### **Example**:

```python
def local_example():
    x = 10  # Local variable
    print(f"Local x: {x}")

local_example()
# print(x)  # NameError: x is not defined
```

#### **Advanced Local Scope: Nested Comprehensions**

- Comprehensions have their own local scope, which is separate from the function or global scope.

```python
x = 5  # Global variable

squares = [x**2 for x in range(3)]  # 'x' here is local to the comprehension
print(squares)  # Output: [0, 1, 4]
print(x)  # Output: 5 (Global 'x' remains unaffected)
```

---

#### **Enclosing Scope (E)**

- The **enclosing scope** applies to nested functions.
- Variables in an enclosing scope are accessible, but **read-only** unless modified with `nonlocal`.

#### **Advanced Example**:

```python
def outer_function():
    outer_var = "I am enclosing"

    def inner_function():
        print(outer_var)  # Accesses the enclosing variable

    inner_function()

outer_function()
```

#### **Overriding Enclosing Scope: `nonlocal`**

- Use `nonlocal` to modify variables in the enclosing scope.

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_func = counter()
print(counter_func())  # Output: 1
print(counter_func())  # Output: 2
```

#### **Edge Case: Enclosing Scope Shadowing**

- If a variable with the same name exists in the local scope, it shadows the enclosing variable.

```python
def outer():
    x = "Outer"

    def inner():
        x = "Inner"  # Local to 'inner', shadows enclosing 'x'
        print(x)

    inner()

outer()  # Output: Inner
```

---

#### **Global Scope (G)**

- The **global scope** exists at the top level of the program.
- Variables in the global scope can be accessed from any function or block unless shadowed by a local variable.

#### **Global Modification Example**:

```python
x = 10  # Global variable

def modify_global():
    global x  # Explicitly references the global variable
    x += 5

modify_global()
print(x)  # Output: 15
```

#### **Edge Case: Avoiding `global` for Immutable Objects**

Using `global` for immutable objects like integers can cause confusion.

**Better Practice**:
Pass global variables as arguments or return modified values explicitly.

```python
x = 10

def modify(value):
    return value + 5

x = modify(x)
print(x)  # Output: 15
```

---

#### **Built-in Scope (B)**

- The **built-in scope** includes Python's built-in functions, constants, and exceptions.
- Always the last scope searched.

#### **Common Mistake: Overriding Built-ins**

- Overriding a built-in function can lead to unexpected errors.

```python
len = 42  # Overrides the built-in 'len'
# print(len([1, 2, 3]))  # TypeError: 'int' object is not callable

del len  # Restore the built-in
print(len([1, 2, 3]))  # Output: 3
```

#### **Key Built-ins**:

- Functions: `print()`, `len()`, `range()`, `str()`, `int()`, etc.
- Exceptions: `TypeError`, `ValueError`, `NameError`, etc.
- Constants: `True`, `False`, `None`.

---

### **Advanced Concepts with LEGB**

#### 1. **Dynamic Scoping vs. Static Scoping**

- Python uses **static scoping** (lexical scoping), meaning the structure of the code determines how names are resolved.
- Dynamic scoping resolves names based on the function call stack, which Python does not use.

**Static Scoping Example**:

```python
x = 10

def outer():
    x = 20  # Enclosing scope
    def inner():
        print(x)  # Refers to 'x' in the enclosing scope
    inner()

outer()  # Output: 20
```

#### 2. **Closures**

Closures retain variables from their enclosing scope even after the enclosing function has finished execution.

```python
def make_closure(msg):
    def display_message():
        print(msg)  # Retains 'msg' from enclosing scope
    return display_message

closure = make_closure("Hello, Closure!")
closure()  # Output: Hello, Closure!
```

---

### **Common Pitfalls and Solutions**

#### **1. Variable Shadowing**

- Shadowing happens when a variable in a local or enclosing scope hides a variable of the same name in an outer scope.
- **Solution**: Use unique variable names to avoid confusion.

```python
x = 10

def shadow_example():
    x = 20  # Shadows global 'x'
    print(x)

shadow_example()  # Output: 20
print(x)  # Output: 10
```

#### **2. Using `global` for Large Programs**

- Using `global` excessively makes the code harder to debug and maintain.
- **Solution**: Encapsulate global data in classes or use function parameters.

---

### **LEGB Search Order Summary**

| **Scope**         | **Priority** | **When Used**                       |
| ----------------- | ------------ | ----------------------------------- |
| **Local (L)**     | Highest      | Inside a function or comprehension. |
| **Enclosing (E)** | Second       | For nested functions.               |
| **Global (G)**    | Third        | At the module level.                |
| **Built-in (B)**  | Lowest       | For built-in functions and objects. |

---

### **Visual Representation of LEGB**

```text
LEGB Search Path
-----------------
Local --> Enclosing --> Global --> Built-in
```

When you call a variable or function, Python starts searching from the innermost (local scope) and moves outward until it finds the name or raises a `NameError`.

---

### **LEGB Debugging Tools**

#### **1. Using `globals()` and `locals()`**

- `globals()`: Returns a dictionary of global scope variables.
- `locals()`: Returns a dictionary of local scope variables.

**Example**:

```python
x = 10

def scope_debug():
    y = 20
    print("Global Scope:", globals())
    print("Local Scope:", locals())

scope_debug()
```

#### **2. Inspecting Built-ins**

Use the `dir()` function to inspect Python's built-in namespace.

```python
print(dir(__builtins__))
```

---

### **Real-World Use Cases**

#### **Closures in Decorators**

Decorators often use closures to encapsulate behavior.

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

#### **Global State in Configuration**

Use global variables sparingly for configuration settings in small scripts.

```python
config = {"debug": True}

def toggle_debug():
    global config
    config["debug"] = not config["debug"]
```

---

By deeply understanding **LEGB**, you’ll master Python’s scoping rules and avoid common pitfalls.
