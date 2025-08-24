# --- 1. Basic NameError: Undefined Variable ---

def basic_name_error_variable():
    print("\n--- 1. Basic NameError: Undefined Variable ---")
    try:
        # Attempt to access a variable that has not been assigned a value
        print(f"  Attempting to print undefined_variable...")
        print(undefined_variable)
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'undefined_variable' was used before it was assigned a value.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Basic NameError (variable) example finished.")

# --- 2. NameError: Undefined Function ---

def basic_name_error_function():
    print("\n--- 2. Basic NameError: Undefined Function ---")
    try:
        # Attempt to call a function that has not been defined
        print(f"  Attempting to call non_existent_function()...")
        non_existent_function()
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'non_existent_function' was called but is not defined.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Basic NameError (function) example finished.")

# --- 3. NameError due to Scope Issues (Local vs. Global) ---

global_value = 10

def scope_name_error():
    print("\n--- 3. NameError due to Scope Issues ---")
    local_value = 20
    
    try:
        # This will work, local_value is in scope
        print(f"  Inside function: local_value = {local_value}")
        # This will work, global_value is accessible from inside function
        print(f"  Inside function: global_value = {global_value}")
    except NameError as e: # This won't be caught here but if variables were not defined
        print(f"  [CAUGHT ERROR - UNEXPECTED IN THIS BLOCK] NameError: {e}")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    
    print("  Exiting scope_name_error function...")

def demonstrate_scope_name_error():
    scope_name_error()
    try:
        # Attempt to access local_value outside its function scope
        print(f"  Outside function: Attempting to print local_value...")
        print(local_value) # This line will raise NameError
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'local_value' is local to 'scope_name_error' and not accessible here.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    
    try:
        # global_value is accessible
        print(f"  Outside function: global_value = {global_value}")
    except NameError as e:
        print(f"  [CAUGHT ERROR - UNEXPECTED] NameError: {e}")
    finally:
        print("  Scope NameError example finished.")

# --- 4. NameError with Module Imports ---

def module_name_error():
    print("\n--- 4. NameError with Module Imports ---")
    try:
        # Attempt to use a module that wasn't imported or has a typo
        print(f"  Attempting to use a function from non_existent_module...")
        non_existent_module.some_function()
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'non_existent_module' was not imported or is misspelled.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    
    try:
        # Correct import
        import os
        print(f"  Successfully imported 'os' module. Current working directory: {os.getcwd()}")
        # Incorrect name for an imported module's function
        print(f"  Attempting to call an incorrect function name from 'os'...")
        os.get_current_directory() # Correct is os.getcwd()
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'get_current_directory' is not a defined function within the 'os' module.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Module NameError example finished.")

# --- 5. NameError in Classes (Methods and Attributes) ---

class MyClass:
    def __init__(self, value):
        self.instance_attribute = value

    def display_value(self):
        print(f"  Instance attribute: {self.instance_attribute}")
        
    def call_undefined_method(self):
        print(f"  Attempting to call an undefined method from inside the class...")
        self.non_existent_method_in_class() # This will raise AttributeError, not NameError
        # NameError would occur if "self" itself wasn't defined (e.g., calling a method outside an instance)

def class_name_error():
    print("\n--- 5. NameError in Classes ---")
    
    my_instance = MyClass(100)
    my_instance.display_value()

    try:
        print(f"  Attempting to access a non-existent attribute...")
        print(my_instance.non_existent_attribute) # This will raise AttributeError
    except NameError as e: # This block will NOT be executed
        print(f"  [CAUGHT ERROR - UNEXPECTED] NameError: {e}")
    except AttributeError as e:
        print(f"  [CAUGHT ERROR] AttributeError: {e}")
        print("  Explanation: Accessing a non-existent attribute on an object raises AttributeError, not NameError.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    try:
        my_instance.call_undefined_method()
    except AttributeError as e:
        print(f"  [CAUGHT ERROR] AttributeError: {e}")
        print("  Explanation: Calling a non-existent method on an object raises AttributeError, not NameError.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    # NameError when trying to use class name before definition (rare in simple scripts)
    # class MyOtherClass: ...  then `MyOtherClass()`
    try:
        # Example of a NameError related to classes:
        # If SomeUndefinedClass was used before it was defined.
        print(f"  Attempting to instantiate an undefined class...")
        obj = SomeUndefinedClass()
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'SomeUndefinedClass' was used before its definition.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Class NameError example finished.")


# --- 6. NameError and `del` keyword ---

def del_name_error():
    print("\n--- 6. NameError and `del` keyword ---")
    
    my_variable = "Hello"
    print(f"  my_variable before del: {my_variable}")
    
    del my_variable # Deletes the name 'my_variable' from the current scope
    print(f"  'my_variable' has been deleted.")

    try:
        print(f"  Attempting to print my_variable after del...")
        print(my_variable)
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: 'my_variable' no longer exists in this scope after 'del'.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  `del` NameError example finished.")


# --- Main Execution Block ---
if __name__ == "__main__":
    basic_name_error_variable()
    input("\nPress Enter to run the next example...")
    
    basic_name_error_function()
    input("\nPress Enter to run the next example...")
    
    demonstrate_scope_name_error()
    input("\nPress Enter to run the next example...")
    
    module_name_error()
    input("\nPress Enter to run the next example...")

    class_name_error()
    input("\nPress Enter to run the next example...")
    
    del_name_error()
    
    print("\nAll Python 'Reference Error' (NameError) demonstrations concluded.")