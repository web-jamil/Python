# --- 1. Missing Colon Errors ---

print("\n--- Missing Colon Errors ---")

# Incorrect: Missing colon after 'if' statement
# if True
#     print("This will cause a SyntaxError")

# Correct:
if True:
    print("Correct: Colon after 'if' statement.")

# Incorrect: Missing colon after 'for' loop
# for i in range(3)
#     print(i)

# Correct:
for i in range(3):
    print(f"Correct: Loop iteration {i}.")

# Incorrect: Missing colon after 'def' (function definition)
# def my_function()
#     pass

# Correct:
def my_function():
    print("Correct: Function defined.")
my_function()

# Incorrect: Missing colon after 'class' definition
# class MyClass
#     pass

# Correct:
class MyClass:
    def __init__(self):
        print("Correct: Class defined.")
MyClass()


# --- 2. Unmatched Delimiters (Parentheses, Brackets, Braces) ---

print("\n--- Unmatched Delimiters ---")

# Incorrect: Missing closing parenthesis
# result = (10 + 5

# Correct:
result = (10 + 5)
print(f"Correct: Result of (10 + 5) is {result}")

# Incorrect: Missing closing square bracket
# my_list = [1, 2, 3

# Correct:
my_list = [1, 2, 3]
print(f"Correct: List is {my_list}")

# Incorrect: Missing closing curly brace for dictionary
# my_dict = {'key': 'value'

# Correct:
my_dict = {'key': 'value'}
print(f"Correct: Dictionary is {my_dict}")


# --- 3. Invalid Assignment Targets ---

print("\n--- Invalid Assignment Targets ---")

# Incorrect: Cannot assign to a literal
# 5 = x

# Correct:
x = 5
print(f"Correct: x is {x}")

# Incorrect: Cannot assign to a function call
# len("hello") = 5

# Correct (this is not an assignment, but a comparison):
is_len_5 = len("hello") == 5
print(f"Correct: Is length of 'hello' 5? {is_len_5}")


# --- 4. Invalid Operators ---

print("\n--- Invalid Operators ---")

# Incorrect: Double plus operator (Python doesn't have ++ for increment)
# increment = x ++ 1

# Correct:
x_val = 10
x_val += 1 # or x_val = x_val + 1
print(f"Correct: x_val after increment is {x_val}")

# Incorrect: Non-existent operator
# value = 10 %/ 3

# Correct:
value_mod = 10 % 3
value_div = 10 / 3
print(f"Correct: Modulo is {value_mod}, Division is {value_div}")


# --- 5. Misspelled or Misused Keywords ---

print("\n--- Misspelled or Misused Keywords ---")

# Incorrect: Typo in 'return'
# def get_data():
#     retern "some data"

# Correct:
def get_data():
    return "some data"
print(f"Correct: Data is '{get_data()}'")

# Incorrect: Using a reserved keyword as a variable name
# class = "Python Class" # 'class' is a reserved keyword

# Correct:
my_class_name = "Python Class"
print(f"Correct: Class name variable is '{my_class_name}'")


# --- 6. Unterminated String Literals ---

print("\n--- Unterminated String Literals ---")

# Incorrect: Missing closing quote for string
# message = "Hello, World!

# Correct:
message = "Hello, World!"
print(f"Correct: Message is '{message}'")

# Incorrect: Mixed quotes (starts with single, ends with double)
# wrong_quote = 'This is wrong"

# Correct:
correct_single_quote = 'This is correct'
correct_double_quote = "This is also correct"
print(f"Correct: '{correct_single_quote}', '{correct_double_quote}'")


# --- 7. Invalid Characters in Identifiers (Variable/Function Names) ---

print("\n--- Invalid Characters in Identifiers ---")

# Incorrect: Hyphen in variable name (interpreted as subtraction)
# my-variable = 10

# Correct:
my_variable = 10 # Use underscore
print(f"Correct: my_variable is {my_variable}")

# Incorrect: Variable name starting with a digit
# 1st_name = "Alice"

# Correct:
first_name = "Alice" # Start with a letter or underscore
print(f"Correct: first_name is {first_name}")


# --- 8. Indentation Issues (Can be IndentationError or SyntaxError) ---

print("\n--- Indentation Issues ---")

# This is usually an IndentationError, but in some edge cases (especially
# if an entire block is unindented where one is expected), it can manifest
# as a SyntaxError depending on the Python version/context.

# Incorrect: Unexpected indentation at the start of a file
#   print("This might be an IndentationError or SyntaxError if misplaced")

# Correct:
print("This line is correctly indented at the top level.")

# Incorrect: Inconsistent indentation (mixing tabs and spaces - TabError, a subclass of IndentationError)
# def example_indent():
# \tprint("Using a tab")
#     print("Using spaces") # Mixed indentation leads to TabError/IndentationError

# Correct: Use consistent indentation (e.g., 4 spaces):
def consistent_indent():
    print("Using 4 spaces for indentation.")
    if True:
        print("More indentation.")
consistent_indent()


# --- 9. Leading Zeros in Decimal Literals (Python 3) ---

print("\n--- Leading Zeros in Decimal Literals ---")

# Incorrect (in Python 3, for non-octal numbers):
# invalid_number = 0123

# Correct (for decimal 123):
valid_number = 123
print(f"Correct: Decimal 123 is {valid_number}")

# Correct (for octal 0o123):
octal_number = 0o123 # This is an octal number, which is allowed
print(f"Correct: Octal 0o123 is {octal_number} (which is 83 in decimal)")


# --- 10. `return` or `yield` Outside Function ---

print("\n--- return/yield Outside Function ---")

# Incorrect:
# return "Cannot return here"

# Incorrect:
# yield "Cannot yield here"

# Correct:
def my_returning_function():
    return "Can return inside a function."

def my_generator_function():
    yield "Can yield inside a generator function."

print(f"Correct: Function return: {my_returning_function()}")
gen = my_generator_function()
print(f"Correct: Generator yield: {next(gen)}")


print("\n--- End of SyntaxError Code Examples ---")
print("Remember, SyntaxErrors stop your program from running before it even starts.")
print("The error message will guide you to the specific line and often the character position.")



# This entire script will fail to run if any of the commented-out
# 'INCORRECT' blocks are uncommented and left as is.

class SyntaxErrorExamples:
    """
    This class is designed to show where SyntaxErrors might appear within
    a class definition. No actual code within the class will execute if
    a SyntaxError exists when the script is parsed.
    """

    def __init__(self, value):
        self.value = value
        print(f"Initialized with value: {self.value}")

    # --- SYNTAX ERROR EXAMPLE 1: Missing colon in method definition ---
    # INCORRECT:
    # def method_with_syntax_error_1()
    #     print("This method has a missing colon.")

    # CORRECT:
    def method_with_correct_syntax_1(self):
        print("This method has the correct colon.")

    # --- SYNTAX ERROR EXAMPLE 2: Unmatched parenthesis in an expression ---
    # INCORRECT:
    # def method_with_syntax_error_2(self):
    #     calculation = (self.value + 5

    # CORRECT:
    def method_with_correct_syntax_2(self):
        calculation = (self.value + 5)
        print(f"Correct calculation: {calculation}")

    # --- SYNTAX ERROR EXAMPLE 3: Invalid variable name ---
    # INCORRECT:
    # def method_with_syntax_error_3(self):
    #     my-variable = 10 # Hyphen is not allowed

    # CORRECT:
    def method_with_correct_syntax_3(self):
        my_variable = 10 # Underscore is correct
        print(f"Correct variable name: {my_variable}")

    # --- SYNTAX ERROR EXAMPLE 4: Unclosed string literal ---
    # INCORRECT:
    # def method_with_syntax_error_4(self):
    #     message = "Hello, world!

    # CORRECT:
    def method_with_correct_syntax_4(self):
        message = "Hello, world!"
        print(f"Correct string: {message}")

    # --- SYNTAX ERROR EXAMPLE 5: Misspelled keyword (e.g., 'defenition') ---
    # INCORRECT:
    # defenition another_method(self):
    #     pass

    # CORRECT:
    def another_method(self):
        print("Another correctly defined method.")

    # --- SYNTAX ERROR EXAMPLE 6: return/yield outside a function/method (if placed directly in class body) ---
    # INCORRECT:
    # This would fail immediately upon parsing the class definition if uncommented.
    # return "This cannot be here"

    # CORRECT (return inside a method):
    def get_value(self):
        return self.value

# --- Instantiation and Method Calls (these lines won't run if a SyntaxError exists above) ---
print("\nAttempting to create an instance of SyntaxErrorExamples...")
try:
    # If any of the 'INCORRECT' sections above are uncommented,
    # the script will stop HERE with a SyntaxError BEFORE this line executes.
    instance = SyntaxErrorExamples(10)
    print("Instance created successfully (no SyntaxError encountered during parsing).")

    instance.method_with_correct_syntax_1()
    instance.method_with_correct_syntax_2()
    instance.method_with_correct_syntax_3()
    instance.method_with_correct_syntax_4()
    instance.another_method()
    print(f"Value from get_value: {instance.get_value()}")

except SyntaxError as e:
    # This except block will NEVER be reached for a true SyntaxError
    # because the error happens at parse time, not runtime.
    # It's included just to emphasize that point.
    print(f"Caught a SyntaxError (this won't actually happen at runtime): {e}")
except Exception as e:
    print(f"Caught an unexpected error at runtime: {e}")

print("\nScript finished (if no SyntaxError prevented execution).")