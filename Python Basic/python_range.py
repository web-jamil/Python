print("--- Python range() Function: Practice Code ---")

# --- 1. What is range()? ---
print("\n--- 1. What is range()? ---")
print("The `range()` function generates an immutable sequence of numbers.")
print("It's commonly used in `for` loops to iterate a specific number of times.")
print("It's memory-efficient because it generates numbers on the fly (it's an iterator),")
print("rather than creating a list of all numbers in memory at once.")

my_range_object = range(5)
print(f"A range object: {my_range_object}")
print(f"Type of range object: {type(my_range_object)}")

# To see the numbers, you usually convert it to a list (for demonstration)
print(f"Numbers in range(5): {list(my_range_object)}")


# --- 2. Forms of range() ---
print("\n--- 2. Forms of range() ---")

# 2.1 range(stop) - Generates numbers from 0 up to (but not including) 'stop'.
print("\n2.1 range(stop):")
# Example: Iterate 5 times (0, 1, 2, 3, 4)
for i in range(5):
    print(f"Iteration: {i}")

print(f"List from range(3): {list(range(3))}") # [0, 1, 2]

# 2.2 range(start, stop) - Generates numbers from 'start' up to (but not including) 'stop'.
print("\n2.2 range(start, stop):")
# Example: Numbers from 2 to 6 (2, 3, 4, 5, 6 is NOT included)
for i in range(2, 7):
    print(f"Number: {i}")

print(f"List from range(10, 15): {list(range(10, 15))}") # [10, 11, 12, 13, 14]

# 2.3 range(start, stop, step) - Generates numbers from 'start' up to (but not including) 'stop',
# incrementing by 'step' each time.
print("\n2.3 range(start, stop, step):")
# Example: Even numbers from 0 to 9
for i in range(0, 10, 2):
    print(f"Even number: {i}")

print(f"List from range(1, 10, 3): {list(range(1, 10, 3))}") # [1, 4, 7]

# 2.4 Using a negative step (for countdown or reverse iteration)
print("\n2.4 Using a negative step:")
# Example: Countdown from 5 to 1
for i in range(5, 0, -1):
    print(f"Countdown: {i}")

print(f"List from range(10, 0, -2): {list(range(10, 0, -2))}") # [10, 8, 6, 4, 2]

# Important: For negative steps, 'start' must be greater than 'stop' for numbers to be generated.
print(f"List from range(0, 5, -1): {list(range(0, 5, -1))}") # [] (empty list)


# --- 3. Characteristics of range() ---
print("\n--- 3. Characteristics of range() ---")

# 3.1 Immutability
# Once a range object is created, you cannot change its start, stop, or step.
my_fixed_range = range(1, 5)
print(f"Original range: {my_fixed_range}")
# my_fixed_range.start = 0 # This would raise an AttributeError

# 3.2 Efficiency (Lazy Evaluation)
# It doesn't create a list in memory for large ranges.
# This is why `range(1_000_000_000)` doesn't crash your system.
print(f"Size of range(10**9): {my_range_object.__sizeof__()} bytes (very small)")
# compared to
# a_large_list = list(range(10**6)) # This would take significant memory
# print(f"Size of list(range(10**6)): {a_large_list.__sizeof__()} bytes (much larger)")

# 3.3 Membership Testing (Efficient)
# You can check if a number is in a range directly, without converting to list.
my_range = range(10, 20)
print(f"Is 15 in range(10, 20)? {15 in my_range}") # True
print(f"Is 20 in range(10, 20)? {20 in my_range}") # False (stop is exclusive)


# --- 4. Common Use Cases for range() ---
print("\n--- 4. Common Use Cases for range() ---")

# 4.1 Looping a fixed number of times
print("\n4.1 Loop fixed times:")
for _ in range(3): # Using '_' when index isn't needed
    print("Performing an action...")

# 4.2 Iterating with an index for lists/strings
print("\n4.2 Iterating with index:")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Fruit at index {i}: {fruits[i]}")

# Note: `enumerate()` is often more Pythonic for index + value
print("\nUsing enumerate() (often preferred):")
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index}: {fruit}")

# 4.3 Creating sequences for other purposes
print("\n4.3 Creating sequences:")
my_numbers = list(range(1, 11)) # Numbers 1 to 10
print(f"Numbers 1-10: {my_numbers}")

# Generating indices for accessing elements in reverse
for i in range(len(fruits) - 1, -1, -1):
    print(f"Fruit in reverse (index {i}): {fruits[i]}")


# --- 5. Important Notes and Cautions ---
print("\n--- 5. Important Notes and Cautions ---")

# 5.1 'stop' is always exclusive
# The sequence stops BEFORE the 'stop' value.
print(f"range(5) does NOT include 5: {list(range(5))}") # [0, 1, 2, 3, 4]

# 5.2 'step' cannot be zero
# try:
#     list(range(1, 5, 0))
# except ValueError as e:
#     print(f"\nCaught ValueError: {e} - step cannot be zero.")

# 5.3 Order of start/stop/step matters
# If step is positive, start must be less than stop for numbers to be generated.
print(f"range(5, 0, 1) (positive step, start > stop): {list(range(5, 0, 1))}") # []
# If step is negative, start must be greater than stop.
print(f"range(0, 5, -1) (negative step, start < stop): {list(range(0, 5, -1))}") # []


print("\n--- End of Python range() Function Practice Code ---")