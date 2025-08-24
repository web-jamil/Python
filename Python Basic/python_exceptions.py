import sys # For demonstrating sys.exc_info()

print("--- Python Exceptions: Practice Code ---")

# --- 1. What are Exceptions? ---
print("\n--- 1. What are Exceptions? ---")
print("Exceptions are events that disrupt the normal flow of a program.")
print("They are objects that are 'raised' when an error or exceptional condition occurs.")
print("Instead of crashing the program, Python's exception handling mechanism allows you to 'catch' and respond to these events.")

# Common Built-in Exceptions (just a few examples):
# - `NameError`: Trying to use an undefined variable.
# - `TypeError`: Operation on an inappropriate type (e.g., adding string to int).
# - `ValueError`: Operation on a correct type but with an inappropriate value (e.g., int('abc')).
# - `IndexError`: Accessing a list index out of range.
# - `KeyError`: Accessing a dictionary key that doesn't exist.
# - `FileNotFoundError`: Trying to open a non-existent file.
# - `ZeroDivisionError`: Division by zero.
# - `AttributeError`: Trying to access a non-existent attribute of an object.


# --- 2. Handling Exceptions: `try`, `except`, `else`, `finally` ---
print("\n--- 2. Handling Exceptions: `try`, `except`, `else`, `finally` ---")
print("This block structure is used to gracefully manage exceptions.")

# 2.1 `try` and `except`
print("\n2.1 `try` and `except`:")
print(" - The `try` block contains code that might raise an exception.")
print(" - The `except` block catches and handles specific exceptions.")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid types for division. Please use numbers.")
    except Exception as e: # Catch any other unexpected error (broad except - use with caution!)
        print(f"An unexpected error occurred: {e}")
    print("--- End of safe_divide function ---")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "2")
safe_divide([1, 2], 3) # Example of another unexpected error (TypeError initially caught)


# 2.2 Multiple `except` blocks
print("\n2.2 Multiple `except` blocks:")
# As shown above, you can have multiple `except` blocks.
# Python checks them in order, from top to bottom. The first matching `except` block is executed.
# More specific exceptions should be listed before more general ones.

def get_list_element(my_list, index):
    try:
        value = my_list[index]
        print(f"Element at index {index}: {value}")
    except IndexError:
        print(f"Error: Index {index} is out of range for list of size {len(my_list)}.")
    except TypeError:
        print("Error: The index must be an integer.")
    print("--- End of get_list_element function ---")

my_list = [10, 20, 30]
get_list_element(my_list, 1)
get_list_element(my_list, 5)
get_list_element(my_list, "a")


# 2.3 `except` without specifying exception (discouraged)
print("\n2.3 `except` without specifying exception (highly discouraged):")
print("`except:` will catch *all* exceptions, including keyboard interrupts (`Ctrl+C`), `SystemExit`, etc.")
print("This can mask real problems and make debugging extremely difficult.")
try:
    x = 1 / 0
except: # Catches ZeroDivisionError, but also anything else
    print("An unknown error occurred (caught by generic except).")

# 2.4 `except Exception as e` (preferred general catch)
print("\n2.4 `except Exception as e` (preferred general catch):")
print("This catches all *non-system-exiting* exceptions. It's generally better than a bare `except`.")
try:
    value = int("hello") # ValueError
except Exception as e:
    print(f"Caught a general Exception: {e} (Type: {type(e).__name__})")


# 2.5 `else` block
print("\n2.5 `else` block:")
print("The `else` block executes only if no exception occurred in the `try` block.")

def process_input(user_input):
    try:
        number = int(user_input)
    except ValueError:
        print(f"'{user_input}' is not a valid integer.")
    else:
        print(f"Successfully converted '{user_input}' to integer: {number}. Proceeding...")
        print(f"Doubled value: {number * 2}")

process_input("123")
process_input("abc")


# 2.6 `finally` block
print("\n2.6 `finally` block:")
print("The `finally` block always executes, regardless of whether an exception occurred or not.")
print("It's typically used for cleanup operations (e.g., closing files, releasing resources).")

def file_operation(filename, mode):
    f = None # Initialize to None
    try:
        f = open(filename, mode)
        f.write("Hello, world!\n")
        print(f"Successfully wrote to {filename}.")
    except IOError as e:
        print(f"Error accessing file {filename}: {e}")
    finally:
        if f: # Ensure f is not None before trying to close
            f.close()
            print(f"File {filename} closed in finally block.")
        else:
            print("File was not opened, so nothing to close.")

# Create a dummy file for success case
with open("test_file.txt", "w") as f:
    f.write("")
file_operation("test_file.txt", "w") # Success case
file_operation("non_existent_dir/bad_file.txt", "w") # Error case
# Clean up dummy file
import os
os.remove("test_file.txt")


# --- 3. Raising Exceptions (`raise`) ---
print("\n--- 3. Raising Exceptions (`raise`) ---")
print("You can explicitly raise an exception using the `raise` keyword.")
print("This is useful when your code detects an error condition it cannot handle.")

def check_positive(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number.")
    if num <= 0:
        raise ValueError("Number must be positive.")
    return f"Number {num} is positive."

print("\nRaising exceptions:")
print(check_positive(5))
try:
    check_positive(-3)
except ValueError as e:
    print(f"Caught expected error: {e}")
try:
    check_positive("hello")
except TypeError as e:
    print(f"Caught expected error: {e}")

# Re-raising an exception: You can catch an exception, do something, and then re-raise it.
def re_raise_example():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print("Performing some logging or cleanup before re-raising.")
        raise # Re-raises the same exception

try:
    re_raise_example()
except ZeroDivisionError:
    print("Caught ZeroDivisionError again after re-raise.")


# --- 4. Custom Exceptions ---
print("\n--- 4. Custom Exceptions ---")
print("You can define your own custom exception classes by inheriting from `Exception` (or a more specific built-in exception).")
print("This helps make your error messages more specific and your code easier to debug.")

class InvalidTemperatureError(Exception):
    """Custom exception raised when a temperature is outside valid range."""
    def __init__(self, temperature, message="Temperature out of valid range (0-100)"):
        self.temperature = temperature
        self.message = f"{message}: {temperature}"
        super().__init__(self.message)

def set_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number.")
    if not 0 <= temp <= 100:
        raise InvalidTemperatureError(temp)
    print(f"Temperature set to: {temp}°C")

print("\nUsing custom exceptions:")
set_temperature(25)
try:
    set_temperature(120)
except InvalidTemperatureError as e:
    print(f"Caught custom exception: {e.message}, provided temp: {e.temperature}")
try:
    set_temperature(-5)
except InvalidTemperatureError as e:
    print(f"Caught custom exception: {e.message}, provided temp: {e.temperature}")


# --- 5. Inspecting Exceptions (`sys.exc_info()`) ---
print("\n--- 5. Inspecting Exceptions (`sys.exc_info()`) ---")
print("`sys.exc_info()` returns a tuple containing information about the exception being handled:")
print("`(type, value, traceback)`.")

try:
    1 / 0
except: # Catch any exception to demonstrate
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"\nException Type: {exc_type.__name__}")
    print(f"Exception Value: {exc_value}")
    # Traceback object provides detailed call stack info.
    # print(f"Exception Traceback: {exc_traceback}") # Uncomment to see full traceback object

# --- 6. Best Practices ---
print("\n--- 6. Best Practices ---")
print("- **Be Specific:** Catch specific exceptions rather than using a bare `except` or `except Exception` unless absolutely necessary (e.g., for a top-level error handler).")
print("- **Handle Gracefully:** Provide meaningful error messages to the user or log them for debugging.")
print("- **Cleanup with `finally`:** Use `finally` for resource cleanup (files, network connections).")
print("- **Raise Early, Handle Late:** Raise exceptions as soon as an invalid state is detected, but handle them at a level where you can actually recover or provide useful information.")
print("- **Custom Exceptions:** Define custom exceptions for domain-specific errors to improve clarity and maintainability.")
print("- **Avoid 'Pass' in `except`:** Never use `pass` in an `except` block without a very clear reason, as it swallows errors silently.")


print("\n--- End of Python Exceptions Practice Code ---")