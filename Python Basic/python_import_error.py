# --- ImportError: All About in Code ---

# An ImportError is raised when a module, or a name within a module,
# cannot be loaded. This typically means the Python interpreter couldn't find
# what it was asked to import.

# ImportError is the base class for `ModuleNotFoundError` (introduced in Python 3.6).
# If you catch `ImportError`, it will also catch `ModuleNotFoundError`.

# --- 1. Basic ImportError: Module Not Found ---
print("--- 1. Basic ImportError: Module Not Found ---")

# Attempting to import a module that does not exist in Python's search path.
try:
    import non_existent_module_xyz
except ImportError as e:
    print(f"Caught ImportError (expected): {e}")
    print("Reason: No module named 'non_existent_module_xyz'.")

# Specifically ModuleNotFoundError (Python 3.6+)
try:
    import another_non_existent_module
except ModuleNotFoundError as e:
    print(f"Caught ModuleNotFoundError (expected): {e}")
    print("Reason: No module named 'another_non_existent_module'.")

print("-" * 50 + "\n")


# --- 2. ImportError: Name Not Found in Module (`from ... import ...`) ---
print("--- 2. ImportError: Name Not Found in Module ---")

# Attempting to import a specific name (function, class, variable)
# from an existing module, but that name does not exist within it.

# Let's import a standard module first
import math

try:
    # 'non_existent_function' is not a function in the 'math' module
    from math import non_existent_function
except ImportError as e:
    print(f"Caught ImportError (expected): {e}")
    print("Reason: cannot import name 'non_existent_function' from 'math'.")

# Similarly for classes or variables if they don't exist
# Example (imaginary scenario if `json` didn't have `loads`):
import json
try:
    from json import non_existent_json_parser
except ImportError as e:
    print(f"Caught ImportError (expected): {e}")
    print("Reason: cannot import name 'non_existent_json_parser' from 'json'.")

print("-" * 50 + "\n")


# --- 3. ImportError due to Relative Imports (Incorrect Usage) ---
print("--- 3. ImportError due to Relative Imports (Incorrect Usage) ---")

# Relative imports are used for modules within the same package.
# They start with a dot (`.`) or multiple dots (`..`).
# These errors often occur when running a submodule directly as a script.

# To demonstrate, we'll create a temporary package structure:
# my_package/
# ├── __init__.py
# ├── module_a.py
# └── submodule/
#     ├── __init__.py
#     └── module_b.py

# Create dummy files for demonstration
import os
import textwrap

package_dir = "temp_my_package"
submodule_dir = os.path.join(package_dir, "submodule")

os.makedirs(submodule_dir, exist_ok=True)

# Create __init__.py
with open(os.path.join(package_dir, "__init__.py"), "w") as f:
    f.write("# Package initialization")
with open(os.path.join(submodule_dir, "__init__.py"), "w") as f:
    f.write("# Submodule initialization")

# Create module_a.py
module_a_content = textwrap.dedent("""
    # module_a.py
    def func_a():
        return "Function A from module_a"
""")
with open(os.path.join(package_dir, "module_a.py"), "w") as f:
    f.write(module_a_content)

# Create module_b.py with a relative import
module_b_content = textwrap.dedent("""
    # module_b.py
    from ..module_a import func_a # Relative import to parent package's module_a

    def func_b():
        return f"Function B from module_b, calling {func_a()}"

    if __name__ == "__main__":
        print("Running module_b directly.")
        try:
            # This relative import will fail when module_b.py is run directly
            # because Python doesn't know its package context.
            print(func_b())
        except ImportError as e:
            print(f"Caught ImportError when running module_b directly (expected): {e}")
            print("Reason: Relative imports don't work when running a submodule directly as main.")
            print("  Try running the package from its parent directory (e.g., `python -m temp_my_package.submodule.module_b`)")
""")
with open(os.path.join(submodule_dir, "module_b.py"), "w") as f:
    f.write(module_b_content)

print(f"Created dummy package structure in '{package_dir}/'.")
print("To see the ImportError for relative imports, try running the generated file:")
print(f"  `python {submodule_dir}/module_b.py` (will cause ImportError)")
print("  Then try `cd {package_dir}/.. && python -m {package_dir}.submodule.module_b` (will work)")

# Clean up dummy files (optional)
# import shutil
# shutil.rmtree(package_dir)

print("-" * 50 + "\n")


# --- 4. ImportError due to Circular Imports (Advanced) ---
print("--- 4. ImportError due to Circular Imports (Advanced) ---")

# Circular imports occur when module A imports B, and B imports A.
# This can lead to ImportError (or sometimes NameError) if a module tries
# to access something from the circularly imported module before it's fully initialized.

# Simulate with classes in a single file to show the concept:
# Imagine this is split into `alpha_module.py` and `beta_module.py`

print("Simulating circular import (can cause ImportError or NameError):")

class AlphaClass:
    def __init__(self):
        print("AlphaClass initialized")
    def alpha_method(self):
        print("Alpha method called.")
        # If BetaClass wasn't fully defined/imported yet, this might fail
        try:
            beta_instance = BetaClass() # Referencing BetaClass
            beta_instance.beta_method()
        except NameError as e:
            print(f"  Caught NameError in AlphaClass (simulated circularity): {e}")
            print("  Reason: 'BetaClass' not fully defined/loaded yet.")
        except ImportError as e:
            print(f"  Caught ImportError in AlphaClass (simulated circularity): {e}")

class BetaClass:
    def __init__(self):
        print("BetaClass initialized")
    def beta_method(self):
        print("Beta method called.")
        # Similar issue if BetaClass tried to reference AlphaClass at this point
        # and AlphaClass wasn't fully initialized.

# The direct execution order in a single file often avoids the ImportError
# but highlights the dependency issue. In real multi-file scenarios:
# 1. module_a.py: `import module_b` then defines `func_a` which calls `module_b.func_b`.
# 2. module_b.py: `import module_a` then defines `func_b` which calls `module_a.func_a`.
# When Python loads `module_a`, it sees `import module_b`. It starts loading `module_b`.
# Inside `module_b`, it sees `import module_a`. Python detects the loop and *reuses*
# the partially initialized `module_a`. If `module_b` then tries to use something
# from `module_a` that isn't defined yet, it fails.

# Direct interaction might work because BetaClass is fully defined when AlphaClass runs:
alpha_obj = AlphaClass()
alpha_obj.alpha_method()

print("Circular import issues are complex; they depend on what names are used when.")
print("-" * 50 + "\n")


# --- 5. ImportError with __init__.py Problems ---
print("--- 5. ImportError with __init__.py Problems ---")

# If an `__init__.py` file (which marks a directory as a Python package)
# contains errors, or tries to import things that fail, it can cause an ImportError
# for the entire package.

# Example: If `my_package/__init__.py` had `raise ValueError("Error in init")`
# Or if it had: `from .non_existent_module import xyz`

# Simulate an `__init__.py` with an error
broken_init_content = textwrap.dedent("""
    # broken_package/__init__.py
    print("Loading broken_package init...")
    from .some_module import a_func
    # This will cause an ImportError if 'some_module' doesn't exist or 'a_func' doesn't.
    # Or, simulate an explicit error:
    # raise ImportError("Simulated error in __init__.py")
""")

broken_package_dir = "temp_broken_package"
os.makedirs(broken_package_dir, exist_ok=True)
with open(os.path.join(broken_package_dir, "__init__.py"), "w") as f:
    f.write(broken_init_content)

# Add a dummy module to try to import, making it a valid package
with open(os.path.join(broken_package_dir, "some_module.py"), "w") as f:
    f.write("def a_func(): pass")

print(f"Trying to import 'temp_broken_package' which has missing name in __init__.py.")
try:
    # Because 'a_func' exists in some_module.py, the above __init__.py content
    # would actually *not* raise an ImportError for missing 'a_func' directly.
    # To force an ImportError in __init__.py, you'd need 'from .non_existent_module import something'.
    # Or as commented, an explicit `raise ImportError`.
    # Let's try importing a non-existent name from an existing module.
    broken_init_content_name_error = textwrap.dedent("""
        # broken_package_name_error/__init__.py
        from .some_module import non_existent_func_in_some_module
    """)
    broken_package_dir_name_error = "temp_broken_package_name_error"
    os.makedirs(broken_package_dir_name_error, exist_ok=True)
    with open(os.path.join(broken_package_dir_name_error, "__init__.py"), "w") as f:
        f.write(broken_init_content_name_error)
    with open(os.path.join(broken_package_dir_name_error, "some_module.py"), "w") as f:
        f.write("def func_exists(): pass") # 'non_existent_func_in_some_module' is missing

    import importlib
    import sys
    sys.path.insert(0, os.getcwd()) # Add current directory to path for import
    try:
        # Use importlib to try to import the dynamically created package
        importlib.import_module("temp_broken_package_name_error")
    except ImportError as e:
        print(f"Caught ImportError (expected from __init__.py): {e}")
        print("Reason: 'non_existent_func_in_some_module' is not found in 'some_module'.")
    finally:
        sys.path.pop(0) # Clean up sys.path
        import shutil
        shutil.rmtree(broken_package_dir_name_error)
        shutil.rmtree(broken_package_dir) # Clean up the first dummy package

except Exception as e:
    print(f"An unexpected error during __init__.py simulation: {e}")

print("-" * 50 + "\n")


# --- 6. Troubleshooting ImportError ---
print("--- 6. Troubleshooting ImportError ---")

# 6.1 Check for Typos: The most common cause. Double-check module and name spellings.
#     `import maths` -> should be `import math`
#     `from os import pathh` -> should be `from os import path`

# 6.2 Python Path (`sys.path`):
#    Python searches for modules in directories listed in `sys.path`.
#    If your module is not in one of these directories, it won't be found.
print("Current Python search path (sys.path):")
import sys
for p in sys.path:
    print(f"  {p}")
print("If your module isn't in one of these, add its containing directory.")
print("Ways to add to sys.path:")
print("  - Temporarily: `sys.path.append('/path/to/your/module_dir')`")
print("  - Permanently (usually discouraged for general use): `PYTHONPATH` environment variable.")
print("  - Using `pip install -e .` for editable installs in packages.")

# 6.3 Correct Relative Imports:
#    - Use `python -m my_package.my_module` to run submodules, not `python my_module.py`.
#    - Ensure the correct number of dots (`.` for same package, `..` for parent package, etc.).

# 6.4 Circular Imports:
#    - Refactor your code: Break down dependencies. Use functions/classes where dependencies
#      are less strict, or defer imports (import inside a function if not needed globally).
#    - Sometimes, just moving the `import` statement to *inside* the function that needs it
#      can resolve circular imports by delaying the import until it's actually required.

# 6.5 Environment/Installation Issues:
#    - Is the package actually installed? `pip list` or `conda list` can confirm.
#    - Are you in the correct Python environment (e.g., virtual environment)?
#    - Corrupted installation? Reinstall the package.

# 6.6 Case Sensitivity: Module names can be case-sensitive depending on the OS and file system.
#     `import mymodule` vs `import MyModule`.

print("--- End of ImportError demonstration ---")



# --- ImportError: More Examples (Continued) ---

# This section provides further illustrations of ImportError,
# including scenarios related to package structures, dynamic imports,
# and issues that arise during module initialization.

# --- 7. ImportError with Missing Package `__init__.py` ---
print("--- 7. ImportError with Missing Package `__init__.py` ---")

# Before Python 3.3, a directory needed an `__init__.py` file to be recognized as a package.
# While Python 3.3+ introduced "implicit namespace packages" (directories without `__init__.py` can still be packages),
# standard packages (which are most common) still rely on `__init__.py`.
# If you expect a directory to be a regular package and it's missing this file,
# or if you're on an older Python version, it might not be importable as a package.

# Create a directory without __init__.py
import os
import shutil

no_init_package_dir = "temp_no_init_package"
no_init_module_path = os.path.join(no_init_package_dir, "my_module.py")

os.makedirs(no_init_package_dir, exist_ok=True)
with open(no_init_module_path, "w") as f:
    f.write("def hello(): return 'Hello from my_module'")

print(f"Created directory '{no_init_package_dir}' without __init__.py.")

# Try to import it as a package (will fail if treated as traditional package)
import sys
sys.path.insert(0, os.getcwd()) # Add current dir to path

try:
    # In modern Python (3.3+), this might work as a namespace package.
    # However, if 'my_module' tries to do relative imports, or if the system
    # expects a traditional package, issues can arise.
    # For a clear ImportError here, imagine a complex scenario or older Python version.
    # Let's try to import a non-existent submodule from it, which relies on package structure.
    import temp_no_init_package.non_existent_submodule
    # If the above passes, it means it's treated as a namespace package.
    # To reliably demonstrate, consider explicitly making it a normal package that fails.
    # For a direct ImportError, you'd typically need to run this in a context
    # where it's *expected* to be a regular package.
    print("Importing `temp_no_init_package.non_existent_submodule` (expected to fail if traditional package).")
except ModuleNotFoundError as e:
    print(f"Caught ModuleNotFoundError (expected due to missing submodule or package structure): {e}")
    print("Reason: Could not find 'non_existent_submodule' within the namespace package.")
except ImportError as e: # Catch base ImportError as well
    print(f"Caught ImportError (general case): {e}")
finally:
    sys.path.pop(0)
    shutil.rmtree(no_init_package_dir, ignore_errors=True) # Clean up

print("Note: In Python 3.3+, directories without `__init__.py` can form 'namespace packages'.")
print("Explicit `__init__.py` is still needed for regular packages that contain code themselves or for relative imports within.")
print("-" * 50 + "\n")


# --- 8. ImportError During Module Initialization (Side Effects) ---
print("--- 8. ImportError During Module Initialization (Side Effects) ---")

# If a module contains code that executes upon import and that code
# itself causes an error (e.g., a NameError, AttributeError, or even another ImportError),
# the original import statement will propagate that error as an ImportError.

# Create a dummy module with an error during its initialization
error_module_content = """
# temp_error_module.py
print("Attempting to load temp_error_module...")
# This line will cause a NameError when the module is loaded
result = undefined_variable_in_module + 1
"""
error_module_path = "temp_error_module.py"
with open(error_module_path, "w") as f:
    f.write(error_module_content)

import sys
sys.path.insert(0, os.getcwd())

try:
    import temp_error_module
except ImportError as e:
    print(f"Caught ImportError (expected, due to error in module itself): {e}")
    print("Reason: The 'temp_error_module' failed to initialize due to 'NameError'.")
    # Python 3 typically wraps the original exception, providing context.
    # e.g., "cannot import name 'temp_error_module' from partially initialized module 'temp_error_module' (most likely due to a circular import) (<path/to/module.py>)"
    # or it directly reports the underlying error (e.g., NameError directly).
    # The actual message can vary slightly depending on Python version and exact scenario.
except NameError as e: # Catch underlying error if not wrapped as ImportError
     print(f"Caught underlying NameError (if not wrapped as ImportError): {e}")
finally:
    sys.path.pop(0)
    os.remove(error_module_path)

print("-" * 50 + "\n")


# --- 9. ImportError from Dynamically Generated Paths ---
print("--- 9. ImportError from Dynamically Generated Paths ---")

# When modifying `sys.path` to import modules from non-standard locations,
# if the path is incorrect or the module isn't there, it will lead to ImportError.

temp_module_dir = "temp_dynamic_import_dir"
temp_module_file = os.path.join(temp_module_dir, "dynamic_module.py")
os.makedirs(temp_module_dir, exist_ok=True)
with open(temp_module_file, "w") as f:
    f.write("def dynamic_func(): return 'I am dynamic!'")

print(f"Created '{temp_module_dir}/dynamic_module.py'.")

# Case 1: Correctly add to sys.path and import (OK)
import sys
sys.path.insert(0, temp_module_dir) # Add the directory containing the module

try:
    import dynamic_module
    print(f"Successfully imported dynamic_module: {dynamic_module.dynamic_func()}")
except ImportError as e:
    print(f"Unexpected ImportError during successful dynamic import: {e}")
finally:
    sys.path.pop(0) # Clean up sys.path
    # Note: dynamic_module is now in sys.modules, so subsequent imports might use the cached version.

# Case 2: Incorrect path or non-existent module
invalid_path = "/non_existent_path_for_modules_123"
sys.path.insert(0, invalid_path)

try:
    import non_existent_dynamic_module
except ImportError as e:
    print(f"Caught ImportError (expected for incorrect dynamic path): {e}")
    print("Reason: Module not found because the added path was incorrect or module name was wrong.")
finally:
    sys.path.pop(0)
    shutil.rmtree(temp_module_dir, ignore_errors=True)

print("-" * 50 + "\n")


# --- 10. ImportError when Trying to Import a Directory as a Module ---
print("--- 10. ImportError when Trying to Import a Directory as a Module ---")

# If you have a directory named, say, `my_script.py`, and you try to `import my_script.py`
# but `my_script.py` is actually a *directory*, it will likely cause an ImportError
# if Python can't interpret it as a package.

# Create a dummy directory with the name that looks like a module file
dir_named_like_module = "temp_module_name.py"
os.makedirs(dir_named_like_module, exist_ok=True)
# You *can* place an __init__.py inside it to make it a package,
# but if it's just an empty directory, it will cause issues.
# For this example, let's keep it as an empty directory named like a file.

print(f"Created a directory named '{dir_named_like_module}'.")

import sys
sys.path.insert(0, os.getcwd())

try:
    # Python tries to import 'temp_module_name.py' but finds a directory.
    # If no `__init__.py` is present, it might be treated as a namespace package
    # but without anything to actually import, leading to ModuleNotFoundError or ImportError
    # when trying to access attributes/submodules.
    # The direct import might fail if the interpreter can't resolve it as a module.
    import temp_module_name
except ModuleNotFoundError as e:
    print(f"Caught ModuleNotFoundError (expected for importing a directory as a module): {e}")
    print("Reason: Python didn't find a '.py' file or a proper package structure for 'temp_module_name'.")
except ImportError as e:
    print(f"Caught general ImportError: {e}")
finally:
    sys.path.pop(0)
    shutil.rmtree(dir_named_like_module, ignore_errors=True)

print("-" * 50 + "\n")

print("--- End of More ImportError Examples ---")
