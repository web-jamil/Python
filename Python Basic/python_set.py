import random

print("--- Python Sets: Practice Code ---")

# --- 1. Creating Sets ---
print("\n--- 1. Creating Sets ---")

# 1.1 Empty set: Use set() constructor, NOT {} (that creates an empty dictionary)
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type of empty_set: {type(empty_set)}")

# 1.2 Set with elements (using curly braces {})
# Sets do not allow duplicate elements; duplicates are automatically removed.
my_set = {1, 2, 3, 2, 4, 1}
print(f"Set with numbers (duplicates removed): {my_set}")

# 1.3 Set from an iterable (using set() constructor)
# Duplicates from the iterable will be removed. Order is not preserved.
set_from_list = set([5, 6, 7, 6, 8])
print(f"Set from list: {set_from_list}")

set_from_string = set("hello world") # Creates a set of unique characters
print(f"Set from string: {set_from_string}")

# 1.4 Set comprehension (similar to list/dict comprehensions)
even_numbers_set = {x for x in range(10) if x % 2 == 0}
print(f"Even numbers set (set comprehension): {even_numbers_set}")


## 2. Set Properties and Accessing Elements

# Sets are **unordered** and **unindexed**. You cannot access elements by index like lists or tuples.
# Sets contain **unique** elements.
# Set elements must be **immutable** (numbers, strings, tuples, but NOT lists or dictionaries).

my_data = {10, 20, "apple", True, 3.14}
print(f"\n--- 2. Set Properties and Accessing Elements ---")
print(f"My data set: {my_data}")

# 2.1 Checking for element existence: 'in' operator
print(f"Is 20 in my_data? {20 in my_data}")
print(f"Is 'banana' in my_data? {'banana' in my_data}")

# 2.2 Iterating through a set (order is not guaranteed)
print("\nIterating through my_data set:")
for item in my_data:
    print(item)

# You cannot access by index:
# try:
#     print(my_data[0]) # This would raise a TypeError
# except TypeError as e:
#     print(f"Caught TypeError: {e} - Sets are unordered and unindexed.")



## 3. Modifying Sets

my_set = {1, 2, 3}
print(f"\n--- 3. Modifying Sets ---")
print(f"Original set: {my_set}")

# 3.1 Adding elements: .add()
my_set.add(4)
print(f"After adding 4: {my_set}")
my_set.add(2) # Adding an existing element has no effect
print(f"After adding 2 (no change): {my_set}")

# 3.2 Updating a set: .update() (adds elements from another iterable)
# This is like union, but modifies the set in place.
my_set.update([5, 6, 1]) # Adds 5, 6. 1 is already there.
print(f"After updating with [5, 6, 1]: {my_set}")
my_set.update({7, 8}) # Can also update with another set
print(f"After updating with {7, 8}: {my_set}")

# 3.3 Removing elements: .remove() (raises KeyError if item not found)
my_set.remove(6)
print(f"After removing 6: {my_set}")
# try:
#     my_set.remove(99) # This would raise a KeyError
# except KeyError as e:
#     print(f"Caught KeyError: {e} - Cannot remove 99 (not in set).")

# 3.4 Removing elements: .discard() (does NOT raise an error if item not found)
my_set.discard(5)
print(f"After discarding 5: {my_set}")
my_set.discard(99) # Discarding a non-existent element does nothing silently
print(f"After discarding 99 (no change): {my_set}")

# 3.5 Removing and returning an arbitrary element: .pop()
# Since sets are unordered, there's no guarantee which element will be popped.
popped_element = my_set.pop()
print(f"After popping {popped_element}: {my_set}")
# Raises KeyError if the set is empty.

# 3.6 Clearing all elements: .clear()
my_set.clear()
print(f"After clearing the set: {my_set}")

# 3.7 Deleting the set entirely: del keyword
del my_set # The set object 'my_set' no longer exists after this.
# print(my_set) # This would now raise a NameError



## 4. Set Operations (Mathematical Set Theory)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2}
print(f"\n--- 4. Set Operations ---")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# 4.1 Union: All unique elements from both sets
# Syntax: set1.union(set2) or set1 | set2
union_set = set_a.union(set_b)
print(f"Union (A | B): {union_set}")

# 4.2 Intersection: Elements common to both sets
# Syntax: set1.intersection(set2) or set1 & set2
intersection_set = set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection_set}")

# 4.3 Difference: Elements in the first set but NOT in the second
# Syntax: set1.difference(set2) or set1 - set2
difference_ab = set_a.difference(set_b)
print(f"Difference (A - B): {difference_ab}")
difference_ba = set_b - set_a
print(f"Difference (B - A): {difference_ba}")

# 4.4 Symmetric Difference: Elements in either set, but NOT in both
# Syntax: set1.symmetric_difference(set2) or set1 ^ set2
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (A ^ B): {symmetric_difference_set}")

# 4.5 Subset: Checks if all elements of one set are in another
# Syntax: set1.issubset(set2) or set1 <= set2
print(f"Is C a subset of A? {set_c.issubset(set_a)}")
print(f"Is A a subset of C? {set_a <= set_c}")

# 4.6 Superset: Checks if one set contains all elements of another
# Syntax: set1.issuperset(set2) or set1 >= set2
print(f"Is A a superset of C? {set_a.issuperset(set_c)}")
print(f"Is C a superset of A? {set_c >= set_a}")

# 4.7 Disjoint: Checks if two sets have NO common elements
# Syntax: set1.isdisjoint(set2)
set_d = {9, 10}
print(f"Are A and D disjoint? {set_a.isdisjoint(set_d)}")
print(f"Are A and B disjoint? {set_a.isdisjoint(set_b)}") # False, they share 4, 5



## 5. Frozen Sets (Immutable Sets)

# `frozenset` is an immutable version of a `set`.
# This means a frozenset can be used as a key in a dictionary or as an element in another set.

frozen_set_a = frozenset([1, 2, 3])
regular_set_b = {3, 4, 5}
print(f"\n--- 5. Frozen Sets ---")
print(f"Frozen Set A: {frozen_set_a}")

# Operations work similarly
frozen_union = frozen_set_a.union(regular_set_b)
print(f"Union with a regular set: {frozen_union}")

# You can use frozensets as dictionary keys
set_as_key_dict = {frozenset({1, 2}): "Pair OneTwo", frozenset({'a', 'b'}): "Pair AB"}
print(f"Dictionary with frozenset keys: {set_as_key_dict}")
# print(set_as_key_dict[{1, 2}]) # This would not work, needs frozenset

# regular sets cannot be dict keys or elements of other sets
# try:
#     invalid_dict = {{1, 2}: "Invalid Key"}
# except TypeError as e:
#     print(f"Caught TypeError: {e} - Sets are mutable and cannot be dictionary keys.")



## 6. Common Set Use Cases

print("\n--- 6. Common Set Use Cases ---")

# 6.1 Removing Duplicates from a List (and losing order)
my_list_with_dupes = [1, 2, 2, 3, 4, 4, 5]
unique_list_from_set = list(set(my_list_with_dupes))
print(f"List with duplicates: {my_list_with_dupes}, Unique list (order not preserved): {unique_list_from_set}")

# 6.2 Membership Testing (faster than lists for large collections)
large_list = list(range(1_000_000))
large_set = set(large_list)

# print("Checking membership in large list (might be slower)...")
# print(999_999 in large_list) # O(n) average case

# print("Checking membership in large set (much faster)...")
# print(999_999 in large_set) # O(1) average case

# 6.3 Finding Common Elements between two collections
students_in_math = {"Alice", "Bob", "Charlie", "David"}
students_in_physics = {"Bob", "David", "Eve", "Frank"}
common_students = students_in_math.intersection(students_in_physics)
print(f"Students in both Math and Physics: {common_students}")

# 6.4 Finding Unique Elements across collections
all_students = students_in_math.union(students_in_physics)
print(f"All unique students enrolled: {all_students}")

# 6.5 Elements only in one collection but not the other
only_math = students_in_math.difference(students_in_physics)
print(f"Students only in Math: {only_math}")

# 6.6 Checking for shared tags/categories
product_tags_A = {"electronics", "mobile", "sale"}
product_tags_B = {"accessories", "sale", "gadget"}
if not product_tags_A.isdisjoint(product_tags_B):
    print(f"Products A and B share common tags: {product_tags_A.intersection(product_tags_B)}")
else:
    print("Products A and B have no common tags.")

print("\n--- End of Python Sets Practice Code ---")