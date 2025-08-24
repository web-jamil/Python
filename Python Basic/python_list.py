import random

print("--- Python Lists: Practice Code ---")

# --- 1. Creating Lists ---
print("\n--- 1. Creating Lists ---")

# 1.1 Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# 1.2 List of integers
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

# 1.3 List of strings
fruits = ["apple", "banana", "cherry", "date"]
print(f"List of fruits: {fruits}")

# 1.4 Mixed data types (generally discouraged for clarity, but possible)
mixed_list = [1, "hello", True, 3.14]
print(f"Mixed list: {mixed_list}")

# 1.5 List from an iterable (e.g., string, tuple, range)
list_from_string = list("python")
print(f"List from string: {list_from_string}")

list_from_tuple = list((10, 20, 30))
print(f"List from tuple: {list_from_tuple}")

list_from_range = list(range(5)) # Generates [0, 1, 2, 3, 4]
print(f"List from range: {list_from_range}")

# 1.6 Nested lists (lists of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested list (matrix): {matrix}")



# --- 2. Accessing Elements ---
print("\n--- 2. Accessing Elements ---")

my_list = ['a', 'b', 'c', 'd', 'e']

# 2.1 By index (0-based)
print(f"First element: {my_list[0]}")
print(f"Third element: {my_list[2]}")

# 2.2 Negative indexing (from the end)
print(f"Last element: {my_list[-1]}")
print(f"Second to last element: {my_list[-2]}")

# 2.3 Accessing elements in nested lists
nested_example = [[10, 11], [20, 21]]
print(f"Element from nested list: {nested_example[1][0]}") # Accesses 20



# --- 3. Slicing Lists ---
print("\n--- 3. Slicing Lists ---")
# Syntax: list[start:end:step]
# 'end' index is exclusive. 'step' is optional, default is 1.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 3.1 Slice from start to index (exclusive)
print(f"Elements from index 0 to 3 (exclusive): {alphabet[0:4]}")
print(f"Same as above (default start is 0): {alphabet[:4]}")

# 3.2 Slice from index to end
print(f"Elements from index 3 to end: {alphabet[3:]}")

# 3.3 Slice the entire list (creates a copy)
print(f"Copy of the list: {alphabet[:]}")

# 3.4 Slice with step
print(f"Every second element: {alphabet[::2]}")
print(f"Elements from index 1 to 6, every third: {alphabet[1:7:3]}")

# 3.5 Reverse a list using slicing
print(f"Reversed list: {alphabet[::-1]}")



# --- 4. Modifying Lists ---
print("\n--- 4. Modifying Lists ---")

shopping_list = ["milk", "bread", "eggs"]
print(f"Original shopping list: {shopping_list}")

# 4.1 Changing an element
shopping_list[1] = "butter"
print(f"After changing an element: {shopping_list}")

# 4.2 Adding elements: .append() (adds to the end)
shopping_list.append("cheese")
print(f"After appending 'cheese': {shopping_list}")

# 4.3 Adding elements: .insert() (adds at a specific index)
shopping_list.insert(0, "yogurt") # Insert at beginning
print(f"After inserting 'yogurt' at index 0: {shopping_list}")

# 4.4 Extending a list: .extend() (adds elements from another iterable)
more_items = ["juice", "cereal"]
shopping_list.extend(more_items)
print(f"After extending with more_items: {shopping_list}")

# 4.5 Removing elements: .remove() (removes first occurrence of value)
shopping_list.remove("eggs") # Oops, butter replaced eggs! Let's remove butter.
shopping_list.remove("butter")
print(f"After removing 'butter': {shopping_list}")

# 4.6 Removing elements: .pop() (removes and returns element by index, or last if no index)
popped_item = shopping_list.pop() # Removes last item
print(f"After popping last item ({popped_item}): {shopping_list}")
popped_item_at_index = shopping_list.pop(0) # Removes item at index 0
print(f"After popping item at index 0 ({popped_item_at_index}): {shopping_list}")

# 4.7 Removing elements: del keyword (removes by index or slice)
del shopping_list[1] # Delete element at index 1
print(f"After deleting element at index 1: {shopping_list}")
del shopping_list[0:2] # Delete slice
print(f"After deleting slice [0:2]: {shopping_list}")

# 4.8 Clearing all elements: .clear()
shopping_list.clear()
print(f"After clearing the list: {shopping_list}")



# --- 5. List Operations and Methods ---
print("\n--- 5. List Operations and Methods ---")

list1 = [10, 20, 30]
list2 = [40, 50]

# 5.1 Concatenation using + operator (creates new list)
combined_list = list1 + list2
print(f"Combined list using +: {combined_list}")

# 5.2 Repetition using * operator
repeated_list = ['x'] * 3
print(f"Repeated list using *: {repeated_list}")

# 5.3 Length of a list: len()
print(f"Length of combined_list: {len(combined_list)}")

# 5.4 Check if element exists: 'in' operator
print(f"Is 'banana' in fruits list? {'banana' in fruits}")
print(f"Is 20 in combined_list? {20 in combined_list}")

# 5.5 Finding an element's index: .index()
# Note: Raises ValueError if item is not found
print(f"Index of 30 in combined_list: {combined_list.index(30)}")

# 5.6 Counting elements: .count()
my_data = [1, 2, 2, 3, 2, 4]
print(f"Count of 2 in my_data: {my_data.count(2)}")

# 5.7 Sorting lists: .sort() (in-place)
unsorted_numbers = [5, 2, 8, 1, 9]
unsorted_numbers.sort()
print(f"Sorted numbers (in-place): {unsorted_numbers}")

# 5.8 Sorting lists: sorted() function (returns new list)
unsorted_fruits = ["cherry", "apple", "banana"]
sorted_fruits = sorted(unsorted_fruits)
print(f"Original fruits: {unsorted_fruits}, Sorted fruits (new list): {sorted_fruits}")

# 5.9 Reverse list order: .reverse() (in-place)
my_order = ['first', 'second', 'third']
my_order.reverse()
print(f"Reversed order (in-place): {my_order}")

# 5.10 Min, Max, Sum of numeric lists
num_list = [10, 5, 25, 12, 8]
print(f"Min of num_list: {min(num_list)}")
print(f"Max of num_list: {max(num_list)}")
print(f"Sum of num_list: {sum(num_list)}")


# --- 6. Iterating Through Lists ---
print("\n--- 6. Iterating Through Lists ---")

colors = ["red", "green", "blue"]

# 6.1 Basic for loop
print("Basic for loop:")
for color in colors:
    print(color)

# 6.2 Iterating with index using enumerate()
print("\nIterating with index using enumerate():")
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# 6.3 Iterating using range(len()) (less Pythonic, but useful sometimes)
print("\nIterating using range(len()):")
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")



# --- 7. List Comprehensions (Concise List Creation) ---
print("\n--- 7. List Comprehensions ---")
# Syntax: [expression for item in iterable if condition]

# 7.1 Basic transformation: Squaring numbers
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

# 7.2 Filtering elements: Even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers up to 9: {even_numbers}")

# 7.3 Transformation and filtering
filtered_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print(f"Uppercase fruits with length > 5: {filtered_fruits}")

# 7.4 Nested list comprehension (e.g., flattening a matrix)
matrix_flat = [num for row in matrix for num in row]
print(f"Flattened matrix: {matrix_flat}")



# --- 8. Common List Use Cases / Patterns ---
print("\n--- 8. Common List Use Cases / Patterns ---")

# 8.1 Copying a list (important to avoid side effects)
original = [1, 2, 3]
copy_slice = original[:] # Recommended way to create a shallow copy
copy_list_constructor = list(original) # Another way
copy_method = original.copy() # Python 3.3+

original[0] = 99
print(f"Original list after modification: {original}")
print(f"Copy created by slice: {copy_slice} (remains unchanged)")
print(f"Copy created by list(): {copy_list_constructor} (remains unchanged)")
print(f"Copy created by .copy(): {copy_method} (remains unchanged)")

# 8.2 Checking if a list is empty
my_data_list = []
if not my_data_list: # Pythonic way
    print("\nmy_data_list is empty.")

# 8.3 Joining list of strings into a single string
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(f"Joined words: {sentence}")

# 8.4 Removing duplicates (maintaining order)
unique_elements = list(dict.fromkeys([1, 2, 2, 3, 1, 4]))
print(f"List with duplicates removed (order preserved): {unique_elements}")

# 8.5 Zipping two lists (pairing elements)
names = ["Alice", "Bob", "Charlie"]
ages = [30, 24, 35]
name_age_pairs = list(zip(names, ages))
print(f"Zipped name-age pairs: {name_age_pairs}")

# 8.6 Generating random items from a list
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
print(f"Random choice from list: {computer_choice}")