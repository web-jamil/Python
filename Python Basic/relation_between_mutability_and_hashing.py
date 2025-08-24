# --- Python: Relation Between Mutability and Hashing in Code ---

# The relationship between mutability and hashing in Python is one of exclusion:
# mutable objects are generally NOT hashable. This is a fundamental design choice
# in Python that ensures the integrity and efficiency of hash-based data structures
# like dictionaries and sets.

# --- 1. What is Mutability? ---

print("--- 1. What is Mutability? ---")

# An object is "mutable" if its state (its value or contents) can be changed
# after it is created.

# 1.1 Examples of Mutable Types:
# - `list` (lists)
# - `dict` (dictionaries)
# - `set` (sets)
# - Custom objects (unless specifically designed to be immutable)
# - Bytearray

my_list = [1, 2, 3]
print(f"Original list: {my_list}, ID: {id(my_list)}")
my_list.append(4) # Modifying the list in-place
print(f"Modified list: {my_list}, ID: {id(my_list)}") # ID remains the same

my_dict = {"a": 1}
print(f"Original dict: {my_dict}, ID: {id(my_dict)}")
my_dict["b"] = 2 # Modifying the dictionary in-place
print(f"Modified dict: {my_dict}, ID: {id(my_dict)}") # ID remains the same

my_set = {1, 2}
print(f"Original set: {my_set}, ID: {id(my_set)}")
my_set.add(3) # Modifying the set in-place
print(f"Modified set: {my_set}, ID: {id(my_set)}") # ID remains the same


# --- 2. What is Hashing? ---

print("\n--- 2. What is Hashing? ---")

# Hashing is the process of converting an object into a fixed-size integer value (its hash code).
# In Python, objects that are "hashable" must satisfy two conditions:
# 1. They have a `__hash__` method that returns an integer.
# 2. Their hash value *must remain constant* throughout their lifetime.
# 3. They have an `__eq__` method, and if two objects are equal (`a == b`), their hash values must also be equal (`hash(a) == hash(b)`).

# The `hash()` built-in function computes the hash value.
print(f"Hash of integer 10: {hash(10)}")
print(f"Hash of string 'Python': {hash('Python')}")
print(f"Hash of tuple (1, 2): {hash((1, 2))}") # Tuples are immutable, so they are hashable if elements are.


# --- 3. The Exclusion: Why Mutable Objects Are Not Hashable ---

print("\n--- 3. The Exclusion: Why Mutable Objects Are Not Hashable ---")

# This is the core of the relationship:
# If an object's value can change after it's created, its hash value *could also change*.
# If a hash value changes while the object is being used as a key in a dictionary
# or an element in a set, it would break the internal data structure.

# Dictionaries and sets rely on hashing for their efficient lookups (average O(1) time complexity).
# When you add a key-value pair to a dictionary, Python calculates the key's hash and uses
# it to determine where to store the pair. If the key's hash changes later, the dictionary
# would look in the wrong place when trying to retrieve or update that key, leading to
# incorrect behavior or data loss.

# 3.1 Attempting to hash a list (will raise TypeError)
try:
    print("\n3.1 Attempting to hash a list...")
    my_list_to_hash = [1, 2, 3]
    list_hash = hash(my_list_to_hash)
    print(f"Hash of list: {list_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")

# 3.2 Attempting to hash a dictionary (will raise TypeError)
try:
    print("\n3.2 Attempting to hash a dictionary...")
    my_dict_to_hash = {"key": "value"}
    dict_hash = hash(my_dict_to_hash)
    print(f"Hash of dict: {dict_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'dict'.")

# 3.3 Attempting to hash a set (will raise TypeError)
try:
    print("\n3.3 Attempting to hash a set...")
    my_set_to_hash = {1, 2, 3}
    set_hash = hash(my_set_to_hash)
    print(f"Hash of set: {set_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'set'.")


# --- 4. Practical Implications: Dictionary Keys and Set Elements ---

print("\n--- 4. Practical Implications: Dictionary Keys and Set Elements ---")

# Because mutable objects are not hashable, they cannot be used as:
# - **Keys in dictionaries**
# - **Elements in sets**

# 4.1 Invalid Dictionary Key Example
try:
    print("\n4.1 Using a list as a dictionary key:")
    invalid_dict_key = {["item1", "item2"]: "Shopping List"}
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")

# 4.2 Invalid Set Element Example
try:
    print("\n4.2 Using a dictionary as a set element:")
    invalid_set_element = {1, 2, {"key": "value"}}
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'dict'.")

# 4.3 Mutable objects *within* an otherwise immutable object (e.g., tuple)
# If a tuple contains a mutable object, the tuple itself becomes unhashable.
unhashable_tuple = (1, [2, 3]) # Contains a mutable list
try:
    print(f"\n4.3 Attempting to hash a tuple with a mutable element: {unhashable_tuple}")
    hash(unhashable_tuple)
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")

# This rule ensures that if an object is used as a key or set element,
# its hash value will remain stable, guaranteeing correct behavior of the data structure.


# --- 5. When Mutability is Desired (and Hashing is Not Applicable) ---

print("\n--- 5. When Mutability is Desired ---")

# While mutable objects cannot be hashed, their mutability is incredibly useful for:
# 5.1 Dynamic Collections: Lists, dictionaries, and sets are perfect for data
#    that needs to grow, shrink, or change frequently.
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.remove("milk")

# 5.2 In-place Modifications: Efficiently update data without creating new objects.
user_settings = {"theme": "dark"}
user_settings["theme"] = "light" # Modify existing setting

# 5.3 Building Complex Structures: Mutable types can contain other mutable or immutable types,
#    allowing for highly flexible data models.
complex_data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ],
    "config": {"debug": True}
}