print("--- Python filter() Function: Practice Code ---")

# --- 1. What is filter()? ---
print("\n--- 1. What is filter()? ---")
print("The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.")
print("It's used to select elements from an iterable based on a specific condition.")
print("It provides a concise way to 'filter out' unwanted items.")

# The filter() function returns a filter object (an iterator)
my_numbers = [1, 2, 3, 4, 5, 6]
filter_object = filter(lambda x: x % 2 == 0, my_numbers)
print(f"A filter object: {filter_object}")
print(f"Type of filter object: {type(filter_object)}")

# To see the results, you typically convert it to a list, tuple, or iterate over it.
print(f"Filtered results (converted to list): {list(filter_object)}")
# Note: filter objects are iterators and can only be consumed once.
# If you try to convert filter_object to a list again, it will be empty.
print(f"Filtered results (consumed again): {list(filter_object)}")


# --- 2. Syntax of filter() ---
print("\n--- 2. Syntax of filter() ---")
print("Syntax: filter(function, iterable)")

# `function`: A function that returns a boolean value (True or False) for each element.
#             This function is often called a 'predicate'.
#             It can be a built-in function, a user-defined function (with `def`), or a `lambda` function.
#             If `function` is `None`, the identity function is assumed, and all elements that are truthy are returned.
# `iterable`: The iterable (list, tuple, set, string, etc.) to be filtered.


# --- 3. filter() with Different Types of Functions ---

# 3.1 Using a built-in function (or None for truthiness)
print("\n3.1 Using a built-in function (or None):")
data = [0, 1, [], [1, 2], "", "hello", None, False, True]
# When function is None, filter returns elements that are truthy.
truthy_elements = list(filter(None, data))
print(f"Original data: {data}")
print(f"Truthy elements (using filter(None, ...)): {truthy_elements}")

# Example: Filtering out empty strings
strings = ["apple", "", "banana", " ", "cherry", ""]
non_empty_strings = list(filter(bool, strings)) # bool() function returns True for non-empty strings
print(f"Original strings: {strings}")
print(f"Non-empty strings: {non_empty_strings}")

# 3.2 Using a user-defined function (with `def`)
print("\n3.2 Using a user-defined function:")
def is_prime(num):
    """Returns True if num is a prime number, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = list(filter(is_prime, numbers_to_check))
print(f"Original numbers: {numbers_to_check}")
print(f"Prime numbers: {prime_numbers}")

# 3.3 Using a lambda function (most common for simple conditions)
print("\n3.3 Using a lambda function:")
ages = [15, 22, 18, 30, 16, 25]
adult_ages = list(filter(lambda age: age >= 18, ages))
print(f"Ages: {ages}")
print(f"Adult ages: {adult_ages}")

# Filtering names starting with 'A'
names = ["Alice", "Bob", "Anna", "Charles", "Amanda"]
names_starting_with_a = list(filter(lambda name: name.startswith('A'), names))
print(f"Names: {names}")
print(f"Names starting with 'A': {names_starting_with_a}")


# --- 4. Lazy Evaluation of filter() ---
print("\n--- 4. Lazy Evaluation of filter() ---")
print("Like `map()` and generator expressions, `filter()` is lazy.")
print("It doesn't create a new collection with all filtered elements immediately.")
print("It yields elements one by one as they are requested, making it memory-efficient for large iterables.")

import sys
large_filter = filter(lambda x: x % 100 == 0, range(1_000_000_000))
print(f"Size of filter object itself: {sys.getsizeof(large_filter)} bytes (small)")

# Contrast with a list comprehension for the same operation (which creates all elements):
# large_list_comp = [x for x in range(1_000_000_000) if x % 100 == 0] # This would take significant memory
# print(f"Size of list comprehension result (for 1M elements): {sys.getsizeof(large_list_comp)} bytes (much larger)")


# --- 5. When to Use filter() vs. List Comprehensions ---
print("\n--- 5. When to Use filter() vs. List Comprehensions ---")

# Both can often achieve the same filtering results.

# Use filter() when:
# - You already have a function (or a simple lambda) that cleanly represents the filtering condition.
# - You need an iterator (lazy evaluation) for potentially very large datasets,
#   and you don't need a full list in memory immediately.
# - The function passed to filter is complex and might be defined separately for reusability.

print("\nExample where filter() is concise:")
numbers_to_filter = [1, -5, 10, 0, -3, 7]
positive_numbers = list(filter(lambda x: x > 0, numbers_to_filter))
print(f"Positive numbers (using filter): {positive_numbers}")

# Use List Comprehensions when:
# - You need both filtering AND transformation.
# - The filtering logic is simple and can be clearly expressed inline.
# - You explicitly need a list as the result.
# - Many Pythonistas find them more readable when both mapping and filtering are involved.

print("\nExample where List Comprehension is often preferred (filtering and transformation):")
numbers_comp = [1, 2, 3, 4, 5, 6]
squared_even_numbers = [num**2 for num in numbers_comp if num % 2 == 0]
print(f"Squared even numbers (list comp): {squared_even_numbers}")

# Doing the above with filter() and map() would be two steps:
even_numbers_filtered = filter(lambda x: x % 2 == 0, numbers_comp)
squared_numbers_mapped = list(map(lambda x: x**2, even_numbers_filtered))
print(f"Squared even numbers (filter/map): {squared_numbers_mapped}")
# For this case, list comprehension is generally considered more concise and readable.


print("\n--- End of Python filter() Function Practice Code ---")