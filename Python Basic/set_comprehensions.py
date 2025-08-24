# --- Set Comprehensions in Python (Code Examples) ---

# Set comprehensions provide a concise way to create sets
# based on existing iterables. They follow the syntax:
# {expression for item in iterable if condition}
# The 'if condition' part is optional.

# -------------------- 1. Basic Set Comprehension --------------------

# Creating a set of squares of numbers from 0 to 9
squares = {x**2 for x in range(10)}
print(f"Set of squares (0-9): {squares}")

# Creating a set of even numbers from 0 to 9
evens = {x for x in range(10) if x % 2 == 0}
print(f"Set of even numbers (0-9): {evens}")

# -------------------- 2. Transforming Elements --------------------

# Converting a list of strings to uppercase and creating a set
words = ["apple", "banana", "cherry"]
uppercase_words = {word.upper() for word in words}
print(f"Set of uppercase words: {uppercase_words}")

# Extracting the length of each word and creating a set
word_lengths = {len(word) for word in words}
print(f"Set of word lengths: {word_lengths}")

# -------------------- 3. Filtering Elements --------------------

# Creating a set of numbers greater than 5 from a list
numbers = [1, 7, 3, 9, 5, 11, 2]
greater_than_five = {num for num in numbers if num > 5}
print(f"Set of numbers greater than 5: {greater_than_five}")

# Creating a set of vowels from a string (case-insensitive)
text = "Hello World"
vowels = {'a', 'e', 'i', 'o', 'u'}
found_vowels = {char.lower() for char in text if char.lower() in vowels}
print(f"Set of vowels in '{text}': {found_vowels}")

# -------------------- 4. Using Multiple Iterables (Nested Loops - Careful!) --------------------

# Creating a set of pairs (not very common for sets, but demonstrates syntax)
# Note: The order might not be as expected due to set's unordered nature.
pairs = {(x, y) for x in range(3) for y in range(2)}
print(f"Set of pairs: {pairs}")

# More practical example: Creating a set of sums of elements from two lists
list1 = [1, 2, 3]
list2 = [4, 5]
sums = {x + y for x in list1 for y in list2}
print(f"Set of sums from list1 and list2: {sums}")

# -------------------- 5. Conditional Expressions within Comprehensions --------------------

# Creating a set where even numbers are kept as is, and odd numbers are doubled
numbers_conditional = {x if x % 2 == 0 else x * 2 for x in range(10)}
print(f"Set with conditional expression: {numbers_conditional}")

# Creating a set of 'positive' or 'negative' labels based on numbers
values = [-2, 1, -5, 3, 0]
labels = {'positive' if v > 0 else 'negative' if v < 0 else 'zero' for v in values}
print(f"Set of labels: {labels}")

# Note: Since sets only store unique elements, if multiple values in 'values' result in the same label,
# the label will only appear once in the 'labels' set.

# -------------------- 6. Working with Strings --------------------

# Creating a set of characters from a string
string = "Mississippi"
unique_chars = {char for char in string}
print(f"Set of unique characters in '{string}': {unique_chars}")

# Creating a set of character codes (ASCII/Unicode) from a string
char_codes = {ord(char) for char in string}
print(f"Set of character codes in '{string}': {char_codes}")

# -------------------- 7. Using Functions within Comprehensions --------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Creating a set of prime numbers from a range
primes = {num for num in range(20) if is_prime(num)}
print(f"Set of prime numbers (0-19): {primes}")

def categorize_number(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

# Creating a set of categories for numbers
categories = {categorize_number(i) for i in range(5)}
print(f"Set of number categories: {categories}")

# -------------------- Key Advantages of Set Comprehensions --------------------
# - **Conciseness:** They allow you to create sets in a single, readable line of code.
# - **Readability:** The intent of the code is often clearer compared to using loops for set creation.
# - **Efficiency:** Python often optimizes comprehensions, making them potentially faster than explicit loops in some cases.

# In summary, set comprehensions are a powerful and Pythonic way to construct sets based on existing iterables with transformations and filtering applied concisely.