import sys # To demonstrate memory usage for generator expressions

print("--- Python Comprehensions: Practice Code ---")

# --- 1. What are Comprehensions? ---
print("\n--- 1. What are Comprehensions? ---")
print("Comprehensions provide a concise and elegant way to create lists, dictionaries, and sets.")
print("They offer a more readable and often more efficient alternative to traditional for loops and `append()` calls.")
print("There are four types: List, Dictionary, Set, and Generator Expressions.")


# --- 2. List Comprehensions ---
print("\n--- 2. List Comprehensions ---")
print("Syntax: [expression for item in iterable if condition]")

# 2.1 Basic List Comprehension: Squaring numbers
print("\n2.1 Basic List Comprehension: Squaring numbers")
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")

# Equivalent traditional loop:
# squared_numbers_loop = []
# for num in numbers:
#     squared_numbers_loop.append(num ** 2)
# print(f"Squared numbers (loop): {squared_numbers_loop}")


# 2.2 List Comprehension with Conditional Filtering
print("\n2.2 List Comprehension with Conditional Filtering: Even numbers")
numbers_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers_filter if num % 2 == 0]
print(f"Original numbers: {numbers_filter}")
print(f"Even numbers: {even_numbers}")

# 2.3 List Comprehension with Conditional Expression (if-else in expression part)
print("\n2.3 List Comprehension with Conditional Expression: Even/Odd labels")
# Note: The `if condition else expression` part comes *before* the `for` loop
labeled_numbers = ["Even" if num % 2 == 0 else "Odd" for num in numbers_filter]
print(f"Labeled numbers: {labeled_numbers}")

# 2.4 Nested List Comprehensions (Flattening a list of lists)
print("\n2.4 Nested List Comprehensions: Flattening a list of lists")
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened list: {flattened_list}")

# Equivalent traditional loop:
# flattened_list_loop = []
# for row in matrix:
#     for num in row:
#         flattened_list_loop.append(num)

# 2.5 Nested List Comprehensions with Conditions (Generating pairs)
print("\n2.5 Nested List Comprehensions with Conditions: (x, y) pairs")
# Generate (x, y) pairs where x is even and y is odd
pairs = [(x, y) for x in range(1, 4) if x % 2 == 0 for y in range(1, 4) if y % 2 != 0]
print(f"Pairs (x even, y odd): {pairs}")


# --- 3. Dictionary Comprehensions ---
print("\n--- 3. Dictionary Comprehensions ---")
print("Syntax: {key_expression: value_expression for item in iterable if condition}")

# 3.1 Basic Dictionary Comprehension: Mapping numbers to their squares
print("\n3.1 Basic Dictionary Comprehension:")
numbers_dict = {num: num ** 2 for num in range(1, 6)}
print(f"Numbers to squares: {numbers_dict}")

# 3.2 Dictionary Comprehension with Conditional Filtering
print("\n3.2 Dictionary Comprehension with Conditional Filtering:")
# Create a dict of numbers and their squares, but only for even numbers
even_squares_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print(f"Even numbers to squares: {even_squares_dict}")

# 3.3 Swapping Keys and Values in a dictionary
print("\n3.3 Swapping Keys and Values:")
old_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {value: key for key, value in old_dict.items()}
print(f"Original dictionary: {old_dict}")
print(f"Swapped dictionary: {swapped_dict}")

# 3.4 Creating a dictionary from two lists (using zip)
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
person_dict = {key: value for key, value in zip(keys, values)}
print(f"Dictionary from two lists: {person_dict}")


# --- 4. Set Comprehensions ---
print("\n--- 4. Set Comprehensions ---")
print("Syntax: {expression for item in iterable if condition}")
print("Sets automatically handle uniqueness.")

# 4.1 Basic Set Comprehension: Unique squared numbers
print("\n4.1 Basic Set Comprehension: Unique squared numbers")
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_squared_numbers = {num ** 2 for num in numbers_with_duplicates}
print(f"Original list (with duplicates): {numbers_with_duplicates}")
print(f"Unique squared numbers (set): {unique_squared_numbers}")

# 4.2 Set Comprehension with Filtering
print("\n4.2 Set Comprehension with Filtering: Unique even numbers")
text = "hello world python programming"
unique_vowels = {char for char in text if char in 'aeiou'}
print(f"Text: '{text}'")
print(f"Unique vowels: {unique_vowels}")


# --- 5. Generator Expressions ---
print("\n--- 5. Generator Expressions ---")
print("Syntax: (expression for item in iterable if condition)")
print("Generator expressions are similar to list comprehensions but use parentheses `()`.")
print("They return a generator object, which is an iterator.")
print("They are 'lazy': they generate values one by one on demand, not all at once.")
print("This makes them highly memory-efficient, especially for large datasets.")

# 5.1 Basic Generator Expression
print("\n5.1 Basic Generator Expression:")
gen_exp = (num * 2 for num in range(1, 6))
print(f"Generator object: {gen_exp}")
print(f"Type of generator object: {type(gen_exp)}")

# You can iterate over a generator expression only once:
print("Iterating over generator (first time):")
for value in gen_exp:
    print(value, end=" ")
print()

print("Iterating over generator (second time - will be empty):")
for value in gen_exp:
    print(value, end=" ") # Nothing will print here
print("(nothing printed)")

# To iterate again, you need to create a new generator object:
gen_exp2 = (num * 2 for num in range(1, 6))
print(f"New generator object to iterate again: {list(gen_exp2)}") # Convert to list to see all values

# 5.2 Memory Efficiency Example
print("\n5.2 Memory Efficiency Example (for large numbers):")
# List comprehension (creates all elements in memory)
large_list = [i for i in range(1_000_000)]
print(f"Memory used by list (1M elements): {sys.getsizeof(large_list)} bytes")

# Generator expression (creates elements on the fly)
large_generator = (i for i in range(1_000_000))
print(f"Memory used by generator (1M elements): {sys.getsizeof(large_generator)} bytes (much smaller!)")
# The generator object itself is small; it doesn't hold all 1M numbers.

# When to use Generator Expressions:
# - When working with very large datasets where memory is a concern.
# - When you only need to iterate over the items once.
# - As arguments to functions that accept iterators (e.g., `sum()`, `min()`, `max()`, `any()`, `all()`).

total_sum = sum(i for i in range(1, 1_000_001)) # Sums numbers without creating a giant list
print(f"Sum of 1 to 1M (using generator expression): {total_sum}")


# --- 6. Best Practices and Readability ---
print("\n--- 6. Best Practices and Readability ---")
print("Comprehensions are powerful, but don't overcomplicate them.")

# Good: Simple transformation or filtering
processed_data = [item.strip().lower() for item in ["  Apple ", " BANANA", " cherry  "]]
print(f"Cleaned strings: {processed_data}")

# Potentially Bad: Too complex, may be harder to read than a loop
# complex_result = [
#     (x, y, z)
#     for x in range(10) if x % 2 == 0
#     for y in range(10) if y % 3 == 0
#     for z in range(10) if z % 5 == 0 and x+y+z > 10
# ]
# In such cases, a regular for loop might be more readable and maintainable.


print("\n--- End of Python Comprehensions Practice Code ---")