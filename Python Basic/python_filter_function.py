# ---------------------------------------------------
# filter() in Python
# ---------------------------------------------------

# The `filter()` function constructs an iterator from elements of an iterable for
# which a function returns true.

# Syntax: filter(function, iterable)
#   - function: A function to be tested for each element of the iterable.
#               If `None`, the identity function is used (i.e., all falsy
#               elements are removed).
#   - iterable: An iterable (like a list, tuple, set, string, etc.)

# The `filter()` function returns an iterator. To see the results, you usually
# convert it to a list, tuple, or another iterable.

# 1. Basic Usage with a User-Defined Function

print("--- 1. Basic Usage with a User-Defined Function ---")

def is_even(num):
    """Returns True if the number is even, False otherwise."""
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out even numbers
even_numbers_iterator = filter(is_even, numbers)
even_numbers_list = list(even_numbers_iterator)
print(f"Original numbers: {numbers}")
print(f"Even numbers (list): {even_numbers_list}") # Output: [2, 4, 6, 8, 10]

# Filter out odd numbers (by negating the `is_even` result)
def is_odd(num):
    return not is_even(num)

odd_numbers_iterator = filter(is_odd, numbers)
odd_numbers_list = list(odd_numbers_iterator)
print(f"Odd numbers (list): {odd_numbers_list}")   # Output: [1, 3, 5, 7, 9]

# 2. Using `filter()` with a `lambda` function (Common Use Case)

print("\n--- 2. Using filter() with a lambda function ---")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greater_than_5}") # Output: [6, 7, 8, 9, 10]

# Filter strings that start with 'a'
words = ["apple", "banana", "apricot", "cherry", "date"]
a_words = list(filter(lambda word: word.startswith('a'), words))
print(f"Words starting with 'a': {a_words}") # Output: ['apple', 'apricot']

# 3. Using `filter()` with `None` as the function (Falsy/Truthy Check)

print("\n--- 3. Using filter() with None ---")

# When `function` is None, `filter()` removes all "falsy" elements.
# Falsy values include: 0, 0.0, '', [], {}, (), None, False.

mixed_list = [0, 1, 'hello', '', False, True, [], [1, 2], None, {'key': 'value'}]
truthy_elements = list(filter(None, mixed_list))
print(f"Original mixed list: {mixed_list}")
print(f"Truthy elements: {truthy_elements}")
# Output: [1, 'hello', True, [1, 2], {'key': 'value'}]

# 4. Filtering Different Data Types

print("\n--- 4. Filtering Different Data Types ---")

# Filtering a list of strings
names = ["Alice", "", "Bob", None, "Charlie", ""]
valid_names = list(filter(None, names)) # Removes empty strings and None
print(f"Valid names: {valid_names}") # Output: ['Alice', 'Bob', 'Charlie']

# Filtering a tuple of numbers
temperatures = (25, 18, 30, -5, 0, 15)
positive_temps = tuple(filter(lambda t: t > 0, temperatures))
print(f"Positive temperatures: {positive_temps}") # Output: (25, 18, 30, 15)

# Filtering a set
scores = {10, 20, 5, 30, 15}
high_scores = set(filter(lambda s: s >= 20, scores))
print(f"High scores: {high_scores}") # Output: {20, 30} (order might vary for sets)

# 5. filter() vs List Comprehensions (Common Alternative)

# List comprehensions are often preferred for their readability and flexibility.
# They can achieve the same filtering results, and more.

print("\n--- 5. filter() vs List Comprehensions ---")

# Using filter()
filtered_by_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered by filter(): {filtered_by_filter}")

# Using a list comprehension
filtered_by_comprehension = [x for x in numbers if x % 2 == 0]
print(f"Filtered by list comprehension: {filtered_by_comprehension}")

# List comprehensions can also transform elements (which filter() cannot do directly)
transformed_and_filtered = [x * 2 for x in numbers if x % 2 == 0]
print(f"Transformed and filtered by comprehension: {transformed_and_filtered}")
# Output: [4, 8, 12, 16, 20] (filter() would only give [2, 4, 6, 8, 10])

# 6. Chaining `filter()` (Less common, but possible)

print("\n--- 6. Chaining filter() ---")

# Filter numbers that are even AND greater than 5
# Method 1: Single lambda
chained_filter_single_lambda = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))
print(f"Chained filter (single lambda): {chained_filter_single_lambda}") # Output: [6, 8, 10]

# Method 2: Chaining filter objects (less readable, but demonstrates iterator chaining)
temp_filter_result = filter(lambda x: x % 2 == 0, numbers)
final_chained_filter = list(filter(lambda x: x > 5, temp_filter_result))
print(f"Chained filter (chained objects): {final_chained_filter}") # Output: [6, 8, 10]

# 7. filter() with Complex Objects

print("\n--- 7. filter() with Complex Objects ---")

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.city})"

people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "London"),
    Person("Charlie", 35, "New York"),
    Person("David", 22, "Paris"),
]

# Filter people older than 28
older_people = list(filter(lambda p: p.age > 28, people))
print(f"People older than 28: {older_people}")
# Output: [Person(Alice, 30, New York), Person(Charlie, 35, New York)]

# Filter people from "New York"
ny_people = list(filter(lambda p: p.city == "New York", people))
print(f"People from New York: {ny_people}")
# Output: [Person(Alice, 30, New York), Person(Charlie, 35, New York)]

# 8. filter() on Dictionaries (items(), keys(), values())

print("\n--- 8. filter() on Dictionaries ---")

my_dict = {'a': 10, 'b': 5, 'c': 12, 'd': 8}

# Filter items where value > 7
filtered_items = dict(filter(lambda item: item[1] > 7, my_dict.items()))
print(f"Filtered dictionary items (value > 7): {filtered_items}") # Output: {'a': 10, 'c': 12, 'd': 8}

# Filter keys that are 'b' or 'd'
filtered_keys = list(filter(lambda key: key in ['b', 'd'], my_dict.keys()))
print(f"Filtered dictionary keys ('b' or 'd'): {filtered_keys}") # Output: ['b', 'd']

# 9. Performance Considerations (Lazy Evaluation)

print("\n--- 9. Performance Considerations (Lazy Evaluation) ---")

# filter() returns an iterator, which means it evaluates elements lazily.
# This is memory-efficient for large iterables because it doesn't create
# a new list in memory immediately.

def expensive_check(n):
    print(f"Checking {n} (expensive operation)...")
    return n % 2 == 0

large_numbers = range(1, 15) # Creates a range object, not a list
filtered_large_numbers = filter(expensive_check, large_numbers)

print("Created filter object. No checks performed yet.")

# Checks are performed only when you iterate over the filter object
for num in filtered_large_numbers:
    print(f"Found even number: {num}")
    if num == 6:
        break # Stop iteration early to demonstrate partial evaluation

print("Iteration stopped. Not all numbers were checked.")

# If you convert to a list immediately, all checks are performed at once:
print("\n--- Immediate Conversion to List (All checks performed) ---")
all_even_numbers = list(filter(expensive_check, large_numbers))
print(f"All even numbers: {all_even_numbers}")

# 10. `filter()` in Functional Programming Contexts

# While list comprehensions are often more "Pythonic" for simple cases,
# `filter()` fits well into a functional programming style, especially when
# chaining operations (map, filter, reduce).

from functools import reduce

print("\n--- 10. Functional Programming Contexts ---")

numbers_fp = [1, 2, 3, 4, 5, 6]

# Find sum of squares of even numbers
# 1. Filter even numbers
even_nums_it = filter(lambda x: x % 2 == 0, numbers_fp)
# 2. Map (transform) to squares
squared_even_nums_it = map(lambda x: x * x, even_nums_it)
# 3. Reduce (aggregate) to sum
sum_of_squares = reduce(lambda acc, x: acc + x, squared_even_nums_it)

print(f"Sum of squares of even numbers: {sum_of_squares}") # Output: 56 (4+16+36)

# Equivalent with list comprehension:
sum_of_squares_comp = sum([x * x for x in numbers_fp if x % 2 == 0])
print(f"Sum of squares (comprehension): {sum_of_squares_comp}")


# End of filter() examples