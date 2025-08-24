from functools import reduce
import operator # For common operations in reduce examples

print("--- Python functools.reduce() Function: Practice Code ---")

# --- 1. What is functools.reduce()? ---
print("\n--- 1. What is functools.reduce()? ---")
print("`reduce()` is a function from the `functools` module.")
print("It applies a given function cumulatively to the items of an iterable,")
print("from left to right, so as to reduce the iterable to a single cumulative result.")
print("It's part of functional programming paradigms, often called 'fold' or 'aggregate' in other languages.")


# --- 2. Syntax of reduce() ---
print("\n--- 2. Syntax of reduce() ---")
print("Syntax: reduce(function, iterable[, initializer])")

# `function`: A function of two arguments (accumulator, current_item).
#             It's applied to the items of the iterable.
#             The function returns a single value, which becomes the new accumulator.
# `iterable`: The sequence (list, tuple, etc.) to be reduced.
# `initializer` (optional): An initial value for the accumulator.
#             If provided, the function is first called with the initializer and the first item.
#             If not provided, the first two items of the iterable are used to start the accumulation.
#             If the iterable is empty and no initializer is given, `reduce()` raises a TypeError.


# --- 3. Basic Usage: Summation ---
print("\n--- 3. Basic Usage: Summation ---")

numbers = [1, 2, 3, 4, 5]

# 3.1 Without Initializer:
# 1. func(1, 2) = 3 (accumulator is 3)
# 2. func(3, 3) = 6 (accumulator is 6)
# 3. func(6, 4) = 10 (accumulator is 10)
# 4. func(10, 5) = 15 (accumulator is 15)
sum_result_no_init = reduce(lambda x, y: x + y, numbers)
print(f"Sum of {numbers} (no initializer): {sum_result_no_init}")

# Equivalent to `sum(numbers)` but demonstrates `reduce`
print(f"Sum of {numbers} (using built-in sum()): {sum(numbers)}")


# 3.2 With Initializer:
# If initializer is 100:
# 1. func(100, 1) = 101 (accumulator is 101)
# 2. func(101, 2) = 103 (accumulator is 103)
# ...
sum_result_with_init = reduce(lambda x, y: x + y, numbers, 100)
print(f"Sum of {numbers} (with initializer 100): {sum_result_with_init}")

# Example with an empty list and initializer
empty_list = []
sum_empty_with_init = reduce(lambda x, y: x + y, empty_list, 0)
print(f"Sum of empty list (with initializer 0): {sum_empty_with_init}")

# What happens with an empty list without initializer:
try:
    reduce(lambda x, y: x + y, empty_list)
except TypeError as e:
    print(f"Caught TypeError for empty list without initializer: {e}")


# --- 4. reduce() with Different Operations ---
print("\n--- 4. reduce() with Different Operations ---")

# 4.1 Product of elements
numbers_for_prod = [1, 2, 3, 4, 5]
product_result = reduce(lambda x, y: x * y, numbers_for_prod)
print(f"Product of {numbers_for_prod}: {product_result}")

# 4.2 Concatenating strings
words = ["Python", "is", "awesome"]
sentence = reduce(lambda acc, word: acc + " " + word, words)
print(f"Concatenated words: '{sentence}'")
# Note: If words was empty and no initializer, it would error.
# With initializer:
empty_words = []
sentence_empty = reduce(lambda acc, word: acc + " " + word, empty_words, "")
print(f"Concatenated empty words (with initializer): '{sentence_empty}'")


# 4.3 Finding the maximum element (without built-in max())
numbers_for_max = [10, 5, 23, 7, 18]
max_value = reduce(lambda current_max, item: current_max if current_max > item else item, numbers_for_max)
print(f"Max value in {numbers_for_max}: {max_value}")


# 4.4 Using functions from the `operator` module (often cleaner than lambdas)
print("\n4.4 Using functions from `operator` module:")
# operator.add is equivalent to lambda x, y: x + y
# operator.mul is equivalent to lambda x, y: x * y
sum_op = reduce(operator.add, numbers)
print(f"Sum using operator.add: {sum_op}")

product_op = reduce(operator.mul, numbers_for_prod)
print(f"Product using operator.mul: {product_op}")

# operator.concat for strings
concat_op = reduce(operator.concat, words)
print(f"Concatenated using operator.concat: {concat_op}")


# --- 5. reduce() with Complex Data Structures ---
print("\n--- 5. reduce() with Complex Data Structures ---")

# 5.1 Flattening a list of lists
list_of_lists = [[1, 2], [3, 4, 5], [6]]
flattened_list = reduce(lambda acc, sublist: acc + sublist, list_of_lists)
print(f"Flattened list: {flattened_list}")

# 5.2 Counting occurrences (like Counter, but demonstrating reduce)
items = ['a', 'b', 'a', 'c', 'b', 'a']
def count_items(accumulator, item):
    accumulator[item] = accumulator.get(item, 0) + 1
    return accumulator

counts = reduce(count_items, items, {}) # Initializer is an empty dictionary
print(f"Counts of items: {counts}")


# --- 6. When to Use reduce() and Alternatives ---
print("\n--- 6. When to Use reduce() and Alternatives ---")
print("`reduce()` can be powerful but often less readable than explicit loops or other built-in functions.")

# 6.1 Alternatives for common operations
print("\nAlternatives for common operations:")
my_data = [1, 2, 3, 4]

# Sum:
# reduce(operator.add, my_data)
print(f"Sum (built-in): {sum(my_data)}")

# Max/Min:
# reduce(lambda x,y: x if x>y else y, my_data)
print(f"Max (built-in): {max(my_data)}")

# All/Any (logical AND/OR of booleans):
bools = [True, True, False, True]
# reduce(lambda x,y: x and y, bools)
print(f"All (built-in): {all(bools)}")
# reduce(lambda x,y: x or y, bools)
print(f"Any (built-in): {any(bools)}")

# Flattening list of lists:
# reduce(operator.add, list_of_lists)
# Often better with list comprehension:
flattened_comp = [item for sublist in list_of_lists for item in sublist]
print(f"Flattened (list comprehension): {flattened_comp}")

print("\nGeneral Recommendation:")
print("- Use `reduce()` when you need to apply a binary function cumulatively to an iterable to reduce it to a single value.")
print("- For simple cases like sum, min, max, all, any, prefer the built-in functions as they are more readable and often optimized.")
print("- For more complex aggregations, a `for` loop might be clearer, especially if the accumulator logic is not straightforward.")
print("- `reduce()` is often used in functional programming contexts.")


print("\n--- End of Python functools.reduce() Function Practice Code ---")