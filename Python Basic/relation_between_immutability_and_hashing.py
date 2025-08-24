# --- Python: Relation Between Immutability and Hashing in Code ---

# In Python, the concepts of immutability and hashing are deeply intertwined,
# especially when it comes to using objects as keys in dictionaries or as
# elements in sets.

# --- 1. What is Hashing? ---

print("--- 1. What is Hashing? ---")

# Hashing is the process of converting an arbitrary-sized input (like an object)
# into a fixed-size value (an integer hash code).
# In Python, objects that are "hashable" have a `__hash__` method and an `__eq__` method.

# Key properties of a good hash function:
# 1. Deterministic: For the same input, it must always produce the same hash value.
# 2. Efficient: It should be fast to compute.
# 3. Uniform Distribution: It should distribute hash values widely to minimize collisions.

# The `hash()` built-in function in Python computes the hash value of an object.

# 1.1 Hashing immutable objects
# Immutable objects like integers, floats, strings, and tuples (if they contain
# only hashable elements) are hashable.
print(f"Hash of integer 10: {hash(10)}")
print(f"Hash of string 'hello': {hash('hello')}")
print(f"Hash of tuple (1, 2): {hash((1, 2))}")
print(f"Hash of float 3.14: {hash(3.14)}")
print(f"Hash of True: {hash(True)}") # True hashes to 1
print(f"Hash of False: {hash(False)}") # False hashes to 0
print(f"Hash of None: {hash(None)}")

# Importantly, the hash value of an immutable object remains constant throughout its lifetime.
# Running the script again might give different hash values (due to hash randomization),
# but within a single run, for the same object, the hash is constant.
s = "Python"
print(f"\nString 'Python' hash: {hash(s)}")
# Even if we create another string with the same content, its hash will be the same.
s2 = "Python"
print(f"String 'Python' (another object) hash: {hash(s2)}")


# --- 2. What is Immutability? ---

print("\n--- 2. What is Immutability? ---")

# An object is "immutable" if its state (its value or contents) cannot be changed
# after it is created.

# 2.1 Examples of Immutable Types:
# - `int`, `float`, `complex` (numbers)
# - `str` (strings)
# - `tuple` (tuples, provided all their elements are also immutable)
# - `bool` (Booleans)
# - `NoneType` (None)
# - `frozenset` (immutable version of set)

# 2.2 Examples of Mutable Types:
# - `list` (lists)
# - `dict` (dictionaries)
# - `set` (sets)
# - Custom objects (unless specifically designed to be immutable)

my_list = [1, 2, 3]
print(f"Original list: {my_list}")
my_list.append(4) # List can be modified
print(f"Modified list: {my_list}")

my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")
try:
    my_tuple[0] = 10 # Attempt to modify tuple (will fail)
except TypeError as e:
    print(f"Error modifying tuple: {e}")


# --- 3. The Relationship: Why Hashable Implies Immutability ---

print("\n--- 3. The Relationship: Why Hashable Implies Immutability ---")

# For an object to be hashable (and thus usable as a dictionary key or set element),
# its hash value *must not change*.
# If an object were mutable and its hash value could change after it's placed
# in a hash-based collection (like a dictionary or set), the collection would
# no longer be able to find it.

# Imagine a dictionary internally uses the hash of a key to quickly find its location.
# If the key changes, its hash changes, and the dictionary would look in the wrong place.

# 3.1 Attempting to hash a mutable object (will raise TypeError)
# Lists, sets, and dictionaries are mutable, so they are not hashable.
try:
    print(f"Hash of list [1, 2]: {hash([1, 2])}")
except TypeError as e:
    print(f"Error hashing list: {e}")

try:
    print(f"Hash of set {{1, 2}}: {hash({1, 2})}")
except TypeError as e:
    print(f"Error hashing set: {e}")

try:
    print(f"Hash of dictionary {{'a': 1}}: {hash({'a': 1})}")
except TypeError as e:
    print(f"Error hashing dictionary: {e}")

# 3.2 Immutability of Tuple Elements for Hashing
# A tuple is hashable *only if all its elements are also hashable*.
# If a tuple contains a mutable object, the tuple itself becomes unhashable.
hashable_tuple = (1, "hello", (3, 4)) # All elements are immutable
print(f"\nHash of hashable tuple: {hash(hashable_tuple)}")

unhashable_tuple_with_list = (1, [2, 3]) # Contains a mutable list
try:
    print(f"Hash of unhashable tuple: {hash(unhashable_tuple_with_list)}")
except TypeError as e:
    print(f"Error hashing tuple with mutable element: {e}")


# --- 4. Practical Implications: Dictionary Keys and Set Elements ---

print("\n--- 4. Practical Implications: Dictionary Keys and Set Elements ---")

# The most direct consequence of this relationship is that:
# - **Dictionary keys must be hashable.**
# - **Elements of a set must be hashable.**

# 4.1 Valid Dictionary Keys
my_dict = {
    "name": "Alice",
    123: "ID",
    (10, 20): "Coordinates",
    frozenset({1, 2}): "Frozen Set Key" # frozenset is immutable, hence hashable
}
print(f"4.1 Dictionary with valid keys: {my_dict}")

# 4.2 Invalid Dictionary Keys (will raise TypeError)
try:
    invalid_dict = {['a', 'b']: "List as key"}
except TypeError as e:
    print(f"\n4.2 Error using list as dict key: {e}")

# 4.3 Valid Set Elements
my_set = {"apple", 10, (True, False), frozenset({3, 4})}
print(f"\n4.3 Set with valid elements: {my_set}")

# 4.4 Invalid Set Elements (will raise TypeError)
try:
    invalid_set = {1, 2, [3, 4]}
except TypeError as e:
    print(f"\n4.4 Error using list as set element: {e}")


# --- 5. When Immutability is Desired (Beyond Hashing) ---

print("\n--- 5. When Immutability is Desired (Beyond Hashing) ---")

# Even when hashing isn't the primary concern, immutability can be beneficial for:
# 5.1 Data Integrity: Ensures that data remains constant and cannot be accidentally modified.
#    E.g., configuration settings, API endpoints, or constants.
API_CONFIG = ("api.example.com", "/v1/users", 8080)
# No one can accidentally change API_CONFIG[0]

# 5.2 Thread Safety: Immutable objects are inherently thread-safe because their state
#    cannot be changed by multiple threads concurrently.
#    (Though Python's GIL often simplifies this for single-process multi-threading).

# 5.3 Functional Programming: Encourages pure functions that don't have side effects,
#    often by working with immutable data and returning new data structures.