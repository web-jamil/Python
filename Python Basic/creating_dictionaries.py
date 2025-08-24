# --- Python Dictionaries: All About Creating Them in Code ---

# Dictionaries are fundamental data structures in Python, used to store data
# in unordered (but insertion-ordered in Python 3.7+) key-value pairs.

# --- 1. Creating Empty Dictionaries ---

print("--- 1. Creating Empty Dictionaries ---")

# The simplest way to create an empty dictionary is using curly braces `{}`.
empty_dict_1 = {}
print(f"1.1 Empty dictionary using {{}}: {empty_dict_1}")
print(f"   Type of empty_dict_1: {type(empty_dict_1)}")

# You can also use the dict() constructor without any arguments.
empty_dict_2 = dict()
print(f"1.2 Empty dictionary using dict(): {empty_dict_2}")
print(f"   Type of empty_dict_2: {type(empty_dict_2)}")

# Both methods result in an identical empty dictionary.


# --- 2. Creating Dictionaries with Initial Key-Value Pairs (Literal Syntax) ---

print("\n--- 2. Creating Dictionaries with Initial Key-Value Pairs ---")

# This is the most common and readable way to define a dictionary
# when you know the key-value pairs at the time of creation.
# Syntax: {key1: value1, key2: value2, ...}

# 2.1 Basic dictionary with string keys and various values
user_profile = {
    "name": "Alice Wonderland",
    "age": 30,
    "is_active": True,
    "email": "alice@example.com"
}
print(f"2.1 User Profile: {user_profile}")

# 2.2 Dictionary with mixed key types (keys must be immutable)
# Keys can be strings, numbers, or tuples (if tuple elements are immutable).
mixed_keys_example = {
    "product_code": "XYZ789",
    101: "Item ID",
    3.14159: "Pi Value",
    (1, 2, 3): "Tuple Key (immutable elements)",
    True: "Boolean Key" # True/False are integers 1/0 internally
}
print(f"2.2 Mixed Keys Example: {mixed_keys_example}")

# 2.3 Dictionary with complex values (lists, other dictionaries, sets)
# Values can be of any data type, including other collections.
company_data = {
    "company_name": "InnovateTech Inc.",
    "founded_year": 2010,
    "departments": ["Engineering", "Marketing", "Sales", "HR"],
    "contact_info": {
        "phone": "555-123-4567",
        "email": "info@innovatetech.com"
    },
    "technologies": {"Python", "JavaScript", "Cloud"} # A set as a value
}
print(f"2.3 Company Data (nested values): {company_data}")


# --- 3. Creating Dictionaries using the dict() Constructor ---

print("\n--- 3. Creating Dictionaries using the dict() Constructor ---")

# The `dict()` constructor is versatile and can take different forms of input.

# 3.1 From keyword arguments (keys become strings)
# This is convenient for simple dictionaries where keys are valid Python identifiers.
# Syntax: dict(key1=value1, key2=value2, ...)
product_info = dict(item="Laptop", brand="Dell", price=1200.00, in_stock=True)
print(f"3.1 Product Info (from keyword args): {product_info}")

# 3.2 From an iterable of key-value pairs (e.g., list of tuples, list of lists)
# The iterable must contain 2-element sequences, where the first element is the key
# and the second is the value.
# Syntax: dict([(key1, value1), (key2, value2), ...])
student_grades_tuples = [
    ("Math", "A"),
    ("Science", "B+"),
    ("History", "A-")
]
grades_dict = dict(student_grades_tuples)
print(f"3.2 Student Grades (from list of tuples): {grades_dict}")

# Can also use a list of lists
student_scores_lists = [
    ["Alice", 95],
    ["Bob", 88],
    ["Charlie", 92]
]
scores_dict = dict(student_scores_lists)
print(f"3.2 Student Scores (from list of lists): {scores_dict}")

# Using zip() with two iterables (one for keys, one for values)
names = ["apple", "banana", "cherry"]
counts = [10, 15, 8]
fruit_counts = dict(zip(names, counts))
print(f"3.2 Fruit Counts (from zip object): {fruit_counts}")

# 3.3 From another dictionary (shallow copy)
# This creates a new dictionary object, but if values are mutable (like lists/dicts),
# they are still referenced by both the original and the new dictionary.
original_settings = {"theme": "dark", "font_size": 12, "plugins": ["spellcheck", "linter"]}
copied_settings = dict(original_settings)
print(f"3.3 Original Settings: {original_settings}")
print(f"    Copied Settings: {copied_settings}")

# Demonstrate shallow copy behavior:
copied_settings["font_size"] = 14 # Modifies top-level item in copy, not original
copied_settings["plugins"].append("formatter") # Modifies mutable item, affects both
print(f"    Original Settings after copy modification: {original_settings}")
print(f"    Copied Settings after copy modification: {copied_settings}")


# --- 4. Creating Dictionaries using Dictionary Comprehensions ---

print("\n--- 4. Creating Dictionaries using Dictionary Comprehensions ---")

# Dictionary comprehensions provide a concise way to create dictionaries
# from existing iterables, often with transformations or filtering.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# 4.1 Basic comprehension: squaring numbers
squares_dict = {num: num**2 for num in range(1, 6)}
print(f"4.1 Squares Dictionary: {squares_dict}") # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 4.2 Comprehension with conditional filtering
even_numbers_and_cubes = {num: num**3 for num in range(10) if num % 2 == 0}
print(f"4.2 Even Numbers and their Cubes: {even_numbers_and_cubes}")

# 4.3 Comprehension from existing dictionary (e.g., swapping keys and values)
# Values must be hashable to become keys.
inverted_dict = {value: key for key, value in squares_dict.items()}
print(f"4.3 Inverted Dictionary (keys/values swapped): {inverted_dict}")

# 4.4 Comprehension from string (mapping characters to their ASCII values)
char_ascii_map = {char: ord(char) for char in "Python"}
print(f"4.4 Character to ASCII map: {char_ascii_map}")


# --- 5. Creating Dictionaries using dict.fromkeys() ---

print("\n--- 5. Creating Dictionaries using dict.fromkeys() ---")

# The `fromkeys()` class method creates a new dictionary with keys from an iterable
# and sets all values to a specified default value (or None if not specified).
# Syntax: dict.fromkeys(iterable_of_keys, value=None)

# 5.1 With a default value
default_user_scores = dict.fromkeys(["math", "science", "english"], 0)
print(f"5.1 Default User Scores: {default_user_scores}") # {'math': 0, 'science': 0, 'english': 0}

# 5.2 Without specifying a value (defaults to None)
empty_status = dict.fromkeys(["task1", "task2", "task3"])
print(f"5.2 Empty Status (values default to None): {empty_status}") # {'task1': None, 'task2': None, 'task3': None}

# 5.3 Important: If the default value is a mutable object, all keys will
# reference the *same* mutable object. Modifying one will modify all.
mutable_default_dict = dict.fromkeys(["userA", "userB"], [])
print(f"5.3 Mutable Default (initial): {mutable_default_dict}")
mutable_default_dict["userA"].append("item1") # Modifies the list for userA
print(f"    Mutable Default (after modifying userA): {mutable_default_dict}")
# Notice that 'userB' also has 'item1' because they share the same list object.

# To avoid this, use a dictionary comprehension or a loop if mutable defaults are needed per key.
safe_mutable_default_dict = {key: [] for key in ["userC", "userD"]}
safe_mutable_default_dict["userC"].append("item1")
print(f"    Safe Mutable Default (after modifying userC): {safe_mutable_default_dict}")
# Now, 'userD' remains empty, as each key got its own distinct list.