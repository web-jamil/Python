The **scope** of a variable refers to the region of the program where the variable is accessible. In Python, the scope determines where in the program a variable can be used, modified, or referenced. Understanding variable scope is essential for writing clean and efficient code, as it prevents naming conflicts, unexpected behaviors, and unintended variable shadowing.

### 1. **Types of Variable Scope in Python**

Python has several scopes for variables, which are primarily determined by where the variable is defined. These scopes follow the **LEGB Rule**, which stands for Local, Enclosing, Global, and Built-in.

#### **LEGB Rule**:

1. **L (Local)**: Variables defined inside a function or block. They are accessible only within that function or block.
2. **E (Enclosing)**: Variables defined in an enclosing function (i.e., the function that contains the current function). These are accessible in the nested functions.
3. **G (Global)**: Variables defined at the top-level of the script or module. They are accessible throughout the module and can be accessed from any function, provided the function doesn't have a local variable with the same name.
4. **B (Built-in)**: Variables that are built into Python, such as `print()`, `len()`, etc. These are always available in any scope.

### 2. **Local Scope**

Variables defined inside a function are in the **local scope** of that function. These variables are only accessible within that function and cannot be accessed outside of it.

#### Example: Local Scope

```python
def my_function():
    local_var = 10  # local_var is in the local scope
    print(local_var)  # Accessible inside the function

my_function()
print(local_var)  # Error: local_var is not accessible outside the function
```

In this example:

- `local_var` is a local variable within `my_function`. It's accessible only inside `my_function`.
- If you try to access `local_var` outside the function, you get a **NameError** because it is not in the global scope.

### 3. **Enclosing Scope**

The **enclosing scope** refers to the scope of functions that enclose the current function, i.e., the outer functions in which the current function is nested. A variable from an enclosing scope is accessible in the nested function.

#### Example: Enclosing Scope

```python
def outer_function():
    enclosing_var = 20  # enclosing_var is in the enclosing scope

    def inner_function():
        print(enclosing_var)  # Accessible from the enclosing scope

    inner_function()

outer_function()
```

Here:

- `enclosing_var` is defined in `outer_function()`, and `inner_function()` (which is nested inside) can access `enclosing_var` because it is in the enclosing scope.
- If you try to access `enclosing_var` directly from outside both functions, you will get an error.

### 4. **Global Scope**

Variables defined at the top-level of a script (outside of all functions and classes) are in the **global scope**. They are accessible throughout the script, including within functions, as long as the function doesn't have a local variable with the same name.

#### Example: Global Scope

```python
global_var = 30  # global_var is in the global scope

def my_function():
    print(global_var)  # Accessible from the global scope

my_function()
print(global_var)  # Accessible globally
```

In this example:

- `global_var` is defined in the global scope and can be accessed both inside `my_function()` and outside the function.
- However, if you modify `global_var` inside a function, Python assumes you are creating a **local variable** unless you explicitly tell Python to use the global variable.

#### **Modifying Global Variables Inside Functions**

To modify a global variable inside a function, you must declare it as `global` within the function. Otherwise, Python will treat it as a local variable.

```python
global_var = 30  # global variable

def my_function():
    global global_var  # Declare global_var as global to modify it
    global_var = 40  # Modify the global variable

my_function()
print(global_var)  # Output: 40
```

Here:

- The `global` keyword is used inside `my_function()` to tell Python that `global_var` refers to the global variable and not a local one.
- Without the `global` keyword, `global_var` inside the function would be treated as a local variable, and the global `global_var` would remain unchanged.

### 5. **Built-in Scope**

The **built-in scope** contains names that are predefined in Python, such as `print()`, `len()`, `int()`, and other built-in functions, exceptions, and objects.

These names are always available in any scope, and you cannot overwrite them directly.

#### Example: Built-in Scope

```python
print(len("Hello"))  # len is a built-in function, accessible everywhere
```

- Built-in variables and functions can be overridden, but this is generally not recommended because it can lead to confusion and bugs. For example, overriding `print` or `len` would change their expected behavior.

### 6. **The `global` and `nonlocal` Keywords**

- **`global`**: Used inside a function to refer to a global variable and modify it. Without `global`, Python assumes you are creating a local variable with the same name.
- **`nonlocal`**: Used inside a nested function to refer to variables in the enclosing (but not global) scope. This allows you to modify variables from enclosing functions.

#### Example: `global` Keyword

```python
x = 10  # Global variable

def modify_global():
    global x  # Refers to the global variable
    x = 20    # Modifies the global variable

modify_global()
print(x)  # Output: 20
```

#### Example: `nonlocal` Keyword

```python
def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x  # Refers to the enclosing variable
        x = 20      # Modifies the enclosing variable

    inner_function()
    print(x)  # Output: 20

outer_function()
```

In the `nonlocal` example:

- The `nonlocal` keyword allows `inner_function()` to modify the `x` variable in the enclosing scope (`outer_function`).
- Without `nonlocal`, `x` would be treated as a local variable inside `inner_function()`.

### 7. **The Scope Resolution Order (LEGB) in Action**

When you reference a variable in Python, it follows the **LEGB** rule to determine which variable to use. It searches in the following order:

1. **Local (L)**: Look for the variable in the local scope of the function.
2. **Enclosing (E)**: If not found, look in the enclosing functions.
3. **Global (G)**: If still not found, look in the global scope.
4. **Built-in (B)**: If the variable is not found in any of the above, check the built-in scope.

#### Example: Scope Resolution Order

```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)  # This will print "Local" (L)

    inner()

outer()
```

In this example:

- The `inner()` function will print `"Local"`, as it directly refers to the `x` in its local scope.
- If `x` wasn't defined locally in `inner()`, it would then check the enclosing scope (from `outer()`), then the global scope.

### 8. **Global vs Local Variables**

#### **Global Variable**:

- Accessible anywhere in the script after its definition.
- Can be modified using the `global` keyword inside a function.

#### **Local Variable**:

- Defined within a function and accessible only inside that function.
- Cannot be accessed from outside the function.

### 9. **Variable Shadowing**

**Shadowing** occurs when a variable defined in a narrower scope (such as a local variable) has the same name as a variable in an outer scope. The inner variable "shadows" the outer one, meaning that the inner variable takes precedence in its scope.

#### Example: Variable Shadowing

```python
x = "Global"

def my_function():
    x = "Local"  # Shadows the global x
    print(x)  # Output: Local

my_function()
print(x)  # Output: Global
```

In this case:

- The local variable `x` inside `my_function()` shadows the global `x`, so when you print `x` inside the function, it prints "Local."
- Outside the function, the global `x` remains unaffected.

### 10. **Summary of Variable Scope Types and Keywords**

- **Local Scope (L)**: Variables defined inside functions, only accessible within those functions.
- **Enclosing Scope (E)**: Variables defined in enclosing (outer) functions, accessible in nested functions.
- **Global Scope (G)**: Variables defined at the module level, accessible throughout the module.
- **Built-in Scope (B)**: Predefined variables and functions, accessible everywhere.

- **`global` keyword**: Used to modify a global variable inside a function.
- **`nonlocal` keyword**: Used to modify a variable from an enclosing scope inside a nested function.

---

### Conclusion

Understanding variable scope is crucial in Python for effective programming. The **LEGB Rule** helps you organize your code and avoid issues such as naming conflicts, shadowing, and unintended changes to global variables. By controlling the scope and understanding how Python searches for variables, you can write cleaner and more efficient code.

Sure! Let's go deeper into the details of **variable scope** in Python, covering more advanced aspects, subtle concepts, and scenarios where scope rules are particularly important.

### 1. **Understanding the LEGB Rule in Depth**

The **LEGB** rule is the fundamental concept in Python's scope resolution. It dictates how Python searches for a variable when it is referenced. Let's explore each part of the LEGB rule in more detail.

#### **Local Scope (L)**

- The **local scope** is the innermost scope where a variable is defined. A variable created inside a function or method is local to that function.
- Local variables are only available inside the function in which they are defined.

**Example**:

```python
def my_function():
    a = 10  # 'a' is local to my_function
    print(a)

my_function()  # Output: 10
print(a)  # Error: 'a' is not defined outside the function
```

**Advanced Note**:

- If you define a variable inside a **lambda function**, that variable is local to the lambda, not the surrounding function.

#### **Enclosing Scope (E)**

- The **enclosing scope** exists in nested functions. It refers to the scope of functions that are not the local function but are still in the hierarchy of functions.
- This is relevant when you have **nested functions**, and a variable in the outer function is used in the inner function.

**Example**:

```python
def outer_function():
    a = 10  # Enclosing variable

    def inner_function():
        print(a)  # 'a' is accessible here (from enclosing scope)

    inner_function()

outer_function()  # Output: 10
```

**Advanced Note**:

- The enclosing scope is important for **closures** in Python, where an inner function can capture variables from the outer function and still access them after the outer function has finished execution.

#### **Global Scope (G)**

- The **global scope** refers to variables that are defined at the top-level of a script or module. Global variables are accessible throughout the module, but they must be declared as `global` if you want to modify them inside a function.

**Example**:

```python
x = 5  # Global variable

def my_function():
    print(x)  # Accessing global variable

my_function()  # Output: 5
```

**Advanced Note**:

- Global variables can be accessed from functions as long as they don’t shadow them with local variables.
- To **modify** a global variable from inside a function, you need to use the `global` keyword.

#### **Built-in Scope (B)**

- The **built-in scope** contains all the built-in names in Python, including functions, exceptions, and constants like `len()`, `print()`, `str()`, and `int()`.
- These built-in names are available in any scope, but it’s generally not recommended to override them, as it can create confusion.

**Example**:

```python
print("Hello")  # Accessing the built-in print function

# However, overriding built-in functions like print() or len() is not recommended
```

**Advanced Note**:

- The built-in scope is the fallback if Python cannot find a variable in any of the other scopes (local, enclosing, or global).

---

### 2. **The `global` and `nonlocal` Keywords (Deep Dive)**

#### **`global` Keyword**

- The `global` keyword is used when you need to refer to a global variable inside a function or to modify it.
- Without the `global` keyword, Python assumes you are creating a new local variable with the same name.

**Example**:

```python
x = 5  # Global variable

def modify_global():
    global x  # Indicate that we are referring to the global variable
    x = 10  # Modify the global variable

modify_global()
print(x)  # Output: 10 (global variable is modified)
```

**Advanced Note**:

- The `global` keyword **does not create a new variable**; it simply allows you to modify an existing global variable within a function.
- If you try to assign a value to a global variable inside a function **without using `global`**, Python will create a local variable with the same name.

#### **`nonlocal` Keyword**

- The `nonlocal` keyword is used to work with variables in the **enclosing (non-global)** scope. It is typically used in nested functions when you want to modify a variable from the enclosing function’s scope.
- Without `nonlocal`, Python would treat the variable as a local variable in the inner function.

**Example**:

```python
def outer():
    x = 5  # Variable in the enclosing scope

    def inner():
        nonlocal x  # Refer to 'x' in the enclosing scope
        x = 10  # Modify the enclosing variable

    inner()
    print(x)  # Output: 10

outer()
```

**Advanced Note**:

- The `nonlocal` keyword allows you to modify variables that are not global but exist in an enclosing function.
- This is especially useful in **closures** or when you need to alter variables that were set by an outer function.

---

### 3. **Mutable vs Immutable Objects in Scope**

When dealing with variable scopes, it’s important to understand how **mutable** and **immutable** objects behave in different scopes.

#### **Immutable Objects**:

- Immutable objects (e.g., integers, floats, strings, and tuples) cannot be modified in place. When you try to modify an immutable object, a new object is created instead.
- If you assign a new value to a variable that holds an immutable object, it creates a new object and doesn’t affect the original one.

**Example (Immutable)**:

```python
x = 5  # Immutable (integer)

def modify():
    x = 10  # Creates a new local variable 'x'
    print(x)  # Output: 10

modify()
print(x)  # Output: 5 (global 'x' is unaffected)
```

#### **Mutable Objects**:

- Mutable objects (e.g., lists, dictionaries, sets) can be changed in place. Modifying a mutable object inside a function can affect the object outside the function, even if the object was passed as an argument.
- **However**, reassigning a mutable object (e.g., reassigning a new list to a variable) inside a function will create a new local variable.

**Example (Mutable)**:

```python
lst = [1, 2, 3]  # Mutable (list)

def modify():
    lst.append(4)  # Modifies the existing list object
    print(lst)  # Output: [1, 2, 3, 4]

modify()
print(lst)  # Output: [1, 2, 3, 4] (global list is modified)
```

If we reassigned `lst` inside the function, it would only affect the local scope:

```python
def modify():
    lst = [4, 5, 6]  # Creates a new local list
    print(lst)  # Output: [4, 5, 6]

modify()
print(lst)  # Output: [1, 2, 3, 4] (global list is unaffected)
```

---

### 4. **Variable Lookup in Nested Functions (Advanced)**

In Python, when you reference a variable inside a function, Python follows the LEGB rule to find the variable. This lookup order can affect how you manage variables in nested functions, closures, and recursive functions.

**Example of Variable Lookup**:

```python
a = 10  # Global variable

def outer():
    a = 20  # Enclosing variable

    def inner():
        a = 30  # Local variable
        print(a)  # The innermost function's 'a' is used

    inner()

outer()  # Output: 30 (Local variable 'a' inside inner() is used)
print(a)  # Output: 10 (Global 'a' is unaffected)
```

**Advanced Note**:

- If you do not have a local or enclosing variable, Python will fall back to the global scope to find the variable. The order of the search (LEGB) can affect how Python resolves the reference.
- Understanding **closures** is important here, as an inner function can "remember" variables from its enclosing scope even after the enclosing function has finished execution.

---

### 5. **Global Variables in Modules (Global Scope)**

In Python, the **global scope** refers not only to variables declared at the top of a script but also to **module-level variables**.

#### **Module-level Global Variables**:

- Variables defined at the module level are accessible across the module and can be accessed by functions within the same module.

**Example**:

```python
global_var = 100  # Global variable at the module level

def my_function():
    print(global_var)  # Accessible in the global scope

my_function()  # Output: 100
```

#### **Importing Global Variables Across Modules**:

- Global variables can also be imported into different modules if needed.

**Example**:

```python
# module1.py
global_var = 50

# module2.py
import module1

print(module1.global_var)  # Accessing the global variable from another module
```

#### **Global Variables with `globals()`**:

- You can use the `globals()` function to access the global variables dynamically. It returns a dictionary representing the global symbol table.

```python
x = 10
print(globals()['x'])  # Output: 10
```

---

### 6. **Global Scope in the REPL (Interactive Mode)**

When working in the Python REPL (Read-Eval-Print Loop), the **global scope** is slightly different, as you interact directly with the interpreter.

- Any variable you define in the REPL becomes part of the **global scope** for that session.
- You can dynamically create and modify global variables in the interactive environment.

---

### 7. **Global Variables in Functions – Pitfalls and Best Practices**

While Python allows you to use global variables within functions, doing so is often discouraged for several reasons:

- **Unintended side effects**: Modifying global variables can lead to bugs and unpredictable behavior if not handled carefully.
- **Hard to track changes**: With a large program, keeping track of which functions modify global variables can be difficult and error-prone.

#### Best Practice:

- Use function arguments and return values to pass data around rather than relying on global variables.
- If global variables are needed, consider using classes or modules to encapsulate them properly.

---

### Conclusion: In-Depth Understanding of Variable Scope in Python

- **LEGB Rule** governs variable lookup, ensuring that Python searches for variables in the correct order.
- **Global**, **local**, **enclosing**, and **built-in** scopes are key to managing variable visibility and accessibility in Python.
- The **`global`** and **`nonlocal`** keywords allow you to modify variables in different scopes.
- Understanding the **mutable** and **immutable** objects behavior helps in managing data correctly.
- **Best practices** include limiting the use of global variables to avoid side effects and improve code readability.

Mastering variable scope is essential for effective Python programming, especially as you work with larger, more complex applications where scope and variable management become crucial.

Certainly! Let's dive even deeper into the concepts of **variable scope** in Python and cover more intricate details, edge cases, and real-world examples to provide a comprehensive understanding.

---

### 1. **Scope and Namespace**

In Python, a **namespace** is a container where variable names are mapped to objects. The scope of a variable refers to where its name is valid (accessible), and the namespace is the structure holding these names.

- A **namespace** is created whenever a function is called, or a module is imported.
- Python’s different scopes have their own namespaces (e.g., global scope has a global namespace).

#### Example of namespaces:

```python
def my_function():
    x = 10  # x in the local namespace of my_function
    print(x)

x = 5  # x in the global namespace
my_function()
```

- Here, `x` exists in two different namespaces:
  - **Global namespace** (`x = 5`)
  - **Local namespace** within `my_function()` (`x = 10`)

### 2. **The Global and Local Namespaces**

The **global namespace** exists for each module and is created when the module is first imported or run. **Local namespaces** are created when a function is called. They are destroyed once the function exits.

#### Example: Global and Local Namespaces

```python
x = 5  # Global variable

def my_function():
    x = 10  # Local variable in my_function
    print(x)

my_function()  # Prints 10 (uses local variable)
print(x)  # Prints 5 (uses global variable)
```

### 3. **Built-in Namespace**

The **built-in namespace** is where Python keeps track of all the built-in functions and exceptions (like `print()`, `len()`, `TypeError`, etc.). These functions and names are available in any scope.

#### Example: Built-in Namespace

```python
print(len("Hello"))  # len() is a built-in function
```

Python automatically imports the built-in namespace into every script, which is why you can access functions like `print()`, `sum()`, and others without importing them explicitly.

### 4. **Shadowing Variables**

**Shadowing** occurs when a variable in a narrower scope (local or inner scope) has the same name as a variable in a broader scope (global or enclosing scope). The variable in the narrower scope "shadows" the one in the broader scope, meaning it hides or overrides it within that scope.

#### Example of Shadowing:

```python
x = 100  # Global variable

def outer_function():
    x = 50  # Enclosing variable

    def inner_function():
        x = 25  # Local variable (shadows enclosing 'x')
        print(x)  # Prints 25 (local variable)

    inner_function()

outer_function()
```

In this case:

- `inner_function()` prints the local `x`, not the enclosing `x`, even though `x` also exists in the enclosing scope (i.e., in `outer_function()`).
- The `x` in `outer_function()` is also not used, since `inner_function()` has its own local variable `x`.

**Important Note**: Shadowing can lead to unexpected behavior, especially in large programs, because it makes it unclear which variable is being referenced. It is a good practice to avoid shadowing if possible.

### 5. **The Role of the `global` Keyword**

The **`global`** keyword tells Python that a variable should refer to a global variable, not a local one. This is especially important when you want to modify a global variable inside a function.

#### Example of `global` Keyword:

```python
x = 5  # Global variable

def modify_global():
    global x  # Indicate that we are using the global 'x'
    x = 10  # Modify the global variable

modify_global()
print(x)  # Output: 10 (global variable is modified)
```

Without the `global` keyword:

```python
x = 5  # Global variable

def modify_global():
    x = 10  # This creates a new local variable 'x', doesn't modify the global one

modify_global()
print(x)  # Output: 5 (global variable is unchanged)
```

#### **Potential Pitfalls with `global`**:

- **Global state**: Overusing the `global` keyword can lead to unwanted side effects because it creates global state, making it harder to reason about your code.
- **Complexity**: If a function modifies many global variables, it may become difficult to track which variables are being changed and where.

To avoid such issues, it's often better to pass variables explicitly as arguments or return them from functions instead of modifying them globally.

### 6. **The Role of `nonlocal` Keyword**

The **`nonlocal`** keyword is used to work with variables in an enclosing scope (but not global). It is most commonly used in nested functions, especially when you need to modify a variable from the outer function.

#### Example of `nonlocal` Keyword:

```python
def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x  # Use the variable from the enclosing function
        x = 20  # Modify the enclosing variable

    inner_function()
    print(x)  # Output: 20

outer_function()
```

Here, `nonlocal x` means that `x` inside `inner_function()` refers to the `x` defined in the enclosing scope (`outer_function()`), not a local variable.

### 7. **Closure**

A **closure** occurs when an inner function remembers and has access to variables from its enclosing (non-global) scope, even after the outer function has finished executing.

#### Example of Closure:

```python
def outer_function(x):
    def inner_function(y):
        return x + y  # 'x' is captured from the enclosing scope
    return inner_function

closure_func = outer_function(10)  # 'x' is set to 10 here
print(closure_func(5))  # Output: 15 (inner function uses 'x' from outer function)
```

In this case:

- `inner_function` "remembers" the value of `x` even after `outer_function` has finished executing, because it forms a closure around `x`.

### 8. **Global Variables in Modules**

Python allows you to access global variables across multiple modules. When you import a module, its global variables are available to be used within the scope of the importing module.

#### Example: Using Global Variables Across Modules

Suppose you have two files: `module1.py` and `module2.py`.

**module1.py**:

```python
global_var = 100  # Global variable in module1
```

**module2.py**:

```python
import module1  # Import module1

print(module1.global_var)  # Access global variable from module1
```

In this case, `module2.py` can access the global variable `global_var` from `module1.py`.

### 9. **Global Variables in the REPL (Interactive Mode)**

In the Python **interactive interpreter** (REPL), the global namespace is automatically created when you start the session. Variables defined in the REPL are part of the global namespace, and you can manipulate them during the session.

#### Example in the REPL:

```python
>>> x = 42  # Global variable in REPL
>>> def my_function():
...     print(x)  # Global variable is accessible inside the function
...
>>> my_function()  # Output: 42
```

In the REPL, you can also modify global variables dynamically. For example, you can change the value of `x` and immediately observe the effects in your program.

### 10. **Managing Variables with Classes**

In larger applications, it’s often better to organize variables in classes and use **instance variables** to manage the state. This provides a more controlled and modular approach than relying heavily on global variables.

#### Example: Managing Variables with Classes

```python
class MyClass:
    def __init__(self, x):
        self.x = x  # Instance variable

    def set_value(self, new_value):
        self.x = new_value  # Modify instance variable

    def get_value(self):
        return self.x  # Access instance variable

obj = MyClass(10)
print(obj.get_value())  # Output: 10
obj.set_value(20)
print(obj.get_value())  # Output: 20
```

In this example, `self.x` is an instance variable that is scoped to the class instance. This allows better organization of state and reduces the need for global variables.

### 11. **Stack vs Heap Memory and Variable Scope**

In Python, the way variables are stored can influence their scope:

- **Stack**: Local variables (e.g., those defined inside functions) are often stored on the stack. These variables are automatically destroyed when the function exits.
- **Heap**: Objects like lists, dictionaries, and other mutable types are stored on the heap. These objects can persist beyond the scope they were created in as long as there are references to them.

#### Example:

```python
def my_function():
    a = [1, 2, 3]  # Mutable object stored on the heap
    print(a)

my_function()
# 'a' is gone, but the object it referred to is still in memory (as long as other references exist)
```

Understanding this distinction can help you optimize memory usage and manage variable lifetimes effectively.

---

### Conclusion

Understanding the **scope** and **namespace** in Python is crucial for writing clean, maintainable code. Here's a recap of what we've covered:

- **LEGB Rule**: Python searches for a variable in the order of Local, Enclosing, Global, and Built-in namespaces.
- **`global` and `nonlocal`**: These keywords help you modify global and enclosing variables within functions.
- **Closures**: Inner functions can remember the variables of their enclosing scopes, even after the outer function finishes executing.
- **Shadowing**: Variables in inner or local scopes can shadow variables in outer or global scopes, leading to potential confusion.
- **Global Variables**: While convenient, they can lead to side effects and bugs if overused.
- **Classes and Instance Variables**: Classes allow for better management of state compared to global variables.

By mastering variable scope, you will be able to manage your variables more effectively, write clearer and more predictable code, and avoid common pitfalls like shadowing and unintended side effects.

Let's go even deeper into the nuances and advanced concepts related to **variable scope** in Python. We will explore some of the less commonly discussed aspects, including the behavior of **mutable** vs. **immutable** objects, **Python closures**, **nested functions**, and more about how the **LEGB rule** works in more complex cases.

---

### 1. **Understanding Mutable vs Immutable Objects in Scope**

The way Python handles **mutable** vs. **immutable** objects in different scopes is crucial for understanding how variables are manipulated and how their values persist across different levels of scope.

#### **Immutable Objects** (e.g., `int`, `float`, `str`, `tuple`)

- Immutable objects cannot be changed in place. Instead of modifying an existing object, when you "change" an immutable object, a new object is created.
- When an immutable object is assigned to a variable in a specific scope (e.g., a function), Python creates a new object in that scope and does not affect any other scope (global or enclosing).

**Example of Immutable Objects**:

```python
x = 5  # Global variable (immutable)

def my_function():
    x = 10  # Local variable (creates a new local x)
    print(x)  # Prints 10

my_function()
print(x)  # Prints 5 (Global variable is unaffected)
```

Here, the global variable `x` remains unaffected by the local `x` in `my_function`, because integers are immutable in Python. The assignment to `x` inside the function creates a new object, which does not modify the global one.

#### **Mutable Objects** (e.g., `list`, `dict`, `set`)

- Mutable objects, on the other hand, can be modified in place. When a mutable object is passed to a function or modified in an inner scope, it **can** change its state in the global or enclosing scope, provided the object is not reassigned.
- If the mutable object is reassigned inside the function, a new object is created in that scope.

**Example of Mutable Objects**:

```python
lst = [1, 2, 3]  # Global variable (mutable)

def modify():
    lst.append(4)  # Modify the existing object (global list)
    print(lst)  # Prints [1, 2, 3, 4]

modify()
print(lst)  # Prints [1, 2, 3, 4] (Global list is modified)
```

If we reassign `lst` inside the function, it would not affect the global variable:

```python
def modify():
    lst = [4, 5, 6]  # Reassign to a new list
    print(lst)  # Prints [4, 5, 6]

modify()
print(lst)  # Prints [1, 2, 3] (Global list remains unaffected)
```

**Important Concepts to Understand**:

- **In-place modification** of mutable objects like lists, dictionaries, and sets can alter the object that is visible across all scopes.
- **Reassigning** a mutable object inside a function creates a new object in the local scope, which doesn't affect the original object in the global or enclosing scopes.

---

### 2. **Nested Functions and Variable Scope**

When you have **nested functions**, Python’s scope mechanism becomes especially important. The behavior of variables inside nested functions relies heavily on the **LEGB rule**.

#### **Accessing Variables in Nested Functions**

Variables in nested functions are searched for using the **LEGB rule**:

1. **Local scope (L)**: If the variable is local to the function, it will be used directly.
2. **Enclosing scope (E)**: If not found locally, Python looks in the enclosing functions’ scopes.
3. **Global scope (G)**: If not found in local or enclosing scopes, Python looks in the global scope.
4. **Built-in scope (B)**: If Python can't find the variable in the previous scopes, it will look in the built-in scope.

**Example of Variable Lookup in Nested Functions**:

```python
x = 10  # Global variable

def outer():
    x = 20  # Enclosing variable

    def inner():
        x = 30  # Local variable
        print(x)  # Prints 30 (local variable)

    inner()

outer()
```

Here, the `inner()` function prints `30`, which is the **local variable** in `inner()`. The enclosing `x` (in `outer()`) and the global `x` are **shadowed** by the local variable.

#### **Modifying Variables in Nested Functions with `nonlocal`**

The **`nonlocal`** keyword is used when you want to refer to and modify variables in the enclosing (but non-global) scope. This is common in **closures** or when you need to mutate a variable from an outer function in a nested function.

**Example of Using `nonlocal`**:

```python
def outer():
    x = 10  # Enclosing variable

    def inner():
        nonlocal x  # Use the enclosing 'x' (not global)
        x = 20  # Modify the enclosing 'x'

    inner()
    print(x)  # Output: 20

outer()
```

Without `nonlocal`, Python would create a new local variable `x` in `inner()`, and the outer `x` would remain unchanged.

#### **Closures**

A **closure** occurs when a nested function captures and "remembers" the variables from the enclosing scope. Closures are powerful and enable things like factory functions, decorators, and callbacks.

**Example of a Closure**:

```python
def outer(x):
    def inner(y):
        return x + y  # 'x' is remembered from the enclosing scope
    return inner

closure_function = outer(10)  # Creates a closure with x = 10
print(closure_function(5))  # Output: 15 (x is remembered)
```

Here, the `inner()` function is a closure because it captures the variable `x` from `outer()` and continues to have access to it even after `outer()` finishes execution.

---

### 3. **The `globals()` and `locals()` Functions**

Python provides the **`globals()`** and **`locals()`** functions to allow you to access and manipulate the global and local namespaces respectively.

#### **Using `globals()`**

- The **`globals()`** function returns a dictionary representing the global namespace. It can be used to dynamically modify or inspect global variables.

**Example of `globals()`**:

```python
x = 10  # Global variable

def modify_global():
    globals()['x'] = 20  # Modify global variable via globals()

modify_global()
print(x)  # Output: 20 (global variable 'x' is modified)
```

- This method allows you to interact with global variables dynamically. However, using `globals()` can make your code harder to follow, so it is best to use it sparingly.

#### **Using `locals()`**

- The **`locals()`** function returns a dictionary representing the local namespace of the current scope. It allows you to inspect or modify local variables.

**Example of `locals()`**:

```python
def my_function():
    x = 10  # Local variable
    print(locals())  # Prints local variables in the current scope

my_function()  # Prints {'x': 10}
```

In the case of functions, **`locals()`** returns a dictionary of the local variables and their values in that scope.

#### **Special Case: Inside Classes and Methods**

In classes and methods, the behavior of `globals()` and `locals()` is slightly different. For example, inside a class, **`locals()`** returns the instance’s attributes, method definitions, etc.

---

### 4. **Advanced Case: Multiple Variables in Different Scopes**

In more complex programs, you might encounter situations where multiple variables exist across different scopes, such as nested functions and class methods. In such cases, it’s important to understand how Python resolves variable lookups when multiple variables with the same name exist in different scopes.

#### **Example with Multiple Scopes**:

```python
x = 10  # Global variable

def outer():
    x = 20  # Enclosing variable

    def inner():
        x = 30  # Local variable
        print(x)  # Prints 30 (local variable)

    inner()
    print(x)  # Prints 20 (enclosing variable)

outer()
print(x)  # Prints 10 (global variable)
```

Here, `inner()` prints the local `x`, `outer()` prints the enclosing `x`, and the global `x` remains unchanged.

**Important Concept**: The closer the scope to the variable reference, the higher priority it has. In this case, the **local variable** in `inner()` takes precedence over the enclosing `x`.

---

### 5. **Mutable Default Arguments**

One subtle edge case in Python involves **mutable default arguments** in functions. Mutable objects (like lists and dictionaries) can be used as default argument values, but they behave differently from immutable objects.

#### **Problem with Mutable Default Arguments**:

```python
def append_to_list(lst=[]):
    lst.append(1)
    return lst

print(append_to_list())  # Output: [1]
print(append_to_list())  # Output: [1] (This is unexpected! It modifies the same list)
```

The issue here is that the default argument is evaluated **once** when the function is defined, and the same list object is reused in subsequent function calls. This can lead to unexpected side effects.

#### **Solution: Use `None` as a Default Value**:

To avoid this, you can use `None` as the default value and initialize the argument inside the function.

```python
def append_to_list(lst=None):
    if lst is None:
        lst = []  # Create a new list each time
    lst.append(1)
    return lst

print(append_to_list())  # Output: [1]
print(append_to_list())  # Output: [1] (Now it's correct, different list each time)
```

---

### 6. **The `exec()` and `eval()` Functions and Scope**

The `exec()` and `eval()` functions can execute Python code dynamically, and they allow you to manipulate the scope in a flexible

way. These functions can execute code in either the global or local namespace.

#### **Using `exec()`**:

```python
x = 10
code = 'x = 20'
exec(code)  # Executes the code in the current namespace
print(x)  # Output: 20 (global x is modified)
```

#### **Using `eval()`**:

```python
x = 10
result = eval('x + 5')
print(result)  # Output: 15 (evaluates the expression and returns the result)
```

`exec()` is used for executing arbitrary code, while `eval()` is used for evaluating expressions and returning results. Both functions should be used with caution, as they can introduce security risks.

---

### Conclusion

Variable scope in Python is a fundamental concept, and mastering it is essential for writing efficient, maintainable code. Here are the key takeaways:

- **LEGB Rule**: Python resolves variables by searching local, enclosing, global, and built-in scopes.
- **Mutable vs Immutable**: Mutable objects (e.g., lists, dictionaries) can be modified in place across scopes, while immutable objects (e.g., integers, strings) cannot.
- **Closures**: Inner functions can capture and remember variables from their enclosing scope, even after the outer function finishes.
- **Mutable Default Arguments**: Be careful when using mutable default arguments as they can lead to unexpected behaviors.
- **Dynamic Execution**: Functions like `exec()` and `eval()` can manipulate scope dynamically, but they should be used cautiously.

By understanding how Python handles variable scopes, you'll be able to write cleaner, more efficient code while avoiding subtle bugs.
