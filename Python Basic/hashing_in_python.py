# --- Python: All About Hashing in Code ---

# Hashing is a fundamental concept in computer science, and in Python, it's
# crucial for the efficient operation of certain built-in data structures
# like dictionaries (`dict`) and sets (`set`).

# --- 1. What is Hashing? ---

print("--- 1. What is Hashing? ---")

# Hashing is the process of converting an arbitrary-sized input (e.g., a string,
# a number, an object) into a fixed-size value, typically an integer. This integer
# is called the "hash value" or "hash code."

# Key properties of a hash function in Python:
# 1.  **Deterministic:** For the same input object, the hash function must always
#     produce the same hash value *within a single Python process run*.
#     (Note: Hash values can differ between different Python runs due to hash randomization for security.)
# 2.  **Efficient:** The computation of the hash value should be very fast.
# 3.  **Collision Resistance (desirable):** A good hash function minimizes "collisions,"
#     where different inputs produce the same hash value. While collisions are
#     unavoidable for a finite output range, they should be rare.

# In Python, objects that are "hashable" have a `__hash__` method and an `__eq__` method.

# The built-in `hash()` function computes the hash value of an object.

# 1.1 Hashing immutable objects (Hashable by default)
# Immutable types like integers, floats, strings, tuples (if their elements are hashable),
# booleans, and None are hashable. Their hash value remains constant throughout their lifetime.

print(f"Hash of integer 10: {hash(10)}")
print(f"Hash of string 'hello': {hash('hello')}")
print(f"Hash of tuple (1, 2): {hash((1, 2))}")
print(f"Hash of float 3.14: {hash(3.14)}")
print(f"Hash of True: {hash(True)}")   # True hashes to 1
print(f"Hash of False: {hash(False)}") # False hashes to 0
print(f"Hash of None: {hash(None)}")

# Demonstrate determinism within a single run
s = "Python"
print(f"\nString '{s}' hash (first call): {hash(s)}")
print(f"String '{s}' hash (second call): {hash(s)}")
s_copy = "Python" # A new string object with the same value
print(f"String '{s_copy}' hash (new object, same value): {hash(s_copy)}") # Same hash as s


print("\n--- 2. The Link to Immutability ---")

# The most crucial rule for hashable objects is that their hash value *must not change*
# during their lifetime. This is why **mutable objects are generally not hashable**.

# If a mutable object (like a list) were used as a dictionary key and then modified,
# its hash value could change. The dictionary would then be unable to find the key
# because it would look in a different "bucket" based on the new hash.

# 2.1 Attempting to hash mutable objects (will raise TypeError)
# Lists, dictionaries, and sets are mutable, so they are not hashable.
try:
    print("\n2.1 Attempting to hash a list...")
    list_to_hash = [1, 2, 3]
    list_hash = hash(list_to_hash)
    print(f"Hash of list: {list_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")

try:
    print("\n2.2 Attempting to hash a dictionary...")
    dict_to_hash = {"key": "value"}
    dict_hash = hash(dict_to_hash)
    print(f"Hash of dict: {dict_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'dict'.")

try:
    print("\n2.3 Attempting to hash a set...")
    set_to_hash = {1, 2, 3}
    set_hash = hash(set_to_hash)
    print(f"Hash of set: {set_hash}") # This line won't be reached
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'set'.")

# 2.4 Tuples with mutable elements are also unhashable
# A tuple is hashable only if all its elements are also hashable.
unhashable_tuple = (1, [2, 3]) # Contains a mutable list
try:
    print(f"\n2.4 Attempting to hash a tuple with a mutable element: {unhashable_tuple}")
    hash(unhashable_tuple)
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")


print("\n--- 3. Hashing in Dictionaries (`dict`) ---")

# Dictionaries are implemented using hash tables. They use the hash value of keys
# to quickly find where a key-value pair is stored.

# 3.1 Using hashable objects as dictionary keys (Valid)
my_dict = {
    "name": "Alice",          # String key
    123: "User ID",           # Integer key
    (10, 20): "Coordinates",  # Tuple key (all elements immutable)
    frozenset({1, 2}): "Frozen Set Key" # Frozenset is immutable, hence hashable
}
print(f"3.1 Dictionary with valid (hashable) keys: {my_dict}")

# 3.2 Attempting to use unhashable objects as dictionary keys (Invalid)
try:
    print("\n3.2 Attempting to use a list as a dictionary key...")
    invalid_dict_key = {["item1", "item2"]: "Shopping List"}
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'list'.")


print("\n--- 4. Hashing in Sets (`set`) ---")

# Sets are also implemented using hash tables. They store unique, hashable elements.

# 4.1 Using hashable objects as set elements (Valid)
my_set = {"apple", 10, (True, False), frozenset({3, 4})}
print(f"4.1 Set with valid (hashable) elements: {my_set}")

# 4.2 Attempting to use unhashable objects as set elements (Invalid)
try:
    print("\n4.2 Attempting to use a dictionary as a set element...")
    invalid_set_element = {1, 2, {"key": "value"}}
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'dict'.")


print("\n--- 5. Custom Objects and Hashing ---")

# By default, custom class instances are hashable if they implement `__eq__`
# and `__hash__` is not explicitly set to `None`.
# If you implement `__eq__` but not `__hash__`, Python will make instances unhashable.
# If you implement both, you must ensure `__hash__` remains constant and
# `a == b` implies `hash(a) == hash(b)`.

# 5.1 Default hashing for custom objects (if no __eq__ or __hash__ is defined)
class MyObject:
    def __init__(self, value):
        self.value = value

obj1 = MyObject(1)
obj2 = MyObject(2)
obj1_copy = MyObject(1) # Different object, same value

print(f"5.1 Default hash of MyObject(1): {hash(obj1)}")
print(f"    Default hash of MyObject(2): {hash(obj2)}")
print(f"    Default hash of MyObject(1) (another instance): {hash(obj1_copy)}")
# By default, instances hash based on their memory address (ID), so obj1 and obj1_copy have different hashes.

# 5.2 Making custom objects hashable based on content
# To make objects hashable based on their content, you need to implement `__eq__` and `__hash__`.
# If the object is mutable, you cannot make it hashable based on its mutable content.
class ImmutablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, ImmutablePoint) and self.x == other.x and self.y == other.y

    def __hash__(self):
        # Hash based on the immutable attributes (x, y)
        return hash((self.x, self.y)) # Hashing a tuple of immutable values

p1 = ImmutablePoint(1, 2)
p2 = ImmutablePoint(3, 4)
p1_copy = ImmutablePoint(1, 2)

print(f"\n5.2 Hash of ImmutablePoint(1, 2): {hash(p1)}")
print(f"    Hash of ImmutablePoint(3, 4): {hash(p2)}")
print(f"    Hash of ImmutablePoint(1, 2) (another instance, same content): {hash(p1_copy)}") # Same hash!

# Now they can be used as dictionary keys or set elements
my_points_dict = {p1: "Start", p2: "End"}
print(f"    Dictionary with custom hashable objects: {my_points_dict}")
print(f"    Value for p1_copy: {my_points_dict[p1_copy]}") # Can retrieve using an equal object

my_points_set = {p1, p2, p1_copy} # p1_copy is considered equal to p1, so only one instance is stored
print(f"    Set with custom hashable objects: {my_points_set}") # Only two distinct points


# 5.3 Attempting to hash a mutable custom object
class MutableContainer:
    def __init__(self, data):
        self.data = data # data is a list, which is mutable

    def __eq__(self, other):
        return isinstance(other, MutableContainer) and self.data == other.data

    # If we try to define __hash__ based on mutable data, it's problematic
    # def __hash__(self):
    #     return hash(self.data) # This would fail because self.data is a list

mutable_obj = MutableContainer([1, 2])
try:
    print(f"\n5.3 Attempting to hash a mutable custom object: {mutable_obj}")
    hash(mutable_obj) # By default, if __eq__ is defined but __hash__ is not, it's unhashable.
except TypeError as e:
    print(f"    Error: {e} - Unhashable type: 'MutableContainer' (due to mutable content or missing __hash__).")