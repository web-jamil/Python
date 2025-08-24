# --- NameError: All About in Code ---

# A NameError is raised when you try to use a variable, function, class, or module
# name that has not been defined or is not in the current scope.

# --- 1. Basic NameError: Undefined Variable ---
print("--- 1. Basic NameError: Undefined Variable ---")

try:
    print(undefined_variable) # 'undefined_variable' has not been assigned a value
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'undefined_variable' is not defined in this scope.")

print("-" * 50 + "\n")


# --- 2. NameError: Typo in Variable Name ---
print("--- 2. NameError: Typo in Variable Name ---")

correct_variable_name = "I am defined"
try:
    print(corrrect_variable_name) # Typo: 'corrrect_variable_name' instead of 'correct_variable_name'
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'corrrect_variable_name' is not defined.")

print("-" * 50 + "\n")


# --- 3. NameError: Using a Variable Before Assignment ---
print("--- 3. NameError: Using a Variable Before Assignment ---")

# Python executes code top-to-bottom. A variable must be assigned a value
# before it can be used.

try:
    value = another_value + 10 # 'another_value' is not yet assigned
    another_value = 5
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'another_value' is referenced before assignment.")

# Correct way:
correct_value = 5
new_value = correct_value + 10
print(f"Correct assignment and usage: {new_value}")

print("-" * 50 + "\n")


# --- 4. NameError: Scope Issues (Local vs Global) ---
print("--- 4. NameError: Scope Issues (Local vs Global) ---")

global_var = "I am global"

def function_scope_example():
    # local_var is defined only within this function
    local_var = "I am local"
    print(f"Inside function: global_var = {global_var}") # Can access global_var

    try:
        # This will raise a NameError because 'another_local_var' is defined
        # AFTER its usage within the function scope.
        print(another_local_var)
        another_local_var = "hello"
    except NameError as e:
        print(f"  Caught NameError inside function (expected): {e}")
        print("  Reason: 'another_local_var' referenced before assignment in local scope.")

function_scope_example()

try:
    print(local_var) # local_var is not accessible outside 'function_scope_example'
except NameError as e:
    print(f"Caught NameError outside function (expected): {e}")
    print("Reason: 'local_var' is not defined in the global scope.")

# Using `global` keyword to modify a global variable inside a function
global_counter = 0
def increment_global():
    global global_counter # Declare intent to modify the global variable
    global_counter += 1
    print(f"Inside increment_global: global_counter = {global_counter}")

increment_global()
print(f"Outside function: global_counter = {global_counter}")

print("-" * 50 + "\n")


# --- 5. NameError: Unimported Module or Incorrect Import ---
print("--- 5. NameError: Unimported Module or Incorrect Import ---")

# Attempting to use a module's function without importing the module
try:
    requests.get("http://example.com") # 'requests' module not imported
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'requests' is not defined.")

# Correct way to import and use:
import json # Correctly importing the 'json' module
data = {'key': 'value'}
json_string = json.dumps(data)
print(f"Used imported module 'json': {json_string}")

# Using a function from a module that wasn't imported with `from ... import ...`
try:
    dumps({'a':1}) # 'dumps' is part of 'json' module, not directly in global scope
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'dumps' is not defined.")

# Correct way to import specific function:
from json import loads # Importing 'loads' directly into the current scope
json_string_to_load = '{"status": "ok"}'
loaded_data = loads(json_string_to_load)
print(f"Used directly imported function 'loads': {loaded_data}")

print("-" * 50 + "\n")


# --- 6. NameError: Class or Function Not Defined Yet ---
print("--- 6. NameError: Class or Function Not Defined Yet ---")

# Similar to variables, classes and functions must be defined before they are called.

try:
    my_instance = MyUndefinedClass() # 'MyUndefinedClass' is not yet defined
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'MyUndefinedClass' is not defined.")

class MyDefinedClass:
    def __init__(self):
        print("MyDefinedClass instance created.")

defined_instance = MyDefinedClass() # Now it works

try:
    call_undefined_function() # 'call_undefined_function' is not yet defined
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'call_undefined_function' is not defined.")

def call_defined_function():
    print("Function called successfully.")

call_defined_function() # Now it works

print("-" * 50 + "\n")


# --- 7. NameError in List Comprehensions / Generator Expressions ---
print("--- 7. NameError in List Comprehensions / Generator Expressions ---")

# Variables defined within a list comprehension are local to that comprehension.
try:
    # 'x' is defined within the list comprehension's scope, not outside
    my_list = [x * 2 for x in range(5)]
    print(f"List: {my_list}")
    print(x) # x is not accessible here
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'x' is not defined outside the comprehension.")

print("-" * 50 + "\n")


# --- 8. NameError with `del` keyword ---
print("--- 8. NameError with `del` keyword ---")

# The `del` keyword removes a name binding from the local or global namespace.
# After `del`, trying to use the name will result in a NameError.

variable_to_delete = "I exist"
print(f"Before del: {variable_to_delete}")

del variable_to_delete
try:
    print(variable_to_delete) # This name is now unbound
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'variable_to_delete' is not defined after `del`.")

# Deleting a non-existent name also raises NameError
try:
    del non_existent_name
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: name 'non_existent_name' is not defined and cannot be deleted.")

print("-" * 50 + "\n")


# --- 9. Common Troubleshooting Tips for NameError ---
print("--- 9. Common Troubleshooting Tips for NameError ---")

# 9.1 Check for typos in variable/function/class names.
# 9.2 Ensure variables are assigned a value before being used.
# 9.3 Verify imports: Is the module imported? Is the specific item imported with 'from ... import ...'?
# 9.4 Understand variable scope: Is the name accessible in the current part of the code?
#     (e.g., local variables in functions are not accessible globally).
# 9.5 If using a name from an outer (non-global) scope in a nested function,
#     ensure it's not being implicitly treated as a new local variable if assigned to.
#     (Use `nonlocal` for modifying variables in enclosing scopes, not global.)

print("--- End of NameError demonstration ---")




# --- NameError: More Examples (Continued) ---

# This section expands on NameError scenarios, particularly focusing on less obvious
# cases, interactions with loops, conditionals, and more complex imports.

# --- 10. NameError in Conditional Blocks (if/else) ---
print("--- 10. NameError in Conditional Blocks (if/else) ---")

# A variable defined only within one branch of an if/else statement
# will cause a NameError if accessed outside that branch AND the branch was not executed.

is_debug_mode = False
# is_debug_mode = True # Uncomment to see the 'else' block cause NameError

if is_debug_mode:
    config_message = "Running in debug mode."
else:
    print("Not in debug mode.")
    # config_message is NOT defined in this branch

try:
    print(config_message) # This will raise NameError if is_debug_mode is False
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'config_message' was not defined in the executed 'else' branch.")

# Correct way to handle: Ensure variable is always initialized or check for its existence.
another_config_message = None # Initialize to None or a default
if is_debug_mode:
    another_config_message = "Running in debug mode (initialized)."
else:
    another_config_message = "Not in debug mode (initialized)."
print(another_config_message)

print("-" * 50 + "\n")


# --- 11. NameError in Loops (for/while) ---
print("--- 11. NameError in Loops (for/while) ---")

# Variables defined within a loop's scope are generally accessible *after* the loop
# for their last assigned value. However, if the loop never runs, the variable might not be defined.

# Example 1: Variable defined inside a 'for' loop, accessed after (OK)
items = [1, 2, 3]
for item in items:
    last_processed_item = item * 2
    print(f"Processing item: {item}")
print(f"Last processed item outside loop: {last_processed_item}") # Accessible

# Example 2: Variable defined inside 'for' loop, but loop never runs
empty_items = []
try:
    for item in empty_items:
        never_defined_var = item * 2 # This line never executes
    print(f"Never defined var: {never_defined_var}") # Will cause NameError
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'never_defined_var' was never assigned because the loop didn't run.")

# Example 3: Variable defined inside a 'while' loop, accessed after (OK if loop runs)
counter = 0
while counter < 2:
    loop_var = f"Loop {counter}"
    print(loop_var)
    counter += 1
print(f"Loop var after loop: {loop_var}")

# Example 4: Variable defined inside 'while' loop, but loop condition is initially false
start = 5
try:
    while start < 5: # This loop never runs
        while_loop_var = "Inside while"
    print(f"While loop var: {while_loop_var}") # Will cause NameError
except NameError as e:
    print(f"Caught NameError (expected): {e}")
    print("Reason: 'while_loop_var' was never assigned because the loop didn't run.")

print("-" * 50 + "\n")


# --- 12. NameError Due to Circular Imports (Advanced) ---
print("--- 12. NameError Due to Circular Imports (Advanced) ---")

# Circular imports occur when two or more modules directly or indirectly
# import each other. This can lead to NameErrors if a module tries to
# access an object from an importing module before that object is fully defined.

# To demonstrate, we'll create temporary files.
# File 1: module_a.py
# from module_b import func_b # This line can cause issues
# def func_a():
#     print("Inside func_a")
#     func_b() # Tries to call func_b which might not be fully loaded yet

# File 2: module_b.py
# from module_a import func_a # This creates a circular dependency
# def func_b():
#     print("Inside func_b")
#     func_a()

# In the current interactive environment, we can simulate this by
# defining classes/functions in a specific order that causes forward-referencing.

# This example simulates a forward reference that would cause NameError
# if ModuleB tried to use 'ClassA' before 'ClassA' was fully defined.
# (Actual circular import issues are more subtle and depend on execution order)

# Simulate module_a.py content:
class ClassA:
    def __init__(self):
        print("ClassA initialized")
    def call_b(self):
        # If ClassB wasn't fully defined yet, this might fail
        # This is more likely with 'from module_b import ClassB' at top
        try:
            instance_b = ClassB() # Reference to ClassB
            instance_b.method_b()
        except NameError as e:
            print(f"  Caught NameError during ClassA.call_b (simulated circularity): {e}")
            print("  Reason: 'ClassB' might not be fully defined/imported yet in a circular scenario.")
        except Exception as e:
            print(f"  Caught other error in ClassA.call_b: {e}")

# Simulate module_b.py content (if it imported ClassA at the top):
# from module_a import ClassA # If this was at the top of a file with ClassB,
#                             # and ClassA referenced ClassB, it's a loop.
class ClassB:
    def __init__(self):
        print("ClassB initialized")
    def method_b(self):
        print("Method B from ClassB")
        # In a circular import, if we tried to call ClassA.call_a() here,
        # and ClassA was still being defined, it could fail.

# Now test the interaction:
print("Testing simulated circular import (NameError if not fully defined):")
# First define ClassA, then ClassB. This order works fine in a single file.
# The NameError occurs when a module tries to access a name from *another*
# module that is still in the process of being defined due to import order.

instance_a = ClassA()
instance_a.call_b() # This works because ClassB is now fully defined.
# If ClassB was imported at the top of a file, and its definition depended
# on ClassA, and ClassA then tried to use ClassB, it would be an issue.

print("Circular import issues are complex; this is a simplified illustration.")
print("-" * 50 + "\n")


# --- 13. NameError in Unreachable Code (Less Common) ---
print("--- 13. NameError in Unreachable Code (Less Common) ---")

# Sometimes, a NameError can exist in code that might never be executed,
# but if the interpreter *parses* it, it might still raise an error at load time.
# However, Python's NameError is mostly a runtime error.

def will_not_be_called():
    print(non_existent_name_here) # This line will not be executed

# No NameError at this point because the function is only defined, not called.
print("Function 'will_not_be_called' is defined but not called, no NameError yet.")

try:
    if False: # This block is never entered
        print(another_undefined_var) # This line is never reached
    print("The 'if False' block with NameError inside did NOT raise an error upon parsing.")
except NameError as e:
    print(f"Caught NameError (unexpectedly, as it should be unreachable): {e}")
    # This specifically would NOT raise NameError at *definition* time.
    # NameError happens when the line is *executed*.

# Only when explicitly called will the NameError surface
try:
    will_not_be_called()
except NameError as e:
    print(f"Caught NameError when 'will_not_be_called' was called: {e}")

print("-" * 50 + "\n")

print("--- End of NameError (More Examples) ---")
