# --- Sets in Python: A Comprehensive Overview (Code-Focused) ---

# -------------------- 1. Basic Set Operations --------------------

# Creating Sets
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")

my_set = {1, 2, 3}
print(f"Initial set: {my_set}")

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 3}
print(f"Set with duplicates: {duplicate_set} (duplicates removed)")

# Creating a set from a list (duplicates will be removed)
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
set_from_list = set(my_list)
print(f"Set from list: {set_from_list}")

# Adding elements to a set
another_set = {10, 20}
another_set.add(30)
print(f"Set after adding 30: {another_set}")

# Adding multiple elements at once
another_set.update([40, 50])
print(f"Set after updating with [40, 50]: {another_set}")

# Removing elements from a set
yet_another_set = {1, 2, 3, 4, 5}
yet_another_set.remove(3)  # Raises KeyError if element not found
print(f"Set after removing 3: {yet_another_set}")

yet_another_set.discard(5) # Does not raise an error if element not found
print(f"Set after discarding 5: {yet_another_set}")

# Popping an arbitrary element (use with caution as order is not guaranteed)
popped_element = yet_another_set.pop()
print(f"Set after popping: {yet_another_set}, Popped element: {popped_element}")

# Clearing all elements from a set
yet_another_set.clear()
print(f"Set after clearing: {yet_another_set}")

# -------------------- 2. Set Theory Operations --------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (elements present in either set A or set B or both)
union_set = set_a.union(set_b)
print(f"Union of A and B (set_a.union(set_b)): {union_set}")
union_set_operator = set_a | set_b
print(f"Union of A and B (set_a | set_b): {union_set_operator}")

# Intersection (elements present in both set A and set B)
intersection_set = set_a.intersection(set_b)
print(f"Intersection of A and B (set_a.intersection(set_b)): {intersection_set}")
intersection_set_operator = set_a & set_b
print(f"Intersection of A and B (set_a & set_b): {intersection_set_operator}")

# Difference (elements present in set A but not in set B)
difference_set = set_a.difference(set_b)
print(f"Difference of A and B (set_a.difference(set_b)): {difference_set}")
difference_set_operator = set_a - set_b
print(f"Difference of A and B (set_a - set_b): {difference_set_operator}")

# Symmetric Difference (elements present in either set A or set B, but not in both)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference of A and B (set_a.symmetric_difference(set_b)): {symmetric_difference_set}")
symmetric_difference_set_operator = set_a ^ set_b
print(f"Symmetric Difference of A and B (set_a ^ set_b): {symmetric_difference_set_operator}")

# -------------------- 3. Set Comparisons --------------------

set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}
set_e = {3, 2, 1}

# Subset (all elements of set C are in set D)
is_subset = set_c.issubset(set_d)
print(f"Is C a subset of D (set_c.issubset(set_d))? {is_subset}")
is_subset_operator = set_c <= set_d
print(f"Is C a subset of D (set_c <= set_d)? {is_subset_operator}")

# Proper Subset (all elements of set C are in set D, and C is not equal to D)
is_proper_subset = set_c < set_d
print(f"Is C a proper subset of D (set_c < set_d)? {is_proper_subset}")

# Superset (all elements of set D are in set C)
is_superset = set_d.issuperset(set_c)
print(f"Is D a superset of C (set_d.issuperset(set_c))? {is_superset}")
is_superset_operator = set_d >= set_c
print(f"Is D a superset of C (set_d >= set_c)? {is_superset_operator}")

# Proper Superset (all elements of set D are in set C, and D is not equal to C)
is_proper_superset = set_d > set_c
print(f"Is D a proper superset of C (set_d > set_c)? {is_proper_superset}")

# Disjoint (sets have no common elements)
set_f = {10, 11}
is_disjoint = set_c.isdisjoint(set_f)
print(f"Are C and F disjoint (set_c.isdisjoint(set_f))? {is_disjoint}")

# Equality (sets contain the same elements, order does not matter)
are_equal = set_c == set_e
print(f"Is C equal to E (set_c == set_e)? {are_equal}")

# -------------------- 4. Frozen Sets (Immutable Sets) --------------------

# Regular sets are mutable (can be changed after creation)
mutable_set = {1, 2, 3}
mutable_set.add(4)
print(f"Mutable set after adding: {mutable_set}")

# Frozen sets are immutable (cannot be changed after creation)
frozen_set = frozenset([1, 2, 3])
print(f"Frozen set: {frozen_set}, Type: {type(frozen_set)}")

# Attempting to modify a frozen set will raise an AttributeError
# frozen_set.add(4)  # This will cause an error

# Frozen sets can be used as elements of other sets or as keys in dictionaries
another_set_with_frozenset = {frozenset({1, 2}), 3, 4}
print(f"Set containing a frozenset: {another_set_with_frozenset}")

# -------------------- 5. Set Comprehensions (Advanced) --------------------

# Creating sets using a concise syntax similar to list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares_set = {x**2 for x in numbers if x % 2 == 0}
print(f"Set of even squares: {even_squares_set}")

string_list = ["apple", "banana", "cherry"]
first_letters_set = {word[0] for word in string_list}
print(f"Set of first letters: {first_letters_set}")

# Conditional logic within set comprehensions
odd_or_large_set = {x if x % 2 != 0 else x * 100 for x in range(1, 6)}
print(f"Set with conditional logic: {odd_or_large_set}")

# -------------------- 6. Applications of Sets --------------------

# Removing duplicates from a list (already seen)
data_with_duplicates = [1, 5, 2, 5, 3, 1, 4]
unique_data = set(data_with_duplicates)
print(f"Unique data from list: {unique_data}")

# Checking for membership efficiently
my_elements = {10, 20, 30, 40, 50}
is_present = 30 in my_elements
print(f"Is 30 present in the set? {is_present}")
is_absent = 60 in my_elements
print(f"Is 60 present in the set? {is_absent}")

# Finding common elements between collections
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print(f"Common elements between list1 and list2: {common_elements}")

# Keeping track of unique items
seen_items = set()
items = ["apple", "banana", "apple", "cherry", "banana"]
for item in items:
    seen_items.add(item)
print(f"Unique items: {seen_items}")

# Performing set operations for data analysis
group_a = {"Alice", "Bob", "Charlie"}
group_b = {"Bob", "David", "Eve"}

common_members = group_a & group_b
print(f"Common members: {common_members}")

only_in_a = group_a - group_b
print(f"Members only in group A: {only_in_a}")

all_members = group_a | group_b
print(f"All members: {all_members}")

# -------------------- Summary --------------------
# Sets are unordered collections of unique elements.
# They support various mathematical set operations like union, intersection, difference, etc.
# Sets are mutable, but frozensets provide an immutable alternative.
# Set comprehensions offer a concise way to create sets.
# Sets are efficient for membership testing and removing duplicates.