# Method 1: Multiple Inputs on Separate Lines

print("--- Method 1: Separate Lines ---")

# Taking the first input (e.g., a name)
print("Please enter your name:")
name = input() # input() reads a line from the console as a string
print(f"Name entered: {name}")

# Taking the second input (e.g., an age, which will be a string initially)
print("Please enter your age:")
age_str = input()
# It's crucial to convert input to the desired type if it's not a string
age = int(age_str) # Convert the string age to an integer
print(f"Age entered (as int): {age}")

# Taking the third input (e.g., a height, which might be a float)
print("Please enter your height in meters (e.g., 1.75):")
height_str = input()
height = float(height_str) # Convert the string height to a float
print(f"Height entered (as float): {height}")

print("\n")




# Method 2: Multiple Inputs on the Same Line (Space-Separated)

print("--- Method 2: Same Line (Space-Separated) ---")

# Example A: Taking two strings/words on the same line
print("Please enter your first name and last name (space-separated):")
# input().split() reads the line and splits it by whitespace into a list of strings
first_name, last_name = input().split()
print(f"First Name: {first_name}, Last Name: {last_name}")

# Example B: Taking multiple integers on the same line
print("Please enter three numbers (space-separated):")
# Read the line, split it into strings, then use map() to convert each string to an integer
num1, num2, num3 = map(int, input().split())
print(f"Numbers entered: {num1}, {num2}, {num3}")
print(f"Sum of numbers: {num1 + num2 + num3}")

# Example C: Taking a variable number of integers on the same line
print("Please enter a list of numbers (space-separated):")
# This creates a list of integers
numbers_list = list(map(int, input().split()))
print(f"List of numbers entered: {numbers_list}")
print(f"First number: {numbers_list[0]}")
print(f"Last number: {numbers_list[-1]}")

print("\n")


# Method 3: Multiple Inputs on the Same Line (Comma-Separated or Custom Delimiter)

print("--- Method 3: Same Line (Custom Delimiter) ---")

# Example A: Taking numbers separated by commas
print("Please enter a few comma-separated numbers (e.g., 10,20,30):")
# input().split(',') splits the string specifically by commas
comma_separated_numbers_str = input().split(',')
# Then map to int to convert them
comma_separated_numbers = [int(x.strip()) for x in comma_separated_numbers_str] # .strip() removes potential whitespace
print(f"Comma-separated numbers: {comma_separated_numbers}")

# Example B: Taking inputs with a different delimiter (e.g., semicolon)
print("Please enter two words separated by a semicolon (e.g., apple;banana):")
word1, word2 = input().split(';')
print(f"Word 1: {word1}, Word 2: {word2}")

print("\n")


# Method 4: Taking N Inputs, each on a New Line

print("--- Method 4: N Inputs on New Lines ---")

print("How many items do you want to enter?")
n = int(input()) # First, get the count of items

my_items = []
print(f"Now enter {n} items, one per line:")
for i in range(n):
    item = input()
    my_items.append(item)

print(f"You entered these items: {my_items}")

# If you know they are all integers:
print("How many numbers do you want to enter?")
m = int(input())
my_numbers = []
print(f"Now enter {m} numbers, one per line:")
for i in range(m):
    num = int(input()) # Convert to int immediately
    my_numbers.append(num)

print(f"You entered these numbers: {my_numbers}")

print("\n")


import sys

# --- Scenario 1: Taking multiple strings/words (space-separated) ---
print("\n--- Scenario 1: Multiple Strings (Space-Separated) ---")
print("Enter your first name and last name (e.g., John Doe):")
name_parts = input().split()
# The 'split()' method with no arguments splits by any whitespace.
# It returns a list of strings.
# Example input: "Alice Wonderland" -> ['Alice', 'Wonderland']

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[1]
    print(f"Hello, {first_name} {last_name}!")
else:
    print("Please enter at least two words.")


# --- Scenario 2: Taking a fixed number of integers (space-separated) ---
print("\n--- Scenario 2: Fixed Number of Integers (Space-Separated) ---")
print("Enter three numbers (e.g., 10 20 30):")
# 1. input(): Reads "10 20 30"
# 2. .split(): Splits into ['10', '20', '30']
# 3. map(int, ...): Applies int() to each string -> map object of (10, 20, 30)
# 4. Unpack: Assigns 10 to num1, 20 to num2, 30 to num3
num1, num2, num3 = map(int, input().split())
print(f"You entered: {num1}, {num2}, {num3}")
print(f"Sum: {num1 + num2 + num3}")


# --- Scenario 3: Taking a variable number of integers (space-separated) ---
print("\n--- Scenario 3: Variable Number of Integers (Space-Separated) ---")
print("Enter a list of numbers (e.g., 5 12 8 20):")
# 1. input(): Reads "5 12 8 20"
# 2. .split(): Splits into ['5', '12', '8', '20']
# 3. map(int, ...): Applies int() to each -> map object (5, 12, 8, 20)
# 4. list(...): Converts the map object into a list: [5, 12, 8, 20]
numbers_list = list(map(int, input().split()))
print(f"Your list: {numbers_list}")
print(f"First element: {numbers_list[0]}")
print(f"Length of list: {len(numbers_list)}")


# --- Scenario 4: Taking multiple floats (space-separated) ---
print("\n--- Scenario 4: Multiple Floats (Space-Separated) ---")
print("Enter two decimal numbers (e.g., 3.14 2.71):")
# Similar to integers, but use float() for conversion
float1, float2 = map(float, input().split())
print(f"You entered: {float1}, {float2}")
print(f"Product: {float1 * float2}")


# --- Scenario 5: Taking inputs with a custom delimiter (e.g., comma-separated) ---
print("\n--- Scenario 5: Custom Delimiter (e.g., Comma-Separated) ---")
print("Enter three fruits (comma-separated, e.g., apple,banana,cherry):")
# Use .split(',') to split specifically by commas
fruit1, fruit2, fruit3 = input().split(',')
print(f"Fruits: {fruit1}, {fruit2}, {fruit3}")

# Important: If there might be spaces around the delimiter (e.g., "apple, banana, cherry")
# use .strip() on each part to remove them.
print("\nEnter three colors (comma-separated, possibly with spaces, e.g., red, green ,blue ):")
colors_str_list = input().split(',')
# Using a list comprehension to apply .strip() and int()
colors = [color.strip() for color in colors_str_list]
print(f"Colors: {colors}")

print("\n--- End of Examples ---")

# --- Example for Competitive Programming Context: Reading N and then N numbers ---
# Often, in competitive programming, the first line gives you a count N,
# and the second line gives you N space-separated numbers.

# print("\n--- Competitive Programming Style Example ---")
# print("Enter the count of numbers (e.g., 5):")
# N = int(input()) # Read N from the first line

# print(f"Enter {N} numbers space-separated on the next line (e.g., 1 2 3 4 5):")
# # Read the N numbers from the second line
# numbers_cp = list(map(int, input().split()))

# # Verify that the number of inputs matches N
# if len(numbers_cp) == N:
#     print(f"Read {N} numbers: {numbers_cp}")
# else:
#     print(f"Warning: Expected {N} numbers but got {len(numbers_cp)}.")


# --- 1. Reading Multiple Strings (Space-Separated) ---
print("\n--- Scenario 1: Reading Multiple Strings (Space-Separated) ---")
print("Enter your first name and last name (e.g., John Doe):")
user_input_line = input() # Read the entire line as a single string
name_parts = user_input_line.split() # Split the string by whitespace into a list of strings

# Check if we got enough parts to unpack safely
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[1]
    print(f"Hello, {first_name} {last_name}!")
else:
    print("Error: Please enter at least two words.")


# --- 2. Reading a Fixed Number of Integers (Space-Separated) ---
print("\n--- Scenario 2: Reading a Fixed Number of Integers (Space-Separated) ---")
print("Enter three numbers (e.g., 10 20 30):")
user_input_numbers_str = input() # Reads "10 20 30" (as a string)
str_numbers_list = user_input_numbers_str.split() # Splits into ['10', '20', '30']

# Use map() to convert each string in the list to an integer
# map(int, ...) returns a map object (an iterator)
# We then unpack this iterator directly into variables num1, num2, num3
num1, num2, num3 = map(int, str_numbers_list) 

print(f"You entered: {num1}, {num2}, {num3}")
print(f"Sum of numbers: {num1 + num2 + num3}")


# --- 3. Reading a Variable Number of Integers (Space-Separated) ---
print("\n--- Scenario 3: Reading a Variable Number of Integers (Space-Separated) ---")
print("Enter a list of numbers (e.g., 5 12 8 20 3):")
user_input_list_str = input() # Reads "5 12 8 20 3"
str_list_parts = user_input_list_str.split() # Splits into ['5', '12', '8', '20', '3']

# Convert all parts to integers and store them in a list
# list(map(int, ...)) converts the map object into an actual list
numbers_list = list(map(int, str_list_parts))

print(f"Your list of numbers: {numbers_list}")
if numbers_list: # Check if the list is not empty
    print(f"First element: {numbers_list[0]}")
    print(f"Last element: {numbers_list[-1]}")
    print(f"Length of list: {len(numbers_list)}")
else:
    print("No numbers were entered.")


# --- 4. Reading Multiple Floats (Space-Separated) ---
print("\n--- Scenario 4: Reading Multiple Floats (Space-Separated) ---")
print("Enter two decimal numbers (e.g., 3.14 2.718):")
float1, float2 = map(float, input().split()) # Directly map to float and unpack

print(f"You entered: {float1}, {float2}")
print(f"Their product: {float1 * float2}")


# --- 5. Reading Inputs with a Custom Delimiter (e.g., Comma-Separated) ---
print("\n--- Scenario 5: Reading Inputs with a Custom Delimiter (e.g., Comma-Separated) ---")
print("Enter three fruits (comma-separated, e.g., apple,banana,cherry):")
# Use .split(',') to explicitly split by the comma character
fruit1, fruit2, fruit3 = input().split(',')
print(f"Fruits: {fruit1}, {fruit2}, {fruit3}")

# --- Important Detail: Handling Spaces Around Custom Delimiters ---
print("\nEnter a few numbers (comma-separated, possibly with spaces, e.g., 10, 20 , 30):")
user_input_with_spaces = input() # User might type "10, 20 , 30"
parts_with_spaces = user_input_with_spaces.split(',') # This might give ['10', ' 20 ', ' 30']

# To remove leading/trailing whitespace from each part, use .strip()
# Use a list comprehension for a concise way to do this
clean_numbers = [int(x.strip()) for x in parts_with_spaces] 

print(f"Cleaned numbers: {clean_numbers}")


# --- 6. Reading a Single Character/String Without Splitting ---
# While this topic is "multiple inputs", sometimes you just need the whole line as a string.
print("\n--- Scenario 6: Reading a single string/line (no splitting) ---")
print("Enter a sentence:")
sentence = input() # Reads the entire line as one string
print(f"Your sentence: '{sentence}'")


print("\n--- End of All Single-Line Input Examples ---")