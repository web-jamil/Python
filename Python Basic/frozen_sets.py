# --- Frozen Sets in Python (Code Examples) ---

# Frozen sets are immutable versions of regular Python sets.
# Once a frozen set is created, you cannot add, remove, or modify its elements.
# They are useful when you need to use sets as keys in dictionaries or as elements in other sets,
# as these operations require hashable objects. Regular sets are mutable and thus not hashable.

# -------------------- 1. Creating Frozen Sets --------------------

# Creating a frozen set from an iterable (like a list or another set)
my_list = [1, 2, 3, 2, 1]
frozen_from_list = frozenset(my_list)
print(f"Frozen set from list: {frozen_from_list}, Type: {type(frozen_from_list)}")

my_set = {4, 5, 6}
frozen_from_set = frozenset(my_set)
print(f"Frozen set from set: {frozen_from_set}")

# Creating an empty frozen set
empty_frozen_set = frozenset()
print(f"Empty frozen set: {empty_frozen_set}")

# -------------------- 2. Immutability in Action --------------------

immutable_frozen_set = frozenset([10, 20, 30])

# Attempting to add an element will raise an AttributeError
# immutable_frozen_set.add(40)  # This line will cause an error

# Attempting to remove an element will also raise an AttributeError
# immutable_frozen_set.remove(20) # This line will cause an error

# Attempting to update the frozen set will also raise an AttributeError
# immutable_frozen_set.update([40, 50]) # This line will cause an error

# -------------------- 3. Set Operations on Frozen Sets --------------------

frozen_set_a = frozenset([1, 2, 3, 4, 5])
frozen_set_b = frozenset([4, 5, 6, 7, 8])

# All standard set operations are available and return new frozen sets
union_frozen = frozen_set_a.union(frozen_set_b)
print(f"Union of frozen sets A and B: {union_frozen}")

intersection_frozen = frozen_set_a.intersection(frozen_set_b)
print(f"Intersection of frozen sets A and B: {intersection_frozen}")

difference_frozen = frozen_set_a.difference(frozen_set_b)
print(f"Difference of frozen sets A and B (A - B): {difference_frozen}")

symmetric_difference_frozen = frozen_set_a.symmetric_difference(frozen_set_b)
print(f"Symmetric difference of frozen sets A and B: {symmetric_difference_frozen}")

# Comparisons also work as expected
is_subset_frozen = frozen_set_a([1, 2]).issubset(frozen_set_a)
print(f"Is frozenset([1, 2]) a subset of frozen_set_a? {is_subset_frozen}")

is_superset_frozen = frozen_set_a.issuperset(frozenset([4, 5]))
print(f"Is frozen_set_a a superset of frozenset([4, 5])? {is_superset_frozen}")

# -------------------- 4. Using Frozen Sets as Dictionary Keys --------------------

# Regular sets cannot be used as dictionary keys because they are not hashable
# my_dict = {{1, 2}: "value"}  # This will raise a TypeError

# Frozen sets, being immutable and hashable, can be used as dictionary keys
config_1 = frozenset({"host": "localhost", "port": 8080})
config_2 = frozenset({"host": "localhost", "port": 80})

settings = {
    config_1: "Default server settings",
    config_2: "Production server settings"
}

print(f"\nDictionary with frozen set keys: {settings}")
print(f"Settings for config_1: {settings[config_1]}")

# -------------------- 5. Using Frozen Sets as Elements of Other Sets --------------------

# Regular sets cannot contain other mutable sets as elements
# my_set_of_sets = {{1, 2}, {3, 4}}  # This will raise a TypeError

# Frozen sets can be elements of regular sets
set_of_frozen_sets = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}
print(f"\nSet of frozen sets: {set_of_frozen_sets} (duplicates are still removed)")

# -------------------- 6. When to Use Frozen Sets --------------------

# - When you need a set-like object that can be used as a key in a dictionary.
# - When you need a set-like object that can be an element of another set.
# - When you want to ensure that the contents of a set cannot be accidentally modified after creation, providing immutability.
# - In situations where you need a hashable representation of a set for comparison or storage purposes.

# In essence, frozen sets provide the benefits of sets (uniqueness, efficient membership testing and set operations) with the added property of immutability, making them suitable for use in contexts where mutability is not desired or allowed.