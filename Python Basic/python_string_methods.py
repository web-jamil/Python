# --- Python String capitalize() Method: All About in Code ---
# Return a copy of the string with its first character capitalized and the rest lowercased.
# The `capitalize()` method is a built-in string method in Python.
# It returns a copy of the string with its first character capitalized
# and the rest of the characters in lowercase.

# Syntax: string.capitalize()
# - It takes no arguments.

print("--- 1. Basic Usage: Capitalizing the First Letter ---")

# 1.1. Simple sentence
text1 = "hello world"
capitalized_text1 = text1.capitalize()
print(f"Original: '{text1}'")
print(f"capitalized(): '{capitalized_text1}'\n")

# 1.2. String already partially capitalized
text2 = "pYtHoN PrOgRaMmInG"
capitalized_text2 = text2.capitalize()
print(f"Original: '{text2}'")
print(f"capitalized(): '{capitalized_text2}'\n") # Note how all other letters become lowercase

# 1.3. String already fully uppercase
text3 = "WELCOME"
capitalized_text3 = text3.capitalize()
print(f"Original: '{text3}'")
print(f"capitalized(): '{capitalized_text3}'\n")

# 1.4. String already fully lowercase
text4 = "coding"
capitalized_text4 = text4.capitalize()
print(f"Original: '{text4}'")
print(f"capitalized(): '{capitalized_text4}'\n")


print("--- 2. Behavior with Non-Alphabetic First Characters ---")

# 2.1. First character is a digit
text5 = "123 python"
capitalized_text5 = text5.capitalize()
print(f"Original: '{text5}'")
print(f"capitalized(): '{capitalized_text5}'\n") # Digits are not affected

# 2.2. First character is a symbol/punctuation
text6 = "@hello world"
capitalized_text6 = text6.capitalize()
print(f"Original: '{text6}'")
print(f"capitalized(): '{capitalized_text6}'\n") # Symbols are not affected, subsequent letters are lowercased

text7 = "# coding"
capitalized_text7 = text7.capitalize()
print(f"Original: '{text7}'")
print(f"capitalized(): '{capitalized_text7}'\n")

# 2.3. String starting with whitespace
text8 = "   hello world"
capitalized_text8 = text8.capitalize()
print(f"Original: '{text8}'")
print(f"capitalized(): '{capitalized_text8}'\n") # Whitespace is preserved, first *letter* after it becomes capitalized

text9 = "\n\tpython"
capitalized_text9 = text9.capitalize()
print(f"Original: '{text9}'")
print(f"capitalized(): '{capitalized_text9}'\n") # Newlines/tabs are preserved, first letter after it capitalized


print("--- 3. Behavior with Empty String ---")

# 3.1. Empty string
text10 = ""
capitalized_text10 = text10.capitalize()
print(f"Original: '{text10}'")
print(f"capitalized(): '{capitalized_text10}'") # Returns an empty string
print(f"Is empty string == '': {capitalized_text10 == ''}\n")


print("--- 4. capitalize() vs. title() vs. upper() vs. lower() ---")

# It's important to understand the distinction between capitalize() and other casing methods.

text_comparison = "this is a MIXED CASE string."

# 4.1. capitalize()
# - First character of the entire string to uppercase.
# - All other characters to lowercase.
capitalized_result = text_comparison.capitalize()
print(f"Original: '{text_comparison}'")
print(f"capitalize(): '{capitalized_result}'")

# 4.2. title()
# - First letter of *each word* to uppercase.
# - Remaining letters in each word to lowercase.
title_result = text_comparison.title()
print(f"title():    '{title_result}'")

# 4.3. upper()
# - All characters to uppercase.
upper_result = text_comparison.upper()
print(f"upper():    '{upper_result}'")

# 4.4. lower()
# - All characters to lowercase.
lower_result = text_comparison.lower()
print(f"lower():    '{lower_result}'\n")


print("--- 5. Return Value and Immutability ---")

# String methods in Python do not modify the original string (strings are immutable).
# They return a *new* string with the desired changes.

my_string = "immutable string"
print(f"Original string variable: '{my_string}'")

new_string = my_string.capitalize()
print(f"New string (after capitalize()): '{new_string}'")
print(f"Original string variable after call: '{my_string}'\n") # Original remains unchanged

# You need to assign the result back to a variable if you want to use the capitalized version.
my_string = my_string.capitalize()
print(f"Original string variable after re-assignment: '{my_string}'\n")


print("--- 6. Practical Use Cases ---")

# 6.1. Formatting user input (e.g., names, cities)
user_name_input = input("Enter your name (e.g., john doe): ")
formatted_name = user_name_input.capitalize()
print(f"Formatted Name: {formatted_name}\n")

# 6.2. Ensuring consistent capitalization for database entries or display
product_name_raw = "ultimate gadget pro"
display_name = product_name_raw.capitalize()
print(f"Product Display Name: {display_name}\n")

# 6.3. Simple sentence casing
raw_sentence = "this is a sentence. it might have weird capitalization."
clean_sentence = raw_sentence.capitalize()
print(f"Cleaned Sentence: {clean_sentence}\n")



# --- Python String casefold() Method: All About in Code ---
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# The `casefold()` method is a built-in string method in Python.
# It returns a caseless version of the string, suitable for caseless matching.
# This means it converts all characters to their casefolded equivalent,
# which can be more aggressive than `lower()` for case-insensitive comparisons,
# especially with Unicode characters.

# Syntax: string.casefold()
# - It takes no arguments.

print("--- 1. Basic Usage: Similar to lower() for ASCII ---")

# For basic ASCII characters, `casefold()` often behaves identically to `lower()`.

text1 = "Hello World"
casefolded_text1 = text1.casefold()
lowercased_text1 = text1.lower()
print(f"Original:          '{text1}'")
print(f"casefold():        '{casefolded_text1}'")
print(f"lower():           '{lowercased_text1}'")
print(f"casefold() == lower(): {casefolded_text1 == lowercased_text1}\n")

text2 = "PYTHON PROGRAMMING"
casefolded_text2 = text2.casefold()
lowercased_text2 = text2.lower()
print(f"Original:          '{text2}'")
print(f"casefold():        '{casefolded_text2}'")
print(f"lower():           '{lowercased_text2}'")
print(f"casefold() == lower(): {casefolded_text2 == lowercased_text2}\n")


print("--- 2. Key Difference: Handling Unicode Characters (more aggressive) ---")

# The main distinction of `casefold()` becomes apparent with certain Unicode characters
# that have specific casefolding rules.

# Example 2.1: German Eszett (ß)
# `lower()` leaves 'ß' as is, while `casefold()` converts it to 'ss'.
# This is crucial for correct caseless matching in languages like German.
text_eszett = "Straße" # German word for 'street'
casefolded_eszett = text_eszett.casefold()
lowercased_eszett = text_eszett.lower()
print(f"Original (German Eszett): '{text_eszett}'")
print(f"casefold():                '{casefolded_eszett}'") # Converts 'ß' to 'ss'
print(f"lower():                   '{lowercased_eszett}'")   # Leaves 'ß' as 'ß'
print(f"casefold() == lower():     {casefolded_eszett == lowercased_eszett}\n")

# Example 2.2: Micro Sign (µ)
# `lower()` leaves 'µ' as is, `casefold()` converts it to 'micro sign' equivalent.
text_micro = "Μικρό" # Greek word for 'small', starts with Capital Mu
# The lowercase equivalent of Greek Capital Mu (Μ) is Mu (μ).
# The micro sign (µ) is a distinct character often visually similar to μ.
# `casefold` aims for full equivalence, so it maps 'µ' to 'mu' equivalents.
# Let's use a more direct example where casefolding is relevant:
# Let's consider a character that might be converted to more than one character or handled specially.
# For example, some characters that are uppercased in Unicode don't have a direct lowercase equivalent
# but are *casefolded* to a canonical representation.

# A common example for casefolding beyond `ß` is the Turkish dotless 'I' and dotted 'i'.
# Python's default locale handling might make this subtle.
# The standard example where `casefold` is more aggressive often points to `ß` (becomes `ss`).
# While other specific Unicode characters exist, `ß` is the most common demonstration.

# Let's consider some tricky character comparisons that `casefold` aims to simplify.
# For instance, if you're trying to match 'FILE' and 'File' and 'file', `lower()` works.
# But if you're matching 'STRASSE' and 'Straße', `lower()` would fail without extra logic.

print("--- 3. Purpose: Robust Case-Insensitive Matching ---")

# The primary purpose of `casefold()` is to enable more robust case-insensitive comparisons
# across different languages and character sets, where `lower()` might not be sufficient.

string_db = ["Straße", "STRASSE", "strasse", "My Document", "MY DOCUMENT"]
search_query = "strasse"

# Using lower() for comparison
print("--- Using .lower() for comparison ---")
found_lower = False
for item in string_db:
    if item.lower() == search_query.lower():
        print(f"  Found (lower): '{item}' matched '{search_query}'")
        found_lower = True
if not found_lower:
    print(f"  '{search_query}' NOT fully matched using .lower()")
print("")

# Using casefold() for comparison (more reliable for international text)
print("--- Using .casefold() for comparison ---")
found_casefold = False
for item in string_db:
    if item.casefold() == search_query.casefold():
        print(f"  Found (casefold): '{item}' matched '{search_query}'")
        found_casefold = True
if not found_casefold:
    print(f"  '{search_query}' NOT fully matched using .casefold()")
print("\n")

# Practical scenario: User enters "STRASSE" or "STRASS" and you want to match "Straße" in your data.
data_entry = "Straße"
user_input_1 = "STRASSE"
user_input_2 = "strasse"

print(f"Database entry: '{data_entry}'")
print(f"User input 1:   '{user_input_1}'")
print(f"User input 2:   '{user_input_2}'\n")

print("Comparison using .lower():")
print(f"'{data_entry.lower()}' == '{user_input_1.lower()}': {data_entry.lower() == user_input_1.lower()}")
print(f"'{data_entry.lower()}' == '{user_input_2.lower()}': {data_entry.lower() == user_input_2.lower()}\n")

print("Comparison using .casefold():")
print(f"'{data_entry.casefold()}' == '{user_input_1.casefold()}': {data_entry.casefold() == user_input_1.casefold()}")
print(f"'{data_entry.casefold()}' == '{user_input_2.casefold()}': {data_entry.casefold() == user_input_2.casefold()}\n")


print("--- 4. Behavior with Non-Alphabetic Characters, Digits, Empty String ---")

# `casefold()` primarily affects alphabetic characters. Digits, symbols,
# and whitespace are generally unaffected.

# 4.1. String with digits and symbols
text_num_sym = "123@PyThOn!"
casefolded_num_sym = text_num_sym.casefold()
lowercased_num_sym = text_num_sym.lower()
print(f"Original:          '{text_num_sym}'")
print(f"casefold():        '{casefolded_num_sym}'")
print(f"lower():           '{lowercased_num_sym}'")
print(f"casefold() == lower(): {casefolded_num_sym == lowercased_num_sym}\n")

# 4.2. String with leading/trailing whitespace
text_whitespace = "   Hello World!   "
casefolded_whitespace = text_whitespace.casefold()
lowercased_whitespace = text_whitespace.lower()
print(f"Original:          '{text_whitespace}'")
print(f"casefold():        '{casefolded_whitespace}'")
print(f"lower():           '{lowercased_whitespace}'")
print(f"casefold() == lower(): {casefolded_whitespace == lowercased_whitespace}\n")


# 4.3. Empty string
text_empty = ""
casefolded_empty = text_empty.casefold()
lowercased_empty = text_empty.lower()
print(f"Original:          '{text_empty}'")
print(f"casefold():        '{casefolded_empty}'")
print(f"lower():           '{lowercased_empty}'")
print(f"casefold() == lower(): {casefolded_empty == lowercased_empty}\n") # Returns an empty string


print("--- 5. Return Value and Immutability ---")

# Like other string methods, `casefold()` returns a new string.
# It does not modify the original string, as strings in Python are immutable.

my_original_string = "CASELESS Text"
print(f"Original string variable: '{my_original_string}'")

result_string = my_original_string.casefold()
print(f"Resulting string (after casefold()): '{result_string}'")
print(f"Original string variable after call: '{my_original_string}'\n") # Original remains unchanged

# To use the casefolded version, you must assign the result.
my_original_string = my_original_string.casefold()
print(f"Original string variable after re-assignment: '{my_original_string}'\n")



# --- Python String center() Method: All About in Code ---

# The `center()` method is a built-in string method in Python.
# It returns a new string that is centered within a specified `width`.
# The padding on the left and right sides is done using a specified `fillchar`
# (which defaults to a space ' ').
# Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space)
# Syntax: string.center(width[, fillchar])
# - `width`: (Required) An integer specifying the total length of the new string.
#            If `width` is less than or equal to the original string's length,
#            the original string is returned unchanged.
# - `fillchar`: (Optional) The character used for padding.
#               It must be a single character string. Defaults to a space (' ').

print("--- 1. Basic Usage: Centering with Default Fill Character (Space) ---")

text1 = "Python"
width1 = 10
centered_text1 = text1.center(width1)
print(f"Original: '{text1}' (length {len(text1)})")
print(f"center({width1}): '{centered_text1}' (length {len(centered_text1)})")
# Expected: "  Python  " (2 spaces left, 2 spaces right)
print(f"Visual representation: '{centered_text1.replace(' ', '.')}'\n")

text2 = "Hello"
width2 = 15
centered_text2 = text2.center(width2)
print(f"Original: '{text2}' (length {len(text2)})")
print(f"center({width2}): '{centered_text2}' (length {len(centered_text2)})")
# Expected: "     Hello     " (5 spaces left, 5 spaces right)
print(f"Visual representation: '{centered_text2.replace(' ', '.')}'\n")


print("--- 2. Centering with a Custom Fill Character ---")

# The `fillchar` argument must be a single character.

text3 = "Code"
width3 = 12
fillchar3 = '*'
centered_text3 = text3.center(width3, fillchar3)
print(f"Original: '{text3}' (length {len(text3)})")
print(f"center({width3}, '{fillchar3}'): '{centered_text3}' (length {len(centered_text3)})")
# Expected: "****Code****" (4 * left, 4 * right)
print(f"Visual representation: '{centered_text3}'\n")

text4 = "Center"
width4 = 11
fillchar4 = '-'
centered_text4 = text4.center(width4, fillchar4)
print(f"Original: '{text4}' (length {len(text4)})")
print(f"center({width4}, '{fillchar4}'): '{centered_text4}' (length {len(centered_text4)})")
# Expected: "---Center--" (Odd difference in padding)
# Explanation: (width - len(string)) / 2. Here (11 - 6) / 2 = 5 / 2 = 2.5.
# Python puts the extra character on the right if the padding cannot be split equally.
# So, 2 on left, 3 on right.
print(f"Visual representation: '{centered_text4}'\n")


print("--- 3. Behavior when `width` is Less Than or Equal to String Length ---")

# If the specified `width` is less than or equal to the original string's length,
# the `center()` method returns the original string unchanged. It does NOT truncate.

text5 = "LongString" # Length 10
width5_a = 5
width5_b = 10

centered_text5_a = text5.center(width5_a)
centered_text5_b = text5.center(width5_b)

print(f"Original: '{text5}' (length {len(text5)})")
print(f"center({width5_a}): '{centered_text5_a}' (length {len(centered_text5_a)})")
# print(f"  Is original unchanged? {text5_a == text5}\n") # True

print(f"center({width5_b}): '{centered_text5_b}' (length {len(centered_text5_b)})")
# print(f"  Is original unchanged? {text5_b == text5}\n") # True


print("--- 4. Behavior with Empty String ---")

# An empty string will be centered just like any other string.

empty_string = ""
width_empty = 5
centered_empty = empty_string.center(width_empty, '.')
print(f"Original: '{empty_string}' (length {len(empty_string)})")
print(f"center({width_empty}, '.'): '{centered_empty}' (length {len(centered_empty)})")
# Expected: "....." (5 dots)
print(f"Visual representation: '{centered_empty}'\n")

# If width is 0 or negative for empty string, it returns empty string
centered_empty_zero_width = empty_string.center(0)
print(f"center(0): '{centered_empty_zero_width}' (length {len(centered_empty_zero_width)})")
print(f"Is empty string == '': {centered_empty_zero_width == ''}\n")


print("--- 5. Return Value and Immutability ---")

# String methods in Python always return a *new* string.
# They do not modify the original string because strings are immutable.

my_original_string = "immutable"
print(f"Original string variable: '{my_original_string}'")

result_string = my_original_string.center(15, '#')
print(f"Resulting string (after center()): '{result_string}'")
print(f"Original string variable after call: '{my_original_string}'\n") # Original remains unchanged

# To use the centered version, you must assign the result back to a variable.
my_original_string = my_original_string.center(15)
print(f"Original string variable after re-assignment: '{my_original_string}'\n")


print("--- 6. Error Handling ---")

# The `fillchar` argument must be a single character.
try:
    "test".center(10, "ab")
except TypeError as e:
    print(f"TypeError caught: {e}")
    print("  'fillchar' must be a single character.\n")

# The `width` argument must be an integer.
try:
    "test".center("ten")
except TypeError as e:
    print(f"TypeError caught: {e}")
    print("  'width' must be an integer.\n")


print("--- 7. Practical Use Cases ---")

# 7.1. Formatting output for console display (e.g., headers, tables)
header_title = "REPORT SUMMARY"
console_width = 80
centered_header = header_title.center(console_width, '=')
print(centered_header)
print("\nThis is the main content of the report.")
print("It aligns nicely under the centered header.\n")
print('=' * console_width + '\n') # Bottom border

# 7.2. Creating fixed-width fields in text files or logs
data_item = "ItemX"
price = "123.45"
quantity = "10"

line_format = "{:^15} {:^10} {:^8}" # Using f-string format specifiers is often more powerful for tables
                                  # but center() can build individual components.
# Using center() directly for fixed-width columns
formatted_item = data_item.center(15)
formatted_price = price.center(10)
formatted_quantity = quantity.center(8)

print(f"|{formatted_item}|{formatted_price}|{formatted_quantity}|")
print(f"|{'Product Name'.center(15)}|{'Price'.center(10)}|{'Qty'.center(8)}|")
print(f"|{'-'*15}|{'-'*10}|{'-'*8}|")


# --- Python String count() Method: All About in Code ---

# The `count()` method is a built-in string method in Python.
# It returns the number of non-overlapping occurrences of a substring
# in the given string.
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

# If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.
# Syntax: string.count(substring[, start[, end]])
# - `substring`: (Required) The string to search for.
# - `start`: (Optional) The starting index of the slice to search within.
#            Defaults to 0 (beginning of the string).
# - `end`: (Optional) The ending index (exclusive) of the slice to search within.
#          Defaults to the end of the string (len(string)).

print("--- 1. Basic Usage: Counting All Occurrences ---")

text1 = "apple banana apple orange apple"
sub1 = "apple"
count1 = text1.count(sub1)
print(f"Original: '{text1}'")
print(f"Counting '{sub1}': {count1} occurrences\n") # Expected: 3

text2 = "aaaaa"
sub2 = "aa"
count2 = text2.count(sub2)
print(f"Original: '{text2}'")
print(f"Counting '{sub2}': {count2} occurrences")
# Expected: 2 (Non-overlapping: "aa" at index 0, then "aa" at index 2. The 'a' at index 4 is left over)
# If it were overlapping, it would be 4. This highlights the "non-overlapping" rule.
print("  (Note: count() finds NON-OVERLAPPING occurrences)\n")

text3 = "Mississippi"
sub3_a = "iss"
sub3_b = "i"
count3_a = text3.count(sub3_a)
count3_b = text3.count(sub3_b)
print(f"Original: '{text3}'")
print(f"Counting '{sub3_a}': {count3_a} occurrences") # Expected: 2 ("Miss"issippi, Miss"iss"ippi)
print(f"Counting '{sub3_b}': {count3_b} occurrences\n") # Expected: 4


print("--- 2. Using `start` and `end` Parameters (Slicing the Search Area) ---")

# The `start` and `end` parameters work like string slicing [start:end].
# The search is performed on `string[start:end]`.

text4 = "python programming is fun and python is great"
sub4 = "python"

# 2.1. Search from a specific `start` index
count4_start = text4.count(sub4, 7) # Search from index 7 onwards
print(f"Original: '{text4}'")
print(f"Counting '{sub4}' from index 7: {count4_start} occurrences") # Expected: 1 (only the second "python")

# 2.2. Search within a specific `slice` (start and end)
count4_slice = text4.count(sub4, 0, 15) # Search from index 0 up to (but not including) index 15
print(f"Counting '{sub4}' from index 0 to 15: {count4_slice} occurrences\n") # Expected: 1 (only the first "python")

# 2.3. Empty slice or substring not found in slice
count4_empty_slice = text4.count(sub4, 50, 60) # Search outside valid range
print(f"Counting '{sub4}' in empty/invalid slice (50, 60): {count4_empty_slice} occurrences") # Expected: 0

text5 = "banana"
# Indexing:   0 1 2 3 4 5
# Characters: b a n a n a

# Count 'a' in "banana"
print(f"Original: '{text5}'")
print(f"Count 'a' in full string: {text5.count('a')}") # Expected: 3

# Count 'a' from index 1 to 4 (i.e., in "anan")
print(f"Count 'a' from index 1 to 4: {text5.count('a', 1, 5)}") # Expected: 2 (at index 1 and 3)
print(f"  String slice considered: '{text5[1:5]}'\n")


print("--- 3. Behavior with Empty Substring ---")

# If `substring` is an empty string, `count()` returns 1 plus the length of the string
# because an empty string can be considered to occur between every character and at the ends.

text6 = "abc"
empty_sub = ""
count6 = text6.count(empty_sub)
print(f"Original: '{text6}'")
print(f"Counting empty string: {count6} occurrences") # Expected: len("abc") + 1 = 4
# Occurrences: ''a''b''c''

empty_string_target = ""
count_empty_in_empty = empty_string_target.count(empty_sub)
print(f"Counting empty string in empty string: {count_empty_in_empty} occurrences\n") # Expected: 1


print("--- 4. Behavior when Substring Not Found ---")

# If the `substring` is not found, `count()` returns 0.

text7 = "hello world"
sub_not_found = "xyz"
count7 = text7.count(sub_not_found)
print(f"Original: '{text7}'")
print(f"Counting '{sub_not_found}': {count7} occurrences\n") # Expected: 0


print("--- 5. Case-Sensitivity ---")

# The `count()` method is case-sensitive.

text8 = "Python python PYTHON"
sub_case_sensitive = "Python"
count8 = text8.count(sub_case_sensitive)
print(f"Original: '{text8}'")
print(f"Counting '{sub_case_sensitive}': {count8} occurrences\n") # Expected: 1

# To perform a case-insensitive count, convert both the string and substring to the same case first:
text8_lower = text8.lower()
sub_case_sensitive_lower = sub_case_sensitive.lower()
count8_case_insensitive = text8_lower.count(sub_case_sensitive_lower)
print(f"Case-insensitive counting of '{sub_case_sensitive}' in '{text8}': {count8_case_insensitive} occurrences\n") # Expected: 3


print("--- 6. Return Value and Immutability ---")

# String methods in Python return a new value (in this case, an integer).
# They do not modify the original string, as strings are immutable.

my_string = "immutable example"
print(f"Original string variable: '{my_string}'")

occurrences = my_string.count('m')
print(f"Occurrences of 'm': {occurrences}")
print(f"Original string variable after call: '{my_string}'\n") # Original remains unchanged


print("--- 7. Error Handling ---")

# The method will raise a TypeError if `substring` is not a string.
try:
    "abc".count(123)
except TypeError as e:
    print(f"TypeError caught (substring not string): {e}\n")

# The start and end arguments must be integers.
try:
    "abc".count("a", "one")
except TypeError as e:
    print(f"TypeError caught (start not int): {e}\n")


print("--- 8. Practical Use Cases ---")

# 8.1. Counting keyword occurrences in text
article_text = "Python is a versatile language. Many developers use Python for data science. Python's community is large."
keyword = "Python"
keyword_count = article_text.count(keyword)
print(f"Keyword '{keyword}' appears {keyword_count} times in the article.\n")

# 8.2. Analyzing character frequencies (simple way)
dna_sequence = "ATGCGTACGTACGTACGTAGCTAGCT"
a_count = dna_sequence.count('A')
t_count = dna_sequence.count('T')
g_count = dna_sequence.count('G')
c_count = dna_sequence.count('C')
print(f"DNA Sequence: {dna_sequence}")
print(f"A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}\n")

# 8.3. Validating data format (e.g., specific delimiters)
csv_line = "value1,value2,value3"
if csv_line.count(',') == 2:
    print(f"'{csv_line}' has the expected number of commas for 3 fields.\n")
else:
    print(f"'{csv_line}' does NOT have the expected number of commas.\n")







# --- Python String encode() Method: All About in Code ---

# The `encode()` method is a built-in string method in Python.
# It returns a new bytes object, where the string has been encoded
# into a sequence of bytes using a specified encoding.

# In Python 3, strings (`str` type) store sequences of Unicode characters.
# When you need to interact with external systems (like files, networks,
# databases), these characters often need to be converted into a sequence
# of bytes. This conversion process is called "encoding."
# str.encode(encoding='utf-8', errors='strict')
# Return the string encoded to bytes.

# encoding defaults to 'utf-8'; see Standard Encodings for possible values.

# # errors controls how encoding errors are handled. If 'strict' (the default), a UnicodeError exception is raised. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error(). See Error Handlers for details.
# Syntax: string.encode(encoding='utf-8', errors='strict')
# - `encoding`: (Optional) The name of the encoding to use.
#               Defaults to 'utf-8'. Common encodings include:
#               - 'utf-8': Most common and recommended for general text.
#               - 'latin-1' (or 'iso-8859-1'): Single-byte encoding for Western European languages.
#               - 'cp1252': Windows-specific Western encoding.
#               - 'ascii': Only supports ASCII characters (0-127).
#               - 'utf-16', 'utf-32': Multi-byte encodings for broader Unicode range.
# - `errors`: (Optional) Specifies how encoding errors should be handled.
#             Defaults to 'strict'. Common error handlers:
#             - 'strict': (Default) Raises a `UnicodeEncodeError` if a character
#                         cannot be encoded in the specified encoding.
#             - 'ignore': Ignores characters that cannot be encoded. (Dangerous, data loss!)
#             - 'replace': Replaces unencodable characters with a replacement character
#                          (e.g., '?'). (Can still lead to data corruption or ambiguity).
#             - 'xmlcharrefreplace': Replaces unencodable characters with XML numeric character references (e.g., '&#123;').
#             - 'backslashreplace': Replaces unencodable characters with Python backslash escaped sequences (e.g., '\xdd').
#             - 'namereplace': Replaces unencodable characters with `\N{...}` escape sequences.

print("--- 1. Basic Usage: Encoding to UTF-8 (Default) ---")

text1 = "Hello, world!"
encoded_text1 = text1.encode() # Defaults to 'utf-8'
print(f"Original string: '{text1}' (type: {type(text1)})")
print(f"Encoded (UTF-8): {encoded_text1} (type: {type(encoded_text1)})\n")
# Notice the 'b' prefix indicating a bytes object.
# For ASCII characters, UTF-8 bytes are the same as ASCII values.

text2 = "你好世界" # Chinese characters
encoded_text2 = text2.encode('utf-8')
print(f"Original string: '{text2}'")
print(f"Encoded (UTF-8): {encoded_text2}\n")
# UTF-8 uses multiple bytes for non-ASCII characters.

text3 = "Café" # Latin character with accent
encoded_text3_utf8 = text3.encode('utf-8')
print(f"Original string: '{text3}'")
print(f"Encoded (UTF-8): {encoded_text3_utf8}\n")
# The 'é' character is represented by two bytes in UTF-8 (b'\xc3\xa9').


print("--- 2. Specifying Different Encodings ---")

# 2.1. Encoding to 'latin-1' (ISO-8859-1)
# Latin-1 is a single-byte encoding, often used for Western European languages.
# It can represent 'é' with a single byte.
text4 = "Café"
encoded_text4_latin1 = text4.encode('latin-1')
print(f"Original string: '{text4}'")
print(f"Encoded (latin-1): {encoded_text4_latin1}\n") # 'é' is b'\xe9' in latin-1

# 2.2. Encoding to 'ascii' (Strict - will fail for non-ASCII)
text5_ascii = "Hello"
encoded_text5_ascii = text5_ascii.encode('ascii')
print(f"Original string: '{text5_ascii}'")
print(f"Encoded (ascii): {encoded_text5_ascii}\n")

text5_non_ascii = "Café"
try:
    encoded_text5_non_ascii = text5_non_ascii.encode('ascii')
    print(f"Encoded (ascii, should fail): {encoded_text5_non_ascii}")
except UnicodeEncodeError as e:
    print(f"UnicodeEncodeError caught for 'ascii' encoding: {e}")
    print("  'Café' cannot be encoded to ASCII because 'é' is not an ASCII character.\n")

# 2.3. Encoding to 'utf-16'
# UTF-16 uses 2 or 4 bytes per character, often starting with a Byte Order Mark (BOM).
text6 = "Hello世界"
encoded_text6_utf16 = text6.encode('utf-16')
print(f"Original string: '{text6}'")
print(f"Encoded (utf-16): {encoded_text6_utf16}\n") # Notice the BOM (b'\xff\xfe') at the beginning.


print("--- 3. Handling Encoding Errors (`errors` parameter) ---")

# This parameter dictates what happens when a character in the string cannot be
# represented in the chosen `encoding`.

problem_text = "Déjà vu €" # Contains 'é', 'à', '€' which are not in ASCII

# 3.1. 'strict' (Default) - Raises UnicodeEncodeError
print("--- Error Handling: 'strict' (default) ---")
try:
    encoded_strict = problem_text.encode('ascii', errors='strict')
    print(f"Encoded (strict): {encoded_strict}")
except UnicodeEncodeError as e:
    print(f"UnicodeEncodeError caught (strict): {e}")
    print("  'strict' handler stops execution when an unencodable character is found.\n")

# 3.2. 'ignore' - Skips unencodable characters
print("--- Error Handling: 'ignore' ---")
encoded_ignore = problem_text.encode('ascii', errors='ignore')
print(f"Original: '{problem_text}'")
print(f"Encoded (ignore): {encoded_ignore}")
print("  'ignore' drops characters that cannot be encoded. Data loss occurs!\n")
# 'Déjà vu €' becomes b'Dja vu '

# 3.3. 'replace' - Replaces with a placeholder (e.g., '?')
print("--- Error Handling: 'replace' ---")
encoded_replace = problem_text.encode('ascii', errors='replace')
print(f"Original: '{problem_text}'")
print(f"Encoded (replace): {encoded_replace}")
print("  'replace' substitutes unencodable chars with a '?'. Can cause ambiguity.\n")
# 'Déjà vu €' becomes b'D?j? vu ?'

# 3.4. 'xmlcharrefreplace' - Replaces with XML numeric character references
print("--- Error Handling: 'xmlcharrefreplace' ---")
encoded_xml = problem_text.encode('ascii', errors='xmlcharrefreplace')
print(f"Original: '{problem_text}'")
print(f"Encoded (xmlcharrefreplace): {encoded_xml}")
print("  Useful for generating XML/HTML where non-ASCII characters need representation.\n")
# 'Déjà vu €' becomes b'D&#233;j&#224; vu &#8364;'

# 3.5. 'backslashreplace' - Replaces with Python's backslash escapes
print("--- Error Handling: 'backslashreplace' ---")
encoded_backslash = problem_text.encode('ascii', errors='backslashreplace')
print(f"Original: '{problem_text}'")
print(f"Encoded (backslashreplace): {encoded_backslash}")
print("  Provides a lossless way to represent unencodable characters as escapes.\n")
# 'Déjà vu €' becomes b'D\\xe9j\\xe0 vu \\xef\\xbf\\xbd' (note: € might become multiple escapes depending on initial string source)
# More accurately for '€': \u20ac in Unicode. ASCII would represent it as '\x80' in some old encodings, but generally unrepresentable.
# In UTF-8 '€' is b'\xe2\x82\xac'. Backslashreplace shows these bytes.


print("--- 4. Return Value and Immutability ---")

# The `encode()` method returns a new `bytes` object.
# It does not modify the original string, as strings in Python are immutable.

my_string = "Hello"
print(f"Original string variable: '{my_string}' (type: {type(my_string)})")

encoded_result = my_string.encode('utf-8')
print(f"Resulting bytes object (after encode()): {encoded_result} (type: {type(encoded_result)})")
print(f"Original string variable after call: '{my_string}' (type: {type(my_string)})\n") # Original unchanged

# To use the encoded version, you must assign the result to a variable.
# You cannot reassign the string variable to the bytes object directly without type change intent.
# my_string = my_string.encode('utf-8') # This would change type of my_string to bytes!


print("--- 5. Key Concepts: Strings vs. Bytes ---")

# In Python 3:
# - `str` (string): Represents text as sequences of Unicode characters.
#   You perform text-based operations on `str` objects.
# - `bytes`: Represents binary data as sequences of bytes (integers from 0 to 255).
#   You perform byte-based operations on `bytes` objects.

# Encoding converts `str` to `bytes`.
# Decoding converts `bytes` back to `str`.

# Example of round-trip:
original_string = "Python 🐍"
print(f"Original string: '{original_string}'")

# Encode (str -> bytes)
encoded_bytes = original_string.encode('utf-8')
print(f"Encoded bytes: {encoded_bytes}")

# Decode (bytes -> str)
decoded_string = encoded_bytes.decode('utf-8')
print(f"Decoded string: '{decoded_string}'")

print(f"Is original string same as decoded? {original_string == decoded_string}\n")


print("--- 6. When to use `encode()` ---")

# You use `encode()` when you need to send text data over a network,
# write it to a file, or store it in a database.
# Essentially, whenever text needs to be converted into a binary format for storage or transmission.

# Example: Writing to a file (often handled implicitly by open() with encoding)
# If you open a file in binary write mode ('wb'), you must write bytes.
try:
    with open("my_encoded_file.txt", "wb") as f:
        message = "This is a test message with a special character: é"
        f.write(message.encode('utf-8')) # Must encode to bytes for 'wb' mode
    print("Encoded message written to 'my_encoded_file.txt' (binary mode).\n")

    # To read it back, you'd read bytes and then decode them:
    with open("my_encoded_file.txt", "rb") as f:
        read_bytes = f.read()
        decoded_message = read_bytes.decode('utf-8')
        print(f"Read and decoded from file: '{decoded_message}'")
except IOError as e:
    print(f"Error handling file: {e}")
finally:
    # Clean up the dummy file
    import os
    if os.path.exists("my_encoded_file.txt"):
        os.remove("my_encoded_file.txt")


# str.endswith(suffix[, start[, end]])
# # Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position. Using start and end is equivalent to str[start:end].endswith(suffix). 


# --- Python String endswith() Method: All About in Code ---

# The `endswith()` method is a built-in string method in Python.
# It returns True if the string ends with the specified suffix, otherwise False.

# Syntax: string.endswith(suffix[, start[, end]])
# - `suffix`: (Required) The string (or a tuple of strings) to check for.
# - `start`: (Optional) An integer specifying the starting position to begin the search.
#            The check is performed on `string[start:]`. Defaults to 0.
# - `end`: (Optional) An integer specifying the ending position (exclusive) to end the search.
#          The check is performed on `string[start:end]`. Defaults to the end of the string.

print("--- 1. Basic Usage: Checking with a Single Suffix ---")

text1 = "hello world"
suffix1_a = "world"
suffix1_b = "ld"
suffix1_c = "worlds"
suffix1_d = "World" # Case-sensitive

print(f"Original: '{text1}'")
print(f"Does it end with '{suffix1_a}'? {text1.endswith(suffix1_a)}") # Expected: True
print(f"Does it end with '{suffix1_b}'? {text1.endswith(suffix1_b)}") # Expected: True
print(f"Does it end with '{suffix1_c}'? {text1.endswith(suffix1_c)}") # Expected: False
print(f"Does it end with '{suffix1_d}'? {text1.endswith(suffix1_d)}\n") # Expected: False (case-sensitive)


print("--- 2. Checking with a Tuple of Suffixes ---")

# You can provide a tuple of strings as the `suffix` argument.
# The method returns True if the string ends with *any* of the suffixes in the tuple.

filename = "report.txt"
image_filename = "photo.jpg"
script_filename = "script.py"

text_files_suffixes = (".txt", ".csv", ".log")
image_suffixes = (".jpg", ".jpeg", ".png", ".gif")
code_suffixes = (".py", ".js", ".html")

print(f"Filename: '{filename}'")
print(f"Is '{filename}' a text file? {filename.endswith(text_files_suffixes)}") # Expected: True
print(f"Is '{filename}' an image file? {filename.endswith(image_suffixes)}\n") # Expected: False

print(f"Filename: '{image_filename}'")
print(f"Is '{image_filename}' an image file? {image_filename.endswith(image_suffixes)}") # Expected: True
print(f"Is '{image_filename}' a code file? {image_filename.endswith(code_suffixes)}\n") # Expected: False

print(f"Filename: '{script_filename}'")
print(f"Is '{script_filename}' a code file? {script_filename.endswith(code_suffixes)}\n") # Expected: True


print("--- 3. Using `start` and `end` Parameters (Slicing the Search Area) ---")

# The `start` and `end` parameters define a portion of the string to search within.
# The check is performed on `string[start:end]`.

text2 = "programming is fun"
# Index:   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
# Chars:   p r o g r a m m i n g   i s   f u n

suffix2 = "fun"
suffix3 = "is fun"
suffix4 = "g"

# 3.1. Searching within a slice using `start`
print(f"Original: '{text2}' (length {len(text2)})")
# Check "programming is fun"[15:] which is "fun"
print(f"'{text2}'.endswith('{suffix2}', 15): {text2.endswith(suffix2, 15)}") # Expected: True

# Check "programming is fun"[12:] which is "is fun"
print(f"'{text2}'.endswith('{suffix3}', 12): {text2.endswith(suffix3, 12)}") # Expected: True

# 3.2. Searching within a slice using `start` and `end`
# Check "programming is fun"[0:11] which is "programming"
print(f"'{text2}'.endswith('{suffix4}', 0, 11): {text2.endswith(suffix4, 0, 11)}") # Expected: True (ends with 'g')

# Check "programming is fun"[0:10] which is "programmin"
print(f"'{text2}'.endswith('{suffix4}', 0, 10): {text2.endswith(suffix4, 0, 10)}") # Expected: False (ends with 'n')

# 3.3. Start/end indices out of bounds (handled gracefully)
print(f"'{text2}'.endswith('{suffix2}', 100): {text2.endswith(suffix2, 100)}") # Expected: False (empty slice)
print(f"'{text2}'.endswith('{suffix2}', -50): {text2.endswith(suffix2, -50)}") # Behaves as 0, so True if ends with suffix

print(f"'{text2}'.endswith('{suffix2}', 0, -1): {text2.endswith(suffix2, 0, -1)}") # Excludes last char, so False (ends with 'u')
print("  (endswith(suffix, 0, -1) means check if string[:-1] ends with suffix)\n")


print("--- 4. Behavior with Empty String as Suffix ---")

# An empty string is considered to be at the end of any string (including an empty string).
text3 = "abc"
empty_suffix = ""
print(f"Does '{text3}' end with an empty string? {text3.endswith(empty_suffix)}") # Expected: True
print(f"Does '' end with an empty string? {''.endswith(empty_suffix)}\n") # Expected: True


print("--- 5. Return Value and Immutability ---")

# The `endswith()` method returns a boolean value (True or False).
# It does not modify the original string, as strings in Python are immutable.

my_string = "check_me.pdf"
print(f"Original string variable: '{my_string}'")

is_pdf = my_string.endswith(".pdf")
print(f"Is it a PDF file? {is_pdf}")
print(f"Original string variable after call: '{my_string}'\n") # Original remains unchanged


print("--- 6. Error Handling ---")

# The `suffix` argument must be a string or a tuple of strings.
try:
    "test".endswith(123)
except TypeError as e:
    print(f"TypeError caught (suffix not string/tuple): {e}\n")

try:
    "test".endswith([".txt", ".csv"]) # List is not allowed, must be tuple
except TypeError as e:
    print(f"TypeError caught (suffix is a list, not tuple): {e}\n")

# `start` and `end` must be integers.
try:
    "test".endswith("st", "two")
except TypeError as e:
    print(f"TypeError caught (start not int): {e}\n")


print("--- 7. Practical Use Cases ---")

# 7.1. File type validation
uploaded_file = "document.docx"
allowed_docs = (".docx", ".pdf", ".txt")
if uploaded_file.endswith(allowed_docs):
    print(f"'{uploaded_file}' is an allowed document type.")
else:
    print(f"'{uploaded_file}' is NOT an allowed document type.")

image_upload = "holiday_pic.JPEG" # Note uppercase extension
if image_upload.lower().endswith((".jpg", ".jpeg", ".png")): # Often convert to lower for case-insensitivity
    print(f"'{image_upload}' is a common image format.\n")
else:
    print(f"'{image_upload}' is not a recognized image format.\n")


# 7.2. Checking URL patterns
url = "https://www.example.com/api/data/"
if url.endswith("/"):
    print(f"URL '{url}' ends with a trailing slash. Normalize if needed.\n")

# 7.3. Processing specific log entries
log_line1 = "INFO: Operation completed."
log_line2 = "ERROR: Failed to connect."
if log_line1.endswith("completed."):
    print(f"Log 1: Operation completed successfully.\n")



# --- Python String find() Method: All About in Code ---
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
# The `find()` method is a built-in string method in Python.
# It returns the lowest (leftmost) index in the string where the
# substring is found. If the substring is not found, it returns -1.

# Syntax: string.find(substring[, start[, end]])
# - `substring`: (Required) The string to search for.
# - `start`: (Optional) An integer specifying the starting position for the search.
#            The search is performed on `string[start:]`. Defaults to 0 (beginning).
# - `end`: (Optional) An integer specifying the ending position (exclusive) for the search.
#          The search is performed on `string[start:end]`. Defaults to the end of the string.

print("--- 1. Basic Usage: Finding the First Occurrence ---")

text1 = "hello world, hello Python"
sub1_a = "hello"
sub1_b = "world"
sub1_c = "Python"
sub1_d = "java" # Not found

index1_a = text1.find(sub1_a)
index1_b = text1.find(sub1_b)
index1_c = text1.find(sub1_c)
index1_d = text1.find(sub1_d)

print(f"Original: '{text1}'")
print(f"Index of '{sub1_a}': {index1_a}") # Expected: 0
print(f"Index of '{sub1_b}': {index1_b}") # Expected: 6
print(f"Index of '{sub1_c}': {index1_c}") # Expected: 14
print(f"Index of '{sub1_d}' (not found): {index1_d}\n") # Expected: -1


print("--- 2. Using `start` and `end` Parameters (Slicing the Search Area) ---")

# The `start` and `end` parameters define a slice of the string
# within which the search is performed. The method still returns
# the index relative to the *beginning of the original string*, not the slice.

text2 = "abracadabra"
# Index:   0 1 2 3 4 5 6 7 8 9 0
# Chars:   a b r a c a d a b r a

sub2 = "a"
sub3 = "abra"

# 2.1. Search from a specific `start` index
# Find 'a' starting from index 1 (i.e., in "bracadabra")
index2_start = text2.find(sub2, 1)
print(f"Original: '{text2}'")
print(f"Find '{sub2}' from index 1: {index2_start}") # Expected: 3 (the 'a' after 'br')

# Find 'a' starting from index 4 (i.e., in "cadabra")
index2_start_later = text2.find(sub2, 4)
print(f"Find '{sub2}' from index 4: {index2_start_later}\n") # Expected: 6 (the 'a' after 'cad')

# 2.2. Search within a specific `slice` (start and end)
# Find 'abra' within text2[0:5] which is "abrac"
index3_slice = text2.find(sub3, 0, 5)
print(f"Find '{sub3}' from index 0 to 5 (in '{text2[0:5]}'): {index3_slice}") # Expected: 0

# Find 'abra' within text2[1:10] which is "bracadabr"
index3_slice_later = text2.find(sub3, 1, 10)
print(f"Find '{sub3}' from index 1 to 10 (in '{text2[1:10]}'): {index3_slice_later}\n") # Expected: -1 (not found in slice)

# 2.3. Negative indices for `start` and `end`
# Python string slicing supports negative indices, and `find()` respects them.
# -1 refers to the last character, -2 to the second to last, etc.
text_neg = "abcdefgh"
print(f"Original: '{text_neg}'")
print(f"Find 'f' from index -3 (in '{text_neg[-3:]}'): {text_neg.find('f', -3)}") # Expected: 5
print(f"Find 'd' from index 0 to -1 (in '{text_neg[0:-1]}'): {text_neg.find('d', 0, -1)}") # Expected: 3
print(f"Find 'h' from index 0 to -1 (in '{text_neg[0:-1]}'): {text_neg.find('h', 0, -1)}\n") # Expected: -1


print("--- 3. Behavior with Empty Substring ---")

# If `substring` is an empty string, `find()` returns the `start` index.
# If `start` is not provided, it returns 0.

text4 = "hello"
empty_sub = ""
print(f"Find empty string in '{text4}': {text4.find(empty_sub)}") # Expected: 0
print(f"Find empty string in '{text4}' from index 2: {text4.find(empty_sub, 2)}") # Expected: 2
print(f"Find empty string in '{text4}' from index 10 (out of bounds): {text4.find(empty_sub, 10)}") # Expected: 5 (len of string)
print(f"Find empty string in '{text4}' from index 0 to 2: {text4.find(empty_sub, 0, 2)}\n") # Expected: 0


print("--- 4. Case-Sensitivity ---")

# The `find()` method is case-sensitive.

text5 = "Python programming"
sub_case_sensitive = "python"
index_case_sensitive = text5.find(sub_case_sensitive)
print(f"Original: '{text5}'")
print(f"Find '{sub_case_sensitive}' (case-sensitive): {index_case_sensitive}\n") # Expected: -1

# To perform a case-insensitive search, convert both the string and substring to the same case first:
text5_lower = text5.lower()
sub_case_sensitive_lower = sub_case_sensitive.lower()
index_case_insensitive = text5_lower.find(sub_case_sensitive_lower)
print(f"Case-insensitive find of '{sub_case_sensitive}' in '{text5}': {index_case_insensitive}\n") # Expected: 0


print("--- 5. Return Value and Immutability ---")

# The `find()` method returns an integer (the index or -1).
# It does not modify the original string, as strings in Python are immutable.

my_string = "search_this_string"
print(f"Original string variable: '{my_string}'")

pos = my_string.find("this")
print(f"Position of 'this': {pos}")
print(f"Original string variable after call: '{my_string}'\n") # Original remains unchanged


print("--- 6. Error Handling ---")

# The `substring` argument must be a string.
try:
    "abc".find(123)
except TypeError as e:
    print(f"TypeError caught (substring not string): {e}\n")

# `start` and `end` must be integers.
try:
    "abc".find("a", "one")
except TypeError as e:
    print(f"TypeError caught (start not int): {e}\n")


print("--- 7. `find()` vs. `index()` ---")

# Both `find()` and `index()` search for a substring and return its lowest index.
# The key difference is how they handle cases where the substring is not found:
# - `find()` returns -1.
# - `index()` raises a `ValueError`.

text_for_comparison = "apple banana"
sub_exists = "banana"
sub_not_exists = "orange"

# Using find()
find_result_exists = text_for_comparison.find(sub_exists)
find_result_not_exists = text_for_comparison.find(sub_not_exists)
print(f"Using find():")
print(f"  '{sub_exists}' found at index: {find_result_exists}") # Expected: 6
print(f"  '{sub_not_exists}' found at index: {find_result_not_exists}\n") # Expected: -1

# Using index()
index_result_exists = text_for_comparison.index(sub_exists)
print(f"Using index():")
print(f"  '{sub_exists}' found at index: {index_result_exists}") # Expected: 6
try:
    index_result_not_exists = text_for_comparison.index(sub_not_exists)
    print(f"  '{sub_not_exists}' found at index: {index_result_not_exists}")
except ValueError as e:
    print(f"  ValueError caught for '{sub_not_exists}' (not found): {e}\n")

# Choose `find()` when you want to handle the "not found" case without an exception.
# Choose `index()` when you expect the substring to always be present, and its absence
# indicates an error condition that should stop execution or be explicitly handled.


print("--- 8. Practical Use Cases ---")

# 8.1. Parsing strings by finding delimiters
log_entry = "2025-07-06 14:30:15 INFO: User logged in from IP 192.168.1.100"
colon_index = log_entry.find(':')
if colon_index != -1:
    log_level = log_entry[colon_index + 2:].split(' ')[0]
    print(f"Log Level: {log_level}\n") # Expected: INFO

# 8.2. Checking for presence of keywords
document = "This document discusses Python programming and data science."
keyword1 = "Python"
keyword2 = "Java"

if document.find(keyword1) != -1:
    print(f"'{keyword1}' found in document.")
else:
    print(f"'{keyword1}' not found in document.")

if document.find(keyword2) == -1:
    print(f"'{keyword2}' not found in document.\n")
else:
    print(f"'{keyword2}' found in document.\n")

# 8.3. Extracting parts of a string based on substring position
full_url = "https://www.example.com/products/item123?category=electronics"
query_start = full_url.find("?")
if query_start != -1:
    base_url = full_url[:query_start]
    query_string = full_url[query_start+1:]
    print(f"Base URL: {base_url}")
    print(f"Query String: {query_string}\n")

# --- Python String expandtabs() Method: All About in Code ---

# The `expandtabs()` method is a built-in string method in Python.
# It returns a copy of the string where all tab characters ('\t') are
# replaced by one or more spaces, extending the tabs to the next tab stop.

# Syntax: string.expandtabs(tabsize=8)
# - `tabsize`: (Optional) An integer specifying the number of spaces each
#              tab stop represents. Defaults to 8 if not specified.
#              Must be a non-negative integer.

print("--- 1. Basic Usage: Default `tabsize` (8) ---")

# By default, a tab character '\t' expands to enough spaces to reach
# the next multiple of 8 column positions.

text1 = "Name:\tJohn Doe\nAge:\t30"
expanded_text1 = text1.expandtabs() # tabsize defaults to 8
print(f"Original:\n'{text1}'")
print(f"expandtabs() (default tabsize=8):\n'{expanded_text1}'\n")
# Expected:
# 'Name:   John Doe' (Name: is 5 chars, needs 3 spaces to reach col 8)
# 'Age:    30'       (Age: is 4 chars, needs 4 spaces to reach col 8)

text2 = "A\tB\tC"
expanded_text2 = text2.expandtabs()
print(f"Original:\n'{text2}'")
print(f"expandtabs() (default tabsize=8):\n'{expanded_text2}'\n")
# Expected:
# 'A       B       C' (A needs 7 spaces, B needs 7 spaces)


print("--- 2. Specifying a Custom `tabsize` ---")

# You can control the number of spaces per tab stop by passing the `tabsize` argument.

text3 = "Col1\tCol2\tCol3"

# 2.1. tabsize = 4
expanded_text3_4 = text3.expandtabs(tabsize=4)
print(f"Original:\n'{text3}'")
print(f"expandtabs(tabsize=4):\n'{expanded_text3_4}'\n")
# Expected:
# 'Col1    Col2    Col3' (Col1 is 4 chars, needs 0 spaces to reach col 4, then 4 to reach col 8, etc.)
# If the text up to the tab is already a multiple of tabsize, the tab expands to `tabsize` spaces.
# Here, 'Col1' (length 4) reaches the first tab stop (column 4), so the '\t' adds 4 spaces.
# 'Col2' (length 4) then starts at column 8. It needs 0 spaces to reach col 8, so the '\t' adds 4 spaces.

# Let's clarify with an example where `len % tabsize != 0`
text4 = "ItemX\tPrice\tQty" # ItemX is 5 chars
expanded_text4_4 = text4.expandtabs(tabsize=4)
print(f"Original:\n'{text4}'")
print(f"expandtabs(tabsize=4):\n'{expanded_text4_4}'\n")
# Expected:
# 'ItemX   Price   Qty'
# ItemX (len 5). Next tab stop after col 5 for tabsize 4 is col 8. Needs 3 spaces.
# Price (len 5). Starts at col 8+3=11. Next tab stop after col 16 for tabsize 4 is col 16. Needs 5 spaces. (16-11)
# No, this is incorrect. It's calculated based on the *current column position*.
# Current column for 'ItemX' is 0. 'ItemX' moves it to column 5.
# `spaces_to_add = tabsize - (current_column_position % tabsize)`
# First tab: Current column is 5. tabsize is 4. `4 - (5 % 4)` = `4 - 1` = 3 spaces.
# So "ItemX" + 3 spaces. This gets us to column 8.
# Second tab: Current column is 8 (after "ItemX" + 3 spaces + "Price").
# "Price" (len 5) starts at col 8, moves to col 13.
# `4 - (13 % 4)` = `4 - 1` = 3 spaces.
# So this would be: 'ItemX   Price   Qty'

text5 = "Line1:\tTabbed Text\tMore Tabs"
print(f"Original:\n'{text5}'")
print(f"expandtabs(tabsize=10):\n'{text5.expandtabs(tabsize=10)}'\n")
# Line1: (6 chars). Next tab stop (multiple of 10) after col 6 is col 10. Needs 4 spaces.
# Tabbed Text (11 chars). Starts at col 10. Moves to col 21. Next tab stop (multiple of 10) after col 21 is col 30. Needs 9 spaces.

print("--- 3. Behavior with No Tab Characters ('\\t') ---")

# If the string does not contain any tab characters, `expandtabs()` returns
# a copy of the original string unchanged.

text6 = "No tabs here."
expanded_text6 = text6.expandtabs()
print(f"Original: '{text6}'")
print(f"expandtabs(): '{expanded_text6}'")
print(f"Is original unchanged? {expanded_text6 == text6}\n")


print("--- 4. Behavior with Empty String ---")

# An empty string will return an empty string, regardless of `tabsize`.

empty_string = ""
expanded_empty = empty_string.expandtabs(tabsize=5)
print(f"Original: '{empty_string}'")
print(f"expandtabs(tabsize=5): '{expanded_empty}'")
print(f"Is empty string == '': {expanded_empty == ''}\n")


print("--- 5. Return Value and Immutability ---")

# String methods in Python always return a *new* string.
# They do not modify the original string because strings are immutable.

my_string = "colA\tcolB"
print(f"Original string variable: '{my_string}'")

new_string = my_string.expandtabs(tabsize=4)
print(f"New string (after expandtabs()): '{new_string}'")
print(f"Original string variable after call: '{my_string}'\n") # Original remains unchanged

# To use the expanded version, you must assign the result back to a variable.
my_string = my_string.expandtabs()
print(f"Original string variable after re-assignment: '{my_string}'\n")


print("--- 6. Error Handling ---")

# The `tabsize` argument must be an integer and non-negative.
try:
    "test\t".expandtabs("invalid")
except TypeError as e:
    print(f"TypeError caught (tabsize not int): {e}\n")

try:
    "test\t".expandtabs(tabsize=-1)
except ValueError as e:
    print(f"ValueError caught (tabsize negative): {e}\n")


print("--- 7. Practical Use Cases ---")

# 7.1. Formatting text for display in fixed-width environments (e.g., terminal)
# This is often used when dealing with data that was originally aligned using tabs,
# but needs to be displayed or processed with consistent spacing.

data_lines = [
    "Name\tAge\tCity",
    "Alice\t30\tNew York",
    "Bob\t25\tLondon",
    "Charlie\t40\tSan Francisco"
]

print("--- Data formatted with expandtabs(8) ---")
for line in data_lines:
    print(line.expandtabs(tabsize=8))
print("")

print("--- Data formatted with expandtabs(12) ---")
for line in data_lines:
    print(line.expandtabs(tabsize=12))
print("")

# 7.2. Processing files that use tabs for alignment
# If you read a file where columns are separated by tabs, and you want to
# convert it to consistent space-separated columns, expandtabs can be useful.
# However, for structured data like CSV/TSV, the `csv` module is generally preferred.

# Example where `expandtabs` helps visually:
code_snippet_with_tabs = """def my_function(arg1):
\tresult = arg1 * 2
\tif result > 10:
\t\tprint("Large result")
\treturn result
"""
print("--- Code snippet with tabs (default editor rendering) ---")
print(code_snippet_with_tabs)

print("--- Code snippet with tabs expanded (tabsize=4) ---")
print(code_snippet_with_tabs.expandtabs(tabsize=4))