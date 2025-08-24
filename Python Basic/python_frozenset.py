import random

print("--- Python frozenset: Practice Code ---")

# --- 1. What is a frozenset? ---
print("\n--- 1. What is a frozenset? ---")
print("A frozenset is an immutable version of a Python set.")
print("Once created, you cannot add, remove, or change its elements.")
print("This immutability makes them 'hashable', meaning they can be used:")
print("  - As keys in dictionaries")
print("  - As elements in other sets (including other frozensets or regular sets)")
print("Regular sets are mutable and therefore not hashable.")


# --- 2. Creating Frozensets ---
print("\n--- 2. Creating Frozensets ---")

# 2.1 Empty frozenset
empty_frozenset = frozenset()
print(f"Empty frozenset: {empty_frozenset}")
print(f"Type of empty_frozenset: {type(empty_frozenset)}")

# 2.2 Frozenset from an iterable (list, tuple, string, set, etc.)
my_list = [1, 2, 3, 2, 4]
fs_from_list = frozenset(my_list)
print(f"Frozenset from list {my_list}: {fs_from_list}")

my_string = "hello world"
fs_from_string = frozenset(my_string) # Contains unique characters from the string
print(f"Frozenset from string '{my_string}': {fs_from_string}")

my_set = {5, 6, 7}
fs_from_set = frozenset(my_set)
print(f"Frozenset from set {my_set}: {fs_from_set}")

my_tuple = (10, 11, 10, 12)
fs_from_tuple = frozenset(my_tuple)
print(f"Frozenset from tuple {my_tuple}: {fs_from_tuple}")

# 2.3 Frozenset containing mixed data types (if elements are hashable)
mixed_fs = frozenset([1, "apple", True, (1, 2)])
print(f"Mixed frozenset: {mixed_fs}")

# You cannot create a frozenset from mutable elements like lists or dictionaries directly
# try:
#     frozenset_with_list = frozenset([1, [2, 3]]) # This would raise a TypeError
# except TypeError as e:
#     print(f"Caught TypeError: {e} - cannot contain mutable items like lists.")


# --- 3. Immutability: What you CANNOT do ---
print("\n--- 3. Immutability: What you CANNOT do ---")

immutable_fs = frozenset([1, 2, 3])
print(f"Immutable frozenset: {immutable_fs}")

# 3.1 Cannot add elements
# try:
#     immutable_fs.add(4)
# except AttributeError as e:
#     print(f"Caught AttributeError: {e} - frozenset has no 'add' method.")

# 3.2 Cannot remove elements
# try:
#     immutable_fs.remove(1)
# except AttributeError as e:
#     print(f"Caught AttributeError: {e} - frozenset has no 'remove' method.")

# 3.3 Cannot clear elements
# try:
#     immutable_fs.clear()
# except AttributeError as e:
#     print(f"Caught AttributeError: {e} - frozenset has no 'clear' method.")

# 3.4 Cannot use pop()
# try:
#     immutable_fs.pop()
# except AttributeError as e:
#     print(f"Caught AttributeError: {e} - frozenset has no 'pop' method.")


# --- 4. Why Use Frozenset? (The Hashability Advantage) ---
print("\n--- 4. Why Use Frozenset? (The Hashability Advantage) ---")

# 4.1 As Dictionary Keys
# You can use a frozenset as a key in a dictionary because it's hashable.
# Regular sets cannot be dictionary keys.
permissions_dict = {
    frozenset({"read", "write"}): "Editor",
    frozenset({"read"}): "Viewer",
    frozenset({"read", "write", "delete"}): "Admin"
}
print(f"Permissions dictionary: {permissions_dict}")
print(f"Role for read/write: {permissions_dict[frozenset({'read', 'write'})]}")

# 4.2 As Elements in Other Sets (including regular sets or other frozensets)
# You can store frozensets inside a regular set or another frozenset.
# This allows for sets of sets.
set_of_sets = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})} # Duplicates are still removed
print(f"Set containing frozensets: {set_of_sets}")

# 4.3 Immutable Function Arguments
# When you need to pass a collection of unique items to a function
# and ensure it's not modified within the function.
def process_tags(tags: frozenset):
    print(f"\nProcessing tags: {tags}")
    # tags.add("new_tag") # This would cause an error
    if "important" in tags:
        print("Important tags found!")

my_product_tags = frozenset({"electronics", "sale", "new"})
process_tags(my_product_tags)


# --- 5. Frozenset Operations (Same as Regular Sets) ---
print("\n--- 5. Frozenset Operations ---")

fs_a = frozenset({1, 2, 3, 4, 5})
fs_b = frozenset({4, 5, 6, 7, 8})
fs_c = frozenset({1, 2})
regular_set_d = {5, 9} # Can interact with regular sets

print(f"Frozenset A: {fs_a}")
print(f"Frozenset B: {fs_b}")
print(f"Frozenset C: {fs_c}")
print(f"Regular Set D: {regular_set_d}")

# 5.1 Union: .union() or |
union_fs = fs_a.union(fs_b)
print(f"Union (A | B): {union_fs}")
union_with_regular = fs_a | regular_set_d
print(f"Union (A | D - with regular set): {union_with_regular}")

# 5.2 Intersection: .intersection() or &
intersection_fs = fs_a.intersection(fs_b)
print(f"Intersection (A & B): {intersection_fs}")

# 5.3 Difference: .difference() or -
difference_ab = fs_a.difference(fs_b)
print(f"Difference (A - B): {difference_ab}")

# 5.4 Symmetric Difference: .symmetric_difference() or ^
symmetric_difference_fs = fs_a.symmetric_difference(fs_b)
print(f"Symmetric Difference (A ^ B): {symmetric_difference_fs}")

# 5.5 Subset: .issubset() or <=
print(f"Is C a subset of A? {fs_c.issubset(fs_a)}")
print(f"Is A a subset of C? {fs_a <= fs_c}")

# 5.6 Superset: .issuperset() or >=
print(f"Is A a superset of C? {fs_a.issuperset(fs_c)}")
print(f"Is C a superset of A? {fs_c >= fs_a}")

# 5.7 Disjoint: .isdisjoint()
fs_e = frozenset({9, 10})
print(f"Are A and E disjoint? {fs_a.isdisjoint(fs_e)}") # No common elements
print(f"Are A and B disjoint? {fs_a.isdisjoint(fs_b)}") # False, they share 4, 5


# --- 6. Accessing Elements (Indirectly) and Iteration ---
print("\n--- 6. Accessing Elements (Indirectly) and Iteration ---")
# Like regular sets, frozensets are unordered and unindexed.
# You cannot access elements by position (e.g., fs[0]).

# 6.1 Iteration
print("Iterating through fs_a:")
for item in fs_a:
    print(item)

# 6.2 Converting to list/tuple for ordered access (creates a new data structure)
fs_example = frozenset({10, 20, 30})
list_from_fs = list(fs_example)
tuple_from_fs = tuple(fs_example)
print(f"Frozenset: {fs_example}")
print(f"Converted to list (order may vary): {list_from_fs}")
print(f"Converted to tuple (order may vary): {tuple_from_fs}")
if list_from_fs:
    print(f"Accessing first element after converting to list: {list_from_fs[0]}")


print("\n--- End of Python frozenset Practice Code ---")