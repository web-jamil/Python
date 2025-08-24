import time
import functools # For @functools.wraps

print("--- Python Decorators: Practice Code ---")

# --- 1. What are Decorators? ---
print("\n--- 1. What are Decorators? ---")
print("A decorator is a design pattern in Python that allows a user to add new functionality to an existing object (like a function or method)")
print("without modifying its structure. They are essentially functions that take another function as an argument,")
print("add some functionality, and then return a new function.")

print("Decorators are syntactic sugar for a specific way of calling a higher-order function.")
print("`@my_decorator` placed above a function `def my_func():` is equivalent to `my_func = my_decorator(my_func)`.")


# --- 2. Understanding the Basics: Functions as First-Class Objects ---
print("\n--- 2. Understanding the Basics: Functions as First-Class Objects ---")
print("Before decorators, it's crucial to understand that functions in Python are 'first-class objects'.")
print("This means you can:")
print("a) Assign them to variables.")
print("b) Pass them as arguments to other functions.")
print("c) Return them from other functions (this is key for closures and decorators).")

def greet(name):
    return f"Hello, {name}!"

# a) Assign to a variable
say_hi = greet
print(f"Assigned function: {say_hi('Alice')}")

# b) Pass as an argument
def call_function(func, arg):
    return func(arg)

print(f"Passed as argument: {call_function(greet, 'Bob')}")

# c) Return from another function (a simple 'closure')
def make_greeter(greeting_word):
    def actual_greeter(name):
        return f"{greeting_word}, {name}!"
    return actual_greeter

evening_greeter = make_greeter("Good Evening")
print(f"Returned function: {evening_greeter('Charlie')}")


# --- 3. Creating a Simple Decorator (Manual Way First) ---
print("\n--- 3. Creating a Simple Decorator (Manual Way First) ---")
print("Let's create a decorator that prints a message before and after a function call.")

def simple_logger(func):
    def wrapper(*args, **kwargs): # `*args`, `**kwargs` ensure it works for any function signature
        print(f"Calling function: {func.__name__}...")
        result = func(*args, **kwargs) # Call the original function
        print(f"Function {func.__name__} finished.")
        return result
    return wrapper

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Manually applying the decorator
add_logged = simple_logger(add)
subtract_logged = simple_logger(subtract)

print("\nManually applied decorators:")
print(f"Result of add_logged(10, 5): {add_logged(10, 5)}")
print(f"Result of subtract_logged(10, 5): {subtract_logged(10, 5)}")


# --- 4. Using the `@` Syntactic Sugar ---
print("\n--- 4. Using the `@` Syntactic Sugar ---")
print("The `@` symbol is syntactic sugar that simplifies decorator application.")
print("`@decorator_name` placed directly above `def function_name():` is equivalent to `function_name = decorator_name(function_name)`.")

@simple_logger # This is syntactic sugar for: multiply = simple_logger(multiply)
def multiply(a, b):
    return a * b

@simple_logger
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

print("\nUsing `@` decorator syntax:")
print(f"Result of multiply(4, 3): {multiply(4, 3)}")
try:
    print(f"Result of divide(10, 0): {divide(10, 0)}")
except ValueError as e:
    print(f"Caught error: {e}")


# --- 5. Decorators with Arguments ---
print("\n--- 5. Decorators with Arguments ---")
print("Sometimes, you want to pass arguments to your decorator itself.")
print("This requires an extra layer of nesting: a function that takes arguments and returns the actual decorator.")

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result # Only return the result of the last call
        return wrapper
    return decorator_repeat

@repeat(num_times=3) # The arguments are passed here
def say_hi_repeated(name):
    print(f"Hi, {name}!")

print("\nDecorator with arguments:")
say_hi_repeated("Python")


# --- 6. The `functools.wraps` Decorator ---
print("\n--- 6. The `functools.wraps` Decorator ---")
print("A problem with decorators is that they hide the original function's metadata (like `__name__`, `__doc__`, `__module__`).")
print("This can make debugging and introspection harder.")
print("`@functools.wraps(func)` is a decorator (itself!) that copies the metadata from the original function to the wrapper function.")

def timer(func):
    @functools.wraps(func) # Use wraps here
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def long_running_task(n):
    """This function simulates a long task."""
    time.sleep(n)
    return f"Task completed in {n} seconds."

print("\nDecorator with @functools.wraps:")
task_result = long_running_task(0.5)
print(f"Task result: {task_result}")

print(f"Name of long_running_task: {long_running_task.__name__}") # Correctly 'long_running_task' due to wraps
print(f"Docstring of long_running_task: {long_running_task.__doc__}") # Correctly the original docstring


# --- 7. Chaining Decorators ---
print("\n--- 7. Chaining Decorators ---")
print("You can apply multiple decorators to a single function by stacking them.")
print("They are applied from bottom to top.")

@simple_logger # Applied first (outermost wrapper)
@timer       # Applied second (inner wrapper)
def complex_operation(x, y):
    """Performs a complex calculation and returns the result."""
    time.sleep(0.2)
    return x * y + x / y

print("\nChaining decorators:")
result_complex = complex_operation(10, 2)
print(f"Complex operation result: {result_complex}")

# Order of execution:
# 1. `complex_operation` is passed to `timer`, which returns `timer_wrapper`.
# 2. `timer_wrapper` is passed to `simple_logger`, which returns `logger_wrapper`.
# So, when `complex_operation()` is called, `logger_wrapper` runs first, then `timer_wrapper`, then the original `complex_operation`.


# --- 8. Use Cases for Decorators ---
print("\n--- 8. Use Cases for Decorators ---")
print("- **Logging:** Add logging messages before/after function calls (as shown with `simple_logger`).")
print("- **Timing:** Measure function execution time (as shown with `timer`).")
print("- **Authentication/Authorization:** Check user permissions before allowing access to a function.")
print("- **Caching:** Store results of expensive function calls to return quickly on subsequent calls.")
print("- **Input Validation:** Validate function arguments before execution.")
print("- **Rate Limiting:** Control how often a function can be called.")
print("- **Retries:** Automatically retry a function call if it fails.")
print("- **Frameworks:** Widely used in web frameworks (e.g., Flask, Django) for routing (`@app.route`).")

print("\nExample: Simple Caching Decorator (concept)")
def cache(func):
    _cache = {} # This dict is part of the closure for `wrapper`
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items()))) # Create a hashable key
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        print(f"Using cache for {func.__name__}({args}, {kwargs})")
        return _cache[key]
    return wrapper

@cache
def expensive_calculation(n):
    print(f"Actually calculating {n}...")
    time.sleep(1) # Simulate expensive computation
    return n * n

print("\nCaching decorator example:")
print(f"Result 1: {expensive_calculation(5)}") # First call, calculates
print(f"Result 2: {expensive_calculation(5)}") # Second call, uses cache
print(f"Result 3: {expensive_calculation(6)}") # New argument, calculates


print("\n--- End of Python Decorators Practice Code ---")