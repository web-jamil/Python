print("--- Python Closures: Practice Code ---")

# --- 1. What is a Closure? ---
print("\n--- 1. What is a Closure? ---")
print("A closure is a function object that remembers values from its enclosing lexical scope")
print("even if the enclosing scope is no longer present in memory.")
print("In simpler terms, it's a function that 'remembers' the environment in which it was created.")
print("This allows it to access and sometimes modify variables from that environment, even after the outer function has finished executing.")

# For a closure to exist, we need:
# 1. A nested function (a function defined inside another function).
# 2. The inner function must refer to a variable defined in the enclosing (outer) function's scope.
# 3. The outer function must return the inner function.

# --- 2. Basic Example of a Closure ---
print("\n--- 2. Basic Example of a Closure ---")

def outer_function(message):
    """
    This is the outer function.
    It takes 'message' as an argument, which becomes part of the closure.
    """
    def inner_function():
        """
        This is the inner (nested) function.
        It refers to 'message' from its enclosing scope.
        """
        print(f"Message from closure: {message}")
    return inner_function # Return the inner function without calling it

# Create instances of the closure
# When make_hello is called, outer_function finishes, but inner_function (now make_hello)
# still 'remembers' the value of 'message' from its creation.
make_hello = outer_function("Hello there!")
make_goodbye = outer_function("Goodbye for now.")

print("\nCalling the closures:")
make_hello()   # Output: Message from closure: Hello there!
make_goodbye() # Output: Message from closure: Goodbye for now.

print(f"\nType of make_hello: {type(make_hello)}")
# You can inspect the closure's free variables (the variables it 'remembers')
print(f"make_hello.__closure__: {make_hello.__closure__}")
if make_hello.__closure__:
    print(f"Value remembered by make_hello: {make_hello.__closure__[0].cell_contents}")


# --- 3. Closures for Creating Function Factories ---
print("\n--- 3. Closures for Creating Function Factories ---")
print("Closures are perfect for creating 'function factories' - functions that generate other functions.")

def make_multiplier(n):
    """
    Returns a function that multiplies its input by 'n'.
    'n' is captured in the closure.
    """
    def multiplier(x):
        return x * n
    return multiplier

# Create specialized multiplier functions
multiply_by_5 = make_multiplier(5)
multiply_by_10 = make_multiplier(10)

print(f"Multiply 7 by 5: {multiply_by_5(7)}")   # 7 * 5 = 35
print(f"Multiply 7 by 10: {multiply_by_10(7)}") # 7 * 10 = 70


# --- 4. Modifying Enclosed Variables using `nonlocal` ---
print("\n--- 4. Modifying Enclosed Variables using `nonlocal` ---")
print("By default, inner functions can *read* variables from the enclosing scope.")
print("To *modify* them, you need to use the `nonlocal` keyword.")

def make_counter():
    count = 0 # This is the variable captured by the closure

    def increment_counter():
        nonlocal count # Declare intent to modify the 'count' from the enclosing scope
        count += 1
        return count
    return increment_counter

counter1 = make_counter()
counter2 = make_counter() # Each call to make_counter creates a new 'count' variable

print(f"\nCounter 1: {counter1()}") # 1
print(f"Counter 1: {counter1()}") # 2
print(f"Counter 2: {counter2()}") # 1 (Independent count for counter2)
print(f"Counter 1: {counter1()}") # 3


# --- 5. Common Use Cases for Closures ---
print("\n--- 5. Common Use Cases for Closures ---")

# 5.1 Callbacks and Event Handlers (e.g., in GUI programming)
# Although we can't run a full GUI here, imagine:
# button.on_click = make_logger("Button A clicked!")
def make_logger(event_name):
    def log_message():
        print(f"LOG: Event '{event_name}' occurred!")
    return log_message

button_a_logger = make_logger("Submit Button Click")
button_b_logger = make_logger("Cancel Button Click")

print("\nSimulating callbacks:")
button_a_logger()
button_b_logger()


# 5.2 Decorators (Closures are fundamental to how decorators work)
print("\n5.2 Decorators (a prime use case for closures):")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"--- Calling {func.__name__} ---")
        result = func(*args, **kwargs) # Call the original function
        print(f"--- Finished {func.__name__} ---")
        return result
    return wrapper

@my_decorator # Syntactic sugar for: say_hello = my_decorator(say_hello)
def say_hello(name):
    print(f"Hello, {name}!")

@my_decorator
def calculate_sum(a, b):
    print(f"Calculating sum of {a} and {b}")
    return a + b

say_hello("World")
sum_result = calculate_sum(10, 20)
print(f"Calculated sum: {sum_result}")

# 5.3 Data Hiding and Encapsulation (mimicking private variables)
print("\n5.3 Data Hiding/Encapsulation:")
def create_bank_account(initial_balance):
    _balance = initial_balance # This variable is effectively "private"

    def get_balance():
        return _balance

    def deposit(amount):
        nonlocal _balance
        _balance += amount
        print(f"Deposited {amount}. New balance: {_balance}")

    def withdraw(amount):
        nonlocal _balance
        if amount <= _balance:
            _balance -= amount
            print(f"Withdrew {amount}. New balance: {_balance}")
        else:
            print(f"Insufficient funds. Balance: {_balance}")

    return {'get_balance': get_balance, 'deposit': deposit, 'withdraw': withdraw}

account = create_bank_account(100)
print(f"Initial balance: {account['get_balance']()}")
account['deposit'](50)
account['withdraw'](70)
account['withdraw'](100)
# print(account._balance) # This would not work, _balance is not directly accessible


# --- 6. The `__closure__` Attribute ---
print("\n--- 6. The `__closure__` Attribute ---")
print("Functions that are closures have a `__closure__` attribute which is a tuple of cells.")
print("Each cell holds the value of a variable from the enclosing scope.")

closure_inspect = make_multiplier(7)
print(f"Closure object: {closure_inspect}")
print(f"__closure__ attribute: {closure_inspect.__closure__}")
if closure_inspect.__closure__:
    print(f"Value remembered by closure: {closure_inspect.__closure__[0].cell_contents}")


# --- 7. Pitfalls: Late Binding of Closures in Loops ---
print("\n--- 7. Pitfalls: Late Binding of Closures in Loops ---")
print("A common mistake is when creating closures in a loop. The inner function captures")
print("the variable, not its *value at the time of creation*, but its *final value* after the loop.")

functions = []
for i in range(3):
    functions.append(lambda: i) # `i` is bound at runtime, after the loop finishes

print("\nDemonstrating late binding issue:")
for f in functions:
    print(f(), end=" ") # All will print the final value of i (which is 2)
print() # New line

# How to fix late binding (using a default argument to capture the value)
fixed_functions = []
for i in range(3):
    fixed_functions.append(lambda x=i: x) # `x=i` binds the current value of `i` to `x` in the lambda's default

print("Demonstrating fixed late binding:")
for f in fixed_functions:
    print(f(), end=" ") # Will print 0 1 2
print()


print("\n--- End of Python Closures Practice Code ---")