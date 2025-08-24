# --- Python Lists: All About in Code ---

# Lists are one of the most versatile and widely used built-in data structures in Python.
# They are used to store collections of items.

# --- 1. Introduction to Lists ---

# 1.1 What are Lists?
# - Ordered: The order of items is preserved.
# - Mutable: You can change, add, and remove elements after creation.
# - Allow duplicate members.
# - Can contain items of different data types.
# - Defined by items separated by commas, enclosed in square brackets `[]`.

# 1.2 Why use Lists?
# - Flexible data storage: Ideal for collections where order matters and elements might change.
# - Dynamic size: Can grow or shrink as needed.
# - Easy iteration: Simple to loop through elements.
# - Stack/Queue implementation: Can be used to simulate these data structures.

print("--- 1. Introduction ---")
print("Lists are ordered, mutable collections of items.")
print("They are defined using square brackets [].")


# --- 2. Creating Lists ---

print("\n--- 2. Creating Lists ---")

# 2.1 Empty List
empty_list_1 = []
print(f"2.1 Empty list using []: {empty_list_1}")
print(f"    Type of empty_list_1: {type(empty_list_1)}")

empty_list_2 = list() # Using the list() constructor
print(f"    Empty list using list(): {empty_list_2}")

# 2.2 List with initial elements (most common)
# Elements are separated by commas, enclosed in square brackets.
numbers = [1, 2, 3, 4, 5]
print(f"2.2 Numbers list: {numbers}")

fruits = ["apple", "banana", "cherry"]
print(f"    Fruits list: {fruits}")

# 2.3 List with mixed data types
mixed_list = ["hello", 123, True, 3.14, None, ["nested", "list"], {"key": "value"}]
print(f"2.3 Mixed data types list: {mixed_list}")

# 2.4 Nested Lists
nested_list = [[1, 2], [3, 4, 5], [6]]
print(f"2.4 Nested list: {nested_list}")

# 2.5 Creating a list from an iterable (using list() constructor)
# Can convert strings, tuples, sets, ranges, etc., into lists.
string_to_list = list("Python")
print(f"2.5 String converted to list: {string_to_list}") # ['P', 'y', 't', 'h', 'o', 'n']

tuple_to_list = list((10, 20, 30))
print(f"    Tuple converted to list: {tuple_to_list}")

set_to_list = list({"red", "green", "blue"}) # Order is not guaranteed from a set
print(f"    Set converted to list (order might vary): {set_to_list}")

range_to_list = list(range(5))
print(f"    Range converted to list: {range_to_list}")


# --- 3. Accessing Elements ---

print("\n--- 3. Accessing Elements ---")

my_list = ["alpha", "beta", "gamma", "delta", "epsilon"]

# 3.1 Indexing (positive and negative)
# - Positive indexing starts from 0 for the first element.
# - Negative indexing starts from -1 for the last element.
print(f"3.1 First element (index 0): {my_list[0]}")
print(f"    Third element (index 2): {my_list[2]}")
print(f"    Last element (index -1): {my_list[-1]}")
print(f"    Second to last element (index -2): {my_list[-2]}")

# Accessing elements in nested lists
nested_access_list = [[1, 2], [3, 4, 5]]
print(f"    First nested list: {nested_access_list[0]}") # [1, 2]
print(f"    Second element of the first nested list: {nested_access_list[0][1]}") # 2

# Attempting to access an out-of-range index will raise an IndexError
try:
    print(my_list[10])
except IndexError as e:
    print(f"    Error: {e} - Index out of range.")

# 3.2 Slicing
# - Extracts a portion of the list.
# - Syntax: `list[start:end:step]`
# - `end` index is exclusive.
# - Returns a new list.
print(f"3.2 Slice from index 1 to 3 (exclusive): {my_list[1:4]}") # ['beta', 'gamma', 'delta']
print(f"    Slice from beginning to index 2 (exclusive): {my_list[:2]}") # ['alpha', 'beta']
print(f"    Slice from index 3 to end: {my_list[3:]}") # ['delta', 'epsilon']
print(f"    Slice with step 2: {my_list[::2]}") # ['alpha', 'gamma', 'epsilon']
print(f"    Reverse the list: {my_list[::-1]}") # ['epsilon', 'delta', 'gamma', 'beta', 'alpha']


# --- 4. Modifying Elements (Mutability) ---

print("\n--- 4. Modifying Elements ---")

# Lists are mutable, meaning you can change their elements in place.

# 4.1 Changing an element by index
mutable_list = [10, 20, 30]
print(f"4.1 Original list: {mutable_list}")
mutable_list[0] = 100
print(f"    List after changing index 0: {mutable_list}") # [100, 20, 30]

# 4.2 Changing a slice
mutable_list[1:3] = [200, 300, 400] # Can change size of the slice
print(f"    List after changing slice [1:3]: {mutable_list}") # [100, 200, 300, 400]

# 4.3 Modifying elements in nested lists
nested_mutable = [[1, 2], [3, 4]]
nested_mutable[0][1] = 20
print(f"    Nested list after modifying inner element: {nested_mutable}") # [[1, 20], [3, 4]]


# --- 5. Adding Elements ---

print("\n--- 5. Adding Elements ---")

my_add_list = [1, 2, 3]

# 5.1 `append(item)`: Adds an item to the end of the list.
my_add_list.append(4)
print(f"5.1 After append(4): {my_add_list}") # [1, 2, 3, 4]

# 5.2 `insert(index, item)`: Inserts an item at a specified index.
my_add_list.insert(0, 0) # Insert 0 at the beginning
print(f"5.2 After insert(0, 0): {my_add_list}") # [0, 1, 2, 3, 4]
my_add_list.insert(3, 2.5) # Insert 2.5 at index 3
print(f"    After insert(3, 2.5): {my_add_list}") # [0, 1, 2, 2.5, 3, 4]

# 5.3 `extend(iterable)`: Adds all elements from an iterable to the end of the list.
my_add_list.extend([5, 6, 7]) # Extend with a list
print(f"5.3 After extend([5, 6, 7]): {my_add_list}") # [0, 1, 2, 2.5, 3, 4, 5, 6, 7]
my_add_list.extend("abc") # Extend with a string (adds characters individually)
print(f"    After extend('abc'): {my_add_list}") # [..., 'a', 'b', 'c']

# 5.4 Concatenation using `+` (creates a new list)
# While it adds elements, it creates a new list, unlike `append` and `extend`.
list_a = [10, 20]
list_b = [30, 40]
new_combined_list = list_a + list_b
print(f"5.4 New list from concatenation: {new_combined_list}") # [10, 20, 30, 40]


# --- 6. Removing Elements ---

print("\n--- 6. Removing Elements ---")

my_remove_list = [10, 20, 30, 20, 40, 50]

# 6.1 `remove(value)`: Removes the *first* occurrence of the specified value.
# Raises `ValueError` if the value is not found.
my_remove_list.remove(20)
print(f"6.1 After remove(20): {my_remove_list}") # [10, 30, 20, 40, 50] (only first 20 removed)

try:
    my_remove_list.remove(99)
except ValueError as e:
    print(f"    Error: {e} - Value not found for remove().")

# 6.2 `pop(index=-1)`: Removes and returns the element at the specified index.
# If no index is given, it removes and returns the last element.
# Raises `IndexError` if the index is out of range.
popped_item = my_remove_list.pop(1) # Remove element at index 1 (which is 30)
print(f"6.2 Popped item at index 1: {popped_item}") # 30
print(f"    After pop(1): {my_remove_list}") # [10, 20, 40, 50]

popped_last_item = my_remove_list.pop() # Remove last item (50)
print(f"    Popped last item: {popped_last_item}") # 50
print(f"    After pop(): {my_remove_list}") # [10, 20, 40]

# 6.3 `del` keyword: Deletes element(s) by index or slice.
# Does not return the deleted element(s).
del my_remove_list[0] # Delete element at index 0 (10)
print(f"6.3 After del my_remove_list[0]: {my_remove_list}") # [20, 40]

del my_remove_list[0:2] # Delete elements from index 0 to 2 (exclusive)
print(f"    After del my_remove_list[0:2]: {my_remove_list}") # []

# 6.4 `clear()`: Removes all elements from the list, making it empty.
my_clear_list = [1, 2, 3]
my_clear_list.clear()
print(f"6.4 After clear(): {my_clear_list}") # []


# --- 7. List Operations (Creating New Lists) ---

print("\n--- 7. List Operations ---")

# 7.1 Concatenation (`+` operator): Creates a new list.
list_part1 = [1, 2]
list_part2 = [3, 4]
new_list_concat = list_part1 + list_part2
print(f"7.1 Concatenation: {new_list_concat}") # [1, 2, 3, 4]

# 7.2 Repetition (`*` operator): Repeats elements to form a new list.
repeated_list = [0, 1] * 3
print(f"7.2 Repetition: {repeated_list}") # [0, 1, 0, 1, 0, 1]

# 7.3 Membership testing (`in` operator): Checks if an item exists.
print(f"7.3 Is 'banana' in fruits? {'banana' in fruits}") # True

# 7.4 Length (`len()` function): Returns the number of elements.
print(f"7.4 Length of fruits: {len(fruits)}") # 3

# 7.5 Min, Max, Sum (for numeric lists)
numeric_list = [10, 5, 20, 15]
print(f"7.5 Min: {min(numeric_list)}, Max: {max(numeric_list)}, Sum: {sum(numeric_list)}")


# --- 8. List Methods (for Information & Reordering) ---

print("\n--- 8. List Methods (Information & Reordering) ---")

my_info_list = [10, 30, 20, 10, 40]

# 8.1 `count(value)`: Returns the number of times a value occurs.
print(f"8.1 Count of 10: {my_info_list.count(10)}") # 2

# 8.2 `index(value, start=0, end=len(list))`: Returns the index of the first occurrence.
print(f"8.2 Index of 20: {my_info_list.index(20)}") # 2
print(f"    Index of 10 starting from index 1: {my_info_list.index(10, 1)}") # 3

# 8.3 `sort(key=None, reverse=False)`: Sorts the list in-place (modifies original list).
# Returns None.
sort_list = [3, 1, 4, 1, 5, 9, 2]
print(f"8.3 Before sort: {sort_list}")
sort_list.sort() # Ascending order
print(f"    After sort (ascending): {sort_list}")

sort_list.sort(reverse=True) # Descending order
print(f"    After sort (descending): {sort_list}")

# Sorting with a custom key (e.g., sort strings by length)
words_to_sort = ["banana", "apple", "fig", "cherry"]
words_to_sort.sort(key=len)
print(f"    Words sorted by length: {words_to_sort}")

# 8.4 `reverse()`: Reverses the order of elements in-place. Returns None.
reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse()
print(f"8.4 After reverse(): {reverse_list}") # [5, 4, 3, 2, 1]

# 8.5 `copy()`: Returns a shallow copy of the list.
# Changes to the copy won't affect the original for top-level elements.
# Nested mutable elements are still shared.
original = [1, [2, 3], 4]
copied = original.copy()
print(f"8.5 Original: {original}, Copied: {copied}")
copied[0] = 100 # Changes copy only
copied[1].append(5) # Changes nested list in both
print(f"    Original after copy modification: {original}")
print(f"    Copied after copy modification: {copied}")


# --- 9. Iterating Through Lists ---

print("\n--- 9. Iterating Through Lists ---")

# 9.1 Basic iteration
print("9.1 Basic iteration:")
for fruit in fruits:
    print(fruit)

# 9.2 Iterating with `enumerate()` (for index and value)
print("\n9.2 Iterating with enumerate():")
for index, number in enumerate(numbers):
    print(f"Index {index}: {number}")

# 9.3 Iterating with `zip()` (for multiple lists)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
print("\n9.3 Iterating with zip():")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")