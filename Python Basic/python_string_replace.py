# --- Python String replace() Method: All About in Code ---

# The `replace()` method is a built-in string method in Python.
# It returns a *new* string where all occurrences of a specified
# substring are replaced with another substring.
# IMPORTANT: Strings in Python are immutable, so `replace()` does not
# modify the original string; it always returns a new one.

# Syntax: string.replace(old, new, count)
# - old: The substring to be replaced.
# - new: The substring to replace `old` with.
# - count (optional): The maximum number of occurrences to replace.
#                    If omitted, all occurrences are replaced.

# --- 1. Basic Usage: Replacing All Occurrences ---

print("--- 1. Basic Usage: Replacing All Occurrences ---")

original_string_1 = "Hello world, hello Python, hello again."
old_substring_1 = "hello"
new_substring_1 = "hi"

# Replace all occurrences of "hello" with "hi"
new_string_1 = original_string_1.replace(old_substring_1, new_substring_1)

print(f"Original: '{original_string_1}'")
print(f"Replaced: '{new_string_1}'")
print(f"Original string remains unchanged: '{original_string_1}'\n")


# Case Sensitivity: `replace()` is case-sensitive.
original_string_2 = "Apple, apple, APPLE, banana"
old_substring_2 = "apple"
new_substring_2 = "orange"

new_string_2 = original_string_2.replace(old_substring_2, new_substring_2)

print(f"Original: '{original_string_2}'")
print(f"Replaced (case-sensitive): '{new_string_2}'") # Only lowercase 'apple' is replaced
print("To replace regardless of case, convert to a consistent case first or use regex (see advanced).\n")


# Replacing with an empty string (effectively removing)
original_string_3 = "This string contains extra spaces."
old_substring_3 = " "
new_substring_3 = ""

new_string_3 = original_string_3.replace(old_substring_3, new_substring_3)

print(f"Original: '{original_string_3}'")
print(f"Removed spaces: '{new_string_3}'\n")


# --- 2. Using the 'count' Parameter ---

print("--- 2. Using the 'count' Parameter ---")

original_string_4 = "one two one three one four one"
old_substring_4 = "one"
new_substring_4 = "FIVE"

# Replace only the first occurrence
new_string_4_first = original_string_4.replace(old_substring_4, new_substring_4, 1)
print(f"Original: '{original_string_4}'")
print(f"Replace first 'one': '{new_string_4_first}'")

# Replace the first two occurrences
new_string_4_two = original_string_4.replace(old_substring_4, new_substring_4, 2)
print(f"Replace first two 'one's: '{new_string_4_two}'")

# If 'count' is greater than the number of occurrences, all occurrences are replaced.
new_string_4_excess_count = original_string_4.replace(old_substring_4, new_substring_4, 100)
print(f"Replace with excess count (100): '{new_string_4_excess_count}'")
print("All 'one's are replaced because 100 > actual occurrences.\n")


# --- 3. What Happens if 'old' Substring is Not Found? ---

print("--- 3. What Happens if 'old' Substring is Not Found? ---")

original_string_5 = "Python programming"
old_substring_5 = "Java"
new_substring_5 = "C++"

# If `old` is not found, the original string is returned unchanged.
new_string_5 = original_string_5.replace(old_substring_5, new_substring_5)

print(f"Original: '{original_string_5}'")
print(f"Replace '{old_substring_5}' (not found): '{new_string_5}'")
print(f"Is new_string_5 identical to original_string_5? {new_string_5 is original_string_5}") # Often True for optimization
print(f"Are their values equal? {new_string_5 == original_string_5}\n")


# --- 4. Chaining replace() Calls ---

print("--- 4. Chaining replace() Calls ---")

sentence = "The cat sat on the mat."
# Replace "cat" with "dog", then "dog" with "mouse"
chained_replace = sentence.replace("cat", "dog").replace("dog", "mouse")

print(f"Original: '{sentence}'")
print(f"Chained replace (cat->dog->mouse): '{chained_replace}'\n")


# --- 5. Replacing Special Characters or Patterns ---

print("--- 5. Replacing Special Characters or Patterns ---")

# Replacing newline characters
text_with_newlines = "Line 1\nLine 2\nLine 3"
single_line_text = text_with_newlines.replace("\n", " ")
print(f"Original with newlines:\n'{text_with_newlines}'")
print(f"Replaced newlines with spaces: '{single_line_text}'\n")

# Replacing multiple consecutive spaces with a single space
# (Note: For more complex whitespace normalization, regex is better)
text_with_multi_spaces = "Hello   world   this    is  a test."
# Simple replace won't handle all cases in one go, usually chained
normalized_spaces = text_with_multi_spaces.replace("  ", " ").replace("  ", " ") # Run twice to catch "   "
print(f"Original with multi spaces: '{text_with_multi_spaces}'")
print(f"Normalized spaces (simple replace): '{normalized_spaces}'\n")

# If you need to replace multiple different substrings, you can iterate
text_for_multi_sub = "I like apples and bananas."
replacements = {
    "apples": "oranges",
    "bananas": "grapes"
}
for old, new in replacements.items():
    text_for_multi_sub = text_for_multi_sub.replace(old, new)
print(f"Original for multi-sub replace: 'I like apples and bananas.'")
print(f"After multiple replacements: '{text_for_multi_sub}'\n")


# --- 6. Performance Considerations ---

print("--- 6. Performance Considerations ---")

# For very large strings or many replacements, `replace()` is implemented
# in C and is highly optimized.
# However, if you're doing many replacements on the *same* string in a loop,
# it can become inefficient due to string immutability (creating new strings repeatedly).
# In such cases, consider using `re.sub()` for regex-based replacement or
# joining parts if you're building a string piecemeal.

# Example of potential inefficiency (for demonstration, not a real bottleneck usually)
long_string = "a" * 100000 + "b" + "a" * 100000
# If you were to do this many times:
# for _ in range(100):
#     long_string = long_string.replace("b", "c")
# This creates 100 new large strings.

print("`replace()` is generally efficient for its purpose.")
print("Consider `re.sub()` for complex patterns (regex) or many different replacements.")
print("For building strings with many small changes, list comprehensions with `.join()` might be better.\n")


# --- 7. Difference from Regular Expressions (re.sub) ---

print("--- 7. Difference from Regular Expressions (re.sub) ---")

import re

# `replace()` performs a literal substring replacement.
# `re.sub()` uses regular expressions for pattern matching and replacement.

text_with_patterns = "My email is test@example.com and phone is 123-456-7890."

# Using replace() - only exact matches
literal_replaced = text_with_patterns.replace("test@example.com", "[EMAIL HIDDEN]")
print(f"Literal replace: '{literal_replaced}'")

# Using re.sub() - can match patterns
# Regex to match an email address (simplified)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_replaced_email = re.sub(email_pattern, "[EMAIL HIDDEN]", text_with_patterns)
print(f"Regex replace (email): '{regex_replaced_email}'")

# Regex to match a phone number (simplified)
phone_pattern = r'\d{3}-\d{3}-\d{4}'
regex_replaced_phone = re.sub(phone_pattern, "[PHONE HIDDEN]", text_with_patterns)
print(f"Regex replace (phone): '{regex_replaced_phone}'\n")

print("Choose `replace()` for simple, literal substring replacements.")
print("Choose `re.sub()` when you need to match patterns (e.g., specific formats, multiple spaces, beginning/end of line).\n")