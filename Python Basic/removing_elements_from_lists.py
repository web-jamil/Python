# --- Python Lists: All About Removing Elements in Code ---

# Lists are mutable, which means you can remove elements from them
# after they have been created. Python provides several ways to do this,
# each with its own use case and behavior.

# Let's start with a sample list for demonstration.
my_list = ["apple", "banana", "cherry", "date", "banana", "elderberry", "fig"]

print("--- 1. Removing by Value: `remove()` Method ---")

# 1.1 `remove(value)`:
# - **Purpose:** Removes the *first* occurrence of the specified `value` from the list.
# - **Syntax:** `list.remove(value)`
# - **Returns:** `None` (modifies the list in-place).
# - **Raises:** `ValueError` if the `value` is not found in the list.

print(f"1.1 Original list: {my_list}")
my_list.remove("banana") # Removes the first 'banana'
print(f"    After remove('banana'): {my_list}") # ['apple', 'cherry', 'date', 'banana', 'elderberry', 'fig']

# Attempting to remove a value that is not in the list
try:
    print("\n    Attempting to remove 'grape' (not in list)...")
    my_list.remove("grape")
except ValueError as e:
    print(f"    Error: {e} - Value 'grape' not found in list.")

# Removing another occurrence of 'banana'
my_list.remove("banana")
print(f"    After removing second 'banana': {my_list}") # ['apple', 'cherry', 'date', 'elderberry', 'fig']


print("\n--- 2. Removing by Index: `pop()` Method ---")

# 2.1 `pop(index=-1)`:
# - **Purpose:** Removes and returns the element at the specified `index`.
#   If no `index` is provided, it removes and returns the *last* element.
# - **Syntax:** `list.pop(index)`
# - **Returns:** The element that was removed.
# - **Raises:** `IndexError` if the `index` is out of range (for non-empty lists).

my_pop_list = [10, 20, 30, 40, 50]
print(f"2.1 Original list: {my_pop_list}")

# Remove element at a specific index
popped_item_at_index_1 = my_pop_list.pop(1) # Removes 20
print(f"    Popped item at index 1: {popped_item_at_index_1}")
print(f"    After pop(1): {my_pop_list}") # [10, 30, 40, 50]

# Remove the last element (default behavior)
popped_last_item = my_pop_list.pop() # Removes 50
print(f"    Popped last item (default pop()): {popped_last_item}")
print(f"    After pop(): {my_pop_list}") # [10, 30, 40]

# Attempting to pop from an empty list
empty_list = []
try:
    print("\n    Attempting to pop from an empty list...")
    empty_list.pop()
except IndexError as e:
    print(f"    Error: {e} - Cannot pop from an empty list.")

# Attempting to pop an out-of-range index
try:
    print("\n    Attempting to pop at index 99 (out of range)...")
    my_pop_list.pop(99)
except IndexError as e:
    print(f"    Error: {e} - Index 99 is out of range.")


print("\n--- 3. Removing by Index or Slice: `del` Keyword ---")

# 3.1 `del list[index]` or `del list[start:end:step]`:
# - **Purpose:** Deletes element(s) from the list by their index or slice.
# - **Syntax:** `del list[index]` or `del list[slice]`
# - **Returns:** `None` (modifies the list in-place).
# - **Raises:** `IndexError` if the index is out of range.

my_del_list = ["one", "two", "three", "four", "five"]
print(f"3.1 Original list: {my_del_list}")

# Delete a single element by index
del my_del_list[1] # Deletes 'two'
print(f"    After del my_del_list[1]: {my_del_list}") # ['one', 'three', 'four', 'five']

# Delete a slice of elements
del my_del_list[1:3] # Deletes 'three' and 'four'
print(f"    After del my_del_list[1:3]: {my_del_list}") # ['one', 'five']

# Delete elements with a step
my_del_list_step = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\n    Original list for step deletion: {my_del_list_step}")
del my_del_list_step[::2] # Deletes elements at even indices (0, 2, 4, 6, 8)
print(f"    After del my_del_list_step[::2]: {my_del_list_step}") # [1, 3, 5, 7, 9]

# Attempting to delete an out-of-range index
try:
    print("\n    Attempting to del at index 99 (out of range)...")
    del my_del_list[99]
except IndexError as e:
    print(f"    Error: {e} - Index 99 is out of range.")


print("\n--- 4. Removing All Elements: `clear()` Method ---")

# 4.1 `clear()`:
# - **Purpose:** Removes all elements from the list, making it empty.
# - **Syntax:** `list.clear()`
# - **Returns:** `None` (modifies the list in-place).

my_clear_list = ["A", "B", "C"]
print(f"4.1 Original list: {my_clear_list}")
my_clear_list.clear()
print(f"    After clear(): {my_clear_list}") # []


print("\n--- 5. Deleting the Entire List Object ---")

# 5.1 `del list_variable`:
# - **Purpose:** Deletes the list variable itself from memory.
# - **Syntax:** `del list_variable`
# - **Returns:** `None`.
# - **Raises:** `NameError` if you try to access the variable after deletion.

my_entire_list = [100, 200, 300]
print(f"5.1 Before deleting the variable: {my_entire_list}")
del my_entire_list # The variable `my_entire_list` is now gone.

try:
    print(my_entire_list) # This line will cause an error
except NameError as e:
    print(f"    Error: {e} - The list variable 'my_entire_list' no longer exists.")


print("\n--- 6. Important: Removing Elements While Iterating ---")

# Modifying a list (adding or removing elements) while iterating over it
# directly can lead to unexpected behavior, skipping elements, or a `RuntimeError`.

# 6.1 UNSAFE example (DO NOT USE IN PRODUCTION CODE)
# This code is commented out because it's problematic.
# numbers_to_filter = [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"6.1 UNSAFE: Original list: {numbers_to_filter}")
# try:
#     for num in numbers_to_filter:
#         if num % 2 == 0:
#             numbers_to_filter.remove(num) # Modifying the list being iterated over
#     print(f"    Result (might be unexpected): {numbers_to_filter}")
# except RuntimeError as e:
#     print(f"    Caught expected RuntimeError: {e}")
# # Output might be [1, 3, 5, 7] or [1, 3, 5, 7, 8] depending on Python version/implementation.

# 6.2 SAFE way 1: Iterate over a copy of the list
# Create a shallow copy of the list to iterate over, while modifying the original.
safe_filter_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"\n6.2 SAFE Way 1: Original list: {safe_filter_list}")
for item in safe_filter_list.copy(): # Iterate over a copy
    if item % 2 == 0:
        safe_filter_list.remove(item) # Modify the original list
print(f"    Result after safe removal: {safe_filter_list}") # [1, 3, 5, 7]

# 6.3 SAFE way 2: Use a list comprehension to create a new list
# This is often the most Pythonic, readable, and efficient way to filter elements.
original_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_filtered_list = [num for num in original_numbers if num % 2 != 0]
print(f"\n6.3 SAFE Way 2: New filtered list: {new_filtered_list}") # [1, 3, 5, 7]
print(f"    Original list remains unchanged: {original_numbers}")