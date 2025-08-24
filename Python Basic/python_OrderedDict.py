from collections import OrderedDict

print("--- Python collections.OrderedDict: All About in Code ---")

# --- 1. Introduction & Basic Creation ---
print("\n--- 1. Introduction & Basic Creation ---")
print("OrderedDict remembers the order in which its key-value pairs were inserted.")
print("It is a subclass of dict.")

# 1.1 Creating an OrderedDict
# From an iterable of key-value pairs (e.g., list of tuples)
ordered_dict1 = OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])
print(f"OrderedDict 1 (from list of tuples): {ordered_dict1}")

# From keyword arguments
ordered_dict2 = OrderedDict(name='Alice', age=30, city='New York')
print(f"OrderedDict 2 (from keyword arguments): {ordered_dict2}")

# From an existing dictionary (order is arbitrary unless it's already ordered)
# If created from a regular dict, the order will depend on how the dict was internally iterated.
# For Python 3.7+, a regular dict will preserve insertion order upon creation of OrderedDict from it.
regular_dict = {'d': 4, 'c': 3, 'a': 1, 'b': 2}
ordered_dict3 = OrderedDict(regular_dict) # Order might not be as defined if regular_dict is pre-3.7 or built in a different order
print(f"OrderedDict 3 (from regular dict): {ordered_dict3}") # Will likely print d,c,a,b if regular_dict was built that way

# Adding elements
ordered_dict1['grape'] = 4
ordered_dict1['date'] = 5
print(f"OrderedDict 1 after adding elements: {ordered_dict1}")


print("\n--- 2. Accessing and Iterating Elements (Order Preservation) ---")

# 2.1 Accessing elements by key
print(f"Value for 'banana': {ordered_dict1['banana']}")

# 2.2 Iterating over keys, values, and items
print("Iterating over keys (in insertion order):")
for key in ordered_dict1:
    print(key, end=" ")
print()

print("Iterating over values (in insertion order):")
for value in ordered_dict1.values():
    print(value, end=" ")
print()

print("Iterating over items (in insertion order):")
for key, value in ordered_dict1.items():
    print(f"({key}: {value})", end=" ")
print()


print("\n--- 3. `OrderedDict` Specific Methods ---")

# 3.1 `move_to_end(key, last=True)`: Moves an existing key to either end of the OrderedDict.
# If `last=True` (default), moves to the end. If `last=False`, moves to the beginning.
print(f"Original ordered_dict1: {ordered_dict1}")

ordered_dict1.move_to_end('apple')
print(f"After moving 'apple' to end: {ordered_dict1}")

ordered_dict1.move_to_end('banana', last=False)
print(f"After moving 'banana' to beginning: {ordered_dict1}")

# 3.2 `popitem(last=True)`: Removes and returns a (key, value) pair.
# If `last=True` (default), LIFO (Last In, First Out) order.
# If `last=False`, FIFO (First In, First Out) order.
print(f"\nOrderedDict before popitem: {ordered_dict1}")
popped_item_lru = ordered_dict1.popitem() # Removes 'date'
print(f"Popped item (LIFO, default): {popped_item_lru}")
print(f"OrderedDict after LIFO pop: {ordered_dict1}")

popped_item_fifo = ordered_dict1.popitem(last=False) # Removes 'banana'
print(f"Popped item (FIFO): {popped_item_fifo}")
print(f"OrderedDict after FIFO pop: {ordered_dict1}")


print("\n--- 4. Equality Comparison (`==`) ---")
print("For OrderedDicts, equality (`==`) checks both keys/values AND insertion order.")
print("For regular dicts (Python 3.7+), equality only checks keys/values (order doesn't matter for `==`).")

od_a = OrderedDict([('x', 1), ('y', 2)])
od_b = OrderedDict([('y', 2), ('x', 1)]) # Different insertion order
od_c = OrderedDict([('x', 1), ('y', 2)]) # Same insertion order as od_a

print(f"od_a: {od_a}")
print(f"od_b: {od_b}")
print(f"od_c: {od_c}")

print(f"od_a == od_b: {od_a == od_b}") # False (order differs)
print(f"od_a == od_c: {od_a == od_c}") # True (order and content match)

# Compare with regular dicts
dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 2, 'x': 1}

print(f"dict_a == dict_b: {dict_a == dict_b}") # True (for regular dicts, order doesn't affect ==)


print("\n--- 5. When to Still Use `OrderedDict` (Post Python 3.7) ---")
print("While standard `dict` preserves insertion order since Python 3.7, `OrderedDict` is still useful for:")

print("\n--- 5.1 Explicit Clarity ---")
print("  - If preserving insertion order is a critical design invariant for your data structure,")
print("    using `OrderedDict` explicitly communicates this intent to other developers.")

print("\n--- 5.2 The `move_to_end()` Method ---")
print("  - This unique method is not available on standard `dict` and is crucial for implementations")
print("    like LRU (Least Recently Used) caches.")

print("Example: Simple LRU Cache using `OrderedDict`")
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed item to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: int) -> None:
        if key in self.cache:
            # If exists, update value and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # If new, add it
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # If cache exceeds capacity, remove the first (least recently used) item
                self.cache.popitem(last=False)

lru = LRUCache(3)
lru.put('a', 1) # Cache: {'a': 1}
lru.put('b', 2) # Cache: {'a': 1, 'b': 2}
lru.put('c', 3) # Cache: {'a': 1, 'b': 2, 'c': 3}
print(f"LRU Cache after initial puts: {lru.cache}")

print(f"Get 'b': {lru.get('b')}") # Cache: {'a': 1, 'c': 3, 'b': 2} ('b' moved to end)
print(f"Cache after get('b'): {lru.cache}")

lru.put('d', 4) # Cache: {'c': 3, 'b': 2, 'd': 4} ('a' was least recently used, popped)
print(f"Cache after put('d',4) (capacity exceeded): {lru.cache}")

print(f"Get 'a': {lru.get('a')}") # Output: -1 (not found)
print(f"Cache after get('a'): {lru.cache}") # No change

print("\n--- 5.3 Working with Older Python Versions (Pre-3.7) ---")
print("  - If your code needs to run on Python versions older than 3.7, `OrderedDict` is essential")
print("    for guaranteed insertion order preservation.")


print("\n--- 6. Performance Considerations ---")
print("In Python 3.7+, standard `dict` is generally more optimized and performs slightly better")
print("for most common operations (insertion, deletion, lookup) than `OrderedDict`.")
print("Only use `OrderedDict` if you specifically need its unique `move_to_end()` method")
print("or its stricter equality comparison (where order matters).")