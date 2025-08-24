# --- Python Lists: All About Modifying Them in Code ---

# Lists are mutable, which is a key characteristic. This means you can
# change their content (elements, order, size) after they have been created.

# Let's start with a sample list for demonstration.
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

print("--- 1. Changing Elements by Index ---")

# You can change the value of a specific element by referring to its index.

# 1.1 Changing a single element
print(f"1.1 Original list: {my_list}")
my_list[1] = "blueberry" # Change 'banana' to 'blueberry'
print(f"    After changing index 1: {my_list}") # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# 1.2 Changing elements in nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"1.2 Original nested list: {nested_list}")
nested_list[0][1] = 20 # Change the second element of the first inner list
print(f"    After changing nested element: {nested_list}") # [[1, 20], [3, 4], [5, 6]]

# 1.3 What happens if the index is out of range? (IndexError)
try:
    my_list[10] = "grape" # List only has 5 elements (indices 0-4)
except IndexError as e:
    print(f"1.3 Error: {e} - Cannot assign to an index that doesn't exist.")


print("\n--- 2. Changing Elements by Slicing ---")

# You can replace a slice of a list with new elements.
# The number of elements in the replacement slice doesn't have to match the original slice size.

my_slice_list = ["a", "b", "c", "d", "e"]
print(f"2.1 Original list for slicing: {my_slice_list}")

# 2.1 Replacing a slice with the same number of elements
my_slice_list[1:3] = ["B", "C"] # Replace 'b', 'c' with 'B', 'C'
print(f"    After replacing slice [1:3] with 2 elements: {my_slice_list}") # ['a', 'B', 'C', 'd', 'e']

# 2.2 Replacing a slice with more elements (expands the list)
my_slice_list[1:2] = ["X", "Y", "Z"] # Replace 'B' with 'X', 'Y', 'Z'
print(f"    After replacing slice [1:2] with 3 elements: {my_slice_list}") # ['a', 'X', 'Y', 'Z', 'C', 'd', 'e']

# 2.3 Replacing a slice with fewer elements (shrinks the list)
my_slice_list[2:5] = ["P"] # Replace 'Y', 'Z', 'C' with 'P'
print(f"    After replacing slice [2:5] with 1 element: {my_slice_list}") # ['a', 'X', 'P', 'd', 'e']

# 2.4 Replacing an empty slice (inserts elements)
my_slice_list.insert(0, "START") # This is equivalent to my_slice_list[0:0] = ["START"]
print(f"    Using insert(0, 'START'): {my_slice_list}")
my_slice_list[1:1] = ["INS1", "INS2"] # Insert at index 1
print(f"    After inserting at slice [1:1]: {my_slice_list}") # ['START', 'INS1', 'INS2', 'a', 'X', 'P', 'd', 'e']


print("\n--- 3. Adding Elements ---")

add_list = [10, 20, 30]

# 3.1 `append(item)`: Adds a single item to the end of the list.
add_list.append(40)
print(f"3.1 After append(40): {add_list}") # [10, 20, 30, 40]

# 3.2 `insert(index, item)`: Inserts an item at a specified index.
# Elements from that index onwards are shifted to the right.
add_list.insert(0, 5) # Insert 5 at the beginning (index 0)
print(f"3.2 After insert(0, 5): {add_list}") # [5, 10, 20, 30, 40]
add_list.insert(3, 25) # Insert 25 at index 3
print(f"    After insert(3, 25): {add_list}") # [5, 10, 20, 25, 30, 40]

# 3.3 `extend(iterable)`: Adds all elements from an iterable (e.g., another list, tuple, string)
# to the end of the current list.
add_list.extend([50, 60]) # Extend with a list
print(f"3.3 After extend([50, 60]): {add_list}") # [..., 50, 60]
add_list.extend("xyz") # Extend with a string (adds characters individually)
print(f"    After extend('xyz'): {add_list}") # [..., 'x', 'y', 'z']

# 3.4 Concatenation using `+` operator (creates a NEW list)
# While it adds elements, it's important to remember this creates a new list
# rather than modifying the original in-place.
list_a = [1, 2]
list_b = [3, 4]
new_list = list_a + list_b
print(f"3.4 New list from concatenation: {new_list}") # [1, 2, 3, 4]
print(f"    Original list_a remains: {list_a}")


print("\n--- 4. Removing Elements ---")

remove_list = ["one", "two", "three", "two", "four", "five"]

# 4.1 `remove(value)`: Removes the *first* occurrence of the specified value.
# Raises `ValueError` if the value is not found.
remove_list.remove("two")
print(f"4.1 After remove('two'): {remove_list}") # ['one', 'three', 'two', 'four', 'five']

try:
    remove_list.remove("nonexistent")
except ValueError as e:
    print(f"    Error: {e} - Value not found for remove().")

# 4.2 `pop(index=-1)`: Removes and returns the element at the specified index.
# If no index is given, it removes and returns the last element.
# Raises `IndexError` if the index is out of range.
popped_item = remove_list.pop(1) # Remove element at index 1 ('three')
print(f"4.2 Popped item at index 1: {popped_item}") # Output: three
print(f"    After pop(1): {remove_list}") # ['one', 'two', 'four', 'five']

popped_last_item = remove_list.pop() # Remove last item ('five')
print(f"    Popped last item: {popped_last_item}") # Output: five
print(f"    After pop(): {remove_list}") # ['one', 'two', 'four']

# 4.3 `del` keyword: Deletes element(s) by index or slice.
# Does not return the deleted element(s).
del remove_list[0] # Delete element at index 0 ('one')
print(f"4.3 After del remove_list[0]: {remove_list}") # ['two', 'four']

del remove_list[0:2] # Delete elements from index 0 up to (but not including) 2
print(f"    After del remove_list[0:2]: {remove_list}") # []

# 4.4 `clear()`: Removes all elements from the list, making it empty.
my_clear_list = [1, 2, 3]
my_clear_list.clear()
print(f"4.4 After clear(): {my_clear_list}") # []


print("\n--- 5. Reordering Elements ---")

reorder_list = [3, 1, 4, 1, 5, 9, 2]

# 5.1 `sort(key=None, reverse=False)`: Sorts the list in-place (modifies the original list).
# Returns `None`.
print(f"5.1 Before sort: {reorder_list}")
reorder_list.sort() # Sorts in ascending order by default
print(f"    After sort (ascending): {reorder_list}")

reorder_list.sort(reverse=True) # Sorts in descending order
print(f"    After sort (descending): {reorder_list}")

# Sorting with a custom key (e.g., sort strings by their length)
words_to_sort = ["banana", "apple", "fig", "cherry"]
words_to_sort.sort(key=len)
print(f"    Words sorted by length: {words_to_sort}") # ['fig', 'apple', 'banana', 'cherry']

# 5.2 `reverse()`: Reverses the order of elements in-place. Returns `None`.
my_reverse_list = [1, 2, 3, 4, 5]
my_reverse_list.reverse()
print(f"5.2 After reverse(): {my_reverse_list}") # [5, 4, 3, 2, 1]


print("\n--- 6. Important: Modifying a List While Iterating ---")

# Modifying a list (adding or removing elements) while iterating over it
# directly can lead to unexpected behavior or `RuntimeError`.

# 6.1 UNSAFE example (do not do this in real code)
# This will likely skip elements or raise an error.
# numbers_to_filter = [1, 2, 3, 4, 5, 6]
# print(f"6.1 UNSAFE: Original list: {numbers_to_filter}")
# try:
#     for i in numbers_to_filter:
#         if i % 2 == 0:
#             numbers_to_filter.remove(i) # Modifying while iterating
#     print(f"    Result (might be unexpected): {numbers_to_filter}")
# except RuntimeError as e:
#     print(f"    Caught expected RuntimeError: {e}")

# 6.2 SAFE way 1: Iterate over a copy of the list
safe_filter_list = [1, 2, 3, 4, 5, 6]
print(f"\n6.2 SAFE Way 1: Original list: {safe_filter_list}")
for item in safe_filter_list.copy(): # Iterate over a copy
    if item % 2 == 0:
        safe_filter_list.remove(item) # Modify the original
print(f"    Result after safe removal: {safe_filter_list}") # [1, 3, 5]

# 6.3 SAFE way 2: Use a list comprehension to create a new list
# This is often the most Pythonic and efficient way for filtering.
original_numbers = [1, 2, 3, 4, 5, 6]
new_filtered_list = [num for num in original_numbers if num % 2 != 0]
print(f"\n6.3 SAFE Way 2: New filtered list: {new_filtered_list}") # [1, 3, 5]
print(f"    Original list remains unchanged: {original_numbers}")