# --- Basic Set Operations in Python (Code Examples) ---

# -------------------- 1. Creating Sets --------------------

# Empty Set
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")

# Set with initial elements
my_set = {1, 2, 3}
print(f"Initial set: {my_set}")

# Creating a set from a list (duplicates are automatically removed)
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
set_from_list = set(my_list)
print(f"Set from list (duplicates removed): {set_from_list}")

# Note: You cannot create a set with mutable elements like lists.
# Trying to do so will result in a TypeError.
# Example (will cause an error):
# invalid_set = {[1, 2]}

# -------------------- 2. Adding Elements --------------------

my_set_to_add = {10, 20}

# Adding a single element using .add()
my_set_to_add.add(30)
print(f"Set after adding 30: {my_set_to_add}")

# Adding multiple elements using .update() with a list
my_set_to_add.update([40, 50])
print(f"Set after updating with [40, 50]: {my_set_to_add}")

# Adding multiple elements using .update() with another set
another_set_to_add = {60, 70}
my_set_to_add.update(another_set_to_add)
print(f"Set after updating with another set: {my_set_to_add}")

# Note: .add() takes a single element, while .update() can take an iterable (like a list or another set).

# -------------------- 3. Removing Elements --------------------

my_set_to_remove = {1, 2, 3, 4, 5}

# Removing a specific element using .remove()
# If the element is not in the set, it raises a KeyError.
my_set_to_remove.remove(3)
print(f"Set after removing 3: {my_set_to_remove}")

# Removing a specific element using .discard()
# If the element is not in the set, it does nothing (no error).
my_set_to_remove.discard(5)
print(f"Set after discarding 5: {my_set_to_remove}")
my_set_to_remove.discard(10) # Element not present, no error
print(f"Set after discarding 10 (not present): {my_set_to_remove}")

# Removing an arbitrary element using .pop()
# Returns the removed element. Since sets are unordered, you don't know which element will be removed.
set_to_pop = {100, 200, 300}
popped_element = set_to_pop.pop()
print(f"Set after popping: {set_to_pop}, Popped element: {popped_element}")

# -------------------- 4. Checking Membership --------------------

my_set_to_check = {10, 20, 30, 40}

# Using the 'in' operator to check if an element is present
is_20_present = 20 in my_set_to_check
print(f"Is 20 in the set? {is_20_present}")

is_50_present = 50 in my_set_to_check
print(f"Is 50 in the set? {is_50_present}")

# Using the 'not in' operator to check if an element is not present
is_60_not_present = 60 not in my_set_to_check
print(f"Is 60 not in the set? {is_60_not_present}")

# -------------------- 5. Set Size --------------------

my_set_to_count = {1, 2, 3, 4, 5}

# Getting the number of elements in a set using the len() function
set_size = len(my_set_to_count)
print(f"Size of the set: {set_size}")

# -------------------- 6. Clearing a Set --------------------

my_set_to_clear = {1, 2, 3}
print(f"Set before clearing: {my_set_to_clear}")

# Removing all elements from a set using .clear()
my_set_to_clear.clear()
print(f"Set after clearing: {my_set_to_clear}")

# -------------------- Summary of Basic Operations --------------------
# - `set()`: Creates a new empty set or a set from an iterable.
# - `{}`: Creates a set with initial elements.
# - `.add(element)`: Adds a single element to the set.
# - `.update(iterable)`: Adds multiple elements from an iterable to the set.
# - `.remove(element)`: Removes a specific element (raises KeyError if not found).
# - `.discard(element)`: Removes a specific element (does nothing if not found).
# - `.pop()`: Removes and returns an arbitrary element.
# - `in`: Checks if an element is present in the set.
# - `not in`: Checks if an element is not present in the set.
# - `len(set)`: Returns the number of elements in the set.
# - `.clear()`: Removes all elements from the set.