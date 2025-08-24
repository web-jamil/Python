import sys # For demonstrating memory usage

print("--- Python Iterators: Practice Code ---")

# --- 1. What are Iterators? ---
print("\n--- 1. What are Iterators? ---")
print("An iterator is an object that represents a stream of data.")
print("It allows you to traverse through all the elements of a collection one by one, without storing them all in memory at once.")
print("Iterators implement two special methods:")
print("  - `__iter__()`: Returns the iterator object itself. This allows an object to be iterable.")
print("  - `__next__()`: Returns the next item from the iteration. If there are no more items, it raises `StopIteration`.")

# --- 2. Iterables vs. Iterators ---
print("\n--- 2. Iterables vs. Iterators ---")
print("An **iterable** is any object that can be iterated over (e.g., lists, tuples, strings, dictionaries, sets).")
print("It has an `__iter__()` method (or a `__getitem__()` method that can be used for iteration).")

print("An **iterator** is an object that keeps track of the current state of iteration.")
print("It has both `__iter__()` (returning itself) and `__next__()` methods.")

my_list = [10, 20, 30]
print(f"my_list is an iterable: {hasattr(my_list, '__iter__')}") # True
print(f"my_list is an iterator: {hasattr(my_list, '__next__')}") # False

# Getting an iterator from an iterable using `iter()`
my_iterator = iter(my_list)
print(f"my_iterator is an iterable: {hasattr(my_iterator, '__iter__')}") # True
print(f"my_iterator is an iterator: {hasattr(my_iterator, '__next__')}") # True

# --- 3. Consuming an Iterator using `next()` ---
print("\n--- 3. Consuming an Iterator using `next()` ---")
print("You can manually get items from an iterator using the `next()` built-in function.")

# Get a fresh iterator
num_iterator = iter([1, 2, 3])

print(f"First item: {next(num_iterator)}")
print(f"Second item: {next(num_iterator)}")
print(f"Third item: {next(num_iterator)}")

try:
    print(f"Fourth item (attempting): {next(num_iterator)}")
except StopIteration:
    print("Caught StopIteration: No more items in the iterator.")

# Once an iterator is exhausted, it cannot be reused.
try:
    print(f"Fifth item (attempting after exhaustion): {next(num_iterator)}")
except StopIteration:
    print("Caught StopIteration again: Iterator remains exhausted.")


# --- 4. Iterators and `for` Loops ---
print("\n--- 4. Iterators and `for` Loops ---")
print("The `for` loop implicitly works with iterators.")
print("When you write `for item in iterable:`, Python internally does this:")
print("1. Calls `iter(iterable)` to get an iterator.")
print("2. Repeatedly calls `next()` on the iterator.")
print("3. Catches `StopIteration` to know when to end the loop.")

print("Iterating over a list using a for loop:")
for num in [4, 5, 6]:
    print(f"Loop item: {num}")

# The list [4, 5, 6] is an iterable. The `for` loop gets an iterator from it.


# --- 5. Creating Your Own Iterator (Custom Iterator Class) ---
print("\n--- 5. Creating Your Own Iterator (Custom Iterator Class) ---")
print("You can define your own custom iterators by creating a class that implements `__iter__` and `__next__`.")

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # __iter__ should return the iterator object itself
        return self

    def __next__(self):
        if self.current < self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

# Using our custom iterator
print("\nUsing MyRange custom iterator:")
for i in MyRange(1, 5):
    print(f"MyRange item: {i}")

# Demonstrate exhaustion
my_range_iter = MyRange(1, 3)
print(f"Next from my_range_iter: {next(my_range_iter)}")
print(f"Next from my_range_iter: {next(my_range_iter)}")
try:
    next(my_range_iter) # This will raise StopIteration
except StopIteration:
    print("MyRange iterator exhausted.")


# --- 6. Generators and Generator Expressions (Easier Iterators) ---
print("\n--- 6. Generators and Generator Expressions (Easier Iterators) ---")
print("Python provides a much simpler way to create iterators using generator functions and expressions.")

# 6.1 Generator Functions (`yield` keyword)
print("\n6.1 Generator Functions:")
def my_generator(n):
    current = 0
    while current < n:
        yield current # `yield` makes this a generator function, returning a generator iterator
        current += 1

# Using the generator function
gen_obj = my_generator(5)
print(f"Generator object: {gen_obj}")
print(f"Type of generator object: {type(gen_obj)}")

print("Iterating over generator:")
for val in gen_obj:
    print(f"Gen item: {val}")

# Generators are also single-use:
gen_obj_re_use = my_generator(3)
print(f"Next from gen_obj_re_use: {next(gen_obj_re_use)}")
print(f"Next from gen_obj_re_use: {next(gen_obj_re_use)}")
try:
    next(gen_obj_re_use)
except StopIteration:
    print("Generator exhausted.")


# 6.2 Generator Expressions (similar to list comprehensions but with `()`)
print("\n6.2 Generator Expressions:")
# List comprehension (creates list in memory):
list_comp = [x * 2 for x in range(10)]
print(f"List comprehension (size: {sys.getsizeof(list_comp)} bytes): {list_comp[:5]}...")

# Generator expression (creates iterator, values on demand):
gen_exp = (x * 2 for x in range(10)) # Uses parentheses instead of brackets
print(f"Generator expression (size: {sys.getsizeof(gen_exp)} bytes): {gen_exp}")

print("Iterating over generator expression:")
for val in gen_exp:
    if val > 10: # We can stop early
        break
    print(f"Gen exp item: {val}")

# Memory efficiency of generators/iterators
# Imagine working with a billion numbers:
# large_list = [i for i in range(1_000_000_000)] # Would consume huge memory
# large_gen = (i for i in range(1_000_000_000)) # Consumes very little memory
# This allows processing huge datasets without memory overflow.


# --- 7. Advantages of Iterators ---
print("\n--- 7. Advantages of Iterators ---")
print("- **Memory Efficiency (Lazy Evaluation):** They generate items on demand, not all at once. Ideal for large datasets.")
print("- **Infinite Sequences:** Can represent sequences that are theoretically infinite (e.g., Fibonacci sequence).")
print("- **Performance:** For one-time processing, they can be faster than creating full lists.")
print("- **Clean Code:** Simplify loops and data processing pipelines.")

print("\nExample: Infinite Fibonacci sequence (conceptually)")
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
print("\nFirst 10 Fibonacci numbers:")
for _ in range(10):
    print(next(fib_gen), end=" ")
print() # New line


print("\n--- End of Python Iterators Practice Code ---")