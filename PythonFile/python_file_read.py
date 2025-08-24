# --- Python File Reading: All About in Code ---

# Reading files is a fundamental operation in programming, allowing your
# Python scripts to access and process data stored in external files.

# The primary way to read a file involves opening it in a read mode ('r', 'rb', 'r+')
# and then using methods like .read(), .readline(), or iterating directly over
# the file object.

import os

# --- 0. Setting up for Demo (Creating Dummy Files) ---

print("--- 0. Setting up for Demo (Creating Dummy Files) ---")

# Create a simple text file
try:
    with open("my_text_file.txt", "w", encoding="utf-8") as f:
        f.write("Line 1: Hello Python!\n")
        f.write("Line 2: This is the second line.\n")
        f.write("Line 3: The quick brown fox jumps over the lazy dog.\n")
        f.write("Line 4: End of text file.") # No newline at the very end
    print("Created 'my_text_file.txt'.")
except IOError as e:
    print(f"Error creating my_text_file.txt: {e}")

# Create a larger text file for demonstrating line-by-line reading
try:
    with open("large_text_file.txt", "w", encoding="utf-8") as f:
        for i in range(1, 101):
            f.write(f"This is line number {i} of 100.\n")
    print("Created 'large_text_file.txt'.")
except IOError as e:
    print(f"Error creating large_text_file.txt: {e}")

# Create a binary file
try:
    with open("my_binary_file.bin", "wb") as f:
        f.write(b'\xDE\xAD\xBE\xEF\x01\x02\x03\x04')
        f.write("Binary data example.".encode('utf-8'))
    print("Created 'my_binary_file.bin'.")
except IOError as e:
    print(f"Error creating my_binary_file.bin: {e}")


# --- 1. Opening Files for Reading (`open()` function) ---

print("\n--- 1. Opening Files for Reading (`open()` function) ---")

# `open()` function: `open(file, mode='r', encoding=None, errors=None)`
# - `file`: The path to the file you want to open.
# - `mode`: Specifies how the file is opened.
#    - 'r': Read mode (default). Opens for reading. File pointer at the beginning.
#    - 'rb': Read binary mode. Opens for reading in binary format.
#    - 'r+': Read and Write mode. Opens for both reading and writing. File pointer at the beginning.
# - `encoding`: For text mode, specifies the character encoding (e.g., 'utf-8', 'latin-1').
#               Crucial for correct interpretation of characters.
#               Not used for binary modes ('b').
# - `errors`: How to handle encoding/decoding errors (e.g., 'strict', 'ignore', 'replace').

# It's best practice to use a `with` statement. This ensures the file is
# automatically closed, even if errors occur.

# Example 1.1: Opening in text read mode ('r')
try:
    with open("my_text_file.txt", "r", encoding="utf-8") as file_object:
        print(f"Successfully opened 'my_text_file.txt' in 'r' mode. File object: {file_object}")
        # We'll read content in later sections
except FileNotFoundError:
    print("Error: 'my_text_file.txt' not found.")
except IOError as e:
    print(f"Error opening 'my_text_file.txt': {e}")


# Example 1.2: Opening in binary read mode ('rb')
try:
    with open("my_binary_file.bin", "rb") as bin_file_object:
        print(f"Successfully opened 'my_binary_file.bin' in 'rb' mode. File object: {bin_file_object}")
except FileNotFoundError:
    print("Error: 'my_binary_file.bin' not found.")
except IOError as e:
    print(f"Error opening 'my_binary_file.bin': {e}")


# --- 2. Reading Entire File Content (`.read()`) ---

print("\n--- 2. Reading Entire File Content (`.read()`) ---")

# `file_object.read(size=-1)`:
# - Reads the entire content of the file.
# - If `size` is specified, reads up to `size` characters (text mode) or bytes (binary mode).
# - Returns a single string (text mode) or bytes object (binary mode).

# Example 2.1: Reading entire text file
try:
    with open("my_text_file.txt", "r", encoding="utf-8") as file:
        full_content = file.read()
        print(f"\nContent of 'my_text_file.txt' (using .read()):\n{full_content}")
        print(f"Type of content: {type(full_content)}\n")
except FileNotFoundError:
    print("Error: 'my_text_file.txt' not found for .read().")
except IOError as e:
    print(f"Error reading 'my_text_file.txt' with .read(): {e}")


# Example 2.2: Reading a specific number of characters from text file
try:
    with open("my_text_file.txt", "r", encoding="utf-8") as file:
        first_10_chars = file.read(10)
        print(f"First 10 characters: '{first_10_chars}'")
        next_5_chars = file.read(5) # Reads from where the cursor left off
        print(f"Next 5 characters: '{next_5_chars}'\n")
except FileNotFoundError:
    print("Error: 'my_text_file.txt' not found for partial .read().")


# Example 2.3: Reading entire binary file
try:
    with open("my_binary_file.bin", "rb") as file:
        full_binary_content = file.read()
        print(f"Content of 'my_binary_file.bin' (using .read()): {full_binary_content}")
        print(f"Type of content: {type(full_binary_content)}")
        print(f"Length of binary content: {len(full_binary_content)} bytes\n")
except FileNotFoundError:
    print("Error: 'my_binary_file.bin' not found for .read().")
except IOError as e:
    print(f"Error reading 'my_binary_file.bin' with .read(): {e}")


# --- 3. Reading Line by Line (`.readline()`) ---

print("\n--- 3. Reading Line by Line (`.readline()`) ---")

# `file_object.readline()`:
# - Reads a single line from the file, including the newline character.
# - Returns an empty string `''` when the end of the file is reached.
# - Memory efficient for large files as it reads one line at a time.

try:
    with open("my_text_file.txt", "r", encoding="utf-8") as file:
        print(f"Reading '{my_text_file.txt}' using .readline():")
        line1 = file.readline()
        print(f"  Line 1 (raw): {repr(line1)}") # repr() shows actual newlines
        line2 = file.readline()
        print(f"  Line 2 (raw): {repr(line2)}")
        line3 = file.readline()
        print(f"  Line 3 (raw): {repr(line3)}")
        line4 = file.readline()
        print(f"  Line 4 (raw): {repr(line4)}") # This line does not have '\n' in the original file
        line5 = file.readline() # Should be empty string at EOF
        print(f"  Line 5 (at EOF): {repr(line5)}")
except FileNotFoundError:
    print("Error: 'my_text_file.txt' not found for .readline().")
except IOError as e:
    print(f"Error reading 'my_text_file.txt' with .readline(): {e}")


# --- 4. Reading All Lines into a List (`.readlines()`) ---

print("\n--- 4. Reading All Lines into a List (`.readlines()`) ---")

# `file_object.readlines()`:
# - Reads all lines from the file and returns them as a list of strings.
# - Each string includes the newline character.
# - Can consume significant memory for very large files.

try:
    with open("my_text_file.txt", "r", encoding="utf-8") as file:
        all_lines_list = file.readlines()

    print(f"Content of 'my_text_file.txt' (using .readlines()):")
    for i, line in enumerate(all_lines_list):
        print(f"  Line {i+1} (raw): {repr(line)}")
    print(f"Type of list: {type(all_lines_list)}")
    print(f"Number of elements in list: {len(all_lines_list)}\n")
except FileNotFoundError:
    print("Error: 'my_text_file.txt' not found for .readlines().")
except IOError as e:
    print(f"Error reading 'my_text_file.txt' with .readlines(): {e}")


# --- 5. Iterating Directly Over File Object (Most Pythonic & Memory Efficient) ---

print("\n--- 5. Iterating Directly Over File Object (Most Pythonic & Memory Efficient) ---")

# This is the preferred way to read large files line by line, as it's memory-efficient
# (it's an iterator, so lines are read one at a time as needed) and clean.
# Each `line` in the loop includes the newline character.

try:
    print(f"Reading '{large_text_file.txt}' by iterating directly (showing first 5 lines):")
    line_count = 0
    with open("large_text_file.txt", "r", encoding="utf-8") as file:
        for line in file: # 'line' includes the newline character
            if line_count < 5:
                print(f"  Line {line_count+1} (stripped): '{line.strip()}'")
            line_count += 1
    print(f"... and {line_count - 5} more lines.")
    print(f"Total lines processed: {line_count}\n")
except FileNotFoundError:
    print("Error: 'large_text_file.txt' not found for iteration.")
except IOError as e:
    print(f"Error iterating 'large_text_file.txt': {e}")


# --- 6. Reading from `r+` (Read and Write) Mode ---

print("\n--- 6. Reading from `r+` (Read and Write) Mode ---")

# `r+` mode:
# - Opens for both reading and writing.
# - File pointer is at the beginning.
# - Does NOT truncate the file (unlike 'w+').
# - If the file does not exist, it raises `FileNotFoundError`.

temp_rplus_file = "temp_rplus.txt"
try:
    with open(temp_rplus_file, "w") as f: # First, create it with some content
        f.write("Original content for r+.\nSecond line.")

    with open(temp_rplus_file, "r+", encoding="utf-8") as file:
        initial_content = file.read()
        print(f"Initial content in '{temp_rplus_file}' (r+ mode): '{initial_content.strip()}'")

        # Now, let's write something. Writing will overwrite existing content from current position.
        file.seek(0) # Move cursor back to beginning to overwrite first part
        file.write("NEW".ljust(len("Original content"))) # Overwrite exactly the same length
        file.seek(0) # Seek back to beginning to read updated content
        updated_content = file.read()
        print(f"Content after writing 'NEW' (r+ mode): '{updated_content.strip()}'")
except FileNotFoundError:
    print(f"Error: '{temp_rplus_file}' not found.")
except IOError as e:
    print(f"Error with 'r+' mode: {e}")


# --- 7. Error Handling During Reading ---

print("\n--- 7. Error Handling During Reading ---")

# Always use `try-except` blocks to handle potential errors.

non_existent_file = "definitely_not_here.txt"

try:
    with open(non_existent_file, "r") as file:
        content = file.read()
        print(f"Content: {content}") # This line won't be reached
except FileNotFoundError:
    print(f"Caught FileNotFoundError: The file '{non_existent_file}' does not exist.")
except PermissionError:
    print(f"Caught PermissionError: Insufficient permissions to read '{non_existent_file}'.")
except IOError as e: # Catch other I/O related errors (e.g., disk full, device error)
    print(f"Caught a general IOError during read: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"Caught an unexpected error: {e}")


# --- 8. Clean up created files ---
print("\n--- 8. Cleaning up created files ---")
files_to_clean = [
    "my_text_file.txt",
    "large_text_file.txt",
    "my_binary_file.bin",
    "temp_rplus_file.txt"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")