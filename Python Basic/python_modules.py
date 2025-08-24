import os # Built-in module for interacting with the operating system
import sys # Built-in module for system-specific parameters and functions

print("--- Python Modules: Practice Code ---")

# --- 1. What is a Module? ---
print("\n--- 1. What is a Module? ---")
print("A Python module is simply a Python file (with a `.py` extension) that contains Python code.")
print("This code can include functions, classes, variables, and even runnable statements.")
print("Modules allow you to organize your code logically, making it more manageable, reusable, and readable.")

# Key Benefits:
# - Reusability: Write code once, use it in multiple programs.
# - Organization: Break down large programs into smaller, manageable files.
# - Namespacing: Prevent name clashes between different parts of your code.


# --- 2. Creating a Simple Module ---
print("\n--- 2. Creating a Simple Module ---")
print("Let's imagine we have a file named `my_utils.py` with the following content:")
print("```python")
print("# my_utils.py")
print("PI = 3.14159")

print("def greet(name):")
print("    return f'Hello, {name} from my_utils!'")

print("def circle_area(radius):")
print("    return PI * radius * radius")

print("class Calculator:")
print("    def add(self, a, b):")
print("        return a + b")

print("    def subtract(self, a, b):")
print("        return a - b")

print("if __name__ == '__main__':")
print("    print('my_utils.py is being run directly!')")
print("    print(f'PI value: {PI}')")
print("```")

# To demonstrate, we'll create this file programmatically:
module_content = """
# my_utils.py
PI = 3.14159

def greet(name):
    return f'Hello, {name} from my_utils!'

def circle_area(radius):
    return PI * radius * radius

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    print('my_utils.py is being run directly!')
    print(f'PI value: {PI}')
"""
module_filename = "my_utils.py"
with open(module_filename, "w") as f:
    f.write(module_content)
print(f"\n'{module_filename}' has been created for demonstration.")


# --- 3. Importing Modules ---
print("\n--- 3. Importing Modules ---")
print("To use the contents of a module, you need to import it.")

# 3.1 `import module_name` (full module import)
print("\n3.1 `import module_name`:")
# This imports the entire module. You access its contents using `module_name.attribute`.
import my_utils
print(f"PI from my_utils: {my_utils.PI}")
print(f"Greeting from my_utils: {my_utils.greet('Alice')}")
print(f"Area of circle (radius 5): {my_utils.circle_area(5)}")
my_calc = my_utils.Calculator()
print(f"5 + 3 using Calculator: {my_calc.add(5, 3)}")


# 3.2 `from module_name import attribute1, attribute2` (selective import)
print("\n3.2 `from module_name import attribute1, attribute2`:")
# This imports specific attributes directly into the current namespace.
# You can use them without the `module_name.` prefix.
from my_utils import PI, greet, Calculator
print(f"PI (directly): {PI}")
print(f"Greeting (directly): {greet('Bob')}")
my_other_calc = Calculator()
print(f"10 - 4 using Calculator: {my_other_calc.subtract(10, 4)}")
# print(circle_area(5)) # This would cause a NameError because circle_area was not explicitly imported.


# 3.3 `import module_name as alias` (aliased import)
print("\n3.3 `import module_name as alias`:")
# This imports the module but gives it a shorter or different name for convenience.
import my_utils as mu
print(f"PI from mu: {mu.PI}")
print(f"Greeting from mu: {mu.greet('Charlie')}")


# 3.4 `from module_name import *` (wildcard import - generally discouraged)
print("\n3.4 `from module_name import *`:")
print("This imports *all* public names from the module into the current namespace.")
print("It can lead to name clashes and make it harder to tell where names came from.")
print("Use with caution, primarily for interactive sessions or when you know the module well.")
from my_utils import * # Suppress warning for example
print(f"PI (* import): {PI}")
print(f"Greeting (* import): {greet('David')}")
# print(circle_area(1)) # This would work too, as it's imported by '*'


# --- 4. Module Search Path (`sys.path`) ---
print("\n--- 4. Module Search Path (`sys.path`) ---")
print("When you `import` a module, Python looks for it in a specific order of directories.")
print("This order is defined in `sys.path`.")

print(f"\nCurrent sys.path (first few entries):")
for i, path in enumerate(sys.path[:5]): # Show first 5 paths
    print(f"  {i}: {path}")

print("\nSearch order:")
print("1. The directory containing the input script (or current directory if interactive).")
print("2. `PYTHONPATH` environment variable (list of directories).")
print("3. Standard library directories (e.g., `site-packages`).")

# You can add directories to `sys.path` at runtime, but it's generally better
# to use environment variables or proper package management for larger projects.
# sys.path.append('/path/to/your/custom_modules')
# import my_custom_module


# --- 5. `__name__` Special Variable ---
print("\n--- 5. `__name__` Special Variable ---")
print("Every Python module has a special built-in variable called `__name__`.")
print("When a script is run directly, `__name__` is set to `'__main__'`. (Check `my_utils.py` output above)")
print("When a script is imported as a module, `__name__` is set to the module's name.")

print(f"__name__ of current script: {__name__}")
print(f"__name__ of imported my_utils: {my_utils.__name__}")

print("\nThis is commonly used to include code that should only run when the script is executed directly:")
print("```python")
print("if __name__ == '__main__':")
print("    # Code to run when script is executed directly")
print("    print('This only runs when the script is not imported.')")
print("```")


# --- 6. Reloading Modules (for development) ---
print("\n--- 6. Reloading Modules (for development) ---")
print("Once a module is imported, it's loaded into memory. If you modify the module's `.py` file,")
print("the imported version won't reflect those changes until you reload it (or restart the interpreter).")
print("Use `import importlib; importlib.reload(module_name)`.")

# Let's modify my_utils.py and reload
with open(module_filename, "a") as f: # Append a new constant
    f.write("\nNEW_CONSTANT = 12345\n")
print(f"\nAppended NEW_CONSTANT to '{module_filename}'.")

# Current `my_utils` object doesn't have NEW_CONSTANT yet
print(f"my_utils.PI (before reload): {my_utils.PI}")
try:
    print(my_utils.NEW_CONSTANT)
except AttributeError as e:
    print(f"Error accessing NEW_CONSTANT before reload: {e}")

import importlib
importlib.reload(my_utils) # Reload the module
print(f"my_utils.PI (after reload, unchanged): {my_utils.PI}") # PI is same
print(f"my_utils.NEW_CONSTANT (after reload): {my_utils.NEW_CONSTANT}") # NEW_CONSTANT is now available


# --- 7. Packages ---
print("\n--- 7. Packages ---")
print("A package is a collection of related modules organized in a directory hierarchy.")
print("A directory becomes a Python package if it contains an `__init__.py` file (even if empty).")
print("This file indicates that the directory should be treated as a package.")

print("\nExample structure:")
print("my_package/")
print("├── __init__.py")
print("├── module_a.py")
print("└── sub_package/")
print("    ├── __init__.py")
print("    └── module_b.py")

print("\nImporting from packages:")
print("`import my_package.module_a`")
print("`from my_package.sub_package import module_b`")
print("`from my_package.module_a import some_function`")


# --- 8. Cleaning Up ---
# Remove the created module file
os.remove(module_filename)
print(f"\nCleaned up: Removed '{module_filename}'.")

print("\n--- End of Python Modules Practice Code ---")