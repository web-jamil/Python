import sys # For sys.argv
import argparse # For advanced argument parsing

print("--- Python Command-Line Arguments: Practice Code ---")

# --- 1. Introduction to Command-Line Arguments ---
print("\n--- 1. Introduction to Command-Line Arguments ---")
print("Command-line arguments are parameters passed to a Python script when it's executed from the terminal.")
print("They allow you to control the script's behavior without modifying its source code.")
print("Example: `python my_script.py arg1 --option value`")


# --- 2. Using `sys.argv` (Simple Access) ---
print("\n--- 2. Using `sys.argv` ---")
print("`sys.argv` is a list in the `sys` module that contains all the command-line arguments.")
print(" - `sys.argv[0]` is always the name of the script itself.")
print(" - Subsequent elements (`sys.argv[1]`, `sys.argv[2]`, etc.) are the arguments passed.")
print(" - All arguments are read as **strings**, regardless of their actual type.")

print("\n--- `sys_argv_example.py` (How you'd run it) ---")
print("Imagine you save the following code as `sys_argv_example.py`:")
print("```python")
print("import sys")
print("")
print("print(f'Script name: {sys.argv[0]}')")
print(f"Total arguments: {len(sys.argv)}")
print(f"All arguments as list: {sys.argv}")
print("")
print("if len(sys.argv) > 1:")
print("    # Accessing specific arguments")
print(f"    First argument: {sys.argv[1]}")
print("    try:")
print("        # Converting arguments to numbers (remember they are strings initially)")
print(f"        Sum of first two args (as int): {int(sys.argv[1]) + int(sys.argv[2])}")
print("    except (IndexError, ValueError):")
print("        print('  Not enough arguments or arguments not convertible to int.')")
print("```")

print("\n--- How to Run `sys_argv_example.py` from your terminal ---")
print("`python sys_argv_example.py`")
print("`python sys_argv_example.py hello world`")
print("`python sys_argv_example.py 10 20`")
print("`python sys_argv_example.py one two three four five`")

# Since I can't run a shell, I'll simulate the output for one example:
print("\n--- Simulated output for `python sys_argv_example.py 10 20` ---")
# Simulate sys.argv for demonstration within this environment
original_argv = sys.argv # Store original to restore later
sys.argv = ['sys_argv_example.py', '10', '20']

print(f'Script name: {sys.argv[0]}')
print(f"Total arguments: {len(sys.argv)}")
print(f"All arguments as list: {sys.argv}")
if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
    try:
        print(f"Sum of first two args (as int): {int(sys.argv[1]) + int(sys.argv[2])}")
    except (IndexError, ValueError):
        print('  Not enough arguments or arguments not convertible to int.')

sys.argv = original_argv # Restore original sys.argv

print("\n`sys.argv` is good for very simple scripts, but quickly becomes cumbersome for more options.")


# --- 3. Using `argparse` Module (Robust Parsing) ---
print("\n--- 3. Using `argparse` Module ---")
print("The `argparse` module makes it easy to write user-friendly command-line interfaces.")
print("It handles parsing arguments, converting types, and generating help messages automatically.")

print("\n--- `argparse_example.py` (How you'd run it) ---")
print("Imagine you save the following code as `argparse_example.py`:")
print("```python")
print("import argparse")
print("")
print("# 1. Create an ArgumentParser object")
print("parser = argparse.ArgumentParser(description='A simple script demonstrating argparse.')")
print("")
print("# 2. Add arguments")
print("# Positional argument (required, order matters)")
print("parser.add_argument('name', type=str, help='Your name')")
print("")
print("# Optional argument with a short and long form")
print("parser.add_argument('-a', '--age', type=int, default=30, help='Your age (default: 30)')")
print("")
print("# Optional boolean flag (store_true means if flag is present, value is True)")
print("parser.add_argument('--verbose', action='store_true', help='Enable verbose output')")
print("")
print("# Optional argument with choices")
print("parser.add_argument('--color', choices=['red', 'green', 'blue'], default='green',")
print("                    help='Choose a color (default: green)')")
print("")
print("# Optional argument that can appear multiple times (nargs='+') or a fixed number (nargs=N)")
print("parser.add_argument('--items', nargs='*', help='A list of items (optional)')")
print("")
print("# 3. Parse the arguments from the command line")
print("args = parser.parse_args()")
print("")
print("# 4. Access the arguments via the 'args' object")
print(f'Hello, {args.name}!')
print(f'You are {args.age} years old.')
print(f'Verbose mode: {args.verbose}')
print(f'Selected color: {args.color}')
print(f'Items: {args.items}')
print("")
print("if args.verbose:")
print("    print('Verbose output is enabled!')")
print("```")

print("\n--- How to Run `argparse_example.py` from your terminal ---")
print("`python argparse_example.py --help`")
print("`python argparse_example.py Alice`")
print("`python argparse_example.py Bob --age 25`")
print("`python argparse_example.py Charlie --verbose --color blue --items apple orange`")
print("`python argparse_example.py David -a 40 --items pen paper book`")
print("`python argparse_example.py Frank --age invalid_text` (This will raise an error from argparse)")

# Simulate `argparse` interaction for a few examples:
print("\n--- Simulated output for `python argparse_example.py Alice --age 25` ---")
# Manually define the arguments that argparse.parse_args() would receive
# In a real script, parse_args() would read from sys.argv
parser = argparse.ArgumentParser(description='A simple script demonstrating argparse.')
parser.add_argument('name', type=str, help='Your name')
parser.add_argument('-a', '--age', type=int, default=30, help='Your age (default: 30)')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('--color', choices=['red', 'green', 'blue'], default='green', help='Choose a color (default: green)')
parser.add_argument('--items', nargs='*', help='A list of items (optional)')

# Simulate args provided by command line
args = parser.parse_args(['Alice', '--age', '25'])
print(f'Hello, {args.name}!')
print(f'You are {args.age} years old.')
print(f'Verbose mode: {args.verbose}')
print(f'Selected color: {args.color}')
print(f'Items: {args.items}')
if args.verbose:
    print('Verbose output is enabled!')

print("\n--- Simulated output for `python argparse_example.py Charlie --verbose --color blue --items apple orange` ---")
args = parser.parse_args(['Charlie', '--verbose', '--color', 'blue', '--items', 'apple', 'orange'])
print(f'Hello, {args.name}!')
print(f'You are {args.age} years old.') # Will be default 30 as no --age was provided
print(f'Verbose mode: {args.verbose}')
print(f'Selected color: {args.color}')
print(f'Items: {args.items}')
if args.verbose:
    print('Verbose output is enabled!')

print("\n`argparse` provides robust argument validation and help messages, making it the preferred choice for most scripts.")

print("\n--- End of Python Command-Line Arguments Practice Code ---")