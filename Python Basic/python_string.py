print("--- Python Strings: Practice Code ---")

# --- 1. Creating Strings ---
print("\n--- 1. Creating Strings ---")

# 1.1 Single quotes
str_single = 'Hello, Python!'
print(f"Single quotes: {str_single}")

# 1.2 Double quotes
str_double = "Hello, World!"
print(f"Double quotes: {str_double}")

# 1.3 Triple quotes (for multi-line strings or docstrings)
str_multi_line = """This is a string
that spans multiple
lines."""
print(f"Triple quotes (multi-line):\n{str_multi_line}")

# 1.4 Raw strings (prefix with 'r' or 'R')
# Ignores escape sequences like \n, \t
path_windows = r"C:\Users\Name\Documents\file.txt"
print(f"Raw string (Windows path): {path_windows}")
print(f"Normal string with backslash n: {'C:\\new\\folder'}") # \n would be newline

# 1.5 Strings using str() constructor
num_str = str(123)
print(f"String from number using str(): {num_str} (Type: {type(num_str)})")


# --- 2. String Immutability ---
print("\n--- 2. String Immutability ---")
# Strings are immutable. Once created, their content cannot be changed.
# Any operation that seems to "modify" a string actually creates a *new* string.

original_str = "Python"
print(f"Original string: {original_str}")
# original_str[0] = 'J' # This would raise a TypeError

modified_str = original_str.replace('P', 'J') # This creates a NEW string
print(f"Original after .replace(): {original_str} (unchanged)")
print(f"New string created by .replace(): {modified_str}")


# --- 3. Accessing Characters (Indexing) ---
print("\n--- 3. Accessing Characters (Indexing) ---")

my_string = "Developer"

# 3.1 Positive indexing (0-based)
print(f"First character: {my_string[0]}")     # D
print(f"Third character: {my_string[2]}")     # v

# 3.2 Negative indexing (from the end)
print(f"Last character: {my_string[-1]}")    # r
print(f"Second to last character: {my_string[-2]}") # e


# --- 4. Slicing Strings ---
print("\n--- 4. Slicing Strings ---")
# Syntax: string[start:end:step]
# 'end' index is exclusive. 'step' is optional, default is 1.

sentence = "The quick brown fox jumps over the lazy dog."

# 4.1 Slice from start to end (exclusive)
print(f"First 3 characters: {sentence[0:3]}")
print(f"Same as above (default start is 0): {sentence[:3]}")

# 4.2 Slice from index to end
print(f"Characters from index 4 to end: {sentence[4:]}")

# 4.3 Slice with step
print(f"Every second character: {sentence[::2]}")
print(f"Characters from index 4 to 10, every third: {sentence[4:11:3]}")

# 4.4 Reverse a string using slicing
print(f"Reversed string: {sentence[::-1]}")


# --- 5. String Concatenation and Repetition ---
print("\n--- 5. String Concatenation and Repetition ---")

# 5.1 Concatenation using + operator
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(f"Concatenation: {message}")

# 5.2 Repetition using * operator
stars = "*" * 10
print(f"Repetition: {stars}")

# 5.3 Joining a list of strings (efficient for many concatenations)
words = ["Python", "is", "awesome!"]
joined_string = " ".join(words)
print(f"Joined string: {joined_string}")
comma_separated = ", ".join(["apple", "banana", "cherry"])
print(f"Comma-separated: {comma_separated}")


# --- 6. String Methods (Commonly Used) ---
print("\n--- 6. String Methods ---")

sample_text = "   Hello World! PyThon is fun.   "
print(f"Original sample_text: '{sample_text}'")

# 6.1 Changing Case
print(f".upper(): '{sample_text.upper()}'")
print(f".lower(): '{sample_text.lower()}'")
print(f".capitalize(): '{sample_text.capitalize()}'") # First char uppercase, rest lowercase
print(f".title(): '{sample_text.title()}'")     # First char of each word uppercase
print(f".swapcase(): '{sample_text.swapcase()}'") # Swaps case of all characters

# 6.2 Stripping whitespace
text_with_whitespace = "   leading and trailing   "
print(f"'{text_with_whitespace}'")
print(f".strip(): '{text_with_whitespace.strip()}'")     # Removes both leading/trailing
print(f".lstrip(): '{text_with_whitespace.lstrip()}'")   # Removes leading only
print(f".rstrip(): '{text_with_whitespace.rstrip()}'")   # Removes trailing only
# Can also strip specific characters:
print(f"'###Hello###'.strip('#'): '{'###Hello###'.strip('#')}'")

# 6.3 Splitting and Partitioning
data_string = "name:Alice,age:30,city:London"
parts = data_string.split(',')
print(f".split(','): {parts}")
print(f"'Hello World'.split(): {'Hello World'.split()} (splits by whitespace by default)")
print(f"'apple,banana,cherry'.split(',', 1): {'apple,banana,cherry'.split(',', 1)} (maxsplit argument)")

sentence_partition = "Python is a powerful language."
before, sep, after = sentence_partition.partition('powerful')
print(f".partition('powerful'): Before='{before}', Separator='{sep}', After='{after}'")

# 6.4 Replacing substrings
email = "user@olddomain.com"
new_email = email.replace("olddomain", "newdomain")
print(f".replace('olddomain', 'newdomain'): {new_email}")
text_replace = "one one two one"
print(f"Replacing 'one' with 'three' (all occurrences): {text_replace.replace('one', 'three')}")
print(f"Replacing 'one' with 'three' (max 2 occurrences): {text_replace.replace('one', 'three', 2)}")

# 6.5 Checking Content / Predicate Methods (return True/False)
check_str = "Python123"
print(f"'{check_str}'.isalpha(): {check_str.isalpha()} (all alphabetic)")
print(f"'{check_str}'.isalnum(): {check_str.isalnum()} (alphanumeric)")
print(f"'{check_str}'.isdigit(): {check_str.isdigit()} (all digits)")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'WORLD'.isupper(): {'WORLD'.isupper()}")
print(f"' '.isspace(): {' '.isspace()}")
print(f"'Title Case'.istitle(): {'Title Case'.istitle()}")
print(f"'Hello World'.startswith('Hello'): {'Hello World'.startswith('Hello')}")
print(f"'Hello World'.endswith('World'): {'Hello World'.endswith('World')}")

# 6.6 Finding substrings
text_find = "The quick brown fox."
print(f".find('quick'): {text_find.find('quick')} (returns index, -1 if not found)")
print(f".index('brown'): {text_find.index('brown')} (returns index, raises ValueError if not found)")
# .count() for occurrences
print(f"'{text_find}'.count('o'): {text_find.count('o')}")


# --- 7. String Formatting ---
print("\n--- 7. String Formatting ---")

# 7.1 f-strings (Formatted String Literals - Python 3.6+) - Most Recommended
name = "Bob"
age = 25
city = "Paris"
print(f"Hello, my name is {name}, I am {age} years old and I live in {city}.")
# Expressions inside f-strings
print(f"5 + 3 = {5 + 3}")
# Formatting options
pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Number with commas: {123456789:,}")
print(f"Percentage: {0.75:.0%}") # .0% means 0 decimal places for percentage

# 7.2 .format() method (Older, but still widely used)
print("Hello, my name is {}, I am {} years old and I live in {}.".format(name, age, city))
# Positional arguments
print("My name is {0} and I'm from {2}. Hello, {0}!".format("Alice", "Engineer", "Berlin"))
# Keyword arguments
print("Product: {product_name}, Price: ${price:.2f}".format(product_name="Laptop", price=999.999))

# 7.3 %-formatting (Oldest method - generally avoided for new code)
print("Hello, my name is %s, I am %d years old." % (name, age))


# --- 8. Miscellaneous String Concepts ---
print("\n--- 8. Miscellaneous String Concepts ---")

# 8.1 Checking Length: len()
print(f"Length of '{my_string}': {len(my_string)}")

# 8.2 String comparison (lexicographical/alphabetical order)
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'Apple' < 'apple': {'Apple' < 'apple'} (Uppercase comes before lowercase)")

# 8.3 Escape Sequences
print("Newline: Line1\nLine2")
print("Tab: Item1\tItem2")
print("Quote inside: 'It\'s a beautiful day.'") # Or use double quotes around single quote
print("Backslash: C:\\Users\\Name")


print("\n--- End of Python Strings Practice Code ---")