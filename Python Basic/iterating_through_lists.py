# --- Python Lists: All About Iterating Through Them in Code ---

# Iterating through a list means visiting each element in the list, typically
# from the first element to the last, to perform some operation or access its value.
# Python provides several convenient ways to do this.

# Let's define a sample list for demonstration.
my_fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("--- 1. Basic Iteration using a `for` loop ---")

# This is the most common and Pythonic way to iterate when you only need the elements themselves.

print("1.1 Iterating directly over the list:")
for fruit in my_fruits:
    print(f"  Current fruit: {fruit}")

# Example: Performing an action for each element
print("\n1.2 Printing each fruit with a prefix:")
for fruit in my_fruits:
    print(f"  I love {fruit}!")


print("\n--- 2. Iterating with Index using `range()` and `len()` ---")

# This method is used when you need both the element and its index.
# It's less Pythonic than `enumerate()` for just getting the index, but useful
# when you need to perform actions based on the index itself (e.g., modifying
# the list in-place at a specific index, though careful with that).

print("2.1 Iterating using `range(len(list))`:")
for i in range(len(my_fruits)):
    print(f"  Fruit at index {i}: {my_fruits[i]}")

# Example: Modifying elements based on their index (in-place)
numbers = [10, 20, 30, 40]
print(f"\n2.2 Original numbers list: {numbers}")
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2 # Double each number
print(f"    Numbers after doubling: {numbers}")


print("\n--- 3. Iterating with Index and Value using `enumerate()` ---")

# This is the most Pythonic and recommended way to get both the index and the value
# simultaneously during iteration.

print("3.1 Iterating using `enumerate()`:")
for index, fruit in enumerate(my_fruits):
    print(f"  Index {index}: {fruit}")

# Example: Printing elements with their position number (starting from 1)
print("\n3.2 Printing items with 1-based numbering:")
for i, item in enumerate(my_fruits, start=1): # Start numbering from 1
    print(f"  Item {i}: {item}")


print("\n--- 4. Iterating Over Multiple Lists Simultaneously using `zip()` ---")

# The `zip()` function allows you to iterate over multiple iterables (lists, tuples, etc.)
# in parallel. It stops when the shortest iterable is exhausted.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
cities = ["New York", "London", "Paris"]

print("4.1 Iterating over three lists using `zip()`:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old and lives in {city}.")

# 4.2 Handling lists of different lengths with `zip()`
short_list = [1, 2]
long_list = ["a", "b", "c", "d"]
print("\n4.2 `zip()` with lists of different lengths (stops at shortest):")
for num, char in zip(short_list, long_list):
    print(f"  Number: {num}, Character: {char}")
# Output will only be for (1, 'a') and (2, 'b')


# --- 5. Iterating in Reverse Order ---

print("\n--- 5. Iterating in Reverse Order ---")

# 5.1 Using `reversed()` function: Returns an iterator that yields elements in reverse order.
# - Does NOT modify the original list.
print("5.1 Iterating in reverse using `reversed()`:")
for fruit in reversed(my_fruits):
    print(f"  Reverse fruit: {fruit}")

# 5.2 Using slicing with a negative step `[::-1]` (creates a new reversed list)
# - Creates a new reversed list in memory. For very large lists, `reversed()` is more memory efficient.
print("\n5.2 Iterating in reverse using slicing `[::-1]`:")
for fruit in my_fruits[::-1]:
    print(f"  Reverse fruit (slicing): {fruit}")


print("\n--- 6. Iterating with `while` loop (Less Common for Lists) ---")

# While possible, `for` loops are generally preferred for iterating through lists
# due to their simplicity and safety. A `while` loop is typically used when the
# iteration condition is not based on a fixed sequence length (e.g., user input,
# specific condition being met).

print("6.1 Iterating using a `while` loop:")
index = 0
while index < len(my_fruits):
    print(f"  Fruit at index {index}: {my_fruits[index]}")
    index += 1


print("\n--- 7. Important: Modifying a List While Iterating ---")

# This is a common pitfall. Modifying a list (adding or removing elements) while
# iterating over it directly can lead to unexpected behavior or `RuntimeError`.

# 7.1 UNSAFE example (DO NOT USE IN PRODUCTION CODE)
# This code is commented out because it's problematic.
# numbers_to_filter = [1, 2, 3, 4, 5, 6]
# print(f"7.1 UNSAFE: Original list: {numbers_to_filter}")
# try:
#     for num in numbers_to_filter:
#         if num % 2 == 0:
#             numbers_to_filter.remove(num) # Modifying the list being iterated over
#     print(f"    Result (might be unexpected): {numbers_to_filter}")
# except RuntimeError as e:
#     print(f"    Caught expected RuntimeError: {e}")

# 7.2 SAFE way 1: Iterate over a copy of the list
# Create a shallow copy of the list to iterate over, while modifying the original.
safe_filter_list = [1, 2, 3, 4, 5, 6]
print(f"\n7.2 SAFE Way 1: Original list: {safe_filter_list}")
for item in safe_filter_list.copy(): # Iterate over a copy
    if item % 2 == 0:
        safe_filter_list.remove(item) # Modify the original list
print(f"    Result after safe removal: {safe_filter_list}") # [1, 3, 5]

# 7.3 SAFE way 2: Use a list comprehension to create a new list
# This is often the most Pythonic, readable, and efficient way to filter or transform elements.
original_numbers = [1, 2, 3, 4, 5, 6]
new_filtered_list = [num for num in original_numbers if num % 2 != 0]
print(f"\n7.3 SAFE Way 2: New filtered list: {new_filtered_list}") # [1, 3, 5]
print(f"    Original list remains unchanged: {original_numbers}")