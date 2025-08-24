import random
import time

print("--- Python Loops: Practice Code ---")

# --- 1. The 'for' Loop: Iterating Over Sequences ---
print("\n--- 1. The 'for' Loop: Iterating Over Sequences ---")

# 1.1 Iterating over a list
print("\n1.1 Iterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 1.2 Iterating over a string (characters)
print("\n1.2 Iterating over a string:")
word = "Python"
for char in word:
    print(f"Character: {char}")

# 1.3 Iterating over a tuple
print("\n1.3 Iterating over a tuple:")
colors = ("red", "green", "blue")
for color in colors:
    print(f"Color: {color}")

# 1.4 Iterating over a set (order is not guaranteed)
print("\n1.4 Iterating over a set:")
unique_numbers = {1, 5, 2, 5, 8}
for num in unique_numbers:
    print(f"Unique number: {num}")

# 1.5 Iterating over a dictionary
print("\n1.5 Iterating over a dictionary:")
student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# By default, iterates over keys
print("Iterating over keys:")
for name in student_scores:
    print(f"Student: {name}")

# Iterating over values explicitly
print("Iterating over values:")
for score in student_scores.values():
    print(f"Score: {score}")

# Iterating over key-value pairs using .items() (most common)
print("Iterating over key-value pairs:")
for name, score in student_scores.items():
    print(f"Student: {name}, Score: {score}")

# 1.6 Using range() function (for fixed number of iterations or indexing)
# range(stop) - 0 to stop-1
print("\n1.6 Using range(5):")
for i in range(5):
    print(f"Iteration {i}")

# range(start, stop) - start to stop-1
print("\nUsing range(2, 7):")
for i in range(2, 7):
    print(f"Number: {i}")

# range(start, stop, step) - start to stop-1, with a step
print("\nUsing range(0, 10, 2) (even numbers):")
for i in range(0, 10, 2):
    print(f"Even number: {i}")

print("\nUsing range(10, 0, -1) (countdown):")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# 1.7 Using enumerate() (for both index and value)
print("\n1.7 Using enumerate() with a list:")
animals = ["cat", "dog", "bird"]
for index, animal in enumerate(animals):
    print(f"Animal at index {index}: {animal}")

# 1.8 Using zip() (for iterating over multiple iterables simultaneously)
print("\n1.8 Using zip() with two lists:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# 1.9 Nested for loops (loops within loops)
print("\n1.9 Nested for loops (Multiplication Table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")

# 1.10 'for' loop with 'else' block
# The 'else' block executes if the loop completes without encountering a 'break'.
print("\n1.10 'for' loop with 'else' block:")
search_list = [10, 20, 30, 40, 50]
target = 35
for num in search_list:
    if num == target:
        print(f"Found {target}!")
        break # This 'break' will prevent the 'else' block from executing
else:
    print(f"{target} not found in the list.")

target_found = 30
for num in search_list:
    if num == target_found:
        print(f"Found {target_found}!")
        break
else:
    print(f"{target_found} not found in the list.")


# --- 2. The 'while' Loop: Repeating as long as a condition is true ---
print("\n--- 2. The 'while' Loop: Repeating as long as a condition is true ---")

# 2.1 Basic while loop (using a counter)
print("\n2.1 Basic while loop (countdown):")
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1 # Decrement the counter
print("Blast off!")

# 2.2 while loop with a changing condition
print("\n2.2 while loop with a changing condition (guess the number):")
secret_number = random.randint(1, 5)
guess = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 5: ")) # In practice, handle input errors
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print(f"Congratulations! You guessed {secret_number}!")

# 2.3 Infinite while loop (and how to exit with 'break')
print("\n2.3 Infinite while loop (type 'quit' to exit):")
while True:
    user_input = input("Enter something (or 'quit'): ")
    if user_input.lower() == 'quit':
        print("Exiting loop.")
        break # Exit the loop
    print(f"You entered: {user_input}")

# 2.4 'while' loop with 'else' block
# The 'else' block executes if the 'while' condition becomes false (without 'break').
print("\n2.4 'while' loop with 'else' block:")
counter = 3
while counter > 0:
    print(f"Processing item {counter}...")
    counter -= 1
else:
    print("All items processed successfully (loop finished naturally).")

counter_broken = 3
while counter_broken > 0:
    print(f"Processing item {counter_broken}...")
    if counter_broken == 2:
        print("Breaking loop prematurely.")
        break # This 'break' will prevent the 'else' block from executing
    counter_broken -= 1
else:
    print("This message will not be printed if loop breaks.")


# --- 3. Loop Control Statements ---
print("\n--- 3. Loop Control Statements ---")

# 3.1 'break': Terminates the loop entirely
print("\n3.1 'break' example (find first even number):")
numbers = [1, 3, 5, 6, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break # Stop the loop
    print(f"Checking {num}...")

# 3.2 'continue': Skips the rest of the current iteration and goes to the next
print("\n3.2 'continue' example (print odd numbers):")
for i in range(1, 11):
    if i % 2 == 0:
        continue # Skip even numbers
    print(f"Odd number: {i}")

# 3.3 'pass': A null operation; nothing happens when it executes.
# Useful as a placeholder when syntax requires a statement but you want to do nothing.
print("\n3.3 'pass' example (placeholder in conditional):")
for i in range(3):
    if i == 1:
        pass # Do nothing for i=1, just continue to next iteration
    else:
        print(f"Value: {i}")


# --- 4. Loop Alternatives / Advanced Concepts ---
print("\n--- 4. Loop Alternatives / Advanced Concepts ---")

# 4.1 List Comprehension (often more Pythonic for list creation/transformation)
# Instead of:
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x**2)
print(f"\nSquares using loop: {squares_loop}")

# Use list comprehension:
squares_comp = [x**2 for x in range(1, 6)]
print(f"Squares using list comprehension: {squares_comp}")

# 4.2 Generator Expressions (memory efficient for large sequences, lazy evaluation)
# (Similar syntax to list comprehension, but uses parentheses instead of square brackets)
# Not explicitly a loop, but an alternative to constructing lists for iteration
gen_exp = (x**2 for x in range(1_000_000))
# print(sum(gen_exp)) # sums squares without creating a full list in memory

# 4.3 Iterators and next() (how loops work internally)
print("\n4.3 Iterators and next():")
my_iterator = iter([10, 20, 30])
print(f"First element: {next(my_iterator)}")
print(f"Second element: {next(my_iterator)}")
# The for loop essentially calls iter() and then next() repeatedly until StopIteration

print("\n--- End of Python Loops Practice Code ---")