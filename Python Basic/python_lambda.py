import functools # For functools.reduce
import operator  # For common operations in reduce example

print("--- Python Lambda Functions: Practice Code ---")

# --- 1. What is a Lambda Function? ---
print("\n--- 1. What is a Lambda Function? ---")
print("A lambda function is a small, anonymous (nameless) function in Python.")
print("It can take any number of arguments, but can only have one expression.")
print("The result of this expression is implicitly returned.")

# --- 2. Syntax of Lambda Functions ---
print("\n--- 2. Syntax of Lambda Functions ---")
print("Syntax: lambda arguments: expression")

# Example 1: Lambda with no arguments (rare, but possible)
greet = lambda: "Hello, world!"
print(f"Greet (no args): {greet()}")

# Example 2: Lambda with one argument
square = lambda x: x * x
print(f"Square of 5: {square(5)}")

# Example 3: Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Sum of 10 and 20: {add(10, 20)}")

# Example 4: Lambda with conditional logic (as an expression)
# Note: This is an expression, not a statement.
max_val = lambda a, b: a if a > b else b
print(f"Max of 7 and 3: {max_val(7, 3)}")


# --- 3. Key Characteristics and Comparison with `def` functions ---
print("\n--- 3. Key Characteristics and Comparison ---")

# 3.1 Anonymous (no name)
# A lambda function is typically defined inline where it's used, without assigning a name.
# While you *can* assign it to a variable (like `square = lambda x: x*x`),
# it's generally discouraged if a `def` function would be clearer.

# 3.2 Single Expression (not statements)
# Lambda functions cannot contain:
# - Multiple expressions (e.g., separated by semicolons)
# - Statements like `if/else` (as statements), `for` loops, `while` loops
# - Variable assignments (`=`)
# - `return`, `yield`, `raise` statements

# BAD examples (will cause SyntaxError):
# bad_lambda_if = lambda x: print(x) if x > 0 else pass # SyntaxError: invalid syntax
# bad_lambda_assign = lambda x: y = x + 1 # SyntaxError: invalid syntax

# 3.3 Implicit Return
# The result of the expression is automatically returned. No `return` keyword needed.

# 3.4 Conciseness
# They are ideal for short, simple operations.

# Comparison:
def square_def(x):
    return x * x
print(f"Square (def function): {square_def(5)}")

# Lambda is more concise for this simple case.
# If you need multiple lines, complex logic, or documentation, use `def`.


# --- 4. Common Use Cases for Lambda Functions ---
print("\n--- 4. Common Use Cases for Lambda Functions ---")
print("Lambdas shine when passed as arguments to higher-order functions.")

# 4.1 With `map()`: Apply a function to each item in an iterable.
print("\n4.1 Using lambda with `map()`:")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")

# Converting temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (9/5) * c + 32, celsius_temps))
print(f"Celsius temps: {celsius_temps}")
print(f"Fahrenheit temps: {fahrenheit_temps}")

# 4.2 With `filter()`: Filter elements from an iterable based on a condition.
print("\n4.2 Using lambda with `filter()`:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

names = ["Alice", "Bob", "Anna", "Charles", "Amanda"]
names_starting_with_a = list(filter(lambda name: name.startswith('A'), names))
print(f"Names starting with 'A': {names_starting_with_a}")

# 4.3 With `sorted()` or `list.sort()`: Custom sorting key.
print("\n4.3 Using lambda with `sorted()` or `list.sort()` (key argument):")

# Sorting a list of tuples by the second element
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_by_second_element = sorted(pairs, key=lambda item: item[1])
print(f"Sorted pairs by second element: {sorted_by_second_element}")

# Sorting a list of dictionaries by a specific key
students = [
    {'name': 'Alice', 'grade': 85, 'age': 20},
    {'name': 'Bob', 'grade': 92, 'age': 22},
    {'name': 'Charlie', 'grade': 78, 'age': 21}
]
sorted_by_grade = sorted(students, key=lambda s: s['grade'], reverse=True)
print(f"Students sorted by grade (desc): {sorted_by_grade}")

# Sorting by multiple criteria (grade then age)
sorted_by_grade_then_age = sorted(students, key=lambda s: (s['grade'], s['age']))
print(f"Students sorted by grade then age: {sorted_by_grade_then_age}")


# 4.4 With `functools.reduce()`: Apply a function cumulatively to the items of an iterable.
# Requires importing `functools`
print("\n4.4 Using lambda with `functools.reduce()`:")
# Example: Sum all numbers in a list
numbers_to_sum = [1, 2, 3, 4, 5]
sum_result = functools.reduce(lambda acc, x: acc + x, numbers_to_sum)
print(f"Sum of {numbers_to_sum} using reduce: {sum_result}")

# Example: Concatenate strings
words = ["Python", "is", "fun"]
combined_string = functools.reduce(lambda acc, word: acc + " " + word, words)
print(f"Concatenated words: {combined_string}")


# 4.5 Event Handlers / Callbacks (common in some GUI frameworks)
# Though not runnable here, imagine a button click:
# button.on_click(lambda: print("Button clicked!"))
# Or with arguments:
# entry.on_change(lambda text: print(f"Text changed to: {text}"))


# --- 5. Lambda and Closures ---
print("\n--- 5. Lambda and Closures ---")
print("Lambdas can 'capture' variables from their enclosing scope (closure).")

def make_multiplier(n):
    # n is captured by the lambda
    return lambda x: x * n

multiply_by_5 = make_multiplier(5)
multiply_by_10 = make_multiplier(10)

print(f"Multiply 7 by 5: {multiply_by_5(7)}")
print(f"Multiply 7 by 10: {multiply_by_10(7)}")

# Common pitfall with loops and lambdas (due to late binding):
# Each lambda captures the *final* value of `i`
print("\nCommon pitfall with loops and lambdas (late binding):")
lambdas = []
for i in range(3):
    lambdas.append(lambda: i)

for f in lambdas:
    print(f(), end=" ") # Output will be 2 2 2, not 0 1 2
print()

# Correct way to capture value in loop: pass it as a default argument
lambdas_fixed = []
for i in range(3):
    lambdas_fixed.append(lambda x=i: x) # x=i binds the current value of i

for f in lambdas_fixed:
    print(f(), end=" ") # Output will be 0 1 2
print()


# --- 6. When to Use and When to Avoid Lambdas ---
print("\n--- 6. When to Use and When to Avoid Lambdas ---")
print("\nUSE Lambdas for:")
print("- Simple, one-off functions needed as arguments to higher-order functions (`map`, `filter`, `sort`, `reduce`).")
print("- Concise code where a `def` function would be overkill.")
print("- Short callbacks/event handlers.")

print("\nAVOID Lambdas when:")
print("- The logic is complex or requires multiple statements/lines.")
print("- The function needs a docstring or type hints (for better documentation and maintainability).")
print("- You need to perform assignments, loop, or use `return` explicitly.")
print("- A named `def` function would make the code clearer and more readable.")


print("\n--- End of Python Lambda Functions Practice Code ---")