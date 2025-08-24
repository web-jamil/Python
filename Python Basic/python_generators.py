import sys # For demonstrating memory usage

print("--- Python Generators: Practice Code ---")

# --- 1. What are Generators? ---
print("\n--- 1. What are Generators? ---")
print("Generators are a special type of iterator in Python.")
print("They allow you to create iterators in a more concise and readable way than implementing `__iter__` and `__next__` methods manually.")
print("Key characteristics:")
print(" - **Lazy Evaluation:** They don't store all their values in memory at once.")
print("   Instead, they generate values one by one on demand.")
print(" - **Memory Efficient:** Ideal for processing large datasets or infinite sequences.")
print(" - **Pausable:** They 'pause' execution after yielding a value and resume from where they left off.")
print(" - **Single-Use:** Once exhausted, they cannot be iterated over again without re-creating them.")


# --- 2. Generator Functions (using `yield` keyword) ---
print("\n--- 2. Generator Functions (using `yield` keyword) ---")
print("A function becomes a generator function if it contains one or more `yield` statements.")
print("When called, a generator function doesn't execute its body immediately; it returns a generator iterator object.")

# Example 2.1: Simple countdown generator
def countdown(n):
    print("Starting countdown...")
    while n > 0:
        yield n # `yield` makes this a generator
        n -= 1
    print("Countdown finished!")

# Calling the generator function returns a generator object
c = countdown(3)
print(f"Generator object: {c}")
print(f"Type of generator object: {type(c)}")

# To get values from the generator, you iterate or use `next()`
print("\nConsuming the countdown generator with `next()`:")
print(f"Next: {next(c)}") # Executes until first yield
print(f"Next: {next(c)}") # Resumes from where it left off
print(f"Next: {next(c)}")
try:
    print(f"Next: {next(c)}") # Will raise StopIteration as no more yields
except StopIteration:
    print("Caught StopIteration: Countdown generator exhausted.")

print("\nConsuming the countdown generator with a `for` loop (preferred):")
for num in countdown(5): # Creates a new generator object
    print(f"Count: {num}")


# Example 2.2: Generating even numbers up to N
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print("\nEven numbers up to 10:")
for num in even_numbers(10):
    print(num, end=" ")
print()


# --- 3. Generator Expressions (similar to list comprehensions) ---
print("\n--- 3. Generator Expressions (similar to list comprehensions) ---")
print("Generator expressions are a more concise way to create generators for simple cases,")
print("using parentheses `()` instead of square brackets `[]` (like list comprehensions).")

# Example 3.1: Doubling numbers using generator expression
numbers = [1, 2, 3, 4, 5]
doubled_gen_exp = (x * 2 for x in numbers)
print(f"\nGenerator expression: {doubled_gen_exp}")
print(f"Type of generator expression: {type(doubled_gen_exp)}")

print("Iterating over doubled_gen_exp:")
for val in doubled_gen_exp:
    print(val, end=" ")
print()

# Example 3.2: Filtering and transforming
filtered_squared_gen = (x**2 for x in range(10) if x % 2 != 0)
print("\nFiltered and squared numbers (odd numbers up to 9):")
print(list(filtered_squared_gen)) # Consume it all at once for demonstration


# --- 4. Memory Efficiency of Generators ---
print("\n--- 4. Memory Efficiency of Generators ---")
print("This is one of the primary advantages of generators.")
print("They only keep track of their state and generate values on demand.")

# Creating a large list vs. a large generator
num_elements = 1_000_000 # One million elements

# List comprehension: All elements are created and stored in memory
list_data = [i for i in range(num_elements)]
print(f"\nSize of list (1M elements): {sys.getsizeof(list_data)} bytes")
# This size includes references to the integer objects, not just the list structure.
# Actual memory usage might be higher depending on Python's integer optimization.

# Generator expression: Only the generator object itself is in memory
gen_data = (i for i in range(num_elements))
print(f"Size of generator object (1M elements): {sys.getsizeof(gen_data)} bytes (much smaller!)")

# You can iterate over the generator without a huge memory footprint:
print("\nIterating over a large generator (simulating processing):")
count = 0
for _ in gen_data: # This loop processes elements one by one
    count += 1
    if count % 100_000 == 0:
        print(f"Processed {count} elements...")
print(f"Finished processing {count} elements.")


# --- 5. When to Use Generators ---
print("\n--- 5. When to Use Generators ---")
print("1. **Large Datasets:** When working with huge amounts of data that don't fit into memory (e.g., processing large files line by line).")
print("2. **Infinite Sequences:** When you need a sequence that theoretically never ends (e.g., Fibonacci sequence).")
print("3. **One-Time Iteration:** When you only need to iterate over the data once.")
print("4. **Performance:** For simple transformations or filters, they can be slightly faster due to less overhead than building a full list.")
print("5. **Readability:** Generator functions can be more readable than custom iterator classes (`__iter__` and `__next__`).")

# Example: Processing a large file (simulated)
def read_large_file(filepath):
    print(f"Opening file: {filepath}")
    # In real life: with open(filepath, 'r') as f:
    for i in range(100): # Simulate reading 100 lines
        yield f"Line {i+1} from {filepath}"
    print(f"Finished reading file: {filepath}")

lines_from_file = read_large_file("my_large_data.txt")
print("\nProcessing lines from simulated file:")
for line in lines_from_file:
    print(f"Processing: {line}")
    if "Line 5" in line: # Stop early if condition met
        break
# Notice "Finished reading file" is printed only after loop finishes or breaks,
# demonstrating lazy evaluation and state preservation.


# --- 6. Generator Methods: `send()`, `throw()`, `close()` ---
print("\n--- 6. Generator Methods: `send()`, `throw()`, `close()` ---")
print("Generators are not just one-way data producers. They can interact with their caller.")

# Example: Coroutine (generator that can receive values)
def echo_generator():
    print("Generator started. Waiting for first value...")
    while True:
        received = yield # This yield both sends None and receives a value
        if received is None:
            print("Received None, exiting.")
            break
        print(f"Generator received: {received}")
        yield f"Echo: {received}" # Yield back a modified value

echoer = echo_generator()
next(echoer) # "Prime" the generator (run until the first yield)

print("\nSending values to the generator:")
print(f"Received from generator: {echoer.send('Hello')}")
print(f"Received from generator: {echoer.send('World')}")

try:
    echoer.throw(ValueError("Something went wrong!")) # Inject an exception
except ValueError as e:
    print(f"Caught exception from generator: {e}")

try:
    echoer.close() # Close the generator (forces it to exit)
    next(echoer)
except StopIteration:
    print("Generator was closed and is now exhausted.")

print("\n--- End of Python Generators Practice Code ---")