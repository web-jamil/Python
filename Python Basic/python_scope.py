print("--- Python Variable Scope: Practice Code ---")

# --- 1. What is Scope? ---
print("\n--- 1. What is Scope? ---")
print("Scope refers to the region of a program where a variable is accessible.")
print("It determines where in your code you can refer to a variable by its name.")
print("Python follows the LEGB rule for scope resolution: Local -> Enclosing -> Global -> Built-in.")


# --- 2. Local Scope (L) ---
print("\n--- 2. Local Scope (L) ---")
print("Variables defined inside a function (or a method, or a class method) have local scope.")
print("They can only be accessed within that function.")
print("They are created when the function is called and destroyed when the function finishes.")

def my_local_function():
    local_variable = "I'm a local variable inside my_local_function"
    print(f"Inside my_local_function: {local_variable}")

my_local_function()
# print(local_variable) # This line would cause a NameError because local_variable is not defined in global scope.
try:
    print(local_variable)
except NameError as e:
    print(f"Error trying to access local_variable outside function: {e}")

# Different function, different local scope
def another_local_function():
    local_variable = "I'm a local variable inside another_local_function"
    print(f"Inside another_local_function: {local_variable}")

another_local_function()


# --- 3. Enclosing Scope (E) (Nonlocal Scope) ---
print("\n--- 3. Enclosing Scope (E) (Nonlocal Scope) ---")
print("This applies to nested functions. A variable defined in an outer (enclosing) function's scope")
print("is accessible to inner (nested) functions, but not to the global scope.")
print("The `nonlocal` keyword is used to modify variables in the enclosing scope.")

def outer_function():
    enclosing_variable = "I'm an enclosing variable"

    def inner_function():
        # inner_function can access enclosing_variable
        print(f"Inside inner_function (accessing enclosing): {enclosing_variable}")

        # If we try to modify enclosing_variable without `nonlocal`, it creates a new local variable
        # enclosing_variable = "Modified locally in inner_function" # This creates a new local variable `enclosing_variable` inside inner_function

        # To modify the enclosing_variable, use `nonlocal`
        nonlocal enclosing_variable
        enclosing_variable = "I'm modified by inner_function via nonlocal"
        print(f"Inside inner_function (after nonlocal modify): {enclosing_variable}")


    inner_function()
    print(f"Inside outer_function (after inner_function call): {enclosing_variable}")

outer_function()

# Example with a counter using closure
def make_counter():
    count = 0 # This is in the enclosing scope for the returned function

    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = make_counter()
counter2 = make_counter()

print(f"Counter 1: {counter1()}") # 1
print(f"Counter 1: {counter1()}") # 2
print(f"Counter 2: {counter2()}") # 1 (each counter has its own 'count' variable)
print(f"Counter 1: {counter1()}") # 3


# --- 4. Global Scope (G) ---
print("\n--- 4. Global Scope (G) ---")
print("Variables defined at the top level of a module (outside any function or class) have global scope.")
print("They can be accessed from anywhere within that module.")
print("The `global` keyword is used to modify a global variable from within a function.")

global_variable = "I'm a global variable"

def access_global():
    print(f"Inside access_global (accessing global): {global_variable}")

access_global()

def modify_global():
    # To modify the global_variable, you must use the `global` keyword.
    # Without `global`, `global_variable = "..."` would create a new LOCAL variable.
    global global_variable
    global_variable = "I'm modified by modify_global function"
    print(f"Inside modify_global (after modify): {global_variable}")

print(f"Before modify_global: {global_variable}")
modify_global()
print(f"After modify_global: {global_variable}")

# Attempt to modify global without 'global' keyword
def shadow_global():
    global_variable = "I'm a new LOCAL variable, not modifying the global one!"
    print(f"Inside shadow_global (local 'global_variable'): {global_variable}")

print(f"Before shadow_global: {global_variable}")
shadow_global()
print(f"After shadow_global (global variable untouched): {global_variable}")


# --- 5. Built-in Scope (B) ---
print("\n--- 5. Built-in Scope (B) ---")
print("This is the outermost scope, containing built-in functions (e.g., `print`, `len`, `sum`)")
print("and built-in exceptions that are always available.")
print("You don't define variables here, but you can access them without importing anything.")

# Example: Using built-in functions
length = len("Python")
print(f"Length of 'Python': {length}")

# Even if you define a variable with the same name, the built-in is still there
# (though your local variable will shadow it in its scope)
len = "I'm a string"
print(f"My local 'len': {len}")
# print(len("another string")) # This would now cause a TypeError because 'len' is a string, not a function.
del len # Delete the local variable to restore the built-in len() function
print(f"Length of 'Python' after deleting local 'len': {len('Python')}")


# --- 6. The LEGB Rule in Action ---
print("\n--- 6. The LEGB Rule in Action ---")
print("Python looks for a variable in this order:")
print("1. Local (L) - in the current function.")
print("2. Enclosing (E) - in any immediately enclosing function's scope.")
print("3. Global (G) - in the top-level of the current module.")
print("4. Built-in (B) - in the predefined Python built-in names.")

x = "global x" # Global

def outer():
    x = "enclosing x" # Enclosing

    def inner():
        x = "local x" # Local
        print(f"Inside inner: {x}") # Accesses local x

    def inner_no_local():
        print(f"Inside inner_no_local: {x}") # Accesses enclosing x

    inner()
    inner_no_local()
    print(f"Inside outer: {x}") # Accesses enclosing x

outer()
print(f"In global scope: {x}") # Accesses global x

print("\nAnother example demonstrating LEGB:")
a = 10 # Global

def func1():
    b = 20 # Enclosing for func2
    def func2():
        c = 30 # Local for func2
        print(f"In func2: c={c}")
        print(f"In func2: b={b}") # Accesses enclosing b
        print(f"In func2: a={a}") # Accesses global a
        # print(d) # NameError if d is not defined anywhere

    func2()
    # print(c) # NameError: c is local to func2
    print(f"In func1: b={b}")
    print(f"In func1: a={a}")

func1()
# print(b) # NameError: b is local to func1 (enclosing for func2)
# print(c) # NameError: c is local to func2

print("\n--- End of Python Variable Scope Practice Code ---")