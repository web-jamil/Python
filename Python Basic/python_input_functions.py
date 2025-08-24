import sys

# 1. Basic Usage of input() without a Prompt
print("--- Example 1: Basic input without a prompt ---")
user_input_no_prompt = input()
print(f"You entered (no prompt): {user_input_no_prompt}")
print(f"Type of user_input_no_prompt: {type(user_input_no_prompt)}")
print("-" * 30)

# 2. Using input() with a Prompt
print("--- Example 2: Input with a prompt ---")
name = input("Please enter your name: ")
print(f"Hello, {name}!")
print(f"Type of name: {type(name)}")
print("-" * 30)

# 3. Handling Different Data Types (Type Conversion)

# Example 3: Converting input to an integer
print("--- Example 3: Converting input to an integer ---")
age_str = input("Enter your age: ")
try:
    age_int = int(age_str)
    print(f"Your age is: {age_int}")
    print(f"Type of age_int: {type(age_int)}")
    print(f"Next year you will be: {age_int + 1}")
except ValueError:
    print("Invalid input for age. Please enter a number.")
print("-" * 30)

# Example 4: Converting input to a float
print("--- Example 4: Converting input to a float ---")
price_str = input("Enter the price of an item: ")
try:
    price_float = float(price_str)
    print(f"The price is: ${price_float:.2f}")
    print(f"Type of price_float: {type(price_float)}")
    discounted_price = price_float * 0.90
    print(f"Price with 10% discount: ${discounted_price:.2f}")
except ValueError:
    print("Invalid input for price. Please enter a number.")
print("-" * 30)

# Example 5: Handling boolean-like input (requires custom logic)
print("--- Example 5: Handling boolean-like input ---")
is_student_str = input("Are you a student? (yes/no): ").lower()
is_student = False
if is_student_str == 'yes':
    is_student = True
print(f"Is student: {is_student}")
print(f"Type of is_student: {type(is_student)}")
print("-" * 30)

# 4. Multiple Inputs in One Line

# Example 6: Getting multiple inputs on one line using split()
print("--- Example 6: Multiple inputs on one line (split) ---")
name_age_str = input("Enter your name and age (e.g., John 30): ")
parts = name_age_str.split()

if len(parts) == 2:
    multi_name = parts[0]
    try:
        multi_age = int(parts[1])
        print(f"Name: {multi_name}, Age: {multi_age}")
        print(f"Type of multi_name: {type(multi_name)}, Type of multi_age: {type(multi_age)}")
    except ValueError:
        print("Invalid age entered.")
else:
    print("Invalid format. Please enter name and age separated by a space.")
print("-" * 30)

# Example 7: Getting multiple numbers and converting them using map()
print("--- Example 7: Multiple numbers using map() ---")
numbers_str = input("Enter three numbers separated by spaces (e.g., 10 20 30): ")
try:
    num1, num2, num3 = map(int, numbers_str.split())
    print(f"Numbers: {num1}, {num2}, {num3}")
    print(f"Sum: {num1 + num2 + num3}")
    print(f"Types: {type(num1)}, {type(num2)}, {type(num3)}")
except ValueError:
    print("Invalid input. Please enter three numbers separated by spaces.")
print("-" * 30)

# 5. Error Handling with input()

# Example 8: Robust error handling for integer input
print("--- Example 8: Robust error handling for integer input ---")
while True:
    try:
        user_number_str = input("Please enter a whole number: ")
        user_number_int = int(user_number_str)
        print(f"You entered: {user_number_int}")
        break
    except ValueError:
        print("That's not a valid whole number! Please try again.")
    except EOFError:
        print("\nEnd of input detected. Exiting.")
        sys.exit() # Exit the program gracefully on EOF
print("-" * 30)




# Prompt the user to enter multiple values separated by spaces
user_input = input("Enter three words/names separated by spaces: ")

# Split the input string into a list of strings
# By default, split() splits by any whitespace (spaces, tabs, newlines)
# and handles multiple spaces between words correctly.
words = user_input.split()

# You can then access individual items by index
if len(words) >= 3:
    word1 = words[0]
    word2 = words[1]
    word3 = words[2]
    print(f"Word 1: {word1}")
    print(f"Word 2: {word2}")
    print(f"Word 3: {word3}")
else:
    print("You did not enter enough words.")

print(f"All words as a list: {words}")
print("-" * 30)

# Example with a specific delimiter (e.g., comma)
user_csv_input = input("Enter three items separated by commas (e.g., apple,banana,cherry): ")
items = user_csv_input.split(',') # Split by comma
print(f"Items: {items}")
print("-" * 30)



# Prompt the user to enter multiple numbers separated by spaces
numbers_input = input("Enter three numbers separated by spaces (e.g., 10 20 30): ")

# Split the input string into a list of string numbers
string_numbers = numbers_input.split()

try:
    # Use map(int, ...) to convert each string number to an integer
    # This returns a map object, which can be converted to a list or directly unpacked.
    num1, num2, num3 = map(int, string_numbers)

    print(f"Number 1: {num1}, Type: {type(num1)}")
    print(f"Number 2: {num2}, Type: {type(num2)}")
    print(f"Number 3: {num3}, Type: {type(num3)}")
    print(f"Sum of numbers: {num1 + num2 + num3}")

except ValueError:
    print("Invalid input. Please ensure you enter three valid numbers separated by spaces.")
except TypeError:
    print("Incorrect number of values entered or invalid type conversion.")
print("-" * 30)

# Example with floats
float_input = input("Enter two decimal numbers separated by spaces (e.g., 3.14 2.71): ")
try:
    f1, f2 = map(float, float_input.split())
    print(f"Float 1: {f1}, Type: {type(f1)}")
    print(f"Float 2: {f2}, Type: {type(f2)}")
    print(f"Product: {f1 * f2}")
except ValueError:
    print("Invalid input. Please enter two valid decimal numbers.")
print("-" * 30)


# User can enter any number of colors
colors_input = input("Enter some colors separated by spaces: ")
colors = colors_input.split()

print("You entered the following colors:")
for color in colors:
    print(f"- {color}")

print(f"Total colors entered: {len(colors)}")
print("-" * 30)


# [type(item) for item in input("Your prompt: ").split()]


# Prompt the user to enter numbers separated by spaces
# Example input: 10 20 30 40
numbers = [int(x) for x in input("Enter multiple integers separated by spaces: ").split()]

print(f"You entered: {numbers}")
print(f"Type of list: {type(numbers)}")
if numbers: # Check if the list is not empty
    print(f"Type of first element: {type(numbers[0])}")
print("-" * 30)

# You can then use the numbers
if len(numbers) >= 2:
    print(f"Sum of first two: {numbers[0] + numbers[1]}")
print("-" * 30)


# Prompt the user to enter decimal numbers separated by spaces
# Example input: 3.14 2.71 1.618
decimals = [float(x) for x in input("Enter multiple decimal numbers separated by spaces: ").split()]

print(f"You entered: {decimals}")
print(f"Type of list: {type(decimals)}")
if decimals:
    print(f"Type of first element: {type(decimals[0])}")
print("-" * 30)


# Prompt the user to enter words/names separated by spaces
# Example input: Alice Bob Charlie David
names = [word for word in input("Enter multiple names separated by spaces: ").split()]

print(f"You entered: {names}")
print(f"Type of list: {type(names)}")
if names:
    print(f"Type of first element: {type(names[0])}")
print("-" * 30)


# Prompt the user to enter values separated by commas
# Example input: apple,banana,cherry
fruits = [item.strip() for item in input("Enter fruits separated by commas: ").split(',')]

print(f"You entered: {fruits}")
print(f"Type of list: {type(fruits)}")
if fruits:
    print(f"Type of first element: {type(fruits[0])}")
print("-" * 30)

# Note: .strip() is added to remove any leading/trailing whitespace
# that might occur if the user types "apple, banana , cherry"

import sys

# Example with error handling (will still stop if one invalid value is given)
print("--- Error Handling (will stop on first invalid) ---")
try:
    user_numbers = [int(x) for x in input("Enter integers (comma-separated, e.g., 1,2,abc,4): ").split(',')]
    print(f"Processed numbers: {user_numbers}")
except ValueError:
    print("Error: One of the inputs could not be converted to an integer. Please try again with only numbers.")
except EOFError:
    print("\nEnd of input detected. Exiting.")
    sys.exit()
print("-" * 30)

# If you want to skip invalid entries (less common for direct input, but possible)
print("--- Filtering out invalid entries (advanced) ---")
input_str = input("Enter mixed values (e.g., 10,abc,20,xyz): ")
valid_numbers = []
for item_str in input_str.split(','):
    try:
        valid_numbers.append(int(item_str.strip()))
    except ValueError:
        # Skip this item if it cannot be converted
        pass
print(f"Valid numbers extracted: {valid_numbers}")
print("-" * 30)