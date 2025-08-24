# --- Python Dictionaries: All About Dictionary Views in Code ---

# In Python 3, the `keys()`, `values()`, and `items()` methods of dictionaries
# return "view objects" instead of lists. These view objects provide a dynamic,
# real-time view into the dictionary's contents.

# --- 1. What are Dictionary Views? ---

print("--- 1. What are Dictionary Views? ---")

# - **Dynamic:** They are not static copies. If the dictionary changes (items are
#   added, removed, or updated), the view objects automatically reflect these changes.
# - **Iterable:** You can iterate over them using `for` loops.
# - **Memory Efficient:** They don't copy the entire dictionary's contents into a new list,
#   which saves memory, especially for large dictionaries. They provide an "on-demand"
#   access to the dictionary's elements.
# - **Set-like Operations (for keys and items views):** `dict_keys` and `dict_items`
#   views support set-like operations (like union, intersection, difference) because
#   keys and items (as tuples) are unique and hashable. `dict_values` do not, as
#   values can be duplicated and are not necessarily hashable.

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}

print(f"Original Dictionary: {my_dict}")

# Get view objects
keys_view = my_dict.keys()
values_view = my_dict.values()
items_view = my_dict.items()

print(f"\n1.1 Initial Views:")
print(f"Keys View: {keys_view}, Type: {type(keys_view)}")
print(f"Values View: {values_view}, Type: {type(values_view)}")
print(f"Items View: {items_view}, Type: {type(items_view)}")


# --- 2. Dynamic Nature of Views ---

print("\n--- 2. Dynamic Nature of Views ---")

# Let's modify the dictionary and observe how the views change automatically.

print(f"Dictionary before modification: {my_dict}")
print(f"Keys view before modification: {keys_view}")
print(f"Values view before modification: {values_view}")
print(f"Items view before modification: {items_view}")

# 2.1 Add a new key-value pair
my_dict["email"] = "alice@example.com"
print(f"\n2.1 After adding 'email':")
print(f"Dictionary: {my_dict}")
print(f"Keys View: {keys_view}")    # 'email' is now included
print(f"Values View: {values_view}") # 'alice@example.com' is now included
print(f"Items View: {items_view}")  # ('email', 'alice@example.com') is now included

# 2.2 Update an existing value
my_dict["age"] = 31
print(f"\n2.2 After updating 'age':")
print(f"Dictionary: {my_dict}")
print(f"Keys View: {keys_view}")    # No change to keys
print(f"Values View: {values_view}") # 'age' value is updated to 31
print(f"Items View: {items_view}")  # ('age', 31) is reflected

# 2.3 Delete a key-value pair
del my_dict["occupation"]
print(f"\n2.3 After deleting 'occupation':")
print(f"Dictionary: {my_dict}")
print(f"Keys View: {keys_view}")    # 'occupation' is removed
print(f"Values View: {values_view}") # 'Engineer' is removed
print(f"Items View: {items_view}")  # ('occupation', 'Engineer') is removed


# --- 3. Iterating Over Views ---

print("\n--- 3. Iterating Over Views ---")

# Views are iterable, which is why they are often used in `for` loops.

print(f"Current Dictionary: {my_dict}")

print("\n3.1 Iterating over `keys_view`:")
for key in keys_view:
    print(f"Key: {key}")

print("\n3.2 Iterating over `values_view`:")
for value in values_view:
    print(f"Value: {value}")

print("\n3.3 Iterating over `items_view` (most common for key-value access):")
for key, value in items_view:
    print(f"Key: {key}, Value: {value}")


# --- 4. Converting Views to Lists ---

print("\n--- 4. Converting Views to Lists ---")

# If you need a static copy of the keys, values, or items (e.g., to modify
# the dictionary while iterating, or to pass to a function that requires a list),
# you can explicitly convert the view object to a list.

list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())
list_of_items = list(my_dict.items())

print(f"List of Keys: {list_of_keys}, Type: {type(list_of_keys)}")
print(f"List of Values: {list_of_values}, Type: {type(list_of_values)}")
print(f"List of Items: {list_of_items}, Type: {type(list_of_items)}")

# Demonstrate that lists are static copies:
my_dict["new_key"] = "new_value"
print(f"\nAfter adding 'new_key' to dictionary:")
print(f"Keys View (dynamic): {my_dict.keys()}")
print(f"List of Keys (static copy): {list_of_keys}") # 'new_key' is NOT in this list


# --- 5. Set-like Operations on `dict_keys` and `dict_items` Views ---

print("\n--- 5. Set-like Operations on Views ---")

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

keys1 = dict1.keys()
keys2 = dict2.keys()

items1 = dict1.items()
items2 = dict2.items()

print(f"Dict1 keys: {keys1}, Dict2 keys: {keys2}")
print(f"Dict1 items: {items1}, Dict2 items: {items2}")

# 5.1 Union (`|` or `.union()`)
# Keys present in either dictionary
union_keys = keys1 | keys2
print(f"\n5.1 Union of keys (keys1 | keys2): {union_keys}") # {'a', 'b', 'c', 'd'}

# Items present in either dictionary (exact key-value pair)
union_items = items1 | items2
print(f"    Union of items (items1 | items2): {union_items}") # {('a', 1), ('b', 2), ('c', 3), ('b', 20), ('c', 30), ('d', 4)}
# Note: Since ('b',2) and ('b',20) are distinct tuples, both are included.

# 5.2 Intersection (`&` or `.intersection()`)
# Keys common to both dictionaries
intersection_keys = keys1 & keys2
print(f"\n5.2 Intersection of keys (keys1 & keys2): {intersection_keys}") # {'b', 'c'}

# Items common to both dictionaries (exact key-value pair)
# In this example, no item is exactly common because values for 'b' and 'c' differ.
intersection_items = items1 & items2
print(f"    Intersection of items (items1 & items2): {intersection_items}") # set()

# Let's make an item common for demonstration
dict3 = {"x": 10, "y": 20}
dict4 = {"y": 20, "z": 30}
items3 = dict3.items()
items4 = dict4.items()
common_item = items3 & items4
print(f"    Common item between {{'x':10, 'y':20}} and {{'y':20, 'z':30}}: {common_item}") # {('y', 20)}


# 5.3 Difference (`-` or `.difference()`)
# Keys in the first dictionary but not in the second
difference_keys = keys1 - keys2
print(f"\n5.3 Difference of keys (keys1 - keys2): {difference_keys}") # {'a'}

# Items in the first dictionary but not in the second
difference_items = items1 - items2
print(f"    Difference of items (items1 - items2): {difference_items}") # {('a', 1), ('b', 2), ('c', 3)}


# 5.4 Symmetric Difference (`^` or `.symmetric_difference()`)
# Keys that are in either dictionary, but not in both
symmetric_difference_keys = keys1 ^ keys2
print(f"\n5.4 Symmetric Difference of keys (keys1 ^ keys2): {symmetric_difference_keys}") # {'a', 'd'}

# Items that are in either dictionary, but not in both
symmetric_difference_items = items1 ^ items2
print(f"    Symmetric Difference of items (items1 ^ items2): {symmetric_difference_items}")
# {('a', 1), ('b', 2), ('c', 3), ('b', 20), ('c', 30), ('d', 4)}


# 5.5 Subset (`<=`) and Superset (`>=`) Checks
# Check if all keys/items of one view are present in another.
print(f"\n5.5 Subset/Superset Checks:")
subset_keys = {'a', 'b'}
print(f"    Is {{'a', 'b'}} a subset of keys1? {subset_keys <= keys1}") # True
print(f"    Is keys1 a superset of {{'a', 'b'}}? {keys1 >= subset_keys}") # True

# Note: `dict_values` views do not support set-like operations directly because
# values are not necessarily unique or hashable.