# --- Python Lists: All About Methods in Code ---

# Lists are mutable, ordered collections of items. They come with a rich set
# of built-in methods that allow you to modify, query, and manipulate their contents
# in-place.

# Let's define a sample list for demonstration.
my_list = ["apple", "banana", "cherry", "date"]


print("--- 1. Methods for Adding Elements ---")

# 1.1 `append(item)`: Adds a single `item` to the end of the list.
# - Modifies in-place, returns `None`.
print(f"1.1 Original list: {my_list}")
my_list.append("elderberry")
print(f"    After append('elderberry'): {my_list}") # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 1.2 `insert(index, item)`: Inserts an `item` at a specified `index`.
# - Elements from that index onwards are shifted to the right.
# - Modifies in-place, returns `None`.
my_list.insert(0, "apricot") # Insert at the beginning
print(f"1.2 After insert(0, 'apricot'): {my_list}") # ['apricot', 'apple', 'banana', ...]
my_list.insert(3, "fig") # Insert in the middle
print(f"    After insert(3, 'fig'): {my_list}") # ['apricot', 'apple', 'banana', 'fig', 'cherry', ...]

# 1.3 `extend(iterable)`: Adds all elements from an `iterable` to the end of the list.
# - The elements are added individually, not as a single nested item.
# - Modifies in-place, returns `None`.
my_list.extend(["grape", "honeydew"]) # Extend with another list
print(f"1.3 After extend(['grape', 'honeydew']): {my_list}")
my_list.extend(("kiwi", "lemon")) # Extend with a tuple
print(f"    After extend(('kiwi', 'lemon')): {my_list}")
my_list.extend("mango") # Extend with a string (adds characters individually)
print(f"    After extend('mango'): {my_list}")


print("\n--- 2. Methods for Removing Elements ---")

current_list_for_removal = ["red", "green", "blue", "green", "yellow", "purple"]

# 2.1 `remove(value)`: Removes the *first* occurrence of the specified `value`.
# - Modifies in-place, returns `None`.
# - Raises `ValueError` if `value` is not found.
print(f"2.1 Original list: {current_list_for_removal}")
current_list_for_removal.remove("green") # Removes the first 'green'
print(f"    After remove('green'): {current_list_for_removal}") # ['red', 'blue', 'green', 'yellow', 'purple']

try:
    current_list_for_removal.remove("black")
except ValueError as e:
    print(f"    Error: {e} - Value 'black' not found for remove().")

# 2.2 `pop(index=-1)`: Removes and returns the element at the specified `index`.
# - If no `index` is given, it removes and returns the last element.
# - Modifies in-place, returns the removed element.
# - Raises `IndexError` if `index` is out of range.
popped_item_at_index_1 = current_list_for_removal.pop(1) # Removes 'blue' (at index 1)
print(f"2.2 Popped item at index 1: {popped_item_at_index_1}") # Output: blue
print(f"    After pop(1): {current_list_for_removal}") # ['red', 'green', 'yellow', 'purple']

popped_last_item = current_list_for_removal.pop() # Removes 'purple' (last element)
print(f"    Popped last item (default pop()): {popped_last_item}") # Output: purple
print(f"    After pop(): {current_list_for_removal}") # ['red', 'green', 'yellow']

# 2.3 `clear()`: Removes all elements from the list, making it empty.
# - Modifies in-place, returns `None`.
current_list_for_removal.clear()
print(f"2.3 After clear(): {current_list_for_removal}") # []


print("\n--- 3. Methods for Reordering Elements ---")

reorder_list = [3, 1, 4, 1, 5, 9, 2, 6]

# 3.1 `sort(key=None, reverse=False)`: Sorts the list in-place.
# - By default, sorts in ascending order.
# - `reverse=True` for descending order.
# - `key` argument for custom sorting logic (e.g., sort strings by length).
# - Modifies in-place, returns `None`.
print(f"3.1 Original list: {reorder_list}")
reorder_list.sort() # Sorts numerically in ascending order
print(f"    After sort (ascending): {reorder_list}") # [1, 1, 2, 3, 4, 5, 6, 9]

reorder_list.sort(reverse=True) # Sorts in descending order
print(f"    After sort (descending): {reorder_list}") # [9, 6, 5, 4, 3, 2, 1, 1]

# Sorting with a custom key function
words_to_sort = ["banana", "apple", "fig", "cherry", "date"]
words_to_sort.sort(key=len) # Sorts by string length
print(f"    Words sorted by length: {words_to_sort}") # ['fig', 'date', 'apple', 'banana', 'cherry']

# 3.2 `reverse()`: Reverses the order of elements in-place.
# - Modifies in-place, returns `None`.
my_reverse_list = [10, 20, 30, 40, 50]
print(f"3.2 Original list: {my_reverse_list}")
my_reverse_list.reverse()
print(f"    After reverse(): {my_reverse_list}") # [50, 40, 30, 20, 10]


print("\n--- 4. Methods for Querying Information ---")

query_list = [10, 20, 30, 20, 40, 50, 20]

# 4.1 `count(value)`: Returns the number of times a specified `value` occurs in the list.
print(f"4.1 Count of 20 in {query_list}: {query_list.count(20)}") # Output: 3
print(f"    Count of 10 in {query_list}: {query_list.count(10)}") # Output: 1
print(f"    Count of 99 in {query_list}: {query_list.count(99)}") # Output: 0

# 4.2 `index(value, start=0, end=len(list))`: Returns the index of the *first* occurrence of `value`.
# - Optional `start` and `end` parameters to search within a slice.
# - Raises `ValueError` if `value` is not found.
print(f"4.2 Index of first 20: {query_list.index(20)}") # Output: 1
print(f"    Index of 20 starting from index 2: {query_list.index(20, 2)}") # Output: 3
print(f"    Index of 20 starting from index 4: {query_list.index(20, 4)}") # Output: 6

try:
    query_list.index(99)
except ValueError as e:
    print(f"    Error: {e} - Value '99' not found for index().")


print("\n--- 5. Methods for Copying Lists ---")

# 5.1 `copy()`: Returns a *shallow copy* of the list.
# - A new list object is created, but if the original list contains mutable objects
#   (like other lists or dictionaries), those nested mutable objects are still
#   referenced by both the original and the new copy.
print(f"5.1 Original list: {my_list}")
shallow_copy_list = my_list.copy()
print(f"    Shallow copy: {shallow_copy_list}")

# Demonstrate shallow copy behavior with a nested list
original_nested = [1, [2, 3], 4]
shallow_copy_nested = original_nested.copy()
print(f"    Original nested: {original_nested}, Shallow copy nested: {shallow_copy_nested}")

shallow_copy_nested[0] = 100 # Modifies top-level element in copy only
shallow_copy_nested[1].append(5) # Modifies nested list in copy, *also affects original*
print(f"    Original nested after shallow copy modification: {original_nested}") # [1, [2, 3, 5], 4]
print(f"    Shallow copy nested after modification: {shallow_copy_nested}") # [100, [2, 3, 5], 4]

# For a *deep copy* (where nested mutable objects are also copied recursively),
# use `copy.deepcopy()` from the `copy` module.
import copy
deep_copy_nested = copy.deepcopy(original_nested)
deep_copy_nested[1].append(6) # Modifies nested list in deep copy, *does NOT affect original*
print(f"    Original nested after deep copy modification: {original_nested}") # [1, [2, 3, 5], 4] (unchanged)
print(f"    Deep copy nested after modification: {deep_copy_nested}") # [1, [2, 3, 5, 6], 4]