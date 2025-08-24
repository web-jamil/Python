from collections import Counter

print("--- Python collections.Counter: Practice Code ---")

# --- 1. What is collections.Counter? ---
print("\n--- 1. What is collections.Counter? ---")
print("`Counter` is a subclass of `dict` that's specifically designed for counting hashable objects.")
print("It's a convenient way to perform frequency analysis on lists, strings, or any iterable.")
print("It maps elements to their counts.")


# --- 2. Creating Counter Objects ---
print("\n--- 2. Creating Counter Objects ---")

# 2.1 From an iterable (list, tuple, string, etc.)
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']
fruit_counts = Counter(my_list)
print(f"Counter from list: {fruit_counts}")

my_string = "programming"
char_counts = Counter(my_string)
print(f"Counter from string: {char_counts}")

my_tuple = (1, 2, 2, 3, 1, 4, 1)
num_counts = Counter(my_tuple)
print(f"Counter from tuple: {num_counts}")

# 2.2 From a dictionary (mapping elements to their initial counts)
initial_stock = {'laptop': 5, 'mouse': 10, 'keyboard': 3}
stock_counter = Counter(initial_stock)
print(f"Counter from dictionary: {stock_counter}")

# 2.3 From keyword arguments
item_inventory = Counter(books=50, pens=100, staplers=10)
print(f"Counter from keyword arguments: {item_inventory}")

# 2.4 Empty Counter
empty_counter = Counter()
print(f"Empty Counter: {empty_counter}")


# --- 3. Accessing Counts ---
print("\n--- 3. Accessing Counts ---")

# Counter objects behave like dictionaries
print(f"Count of 'apple': {fruit_counts['apple']}")
print(f"Count of 'orange': {fruit_counts['orange']}")

# Accessing a non-existent item returns 0 (not a KeyError, which is useful)
print(f"Count of 'mango' (non-existent): {fruit_counts['mango']}")

# Iterating over a Counter (iterates over elements with positive counts)
print("\nIterating over char_counts:")
for char in char_counts:
    print(f"Character: '{char}', Count: {char_counts[char]}")


# --- 4. Modifying Counts ---
print("\n--- 4. Modifying Counts ---")

# 4.1 Incrementing/Decrementing directly
my_mod_counter = Counter({'a': 2, 'b': 1})
print(f"Original: {my_mod_counter}")

my_mod_counter['a'] += 1
print(f"After incrementing 'a': {my_mod_counter}")

my_mod_counter['b'] -= 1
print(f"After decrementing 'b': {my_mod_counter}") # Count can be 0 or negative

my_mod_counter['c'] += 1 # Adds a new element
print(f"After adding 'c': {my_mod_counter}")

# 4.2 .update() method: Add counts from another iterable or mapping
# Adds new elements and increments counts of existing ones.
more_fruits = ['apple', 'grape', 'grape', 'kiwi']
fruit_counts.update(more_fruits)
print(f"After updating fruit_counts with {more_fruits}: {fruit_counts}")

# Can also update with another Counter or dict
sales_today = Counter({'laptop': 2, 'keyboard': 1, 'monitor': 1})
stock_counter.update(sales_today)
print(f"After updating stock_counter with sales: {stock_counter}")

# 4.3 .subtract() method: Subtract counts from another iterable or mapping
# Decrements counts. Counts can go below zero.
returns_today = Counter({'mouse': 1, 'laptop': 1})
stock_counter.subtract(returns_today)
print(f"After subtracting returns from stock_counter: {stock_counter}")

# 4.4 .clear() method: Resets all counts to zero (removes all elements)
temp_counter = Counter("hello")
print(f"Before clear: {temp_counter}")
temp_counter.clear()
print(f"After clear: {temp_counter}")


# --- 5. Useful Counter Methods ---
print("\n--- 5. Useful Counter Methods ---")

# 5.1 .elements(): Returns an iterator over elements, repeating each element as many times as its count.
# Elements with zero or negative counts are not included.
print(f"Fruit counts for elements(): {fruit_counts}")
print("Elements in fruit_counts:")
for fruit in fruit_counts.elements():
    print(fruit, end=" ")
print() # New line

# 5.2 .most_common(n): Returns a list of the n most common elements and their counts, from the most
# common to the least. If n is omitted or None, returns all elements.
print(f"Most common 2 fruits: {fruit_counts.most_common(2)}")
print(f"All elements sorted by commonality: {fruit_counts.most_common()}")

# 5.3 .items(), .keys(), .values() (inherited from dict)
print(f"Fruit counts items: {fruit_counts.items()}")
print(f"Fruit counts keys: {fruit_counts.keys()}")
print(f"Fruit counts values: {fruit_counts.values()}")


# --- 6. Counter Arithmetic and Set Operations ---
print("\n--- 6. Counter Arithmetic and Set Operations ---")
# Operations only keep elements with positive counts.

c1 = Counter(a=3, b=1, c=0, d=-2)
c2 = Counter(a=1, b=2, c=3, d=1)
print(f"c1: {c1}")
print(f"c2: {c2}")

# 6.1 Addition (+): Adds counts, keeping only positive results.
print(f"c1 + c2: {c1 + c2}")

# 6.2 Subtraction (-): Subtracts counts, keeping only positive results.
print(f"c1 - c2: {c1 - c2}")
print(f"c2 - c1: {c2 - c1}")

# 6.3 Intersection (&): Returns the minimum of corresponding counts (like set intersection).
# Keeps only positive results.
print(f"c1 & c2 (intersection): {c1 & c2}")

# 6.4 Union (|): Returns the maximum of corresponding counts (like set union).
# Keeps only positive results.
print(f"c1 | c2 (union): {c1 | c2}")

# 6.5 Unary Plus (+c): Removes zero or negative counts.
negative_counter = Counter(x=5, y=-2, z=0, w=3)
print(f"Negative counter: {negative_counter}")
print(f"+negative_counter: {+negative_counter}") # Result: Counter({'x': 5, 'w': 3})

# 6.6 Unary Minus (-c): Flips signs and removes zero or negative counts.
print(f"-negative_counter: {-negative_counter}") # Result: Counter({'y': 2})


# --- 7. Comparison and Conversion ---
print("\n--- 7. Comparison and Conversion ---")

# 7.1 Equality (==): Counters are equal if they have the same elements with the same positive counts.
# Zero/negative counts are ignored for equality.
c_eq1 = Counter(a=1, b=2)
c_eq2 = Counter(b=2, a=1)
c_eq3 = Counter(a=1, b=2, c=0)
print(f"c_eq1 ({c_eq1}) == c_eq2 ({c_eq2}): {c_eq1 == c_eq2}") # True
print(f"c_eq1 ({c_eq1}) == c_eq3 ({c_eq3}): {c_eq1 == c_eq3}") # True (c=0 is ignored)

# 7.2 Conversion to other types
converted_dict = dict(fruit_counts)
print(f"fruit_counts as dict: {converted_dict}")

converted_list_of_keys = list(fruit_counts)
print(f"fruit_counts keys as list: {converted_list_of_keys}")

converted_list_of_elements = list(fruit_counts.elements())
print(f"fruit_counts elements as list: {converted_list_of_elements}")

converted_set_of_keys = set(fruit_counts)
print(f"fruit_counts keys as set: {converted_set_of_keys}")


# --- 8. Practical Use Case: Word Frequency Analysis ---
print("\n--- 8. Practical Use Case: Word Frequency Analysis ---")

text = "This is a simple text. This text demonstrates how to count words in a text using Counter."
# Convert to lowercase and split into words
words = text.lower().replace('.', '').split()
print(f"Raw words: {words}")

word_frequencies = Counter(words)
print(f"Word frequencies: {word_frequencies}")

print(f"Top 3 most common words: {word_frequencies.most_common(3)}")


print("\n--- End of Python collections.Counter Practice Code ---")