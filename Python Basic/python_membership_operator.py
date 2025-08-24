print("--- Python Membership Operators ---")
print("-----------------------------------\n")

# Membership operators are used to test if a sequence (string, list, tuple, set, dictionary)
# contains a specific value.

# 1. `in` Operator
print("1. `in` Operator:")
# Returns True if the specified value is found in the sequence.
# Returns False otherwise.

# --- Examples with Strings ---
my_string = "Hello, Python!"
print(f"String: '{my_string}'")
print(f"'H' in my_string: {'H' in my_string}")       # True (single character)
print(f"'Py' in my_string: {'Py' in my_string}")      # True (substring)
print(f"'py' in my_string: {'py' in my_string}")      # False (case-sensitive)
print(f"'xyz' in my_string: {'xyz' in my_string}\n")   # False


# --- Examples with Lists ---
my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")
print(f"30 in my_list: {30 in my_list}")         # True
print(f"15 in my_list: {15 in my_list}")         # False
print(f"[10, 20] in my_list: {[10, 20] in my_list}") # False (checks for the sublist itself, not elements)
print(f"10 in [10, 20]: {10 in [10, 20]}\n") # True


# --- Examples with Tuples ---
my_tuple = ('apple', 'banana', 'cherry')
print(f"Tuple: {my_tuple}")
print(f"'banana' in my_tuple: {'banana' in my_tuple}") # True
print(f"'grape' in my_tuple: {'grape' in my_tuple}\n")   # False


# --- Examples with Sets ---
my_set = {'red', 'green', 'blue'}
print(f"Set: {my_set}")
print(f"'green' in my_set: {'green' in my_set}")   # True
print(f"'yellow' in my_set: {'yellow' in my_set}\n") # False


# --- Examples with Dictionaries ---
# For dictionaries, `in` checks for the presence of a KEY.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Dictionary: {my_dict}")
print(f"'name' in my_dict: {'name' in my_dict}")     # True (key exists)
print(f"'age' in my_dict: {'age' in my_dict}")       # True
print(f"'country' in my_dict: {'country' in my_dict}") # False
print(f"30 in my_dict: {30 in my_dict}")           # False (30 is a value, not a key)
print(f"'Alice' in my_dict.values(): {'Alice' in my_dict.values()}") # True (to check values)
print(f"('age', 30) in my_dict.items(): {('age', 30) in my_dict.items()}\n") # True (to check key-value pairs)


# 2. `not in` Operator
print("2. `not in` Operator:")
# Returns True if the specified value is NOT found in the sequence.
# Returns False otherwise.

# --- Examples with Strings ---
print(f"'X' not in my_string: {'X' not in my_string}")     # True
print(f"'Python' not in my_string: {'Python' not in my_string}\n") # False


# --- Examples with Lists ---
print(f"100 not in my_list: {100 not in my_list}")     # True
print(f"20 not in my_list: {20 not in my_list}\n")     # False


# --- Examples with Dictionaries ---
print(f"'zip_code' not in my_dict: {'zip_code' not in my_dict}") # True
print(f"'city' not in my_dict: {'city' not in my_dict}\n")     # False


# --- Practical Use Cases ---
print("--- Practical Use Cases ---\n")

# Use Case 1: Conditional Logic / Flow Control
username = "admin"
allowed_users = ["admin", "moderator", "editor"]

if username in allowed_users:
    print(f"Access granted for user: {username}\n")
else:
    print(f"Access denied for user: {username}\n")

email_input = "test@example.com"
if "@" in email_input and "." in email_input:
    print("Looks like a valid email address format.\n")
else:
    print("Invalid email format.\n")


# Use Case 2: Data Validation
valid_choices = ['yes', 'no', 'maybe']
user_choice = input("Enter your choice (yes/no/maybe): ").lower() # Convert to lowercase for case-insensitivity

if user_choice not in valid_choices:
    print(f"'{user_choice}' is not a valid choice. Please choose from {valid_choices}.\n")
else:
    print(f"You chose: '{user_choice}'.\n")


# Use Case 3: Searching and Counting (though `count()` is often better)
sentence = "the quick brown fox jumps over the lazy dog"
word_to_find = "fox"
if word_to_find in sentence:
    print(f"'{word_to_find}' found in sentence.")
    # For number of occurrences, string.count() is usually better:
    print(f"'{word_to_find}' appears {sentence.count(word_to_find)} time(s).\n")
else:
    print(f"'{word_to_find}' not found in sentence.\n")


# Use Case 4: Filtering lists (though list comprehensions are often more efficient)
all_items = ['apple', 'banana', 'orange', 'grape', 'kiwi']
fruits_to_exclude = ['orange', 'kiwi']

filtered_fruits = [fruit for fruit in all_items if fruit not in fruits_to_exclude]
print(f"All items: {all_items}")
print(f"Fruits to exclude: {fruits_to_exclude}")
print(f"Filtered fruits: {filtered_fruits}\n")


print("--- End of Python Membership Operators Demonstration ---")