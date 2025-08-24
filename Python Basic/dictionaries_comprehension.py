# --- Python Dictionaries: All About Dictionary Comprehensions in Code ---

# Dictionary comprehensions provide a concise and efficient way to create
# dictionaries from iterables, often with transformations or filtering applied.
# They are a more readable and often faster alternative to traditional for loops
# for dictionary creation.

# --- 1. Basic Syntax of Dictionary Comprehension ---

print("--- 1. Basic Syntax ---")

# The general syntax is:
# {key_expression: value_expression for item in iterable if condition}

# - `key_expression`: An expression that defines the key for each item.
# - `value_expression`: An expression that defines the value for each item.
# - `item`: The variable that takes on each value from the `iterable`.
# - `iterable`: Any object that can be iterated over (e.g., list, tuple, string, range, another dictionary).
# - `if condition` (optional): A filter that includes only items for which the condition is True.

# Example 1.1: Creating a dictionary where keys are numbers and values are their squares.
# Equivalent to:
# squares = {}
# for num in range(1, 6):
#     squares[num] = num**2
squares = {num: num**2 for num in range(1, 6)}
print(f"1.1 Squares Dictionary: {squares}")
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 1.2: Mapping strings to their lengths.
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(f"1.2 Word Lengths: {word_lengths}")
# Output: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}


# --- 2. Dictionary Comprehension with Conditional Filtering ---

print("\n--- 2. With Conditional Filtering ---")

# You can include an `if` clause to filter items from the iterable.

# Example 2.1: Only include even numbers and their cubes.
# Equivalent to:
# even_cubes = {}
# for num in range(10):
#     if num % 2 == 0:
#         even_cubes[num] = num**3
even_cubes = {num: num**3 for num in range(10) if num % 2 == 0}
print(f"2.1 Even Numbers and their Cubes: {even_cubes}")
# Output: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# Example 2.2: Filter words longer than 5 characters.
long_words = {word: len(word) for word in words if len(word) > 5}
print(f"2.2 Long Words (length > 5): {long_words}")
# Output: {'banana': 6, 'cherry': 6}

# Example 2.3: Conditional assignment of values (using a ternary operator)
# Assign 'Even' or 'Odd' based on the number.
even_odd_status = {num: "Even" if num % 2 == 0 else "Odd" for num in range(5)}
print(f"2.3 Even/Odd Status: {even_odd_status}")
# Output: {0: 'Even', 1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even'}


# --- 3. Creating Dictionaries from Existing Dictionaries ---

print("\n--- 3. From Existing Dictionaries ---")

# Dictionary comprehensions are excellent for transforming or filtering
# existing dictionaries.

# Example 3.1: Swapping keys and values (values must be hashable to become keys).
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(f"3.1 Inverted Dictionary: {inverted_dict}")
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Example 3.2: Filtering items from an existing dictionary.
filtered_items = {key: value for key, value in original_dict.items() if value > 1}
print(f"3.2 Filtered Items (value > 1): {filtered_items}")
# Output: {'b': 2, 'c': 3}

# Example 3.3: Transforming values in an existing dictionary.
# Make values strings and add a prefix.
transformed_values = {key: f"Value_{value}" for key, value in original_dict.items()}
print(f"3.3 Transformed Values: {transformed_values}")
# Output: {'a': 'Value_1', 'b': 'Value_2', 'c': 'Value_3'}

# Example 3.4: Creating a new dictionary with only specific keys
selected_keys_dict = {k: original_dict[k] for k in ["a", "c"]}
print(f"3.4 Selected Keys Dictionary: {selected_keys_dict}")
# Output: {'a': 1, 'c': 3}


# --- 4. Nested Dictionary Comprehensions (Less Common, More Complex) ---

print("\n--- 4. Nested Dictionary Comprehensions ---")

# While possible, nested comprehensions can quickly become hard to read.
# Use them judiciously.

# Example 4.1: Create a dictionary of dictionaries (e.g., student scores per subject)
subjects = ["Math", "Physics"]
students = ["Alice", "Bob"]
# This example is more illustrative of structure than practical use for nested dict comp
# A loop or pre-defined data structure is often clearer for this.
student_scores = {
    student: {
        subject: random.randint(70, 100) for subject in subjects
    } for student in students
}
print(f"4.1 Nested Student Scores: {student_scores}")
# Output example: {'Alice': {'Math': 85, 'Physics': 92}, 'Bob': {'Math': 78, 'Physics': 89}}


# --- 5. Performance and Readability ---

print("\n--- 5. Performance and Readability ---")

# - **Readability:** For simple transformations and filtering, dictionary comprehensions
#   are generally more readable than equivalent `for` loops.
# - **Performance:** They are often more efficient than `for` loops because they are
#   optimized at the C level in Python's interpreter.

# Example of readability comparison:
# Using comprehension
comprehension_dict = {i: i*i for i in range(5)}

# Equivalent using a loop
loop_dict = {}
for i in range(5):
    loop_dict[i] = i*i

print(f"Comprehension: {comprehension_dict}")
print(f"Loop:          {loop_dict}")

# For complex logic, multiple lines with a loop might be clearer.
# For simple, single-line transformations, comprehensions shine.