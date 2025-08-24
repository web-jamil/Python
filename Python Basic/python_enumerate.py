print("--- Python enumerate() Function: Practice Code ---")

# --- 1. What is enumerate()? ---
print("\n--- 1. What is enumerate()? ---")
print("The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object.")
print("It provides a way to iterate over both the elements of a sequence AND their index at the same time.")
print("This is incredibly useful when you need to know the position of an item during iteration.")

# Example of an enumerate object (it's an iterator)
my_list = ['apple', 'banana', 'cherry']
enum_object = enumerate(my_list)
print(f"An enumerate object: {enum_object}")
print(f"Type of enumerate object: {type(enum_object)}")

# To see the items, you typically iterate over it or convert to a list of tuples
print(f"Items from enumerate: {list(enum_object)}")


# --- 2. Basic Usage: Iterating with Index and Value ---
print("\n--- 2. Basic Usage: Iterating with Index and Value ---")

# 2.1 Iterating over a list
print("\n2.1 Iterating over a list:")
fruits = ["apple", "banana", "cherry", "date"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# 2.2 Iterating over a tuple
print("\n2.2 Iterating over a tuple:")
colors = ("red", "green", "blue")
for i, color in enumerate(colors):
    print(f"Position {i}: {color}")

# 2.3 Iterating over a string (characters)
print("\n2.3 Iterating over a string:")
word = "Python"
for idx, char in enumerate(word):
    print(f"Char '{char}' is at index {idx}")

# 2.4 Iterating over a set (index is arbitrary due to set's unordered nature)
print("\n2.4 Iterating over a set:")
unique_numbers = {10, 20, 30}
for i, num in enumerate(unique_numbers):
    print(f"Arbitrary Index {i}: {num}")


# --- 3. The 'start' Parameter ---
print("\n--- 3. The 'start' Parameter ---")
print("By default, `enumerate()` starts counting from 0.")
print("You can change the starting index using the `start` argument.")

# Example: Start counting from 1
print("\nCounting from 1:")
for rank, student in enumerate(["Alice", "Bob", "Charlie"], start=1):
    print(f"Rank {rank}: {student}")

# Example: Start counting from 100
print("\nCounting from 100:")
items = ["Pen", "Pencil", "Eraser"]
for item_id, item_name in enumerate(items, start=100):
    print(f"Item ID: {item_id}, Name: {item_name}")


# --- 4. Why `enumerate()` over `range(len())`? ---
print("\n--- 4. Why enumerate() over range(len())? ---")
print("Consider the alternative for getting index and value:")

# Using range(len()) - Less Pythonic, potentially less efficient, and can lead to IndexError
print("\nUsing range(len()) (Less Pythonic):")
data = ['A', 'B', 'C']
for i in range(len(data)):
    print(f"Index: {i}, Value: {data[i]}")

# Advantages of enumerate():
# 4.1 Readability: It clearly expresses intent (you want index and value).
# 4.2 Efficiency: It avoids an extra lookup (data[i]) in each iteration.
# 4.3 Safety: It avoids potential IndexError if `data` is modified *during* iteration
#            (though modifying a list while iterating over it directly is generally discouraged).
print("\nAdvantages of enumerate(): More readable, often more efficient, safer.")


# --- 5. Unpacking the Tuples ---
print("\n--- 5. Unpacking the Tuples ---")
print("`enumerate()` yields tuples of (index, value).")
print("You can access these directly or unpack them into separate variables.")

my_items_tuple = ('alpha', 'beta', 'gamma')
for item_tuple in enumerate(my_items_tuple):
    print(f"Raw tuple from enumerate: {item_tuple}")
    # Accessing elements of the tuple
    print(f"Index: {item_tuple[0]}, Value: {item_tuple[1]}")

# This is why tuple unpacking in the for loop is so common and convenient:
# for index, value in enumerate(iterable):


# --- 6. Common Use Cases for enumerate() ---
print("\n--- 6. Common Use Cases for enumerate() ---")

# 6.1 Conditional logic based on index
print("\n6.1 Conditional logic based on index:")
numbers = [10, 25, 30, 45, 50]
for i, num in enumerate(numbers):
    if i % 2 == 0: # Check if index is even
        print(f"Even index {i}: {num}")
    else:
        print(f"Odd index {i}: {num}")

# 6.2 Creating a dictionary where values are items and keys are indices
print("\n6.2 Creating a dictionary (index as key):")
names = ["Emma", "Liam", "Olivia"]
name_dict = {i: name for i, name in enumerate(names)}
print(f"Dictionary from names: {name_dict}")

# 6.3 Tracking progress or line numbers
print("\n6.3 Tracking progress / Line numbers:")
code_lines = [
    "import os",
    "print('Hello')",
    "x = 10",
    "y = x + 5"
]
print("Code Snippet:")
for line_num, line_content in enumerate(code_lines, start=1):
    print(f"{line_num:2d}: {line_content}") # f-string formatting for alignment

# 6.4 Modifying a list in place (when necessary, be careful!)
# It's generally safer to create a new list or use list comprehensions,
# but sometimes modifying in place by index is required.
print("\n6.4 Modifying a list in place (use with caution):")
scores = [85, 90, 78, 92]
print(f"Original scores: {scores}")
for i, score in enumerate(scores):
    if score < 80:
        scores[i] += 5 # Add 5 points to scores below 80
print(f"Adjusted scores: {scores}")


print("\n--- End of Python enumerate() Function Practice Code ---")


print("--- Python's Built-in enumerate() Function ---")
print("-------------------------------------------\n")

# 1. Basic Usage: Iterating with Index
print("1. Basic Usage: Iterating with Index")
my_list = ['apple', 'banana', 'cherry', 'date']

print("Iterating through a list:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

print("\nIterating through a string:")
my_string = "Python"
for i, char in enumerate(my_string):
    print(f"Position: {i}, Character: {char}")

print("\nIterating through a tuple:")
my_tuple = ('red', 'green', 'blue')
for idx, color in enumerate(my_tuple):
    print(f"Number: {idx}, Color: {color}\n")

# 2. Starting Index from a Different Number (start parameter)
print("2. Starting Index from a Different Number (start parameter)")
# By default, enumerate starts counting from 0.
# You can change this using the 'start' argument.
print("Starting enumeration from 1:")
for rank, item in enumerate(my_list, start=1):
    print(f"Rank: {rank}, Item: {item}")

print("\nStarting enumeration from 100:")
for code, fruit in enumerate(my_list, start=100):
    print(f"Code: {code}, Fruit: {fruit}\n")

# 3. enumerate() with Dictionaries
print("3. enumerate() with Dictionaries")
# When enumerating a dictionary directly, you get the keys.
my_dict = {'a': 10, 'b': 20, 'c': 30}

print("Iterating through dictionary keys:")
for index, key in enumerate(my_dict):
    print(f"Index: {index}, Key: {key}, Value: {my_dict[key]}")

print("\nIterating through dictionary items (key-value pairs):")
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}\n")

# 4. enumerate() with Sets (Order Not Guaranteed)
print("4. enumerate() with Sets (Order Not Guaranteed)")
# Sets are inherently unordered, so the index assignment is arbitrary
# and can change across runs or Python versions.
my_set = {'cat', 'dog', 'mouse'}
print("Iterating through a set (order might vary):")
for index, animal in enumerate(my_set):
    print(f"Index: {index}, Animal: {animal}\n")

# 5. enumerate() as an Iterator Object
print("5. enumerate() as an Iterator Object")
# enumerate() returns an iterator. You can convert it to a list of tuples
# or iterate over it lazily.
enum_object = enumerate(my_list)
print(f"Type of enumerate object: {type(enum_object)}")
print(f"First element: {next(enum_object)}")
print(f"Second element: {next(enum_object)}")

print("\nConverting to a list of tuples:")
list_of_tuples = list(enumerate(my_list))
print(f"list(enumerate(my_list)): {list_of_tuples}")

print("\nConverting to a list of tuples with custom start:")
list_of_tuples_start_1 = list(enumerate(my_list, start=1))
print(f"list(enumerate(my_list, start=1)): {list_of_tuples_start_1}\n")

# 6. Practical Use Cases
print("6. Practical Use Cases")

# a) Updating items in a list by index
print("a) Updating items in a list by index:")
numbers = [10, 20, 30, 40]
for i, num in enumerate(numbers):
    if num > 25:
        numbers[i] = num * 2 # Double numbers greater than 25
print(f"Original numbers: [10, 20, 30, 40]")
print(f"Updated numbers: {numbers}\n")

# b) Creating a dictionary from a list with indices as keys
print("b) Creating a dictionary from a list with indices as keys:")
fruits = ['apple', 'orange', 'grape']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(f"Dictionary from fruits: {fruit_dict}\n")

# c) Displaying numbered lists to users
print("c) Displaying numbered lists to users:")
tasks = ["Finish report", "Buy groceries", "Call plumber"]
print("Your To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
print("\n")

# d) Finding the index of a specific item
print("d) Finding the index of a specific item:")
search_item = "cherry"
found_index = -1
for i, item in enumerate(my_list):
    if item == search_item:
        found_index = i
        break # Found it, no need to continue
if found_index != -1:
    print(f"'{search_item}' found at index {found_index}.")
else:
    print(f"'{search_item}' not found.")

search_item_not_found = "kiwi"
found_index_not_found = -1
for i, item in enumerate(my_list):
    if item == search_item_not_found:
        found_index_not_found = i
        break
if found_index_not_found != -1:
    print(f"'{search_item_not_found}' found at index {found_index_not_found}.")
else:
    print(f"'{search_item_not_found}' not found.\n")

print("--- End of enumerate() Function Demonstration ---")