# --- Python Lists: All About Operations in Code ---

# Lists are ordered, mutable collections of items. They support a wide range
# of operations, many of which create new lists, while others modify the list in-place.

# Let's define some sample lists for demonstration.
list1 = [1, 2, 3]
list2 = [4, 5]
list_mixed = ["apple", 123, True]
list_numeric = [10, 5, 20, 15]
list_strings = ["banana", "apple", "cherry"]


print("--- 1. Concatenation (`+` Operator) ---")

# The `+` operator is used to concatenate (join) two or more lists.
# It creates a *new* list containing all elements from the operands in order.

# 1.1 Basic concatenation
combined_list = list1 + list2
print(f"1.1 {list1} + {list2} = {combined_list}") # Output: [1, 2, 3, 4, 5]

# 1.2 Concatenating multiple lists
longer_list = list1 + list2 + [6, 7, 8]
print(f"1.2 {list1} + {list2} + [6, 7, 8] = {longer_list}") # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 1.3 Concatenating with an empty list
empty_list = []
result_with_empty = list1 + empty_list
print(f"1.3 {list1} + {empty_list} = {result_with_empty}") # Output: [1, 2, 3]

# Important: You cannot concatenate a list with a non-list iterable using `+` directly.
# Use `extend()` method for that (covered in "Adding Elements" section).
try:
    list1 + (6, 7) # This would raise a TypeError
except TypeError as e:
    print(f"\n1.4 Error: Cannot concatenate list with tuple using `+`: {e}")


print("\n--- 2. Repetition (`*` Operator) ---")

# The `*` operator is used to repeat the elements of a list a specified number of times.
# It creates a *new* list.

# 2.1 Basic repetition
repeated_list = list1 * 2
print(f"2.1 {list1} * 2 = {repeated_list}") # Output: [1, 2, 3, 1, 2, 3]

# 2.2 Repetition with 0 (results in an empty list)
empty_repetition = list1 * 0
print(f"2.2 {list1} * 0 = {empty_repetition}") # Output: []

# 2.3 Repetition by a negative number (also results in an empty list)
negative_repetition = list1 * -2
print(f"2.3 {list1} * -2 = {negative_repetition}") # Output: []

# 2.4 Important: Repetition with mutable elements (shallow copy issue)
# If the list contains mutable objects (like other lists), repetition creates
# multiple references to the *same* mutable object.
list_of_lists = [[]] * 3 # Creates a list with 3 references to the *same* empty list
print(f"\n2.4 List of lists (initial): {list_of_lists}")
list_of_lists[0].append(10) # Modifies the first inner list
print(f"    After modifying first inner list: {list_of_lists}") # All inner lists are modified!

# To create a list of *distinct* mutable objects, use a list comprehension:
distinct_lists = [[] for _ in range(3)]
print(f"    List of distinct lists (initial): {distinct_lists}")
distinct_lists[0].append(10)
print(f"    After modifying first inner list (distinct): {distinct_lists}") # Only the first is modified.


print("\n--- 3. Membership Testing (`in` Operator) ---")

# The `in` operator checks if a specific item exists within the list.
# It returns `True` if the item is found, and `False` otherwise.

# 3.1 Checking for existing elements
print(f"3.1 Is 2 in {list1}? {2 in list1}") # Output: True
print(f"    Is 'apple' in {list_strings}? {'apple' in list_strings}") # Output: True

# 3.2 Checking for non-existent elements
print(f"3.2 Is 5 in {list1}? {5 in list1}") # Output: False
print(f"    Is 'grape' in {list_strings}? {'grape' in list_strings}") # Output: False

# 3.3 Case sensitivity for strings
print(f"3.3 Is 'Apple' in {list_strings}? {'Apple' in list_strings}") # Output: False (case-sensitive)


print("\n--- 4. Length (`len()` Function) ---")

# The `len()` built-in function returns the number of elements in the list.

# 4.1 Basic length
print(f"4.1 Length of {list1}: {len(list1)}") # Output: 3
print(f"    Length of {list_strings}: {len(list_strings)}") # Output: 3
print(f"    Length of empty_list: {len(empty_list)}") # Output: 0

# 4.2 Length of nested lists (counts the nested list as one element)
nested_list = [[1, 2], [3, 4, 5]]
print(f"4.2 Length of {nested_list}: {len(nested_list)}") # Output: 2 (counts two inner lists)


print("\n--- 5. Min, Max, Sum (for numeric lists) ---")

# For lists containing only numeric types, you can use `min()`, `max()`, and `sum()`.

print(f"Numeric list: {list_numeric}")

# 5.1 `min()`: Returns the smallest item in the list.
print(f"5.1 Minimum value: {min(list_numeric)}") # Output: 5

# 5.2 `max()`: Returns the largest item in the list.
print(f"5.2 Maximum value: {max(list_numeric)}") # Output: 20

# 5.3 `sum()`: Returns the sum of all items in the list.
print(f"5.3 Sum of values: {sum(list_numeric)}") # Output: 50

# Attempting to use min/max/sum on non-numeric or mixed-type lists will raise a TypeError.
try:
    sum(list_strings)
except TypeError as e:
    print(f"\n5.4 Error: Cannot sum non-numeric list: {e}")


print("\n--- 6. Comparison Operations ---")

# Lists can be compared using standard comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`).
# Comparison is performed element by element, from left to right (lexicographical order).

# 6.1 Equality (`==`)
print(f"6.1 Is [1, 2, 3] == [1, 2, 3]? {[1, 2, 3] == [1, 2, 3]}") # True
print(f"    Is [1, 2, 3] == [1, 2, 4]? {[1, 2, 3] == [1, 2, 4]}") # False (different last element)
print(f"    Is [1, 2, 3] == [1, 2]? {[1, 2, 3] == [1, 2]}") # False (different length)

# 6.2 Less than (`<`) - Lexicographical comparison
# Compares the first differing element. If one list is a prefix of another, the shorter is smaller.
print(f"6.2 Is [1, 2, 3] < [1, 2, 4]? {[1, 2, 3] < [1, 2, 4]}") # True (3 < 4)
print(f"    Is [1, 5] < [2, 1]? {[1, 5] < [2, 1]}") # True (1 < 2)
print(f"    Is [1, 2] < [1, 2, 3]? {[1, 2] < [1, 2, 3]}") # True (shorter list is smaller if it's a prefix)
print(f"    Is ['apple', 'banana'] < ['apple', 'cherry']? {['apple', 'banana'] < ['apple', 'cherry']}") # True ('banana' < 'cherry')

# Elements must be comparable (e.g., cannot compare int with string directly).
try:
    [1, 'a'] < [1, 2]
except TypeError as e:
    print(f"\n6.3 Error: Cannot compare mixed types in list: {e}")