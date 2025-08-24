# --- 1. Class for Demonstrating Basic NameError Scenarios ---
class NameErrorBasics:
    def __init__(self):
        self.instance_attribute = "Hello"

    def demonstrate_undefined_variable(self):
        print("\n--- 1. Class: Undefined Variable NameError ---")
        try:
            # Attempt to use a variable that has not been defined in this method's scope
            print(f"  Attempting to print `non_existent_var`...")
            print(non_existent_var)
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `non_existent_var` was never assigned a value or defined.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  Undefined variable demonstration finished.")

    def demonstrate_undefined_method_call(self):
        print("\n--- 1. Class: Undefined Method Call NameError ---")
        try:
            # Attempt to call a function/method that isn't defined or isn't a method of self
            print(f"  Attempting to call `undefined_func_or_method()`...")
            undefined_func_or_method()
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `undefined_func_or_method` is not a known global function or local variable.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  Undefined method call demonstration finished.")

    def run_all_basic_demos(self):
        self.demonstrate_undefined_variable()
        self.demonstrate_undefined_method_call()


# --- 2. Class for Demonstrating Scope-Related NameErrors ---
class ScopeNameErrorDemo:
    global_class_var = "I am a class-level variable."

    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.instance_var = f"Instance var for {instance_id}."

    def method_with_local_scope(self):
        local_var = "I am a local variable inside method_with_local_scope."
        print(f"\n--- 2. Class: Scope - Inside method_with_local_scope() ---")
        print(f"  Accessing local_var: '{local_var}'")
        print(f"  Accessing instance_var: '{self.instance_var}'")
        print(f"  Accessing class_level_var via self: '{self.global_class_var}'")
        print(f"  Accessing class_level_var via class: '{ScopeNameErrorDemo.global_class_var}'")
        
        # This creates a NEW local variable named global_class_var, it does NOT modify the class variable
        # global_class_var = "This is a new local variable, not the class one!" 
        # print(f"  New local 'global_class_var': '{global_class_var}'")

    def demonstrate_scope_errors(self):
        print(f"\n--- 2. Class: Scope-Related NameErrors for '{self.instance_id}' ---")
        
        self.method_with_local_scope()
        
        # Attempt to access `local_var` from `method_with_local_scope`
        try:
            print(f"\n  Attempting to access `local_var` outside its method...")
            print(local_var) # This will raise NameError
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `local_var` is local to `method_with_local_scope` and not accessible here.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

        # Attempt to access `self.instance_var` directly as `instance_var`
        try:
            print(f"\n  Attempting to access `instance_var` without `self.` prefix...")
            print(instance_var) # This will raise NameError
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `instance_var` is an instance attribute and must be accessed via `self.instance_var`.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  Scope-related NameError demonstration finished.")


# --- 3. Class for Demonstrating NameError with Modules and `del` ---
import os # This import makes 'os' available

class ModuleAndDelNameErrorDemo:
    def demonstrate_missing_module_import(self):
        print("\n--- 3. Class: Missing Module Import NameError ---")
        try:
            # Attempt to use a module that hasn't been imported
            print(f"  Attempting to use `sys_path` from unimported `sys` module...")
            print(sys_path) # Assumes 'sys' module is not globally imported here
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `sys_path` or `sys` itself is not defined/imported.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  Missing module import demonstration finished.")

    def demonstrate_module_member_name_error(self):
        print("\n--- 3. Class: Module Member NameError ---")
        try:
            # `os` is imported at the top of the file, so it's available.
            print(f"  Attempting to call `os.get_current_dir()` (typo for `os.getcwd()`)...")
            os.get_current_dir() # This will raise AttributeError, not NameError
        except NameError as e: # This block will NOT be executed for a non-existent method
            print(f"  [CAUGHT ERROR - UNEXPECTED] NameError: {e}")
        except AttributeError as e:
            print(f"  [CAUGHT ERROR] AttributeError: {e}")
            print("  Explanation: `get_current_dir` is not an attribute/method of the `os` module.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  Module member NameError demonstration finished.")

    def demonstrate_del_keyword_name_error(self):
        print("\n--- 3. Class: `del` Keyword NameError ---")
        my_data = "Some important data."
        print(f"  `my_data` before `del`: '{my_data}'")
        
        del my_data # Remove the name `my_data` from the current namespace
        print(f"  `my_data` has been deleted from the current scope.")

        try:
            print(f"  Attempting to print `my_data` after `del`...")
            print(my_data)
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `my_data` no longer exists in this scope after `del`.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print("  `del` keyword NameError demonstration finished.")

    def run_all_module_and_del_demos(self):
        self.demonstrate_missing_module_import()
        self.demonstrate_module_member_name_error()
        self.demonstrate_del_keyword_name_error()

# --- Main Execution Block ---
if __name__ == "__main__":
    
    # Run basic NameError demos
    basic_demos = NameErrorBasics()
    basic_demos.run_all_basic_demos()
    
    input("\nPress Enter to run the next example: Scope-related NameErrors...")
    
    # Run scope-related NameError demos
    scope_demo_instance = ScopeNameErrorDemo("main_instance")
    scope_demo_instance.demonstrate_scope_errors()
    
    input("\nPress Enter to run the next example: Module and `del` NameErrors...")

    # Run module and `del` NameError demos
    module_del_demos = ModuleAndDelNameErrorDemo()
    module_del_demos.run_all_module_and_del_demos()

    print("\nAll Python NameError demonstrations using classes concluded.")


# --- 1. Basic NameError: Undefined Variable ---

def demonstrate_undefined_variable_function():
    print("\n--- 1. Function: Undefined Variable NameError ---")
    try:
        # Attempt to access a variable that has not been assigned a value
        print(f"  Attempting to print `undefined_variable`...")
        print(undefined_variable)
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: `undefined_variable` was used before it was assigned a value.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Undefined variable demonstration finished.")

# --- 2. Basic NameError: Undefined Function Call ---

def demonstrate_undefined_function_call_function():
    print("\n--- 2. Function: Undefined Function Call NameError ---")
    try:
        # Attempt to call a function that has not been defined in the global scope
        print(f"  Attempting to call `non_existent_function()`...")
        non_existent_function()
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: `non_existent_function` was called but is not defined.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Undefined function call demonstration finished.")

# --- 3. NameError due to Scope Issues (Local vs. Enclosing vs. Global) ---

global_scope_var = "I am a global variable."

def outer_function():
    enclosing_scope_var = "I am an enclosing scope variable."

    def inner_function():
        local_scope_var = "I am a local variable inside inner_function."
        print(f"\n--- 3. Function: Scope - Inside inner_function() ---")
        print(f"  Accessing local_scope_var: '{local_scope_var}'")
        print(f"  Accessing enclosing_scope_var: '{enclosing_scope_var}'") # Accessible from inner
        print(f"  Accessing global_scope_var: '{global_scope_var}'") # Accessible from inner

        try:
            print(f"  Attempting to access `another_local_var` (undefined here)...")
            print(another_local_var) # This would be a NameError if it wasn't defined
        except NameError as e:
            print(f"  [CAUGHT ERROR] NameError: {e}")
            print("  Explanation: `another_local_var` is not defined in this (inner) scope.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    inner_function() # Call the inner function

    # Attempt to access `local_scope_var` from `inner_function`
    try:
        print(f"\n--- 3. Function: Scope - Inside outer_function() ---")
        print(f"  Attempting to access `local_scope_var` from `inner_function`...")
        print(local_scope_var) # This will raise NameError
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: `local_scope_var` is local to `inner_function` and not accessible here.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

def demonstrate_scope_name_error_function():
    outer_function()
    
    # Attempt to access `enclosing_scope_var` from `outer_function`
    try:
        print(f"\n--- 3. Function: Scope - Outside outer_function() ---")
        print(f"  Attempting to access `enclosing_scope_var` from `outer_function`...")
        print(enclosing_scope_var) # This will raise NameError
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: `enclosing_scope_var` is local to `outer_function` and not accessible here.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    
    # Global variable is accessible
    print(f"  Accessing global_scope_var: '{global_scope_var}'")
    
    print("  Scope NameError demonstration finished.")

# --- 4. NameError with Module Imports and Missing Module Members ---

def demonstrate_module_import_name_error_function():
    print("\n--- 4. Function: Module Import NameError ---")
    try:
        # Attempt to use a module that hasn't been imported
        print(f"  Attempting to use a function from unimported `sys` module, e.g., `sys.version`...")
        print(sys.version) # `sys` is not imported here
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: The `sys` module was not imported before use.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    
    # Now, import the module correctly
    import os # `os` module is now available in this function's scope (or global if imported outside)
    print(f"  Successfully imported `os` module. Current working directory: {os.getcwd()}")

    try:
        # Correct module, but incorrect member name
        print(f"  Attempting to call `os.get_current_directory()` (typo for `os.getcwd()`)...")
        os.get_current_directory() # This will raise AttributeError, not NameError
    except NameError as e: # This block will NOT be executed for a non-existent method
        print(f"  [CAUGHT ERROR - UNEXPECTED] NameError: {e}")
    except AttributeError as e:
        print(f"  [CAUGHT ERROR] AttributeError: {e}")
        print("  Explanation: `get_current_directory` is not a defined function within the `os` module.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Module import and member NameError demonstration finished.")

# --- 5. NameError with `del` Keyword ---

def demonstrate_del_keyword_name_error_function():
    print("\n--- 5. Function: `del` Keyword NameError ---")
    
    my_data = "This variable exists."
    print(f"  `my_data` before `del`: '{my_data}'")
    
    del my_data # Deletes the name `my_data` from the current namespace
    print(f"  The name `my_data` has been removed from the current scope.")

    try:
        print(f"  Attempting to print `my_data` after `del`...")
        print(my_data)
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: `my_data` no longer refers to anything in this scope after `del`.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  `del` keyword NameError demonstration finished.")

# --- 6. NameError and Variable Shadowing ---

# global_var = 10 # Defined globally

def variable_shadowing_name_error_function():
    print("\n--- 6. Function: Variable Shadowing NameError ---")
    
    # If a variable is assigned within a function, it becomes local to that function.
    # It "shadows" any global variable of the same name.
    
    x = 100 # This 'x' is local to this function
    
    def inner_shadowing_func():
        # This 'x' is local to inner_shadowing_func, it shadows the 'x' in the outer function
        # and any potential global 'x'.
        x = 200 
        print(f"  Inside inner_shadowing_func: x = {x}")
        # If we uncomment this, it would be a NameError if no 'y' existed
        # print(y) 
    
    inner_shadowing_func()
    print(f"  Outside inner_shadowing_func (but inside variable_shadowing_name_error_function): x = {x}")

    # Now, try to use a name from an inner scope
    try:
        print(f"  Attempting to access `inner_shadowing_func_local_x` (hypothetical, undefined here)...")
        # This would be a NameError if `inner_shadowing_func_local_x` was a variable
        # defined ONLY inside `inner_shadowing_func`
        print(inner_shadowing_func_local_x) 
    except NameError as e:
        print(f"  [CAUGHT ERROR] NameError: {e}")
        print("  Explanation: Variables defined in inner functions are not accessible in outer functions.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Variable shadowing NameError demonstration finished.")

# --- Main Execution Block ---
if __name__ == "__main__":
    
    demonstrate_undefined_variable_function()
    input("\nPress Enter to run the next example...")
    
    demonstrate_undefined_function_call_function()
    input("\nPress Enter to run the next example...")
    
    demonstrate_scope_name_error_function()
    input("\nPress Enter to run the next example...")
    
    demonstrate_module_import_name_error_function()
    input("\nPress Enter to run the next example...")
    
    demonstrate_del_keyword_name_error_function()
    input("\nPress Enter to run the next example...")

    variable_shadowing_name_error_function()
    
    print("\nAll Python NameError demonstrations using functions concluded.")