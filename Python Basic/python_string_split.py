# --- Python String Split Methods: All About in Code ---

# Python provides several methods to split a string into a list of substrings.
# The most common are `split()`, `rsplit()`, `splitlines()`.

# --- 1. The `split()` Method ---

# Syntax: string.split(sep=None, maxsplit=-1)
# - sep (optional): The delimiter string. The string will be split by this separator.
#                  If `sep` is None (default), any whitespace is used as a delimiter,
#                  and empty strings are removed from the result.
# - maxsplit (optional): The maximum number of splits to perform.
#                        If specified, the list will have at most `maxsplit + 1` elements.
#                        If `maxsplit` is -1 (default), no limit is set (all occurrences).

print("--- 1. The `split()` Method ---")

# 1.1. Basic `split()` with default whitespace delimiter (sep=None)
# - Splits by any sequence of whitespace (spaces, tabs, newlines).
# - Consecutive whitespace characters are treated as a single delimiter.
# - Leading/trailing whitespace results in no empty strings at the beginning/end.
text_default = "  Hello   world\nThis is a test.\t123  "
words_default = text_default.split()
print(f"Original: '{text_default}'")
print(f"split() (default): {words_default}\n")


# 1.2. Splitting by a specific single character delimiter
# - The delimiter character is not included in the resulting list.
# - Consecutive delimiters *will* result in empty strings.
# - Leading/trailing delimiters *will* result in empty strings at the beginning/end.
csv_line = "apple,banana,,orange,grape"
items_comma = csv_line.split(',')
print(f"Original: '{csv_line}'")
print(f"split(',') : {items_comma}\n")

ip_address = "192.168.1.100"
octets = ip_address.split('.')
print(f"Original: '{ip_address}'")
print(f"split('.') : {octets}\n")


# 1.3. Splitting by a specific string delimiter (more than one character)
sentence = "Python is awesome. Python is versatile. Python is easy."
parts_python = sentence.split("Python")
print(f"Original: '{sentence}'")
print(f"split('Python') : {parts_python}\n") # Notice empty string at start if it begins with delimiter


# 1.4. Using `maxsplit` to limit the number of splits
path_str = "/home/user/documents/report.txt"

# Split only by the first '/'
first_split = path_str.split('/', 1)
print(f"Original: '{path_str}'")
print(f"split('/', 1) : {first_split}")

# Split by the first two '/'
two_splits = path_str.split('/', 2)
print(f"split('/', 2) : {two_splits}\n")

# If maxsplit is -1 (default), all occurrences are split
all_splits = path_str.split('/')
print(f"split('/') (all): {all_splits}") # Empty string at beginning due to leading '/'
print("Note: default split() with no arguments handles leading/trailing/multiple whitespace better.\n")


# --- 2. The `rsplit()` Method ---

# Syntax: string.rsplit(sep=None, maxsplit=-1)
# - Identical to `split()`, but splits from the RIGHT side of the string.
# - Useful when you want to split a limited number of times from the end.

print("--- 2. The `rsplit()` Method ---")

filename = "archive.tar.gz"
# Get the filename and extension (splitting from the right once)
name_ext = filename.rsplit('.', 1)
print(f"Original: '{filename}'")
print(f"rsplit('.', 1) : {name_ext}\n")

long_log_entry = "INFO: User login success: user_id=123: timestamp=2025-07-04"
# Get the last two parts of the log
last_two_parts = long_log_entry.rsplit(':', 2)
print(f"Original: '{long_log_entry}'")
print(f"rsplit(':', 2) : {last_two_parts}\n")

# rsplit() with default arguments behaves the same as split() with default arguments
text_default_rsplit = "  Hello   world\nThis is a test.\t123  "
words_default_rsplit = text_default_rsplit.rsplit() # Same as .split()
print(f"rsplit() (default, same as split()): {words_default_rsplit}\n")


# --- 3. The `splitlines()` Method ---

# Syntax: string.splitlines(keepends=False)
# - Splits the string at line breaks.
# - Line breaks include '\n', '\r', '\r\n', and Unicode line terminators.
# - Returns a list of lines.
# - keepends (optional): If True, line breaks are included in the resulting list elements.
#                        Default is False.

print("--- 3. The `splitlines()` Method ---")

multi_line_string = "Line 1\nLine 2\rLine 3\r\nLine 4\n"

# 3.1. Basic `splitlines()` (keepends=False)
lines_no_ends = multi_line_string.splitlines()
print(f"Original:\n'{multi_line_string}'")
print(f"splitlines() (no ends): {lines_no_ends}\n")

# 3.2. `splitlines(keepends=True)`
lines_with_ends = multi_line_string.splitlines(keepends=True)
print(f"splitlines(keepends=True): {lines_with_ends}\n")

# Empty strings for empty lines
empty_line_string = "Line A\n\nLine B"
lines_empty = empty_line_string.splitlines()
print(f"Original:\n'{empty_line_string}'")
print(f"splitlines() with empty line: {lines_empty}\n")


# --- 4. Common Use Cases and Considerations ---

print("--- 4. Common Use Cases and Considerations ---")

# 4.1. Parsing CSV-like data (when not using `csv` module)
# Use `split(',')` if you are sure there are no commas within fields.
# For robust CSV parsing, always prefer the `csv` module.
data_row = "Name,Age,City"
header = data_row.split(',')
print(f"CSV header: {header}")


# 4.2. Tokenizing sentences into words (simple cases)
sentence_to_tokenize = "Python is an amazing language for data science."
words_tokenized = sentence_to_tokenize.split() # Uses default whitespace
print(f"Words from sentence: {words_tokenized}")


# 4.3. Splitting and then processing/cleaning parts
dirty_input = "  item1   ,item2 , item3  "
cleaned_items = [item.strip() for item in dirty_input.split(',')]
print(f"Cleaned items: {cleaned_items}\n")


# 4.4. What if the delimiter is at the start/end?
string_start_end = ",start,middle,end,"
parts_start_end = string_start_end.split(',')
print(f"String with start/end delimiter: '{string_start_end}'")
print(f"Split result: {parts_start_end}") # Note the empty strings


# 4.5. Handling strings that do not contain the delimiter
no_delimiter_string = "NoCommaHere"
result_no_delimiter = no_delimiter_string.split(',')
print(f"String with no delimiter: '{no_delimiter_string}'")
print(f"Split result: {result_no_delimiter}\n") # Returns a list with the original string as the only element


# --- 5. Combining `split()` with `strip()` and `join()` ---

print("--- 5. Combining `split()` with `strip()` and `join()` ---")

# Often, after splitting, you'll want to clean up whitespace around the resulting parts.
messy_data = "  apple  ,banana , orange,grape "
# Split, then strip each part, then join back with a clean comma and space
cleaned_and_joined = ", ".join([item.strip() for item in messy_data.split(',')])
print(f"Original messy data: '{messy_data}'")
print(f"Cleaned and rejoined: '{cleaned_and_joined}'\n")



# --- Python String rsplit() Method: All About in Code ---

# The `rsplit()` method is a built-in string method in Python.
# It splits a string into a list of substrings using a specified delimiter,
# starting the split from the RIGHT side of the string.
# It is very similar to `split()`, but the direction of splitting changes
# how `maxsplit` behaves.

# Syntax: string.rsplit(sep=None, maxsplit=-1)
# - sep (optional): The delimiter string. The string will be split by this separator.
#                  If `sep` is None (default), any whitespace is used as a delimiter,
#                  and empty strings are removed from the result.
# - maxsplit (optional): The maximum number of splits to perform.
#                        If specified, the list will have at most `maxsplit + 1` elements.
#                        The splitting will occur from the rightmost occurrences of the separator.
#                        If `maxsplit` is -1 (default), no limit is set (all occurrences are split).

print("--- 1. Basic Usage: rsplit() with Default Whitespace Delimiter ---")

# 1.1. Default `rsplit()` (sep=None, maxsplit=-1)
# - Splits by any sequence of whitespace (spaces, tabs, newlines).
# - Consecutive whitespace characters are treated as a single delimiter.
# - Leading/trailing whitespace results in no empty strings at the beginning/end.
# - When `maxsplit` is -1 (default), `rsplit()` behaves identically to `split()`.
text_default_rsplit = "  Hello   world\nThis is a test.\t123  "
words_default_rsplit = text_default_rsplit.rsplit()
print(f"Original: '{text_default_rsplit}'")
print(f"rsplit() (default): {words_default_rsplit}\n")


print("--- 2. rsplit() with a Specific Delimiter (No maxsplit) ---")

# 2.1. Splitting by a specific single character delimiter (all occurrences)
# - The delimiter character is not included in the resulting list.
# - Consecutive delimiters *will* result in empty strings.
# - Leading/trailing delimiters *will* result in empty strings at the beginning/end.
# - When `maxsplit` is -1, `rsplit()` behaves identically to `split()` here as well.
data_string = "value1,value2,,value3,value4"
items_comma = data_string.rsplit(',') # Equivalent to data_string.split(',') here
print(f"Original: '{data_string}'")
print(f"rsplit(',') : {items_comma}\n")

# 2.2. Splitting by a specific string delimiter (all occurrences)
sentence_multi_sep = "applepie_orangejuice_strawberryshake"
parts_underscore = sentence_multi_sep.rsplit('_') # Equivalent to split('_') here
print(f"Original: '{sentence_multi_sep}'")
print(f"rsplit('_') : {parts_underscore}\n")


print("--- 3. The Key Difference: Using `maxsplit` with rsplit() ---")

# This is where `rsplit()` truly differentiates itself from `split()`.
# `maxsplit` tells `rsplit` to perform at most `maxsplit` operations,
# starting from the rightmost delimiter occurrences.

# Example: Parsing a filename to get the base name and last extension
filename = "document.report.v2.pdf"

# Using rsplit('.', 1) to get only the last extension
base_name, extension = filename.rsplit('.', 1)
print(f"Original filename: '{filename}'")
print(f"rsplit('.', 1) -> Base name: '{base_name}', Extension: '{extension}'\n")

# Compare with split('.', 1) which would give 'document' and 'report.v2.pdf'
base_name_split, rest_split = filename.split('.', 1)
print(f"split('.', 1) -> Base name: '{base_name_split}', Rest: '{rest_split}'\n")


# Example: Getting the last few components of a path
complex_path = "/usr/local/bin/python/script.py"

# Get the last two components (e.g., the script name and its parent directory)
last_two_components = complex_path.rsplit('/', 2)
print(f"Original path: '{complex_path}'")
print(f"rsplit('/', 2) : {last_two_components}")
# [('/usr/local/bin', 'python', 'script.py')]

# Get the last component (filename)
last_component = complex_path.rsplit('/', 1)
print(f"rsplit('/', 1) : {last_component}\n")


print("--- 4. What Happens if 'sep' is Not Found? ---")

# If the separator is not found in the string, `rsplit()` returns a list
# containing the original string as the only element.

no_sep_string = "HelloWorld"
result_no_sep = no_sep_string.rsplit('-')
print(f"Original: '{no_sep_string}'")
print(f"rsplit('-') (separator not found): {result_no_sep}\n")

# This is consistent whether `maxsplit` is specified or not, as no splits can occur.
result_no_sep_maxsplit = no_sep_string.rsplit('-', 5)
print(f"rsplit('-', 5) (separator not found): {result_no_sep_maxsplit}\n")


print("--- 5. Handling Leading/Trailing/Consecutive Delimiters (with specified `sep`) ---")

# When `sep` is explicitly provided, `rsplit()` treats consecutive delimiters
# and leading/trailing delimiters as producing empty strings.

consecutive_sep = "::item1::item2::"
parts_consecutive = consecutive_sep.rsplit(':', 3) # Split from right, 3 times
print(f"Original: '{consecutive_sep}'")
print(f"rsplit(':', 3) : {parts_consecutive}") # Note the empty strings from leading/consecutive delimiters

parts_all = consecutive_sep.rsplit(':') # All splits (behaves like split(':'))
print(f"rsplit(':') (all): {parts_all}\n")


print("--- 6. Chaining rsplit() or Combining with other methods ---")

# You can chain `rsplit()` calls or combine it with `strip()` or `join()`.

# Example: Get the base filename without extension and then replace parts
full_filename = "document_old.final.txt"
base_filename = full_filename.rsplit('.', 1)[0] # Get the part before the last dot
cleaned_base = base_filename.replace('_old', '')
print(f"Original filename: '{full_filename}'")
print(f"Cleaned base name: '{cleaned_base}'\n")

# Example: Split by space from right, then remove leading/trailing spaces from result
sentence_with_padding = "  One Two Three Four  "
# Get the last two words (from right)
parts_from_right = sentence_with_padding.rsplit(' ', 2)
# Strip each resulting part (if the delimiter was a space, there might be empty strings or leading/trailing spaces)
stripped_parts = [p.strip() for p in parts_from_right if p.strip()] # Remove empty strings from list
print(f"Original padded sentence: '{sentence_with_padding}'")
print(f"rsplit(' ', 2) then strip: {stripped_parts}\n")


print("--- 7. Performance Note ---")

# Similar to `split()`, `rsplit()` is implemented in C and is highly optimized.
# For most common use cases, its performance is excellent.
# When working with extremely large strings and many operations, always consider
# whether a more specialized approach (e.g., regex if patterns are complex, or
# processing data in chunks if reading from a file) might be more appropriate.


# --- Python String splitlines() Method: All About in Code ---

# The `splitlines()` method is a built-in string method in Python.
# It splits the string into a list of lines, breaking at various line boundaries.
# This method is specifically designed for handling different types of line endings.

# Syntax: string.splitlines(keepends=False)
# - keepends (optional): A boolean value.
#                        If True, the line breaks are included at the end of each line
#                        in the resulting list.
#                        If False (default), the line breaks are not included.

print("--- 1. Basic Usage: splitlines() (keepends=False by Default) ---")

# 1.1. Common newline characters: \n (LF - Line Feed, Unix/Linux/macOS)
text_lf = "First line.\nSecond line.\nThird line."
lines_lf = text_lf.splitlines()
print(f"Original (LF):\n'{text_lf}'")
print(f"splitlines(): {lines_lf}\n")

# 1.2. Common newline characters: \r (CR - Carriage Return, old Mac)
text_cr = "Line A.\rLine B.\rLine C."
lines_cr = text_cr.splitlines()
print(f"Original (CR):\n'{text_cr}'")
print(f"splitlines(): {lines_cr}\n")

# 1.3. Common newline characters: \r\n (CRLF - Carriage Return Line Feed, Windows)
text_crlf = "Statement 1.\r\nStatement 2.\r\nStatement 3."
lines_crlf = text_crlf.splitlines()
print(f"Original (CRLF):\n'{text_crlf}'")
print(f"splitlines(): {lines_crlf}\n")

# 1.4. Mixed newline characters
text_mixed = "Mixed line 1\nMixed line 2\r\nMixed line 3\rMixed line 4"
lines_mixed = text_mixed.splitlines()
print(f"Original (Mixed):\n'{text_mixed}'")
print(f"splitlines(): {lines_mixed}\n")


print("--- 2. Using `keepends=True` ---")

# When `keepends=True`, the line termination characters are preserved
# at the end of each corresponding element in the list.

# 2.1. LF with keepends=True
text_lf_keep = "Line one.\nLine two."
lines_lf_keep = text_lf_keep.splitlines(keepends=True)
print(f"Original (LF):\n'{text_lf_keep}'")
print(f"splitlines(keepends=True): {lines_lf_keep}\n")

# 2.2. CRLF with keepends=True
text_crlf_keep = "Entry 1.\r\nEntry 2.\r\n"
lines_crlf_keep = text_crlf_keep.splitlines(keepends=True)
print(f"Original (CRLF):\n'{text_crlf_keep}'")
print(f"splitlines(keepends=True): {lines_crlf_keep}\n")


print("--- 3. Handling Empty Lines ---")

# 3.1. Empty lines within the string
text_empty_lines = "Data A\n\nData B\nData C"
lines_empty_within = text_empty_lines.splitlines()
print(f"Original (empty lines within):\n'{text_empty_lines}'")
print(f"splitlines(): {lines_empty_within}\n") # An empty string represents the empty line

# 3.2. String starting or ending with a newline
text_start_end_newline = "\nFirst line\nSecond line\n"
lines_start_end_newline = text_start_end_newline.splitlines()
print(f"Original (start/end newline):\n'{text_start_end_newline}'")
print(f"splitlines(): {lines_start_end_newline}\n") # Note the empty string at the beginning/end


print("--- 4. What Happens if No Line Breaks are Present? ---")

# If the string does not contain any recognized line breaks,
# `splitlines()` returns a list containing the original string as the only element.

single_line_text = "This is a single line of text."
lines_single = single_line_text.splitlines()
print(f"Original (no line breaks): '{single_line_text}'")
print(f"splitlines(): {lines_single}\n")

# This also applies if the string is empty
empty_string = ""
lines_empty_str = empty_string.splitlines()
print(f"Original (empty string): '{empty_string}'")
print(f"splitlines(): {lines_empty_str}\n") # Returns an empty list


print("--- 5. Differences from `split('\n')` ---")

# `splitlines()` is more robust for handling various newline characters
# and typically handles trailing/leading newlines and empty lines more naturally
# for line-by-line processing.

text_compare = "First\r\nSecond\nThird\r"

# Using splitlines()
lines_splitlines = text_compare.splitlines()
print(f"Original:\n'{text_compare}'")
print(f"splitlines(): {lines_splitlines}")

# Using split('\n') - note how \r is retained in "Second\r"
lines_split_n = text_compare.split('\n')
print(f"split('\\n') : {lines_split_n}\n")

# If `split('\n')` is used with `strip()`
lines_split_n_stripped = [line.strip() for line in text_compare.split('\n')]
print(f"split('\\n') and then strip(): {lines_split_n_stripped}\n")


print("--- 6. Handling Other Unicode Line Terminators ---")

# `splitlines()` also recognizes other Unicode line terminators like:
# - `\u000B` (Vertical Tab)
# - `\u000C` (Form Feed)
# - `\u001C` (File Separator)
# - `\u001D` (Group Separator)
# - `\u001E` (Record Separator)
# - `\u0085` (Next Line - NEL)
# - `\u2028` (Line Separator)
# - `\u2029` (Paragraph Separator)

unicode_newlines = "Line One\u2028Line Two\u0085Line Three\u000BLine Four"
lines_unicode = unicode_newlines.splitlines()
print(f"Original (Unicode Newlines):\n'{unicode_newlines}'")
print(f"splitlines(): {lines_unicode}\n")


print("--- 7. Practical Use Case: Processing Text Files ---")

# When reading text files, especially those created on different operating systems,
# `splitlines()` is often the most reliable way to break content into logical lines.

# Simulate reading a file
file_content = """Header Line 1
Header Line 2
Data Row 1,Value A
Data Row 2,Value B
Data Row 3,Value C\r\nFooter\n"""

# Process lines, skipping headers or footers
all_file_lines = file_content.splitlines()
print(f"All lines from simulated file:\n{all_file_lines}")

# Example: Extracting data rows assuming first two are headers and last is footer
data_rows_only = all_file_lines[2:-1] # From index 2 up to the second-to-last
print(f"Data rows only: {data_rows_only}")

# You can then further split each data row
parsed_data = [row.split(',') for row in data_rows_only]
print(f"Parsed data: {parsed_data}\n")