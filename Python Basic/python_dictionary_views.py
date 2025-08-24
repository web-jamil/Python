print("--- Python Dictionary Views ---")
print("-------------------------------\n")

# Dictionary views are dynamic, read-only objects that provide a "view" into
# a dictionary's keys, values, or key-value pairs (items).
# They are not lists and do not contain copies of the dictionary's data.
# Instead, they reflect the current state of the dictionary.
# This means if the original dictionary changes, the view also changes.

# Three types of dictionary views:
# 1. `dict.keys()`: A view object that displays a list of all the keys in the dictionary.
# 2. `dict.values()`: A view object that displays a list of all the values in the dictionary.
# 3. `dict.items()`: A view object that displays a list of a dictionary's key-value tuple pairs.

print("Let's start with a sample dictionary:")
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Software Engineer"
}
print(f"Original Dictionary: {my_dict}\n")


# --- 1. `dict.keys()` View ---
print("1. `dict.keys()` View:")
keys_view = my_dict.keys()
print(f"Keys View: {keys_view}")
print(f"Type of keys_view: {type(keys_view)}")

print("\n--- Demonstrating dynamism of keys view ---")
print("Modifying the original dictionary:")
my_dict["country"] = "USA"
del my_dict["age"]
print(f"Modified Dictionary: {my_dict}")
print(f"Keys View (after modification): {keys_view}") # The view automatically updates
print("Notice how 'country' is added and 'age' is removed in the view.\n")

print("--- Operations on keys view ---")
# Membership testing (efficient for keys)
print(f"'name' in keys_view: {'name' in keys_view}")
print(f"'age' in keys_view: {'age' in keys_view}") # False now
print(f"'country' in keys_view: {'country' in keys_view}\n")

# Iteration
print("Iterating through keys_view:")
for key in keys_view:
    print(f"  Key: {key}")
print()

# Conversion to list (creates a static copy)
keys_list = list(keys_view)
print(f"Keys converted to list: {keys_list}")
my_dict["new_key"] = 99 # Add another item
print(f"Keys List (after further modification): {keys_list}") # List does NOT update
print(f"Keys View (after further modification): {keys_view}\n")


# --- 2. `dict.values()` View ---
print("2. `dict.values()` View:")
values_view = my_dict.values()
print(f"Values View: {values_view}")
print(f"Type of values_view: {type(values_view)}")

print("\n--- Demonstrating dynamism of values view ---")
my_dict["city"] = "London" # Change a value
my_dict["company"] = "Google" # Add a new key-value pair
print(f"Modified Dictionary: {my_dict}")
print(f"Values View (after modification): {values_view}") # The view updates
print("Notice how 'New York' changed to 'London' and 'Google' is added.\n")

print("--- Operations on values view ---")
# Membership testing (less efficient than for keys, needs to scan all values)
print(f"'Alice' in values_view: {'Alice' in values_view}")
print(f"'London' in values_view: {'London' in values_view}")
print(f"'Paris' in values_view: {'Paris' in values_view}\n")

# Iteration
print("Iterating through values_view:")
for value in values_view:
    print(f"  Value: {value}")
print()

# Conversion to list
values_list = list(values_view)
print(f"Values converted to list: {values_list}\n")


# --- 3. `dict.items()` View ---
print("3. `dict.items()` View:")
items_view = my_dict.items()
print(f"Items View: {items_view}")
print(f"Type of items_view: {type(items_view)}")

print("\n--- Demonstrating dynamism of items view ---")
my_dict["name"] = "Bob" # Change a key's value
del my_dict["occupation"] # Remove an item
print(f"Modified Dictionary: {my_dict}")
print(f"Items View (after modification): {items_view}") # The view updates
print("Notice how ('Alice') changed to ('Bob') and 'occupation' pair is removed.\n")

print("--- Operations on items view ---")
# Membership testing (checks for exact key-value pair tuple)
print(f"('name', 'Bob') in items_view: {('name', 'Bob') in items_view}")
print(f"('city', 'New York') in items_view: {('city', 'New York') in items_view}") # False now
print(f"('city', 'London') in items_view: {('city', 'London') in items_view}\n")

# Iteration (most common way to iterate through key-value pairs)
print("Iterating through items_view:")
for key, value in items_view: # Unpacking the tuple
    print(f"  Key: {key}, Value: {value}")
print()

# Conversion to list
items_list = list(items_view)
print(f"Items converted to list: {items_list}\n")


# --- Key Characteristics and Benefits of Dictionary Views ---
print("--- Key Characteristics and Benefits ---")

print("\n1. Dynamic Nature (Live View):")
original = {'a': 1, 'b': 2}
k_view = original.keys()
v_view = original.values()
i_view = original.items()

print(f"Initial: {original}, Keys: {k_view}, Values: {v_view}, Items: {i_view}")
original['c'] = 3
original['a'] = 10
del original['b']
print(f"After change: {original}, Keys: {k_view}, Values: {v_view}, Items: {i_view}")
print("Views reflect changes immediately. This is a primary benefit.\n")

print("2. Memory Efficiency:")
# Views do not copy the dictionary data, saving memory, especially for large dictionaries.
# They just provide an interface to the underlying data structure.

print("3. Iterability:")
# All view objects are iterable. This allows you to loop directly over keys, values, or items.
# This is often more efficient than converting to a list first if you only need to iterate once.

print("4. Set-like Operations (for keys view and items view in Python 3.x):")
# `keys()` views support set-like operations (union, intersection, difference, symmetric difference)
# when compared with other key views or sets.
# `items()` views also support these. `values()` views do not.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 3, 'd': 4}

keys1 = dict1.keys()
keys2 = dict2.keys()

print(f"Keys 1: {keys1}")
print(f"Keys 2: {keys2}")
print(f"Intersection of keys: {keys1 & keys2}") # {'b', 'c'}
print(f"Union of keys: {keys1 | keys2}")      # {'a', 'b', 'c', 'd'}
print(f"Keys in dict1 but not dict2: {keys1 - keys2}\n") # {'a'}

# For items view, comparison requires exact (key, value) match
items1 = dict1.items()
items2 = dict2.items()
print(f"Items 1: {items1}")
print(f"Items 2: {items2}")
print(f"Intersection of items: {items1 & items2}") # Only ('c', 3) is common
print("Note: Items view intersection only includes (key, value) pairs that are identical in both.\n")

print("5. Read-Only Nature:")
# You cannot modify the dictionary through its views.
# For example, `keys_view.append('x')` would raise an AttributeError.
try:
    keys_view.add("new_key_from_view")
except AttributeError as e:
    print(f"Attempting to modify keys_view failed: {e}")
print("Views are not mutable sequences themselves; they just reflect the dictionary.\n")


print("--- End of Python Dictionary Views Demonstration ---")