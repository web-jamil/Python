print("--- Python map() Function: Practice Code ---")

# --- 1. What is map()? ---
print("\n--- 1. What is map()? ---")
print("The `map()` function applies a given function to every item of an iterable (or multiple iterables)")
print("and returns an iterator that yields the results.")
print("It's a functional programming construct that allows you to transform data concisely.")

# The map() function returns a map object (an iterator)
my_list = [1, 2, 3]
map_object = map(lambda x: x * 2, my_list)
print(f"A map object: {map_object}")
print(f"Type of map object: {type(map_object)}")

# To see the results, you typically convert it to a list, tuple, or iterate over it.
print(f"Results (converted to list): {list(map_object)}")
# Note: map objects are iterators and can only be consumed once.
# If you try to convert map_object to a list again, it will be empty.
print(f"Results (consumed again): {list(map_object)}")


# --- 2. Syntax of map() ---
print("\n--- 2. Syntax of map() ---")
print("Syntax: map(function, iterable, ...)")

# `function`: The function to apply to each item. It can be a built-in function,
#             a user-defined function (with `def`), or a `lambda` function.
# `iterable`: One or more iterables (lists, tuples, sets, strings, etc.)
#             If multiple iterables are provided, the function must accept that many arguments.
#             Iteration stops when the shortest iterable is exhausted.

# --- 3. map() with Different Types of Functions ---

# 3.1 Using a built-in function
print("\n3.1 Using a built-in function:")
numbers = [1.5, 2.7, 3.1, 4.9]
floored_numbers = list(map(int, numbers)) # int() converts float to integer (truncates)
print(f"Original floats: {numbers}")
print(f"Floored integers: {floored_numbers}")

string_numbers = ['1', '2', '3']
converted_to_int = list(map(int, string_numbers))
print(f"String numbers: {string_numbers}")
print(f"Converted to int: {converted_to_int}")

# 3.2 Using a user-defined function (with `def`)
print("\n3.2 Using a user-defined function:")
def capitalize_word(word):
    """Capitalizes the first letter of a word."""
    return word.capitalize()

words = ["apple", "banana", "cherry"]
capitalized_words = list(map(capitalize_word, words))
print(f"Original words: {words}")
print(f"Capitalized words: {capitalized_words}")

# 3.3 Using a lambda function (most common for simple transformations)
print("\n3.3 Using a lambda function:")
salaries = [50000, 60000, 75000]
raise_percentage = 1.05 # 5% raise
new_salaries = list(map(lambda salary: salary * raise_percentage, salaries))
print(f"Original salaries: {salaries}")
print(f"New salaries (5% raise): {new_salaries}")

# Lambda for string transformation
names = ["Alice", "Bob", "Charlie"]
greeting_messages = list(map(lambda name: f"Hello, {name}!", names))
print(f"Greeting messages: {greeting_messages}")


# --- 4. map() with Multiple Iterables ---
print("\n--- 4. map() with Multiple Iterables ---")
print("When using multiple iterables, the function passed to `map()` must accept")
print("as many arguments as there are iterables.")
print("The iteration stops when the shortest iterable is exhausted.")

# Example: Adding elements from two lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"List1: {list1}, List2: {list2}")
print(f"Sums of corresponding elements: {sums}")

# Example with different lengths (shorter iterable dictates length)
list_a = [1, 2, 3, 4]
list_b = [10, 20]
combined = list(map(lambda x, y: (x, y), list_a, list_b))
print(f"List A: {list_a}, List B: {list_b}")
print(f"Combined (stops at shortest): {combined}") # Output: [(1, 10), (2, 20)]

# Using zip() with map() (often equivalent, zip is also an iterator)
print(f"Using zip(): {list(zip(list_a, list_b))}")


# --- 5. Lazy Evaluation of map() ---
print("\n--- 5. Lazy Evaluation of map() ---")
print("Like generator expressions, `map()` is lazy. It doesn't compute all results at once.")
print("It yields results one by one as they are requested.")
print("This is memory-efficient for large iterables.")

# Example: Creating a large map object (without consuming it)
import sys
large_map = map(lambda x: x * 2, range(1_000_000_000))
print(f"Size of map object itself: {sys.getsizeof(large_map)} bytes (small)")

# Contrast with a list comprehension for the same operation (which creates all elements):
large_list_comp = [x * 2 for x in range(1_000_000)]
print(f"Size of list comprehension result (1M elements): {sys.getsizeof(large_list_comp)} bytes (much larger)")
del large_list_comp # Free up memory


# --- 6. When to Use map() vs. List Comprehensions ---
print("\n--- 6. When to Use map() vs. List Comprehensions ---")

# Both can often achieve the same results, but there are stylistic and minor performance differences.

# Use map() when:
# - You already have a function defined (or a simple lambda) that you want to apply to every item.
# - The operation is a simple transformation.
# - You need an iterator (lazy evaluation) rather than a full list in memory.
# - You're working with multiple iterables.

print("\nExample where map() is concise:")
import math
sqrt_values = list(map(math.sqrt, [1, 4, 9, 16]))
print(f"Square roots using map(math.sqrt, ...): {sqrt_values}")

# Use List Comprehensions when:
# - You need to filter elements (map doesn't filter directly).
# - The transformation logic is simple enough to fit inline without being too complex for readability.
# - You explicitly need a list as the result.
# - Many Pythonistas find them more readable for complex transformations or when filtering is involved.

print("\nExample where List Comprehension is often preferred (with filtering):")
numbers_comp = [1, 2, 3, 4, 5, 6]
filtered_and_squared = [num**2 for num in numbers_comp if num % 2 != 0]
print(f"Filtered and squared (list comp): {filtered_and_squared}")

# If you tried to do the above with map, it would be two steps:
filtered_numbers = filter(lambda x: x % 2 != 0, numbers_comp)
filtered_and_squared_map = list(map(lambda x: x**2, filtered_numbers))
print(f"Filtered and squared (map/filter): {filtered_and_squared_map}")
# For this case, list comprehension is more concise and readable.


print("\n--- End of Python map() Function Practice Code ---")