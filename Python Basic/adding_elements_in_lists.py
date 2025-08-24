# --- Python Lists: All About Adding Elements to Them in Code ---

# Lists in Python are mutable, which means you can change their content
# after they have been created. This includes adding new elements.

# Let's start with a sample list for demonstration.
my_shopping_list = ["milk", "bread", "eggs"]

print("--- 1. Adding a Single Element: `append()` ---")

# 1.1 `append(item)`:
# - **Purpose:** Adds a single `item` to the very end of the list.
# - **Syntax:** `list.append(item)`
# - **Returns:** `None` (modifies the list in-place).

print(f"1.1 Original list: {my_shopping_list}")
my_shopping_list.append("cheese")
print(f"    After append('cheese'): {my_shopping_list}") # Output: ['milk', 'bread', 'eggs', 'cheese']

# You can append any data type, including other lists or dictionaries.
my_shopping_list.append(["apples", "oranges"]) # Appends a list as a single element
print(f"    After append(['apples', 'oranges']): {my_shopping_list}")
# Output: ['milk', 'bread', 'eggs', 'cheese', ['apples', 'oranges']]

my_shopping_list.append({"item": "coffee", "qty": 1}) # Appends a dictionary
print(f"    After append({{'item': 'coffee', 'qty': 1}}): {my_shopping_list}")


print("\n--- 2. Inserting an Element at a Specific Position: `insert()` ---")

# 2.1 `insert(index, item)`:
# - **Purpose:** Inserts an `item` at a specified `index`.
#   Elements from that `index` onwards are shifted to the right.
# - **Syntax:** `list.insert(index, item)`
# - **Returns:** `None` (modifies the list in-place).

my_numbers = [10, 20, 30, 40]
print(f"2.1 Original list: {my_numbers}")

# Insert at the beginning (index 0)
my_numbers.insert(0, 5)
print(f"    After insert(0, 5): {my_numbers}") # Output: [5, 10, 20, 30, 40]

# Insert in the middle (e.g., at index 3)
my_numbers.insert(3, 25)
print(f"    After insert(3, 25): {my_numbers}") # Output: [5, 10, 20, 25, 30, 40]

# Inserting at an index greater than the current length appends to the end.
my_numbers.insert(len(my_numbers), 50) # Same as append(50)
print(f"    After insert(len, 50): {my_numbers}") # Output: [5, 10, 20, 25, 30, 40, 50]

my_numbers.insert(999, 100) # Inserting at a very large index also appends to the end
print(f"    After insert(999, 100): {my_numbers}")


print("\n--- 3. Adding Multiple Elements from an Iterable: `extend()` ---")

# 3.1 `extend(iterable)`:
# - **Purpose:** Adds all elements from an `iterable` (e.g., another list, tuple, string, set)
#   to the end of the current list. The elements are added individually.
# - **Syntax:** `list.extend(iterable)`
# - **Returns:** `None` (modifies the list in-place).

my_colors = ["red", "green"]
print(f"3.1 Original list: {my_colors}")

# Extend with another list
my_colors.extend(["blue", "yellow"])
print(f"    After extend(['blue', 'yellow']): {my_colors}") # Output: ['red', 'green', 'blue', 'yellow']

# Extend with a tuple
my_colors.extend(("orange", "purple"))
print(f"    After extend(('orange', 'purple')): {my_colors}") # Output: ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# Extend with a string (each character is added as a separate element)
my_colors.extend("pink")
print(f"    After extend('pink'): {my_colors}") # Output: [..., 'p', 'i', 'n', 'k']

# Extend with a set (order not guaranteed for elements from the set)
my_colors.extend({"cyan", "magenta"})
print(f"    After extend({{'cyan', 'magenta'}}): {my_colors}") # Output: [..., 'cyan', 'magenta'] (order may vary)


print("\n--- 4. Adding Elements using Concatenation (`+` Operator) ---")

# 4.1 `list1 + list2`:
# - **Purpose:** Creates a *new* list by joining two or more lists.
# - **Syntax:** `list1 + list2`
# - **Returns:** A *new* list (does NOT modify the original lists in-place).

list_part1 = [10, 20]
list_part2 = [30, 40]
new_combined_list = list_part1 + list_part2
print(f"4.1 list_part1: {list_part1}, list_part2: {list_part2}")
print(f"    New combined list: {new_combined_list}") # Output: [10, 20, 30, 40]
print(f"    Original list_part1 remains unchanged: {list_part1}") # Output: [10, 20]

# You can concatenate multiple lists
all_numbers = [1, 2] + [3, 4] + [5]
print(f"    Concatenating multiple lists: {all_numbers}")

# Important: You cannot concatenate a list with a non-list type directly.
try:
    [1, 2] + (3, 4) # This will raise a TypeError
except TypeError as e:
    print(f"4.2 Error: Cannot concatenate list with tuple: {e}")


print("\n--- 5. Adding Elements using List Comprehensions ---")

# 5.1 `[expression for item in iterable if condition]`:
# - **Purpose:** Creates a *new* list by applying an `expression` to each `item`
#   from an `iterable`, optionally filtering with a `condition`.
# - **Returns:** A *new* list.

# Example: Create a list of even numbers from 0 to 10
even_numbers = [num for num in range(0, 11) if num % 2 == 0]
print(f"5.1 New list of even numbers: {even_numbers}") # Output: [0, 2, 4, 6, 8, 10]

# Example: Create a list of strings with a prefix
original_items = ["pen", "book", "mug"]
prefixed_items = [f"item_{item}" for item in original_items]
print(f"    New list with prefixed items: {prefixed_items}") # ['item_pen', 'item_book', 'item_mug']


print("\n--- 6. Adding Elements by Slice Assignment ---")

# 6.1 `list[start:end] = iterable`:
# - **Purpose:** Replaces a slice of the list with elements from an `iterable`.
#   If the slice is empty, it effectively inserts elements.
# - **Returns:** `None` (modifies the list in-place).

my_slice_list = ["a", "b", "c", "d"]
print(f"6.1 Original list: {my_slice_list}")

# Insert elements at the beginning (replace an empty slice at index 0)
my_slice_list[0:0] = ["X", "Y"]
print(f"    After inserting at start (slice assignment): {my_slice_list}") # ['X', 'Y', 'a', 'b', 'c', 'd']

# Insert elements in the middle (replace an empty slice)
my_slice_list[3:3] = [1, 2, 3]
print(f"    After inserting in middle (slice assignment): {my_slice_list}") # ['X', 'Y', 'a', 1, 2, 3, 'b', 'c', 'd']