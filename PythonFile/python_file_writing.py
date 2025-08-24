# --- Python File Writing: All About in Code ---

# Writing to files is a fundamental operation in Python, allowing you to
# persist data from your programs to external storage.

# The primary way to write to a file involves opening it in a write mode
# ('w', 'a', 'x', 'w+') and then using methods like .write() or .writelines().

import os
import shutil

# --- 1. Opening Files for Writing (`open()` function) ---

print("--- 1. Opening Files for Writing (`open()` function) ---")

# `open()` function: `open(file, mode='w', encoding=None, errors=None)`
# - `file`: The path to the file you want to open/create.
# - `mode`: Specifies how the file is opened for writing.
#    - 'w': Write mode. Creates a new file or TRUNCATES (empties) an existing one.
#           File pointer at the beginning.
#    - 'a': Append mode. Creates a new file or appends to an existing one.
#           File pointer at the end.
#    - 'x': Exclusive creation mode. Creates a new file. Raises FileExistsError if it exists.
#    - 'wb', 'ab', 'xb': Binary versions of 'w', 'a', 'x'. For writing bytes.
#    - 'w+', 'a+', 'x+': Read/Write modes. Allow both reading and writing.
# - `encoding`: For text mode, specifies the character encoding (e.g., 'utf-8').
#               Crucial for correct storage of characters. Not used for binary modes.

# It's best practice to use a `with` statement. This ensures the file is
# automatically closed, even if errors occur, preventing data loss or resource leaks.

# Example 1.1: Opening in text write mode ('w')
# This will create 'my_output_file.txt' or empty it if it exists.
try:
    with open("my_output_file.txt", "w", encoding="utf-8") as file_object:
        print(f"Successfully opened 'my_output_file.txt' in 'w' mode. File object: {file_object}")
        # We'll write content in later sections
except IOError as e:
    print(f"Error opening 'my_output_file.txt': {e}")


# Example 1.2: Opening in text append mode ('a')
# This will create 'my_append_file.txt' or append to it if it exists.
try:
    with open("my_append_file.txt", "a", encoding="utf-8") as file_object:
        print(f"Successfully opened 'my_append_file.txt' in 'a' mode. File object: {file_object}")
except IOError as e:
    print(f"Error opening 'my_append_file.txt': {e}")


# Example 1.3: Opening in exclusive creation mode ('x')
# This will create 'my_exclusive_file.txt' if it doesn't exist.
# If it exists, it will raise FileExistsError.
try:
    with open("my_exclusive_file.txt", "x", encoding="utf-8") as file_object:
        file_object.write("This file was created exclusively.\n")
    print(f"Successfully created and wrote to 'my_exclusive_file.txt' in 'x' mode.")
except FileExistsError:
    print("Error: 'my_exclusive_file.txt' already exists (expected if run multiple times).")
except IOError as e:
    print(f"Error opening 'my_exclusive_file.txt': {e}")


# --- 2. Writing String Content (`.write()`) ---

print("\n--- 2. Writing String Content (`.write()`) ---")

# `file_object.write(string)`:
# - Writes the given string to the file at the current file pointer position.
# - Returns the number of characters written.
# - Does NOT automatically add a newline character. You must include `\n` yourself.

# Example 2.1: Writing to a new/truncated file ('w' mode)
try:
    with open("write_example.txt", "w", encoding="utf-8") as file:
        chars_written1 = file.write("Hello, world!\n") # Includes newline
        print(f"Wrote '{chars_written1}' characters.")
        chars_written2 = file.write("This is the second line.") # No newline
        print(f"Wrote '{chars_written2}' characters.")
        chars_written3 = file.write(" And this is still on the second line.\n")
        print(f"Wrote '{chars_written3}' characters.")
    print("Content written to 'write_example.txt'.")
except IOError as e:
    print(f"Error writing to 'write_example.txt': {e}")

# Verify content
try:
    with open("write_example.txt", "r", encoding="utf-8") as file:
        print(f"\nContent of 'write_example.txt':\n{file.read().strip()}")
except FileNotFoundError:
    print("Error: 'write_example.txt' not found for verification.")


# --- 3. Appending Content (`.write()` with 'a' mode) ---

print("\n--- 3. Appending Content (`.write()` with 'a' mode) ---")

# 'a' mode:
# - Creates the file if it doesn't exist.
# - If the file exists, content is added to the end.
# - The file pointer is automatically positioned at the end.

try:
    # First, create/reset the file with some initial content
    with open("append_example.txt", "w", encoding="utf-8") as file:
        file.write("Initial content for append demo.\n")
    print("Created 'append_example.txt' with initial content.")

    # Now, append to it
    with open("append_example.txt", "a", encoding="utf-8") as file:
        file.write("This line is appended.\n")
        file.write("Another line appended.\n")
    print("Content appended to 'append_example.txt'.")
except IOError as e:
    print(f"Error appending to 'append_example.txt': {e}")

# Verify appended content
try:
    with open("append_example.txt", "r", encoding="utf-8") as file:
        print(f"\nContent of 'append_example.txt' after append:\n{file.read().strip()}")
except FileNotFoundError:
    print("Error: 'append_example.txt' not found for verification.")


# --- 4. Writing Lists of Strings (`.writelines()`) ---

print("\n--- 4. Writing Lists of Strings (`.writelines()`) ---")

# `file_object.writelines(iterable_of_strings)`:
# - Writes an iterable (e.g., list, tuple) of strings to the file.
# - IMPORTANT: It does NOT automatically add newline characters.
#   Each string in the iterable should typically end with `\n` if you want
#   them on separate lines in the file.

list_of_lines = [
    "Line A from writelines.\n",
    "Line B from writelines.\n",
    "Line C from writelines (no newline here)." # This line will not have a newline
]

try:
    with open("writelines_example.txt", "w", encoding="utf-8") as file:
        file.writelines(list_of_lines)
    print("Content written to 'writelines_example.txt' using .writelines().")
except IOError as e:
    print(f"Error writing to 'writelines_example.txt': {e}")

# Verify content
try:
    with open("writelines_example.txt", "r", encoding="utf-8") as file:
        print(f"\nContent of 'writelines_example.txt':\n{file.read()}") # Read raw to see missing newline
except FileNotFoundError:
    print("Error: 'writelines_example.txt' not found for verification.")


# --- 5. Writing to Binary Files (`.write()` with 'wb', 'ab', 'xb' modes) ---

print("\n--- 5. Writing to Binary Files ---")

# For binary files, you must use modes with 'b' (e.g., 'wb', 'ab').
# Data written must be `bytes` objects, not strings.
# No `encoding` parameter is used.

try:
    with open("my_binary_output.bin", "wb") as file:
        file.write(b'\x01\x02\x03\x04') # Write bytes literal
        file.write(bytes([65, 66, 67])) # Write bytes from a list of integers (ASCII 'ABC')
        string_to_bytes = "Hello Binary!".encode('utf-8') # Encode a string to bytes
        file.write(string_to_bytes)
        file.write(b'\xFF\xEE\xDD') # More bytes
    print("Content written to 'my_binary_output.bin'.")
except IOError as e:
    print(f"Error writing to 'my_binary_output.bin': {e}")

# Verify content (read back in binary mode)
try:
    with open("my_binary_output.bin", "rb") as file:
        binary_content = file.read()
        print(f"\nContent of 'my_binary_output.bin': {binary_content}")
        print(f"Type of content: {type(binary_content)}")
except FileNotFoundError:
    print("Error: 'my_binary_output.bin' not found for verification.")


# --- 6. Writing with `w+` (Write and Read) Mode ---

print("\n--- 6. Writing with `w+` (Write and Read) Mode ---")

# `w+` mode:
# - Creates a new file or TRUNCATES an existing one.
# - Allows both writing and reading.
# - File pointer starts at the beginning.

try:
    with open("wplus_example.txt", "w+", encoding="utf-8") as file:
        file.write("First write with w+.\n")
        file.write("Second write with w+.\n")
        print(f"Current file pointer position after writing: {file.tell()}") # Shows byte offset

        file.seek(0) # Move file pointer to the beginning to read
        content_after_write = file.read()
        print(f"\nContent read after writing and seeking to 0:\n{content_after_write.strip()}")

        file.write("OVERWRITE ME!") # This will overwrite from the current position (beginning)
        file.seek(0)
        content_after_overwrite = file.read()
        print(f"Content after overwriting from beginning:\n{content_after_overwrite.strip()}")
except IOError as e:
    print(f"Error with 'w+' mode: {e}")


# --- 7. Error Handling During Writing ---

print("\n--- 7. Error Handling During Writing ---")

# Always use `try-except` blocks to handle potential errors.

# Example 7.1: PermissionError (attempting to write to a protected location)
# This depends on your OS and user permissions.
protected_path = "/nonexistent_protected_dir/restricted_write.txt" # Likely to fail

try:
    with open(protected_path, "w") as file:
        file.write("Trying to write to a protected area.")
    print(f"Successfully wrote to '{protected_path}' (this might indicate elevated privileges).")
except FileNotFoundError:
    print(f"Caught FileNotFoundError: Parent directory for '{protected_path}' does not exist.")
except PermissionError:
    print(f"Caught PermissionError: Insufficient permissions to write to '{protected_path}'.")
except IOError as e:
    print(f"Caught a general IOError during write: {e}")
except Exception as e:
    print(f"Caught an unexpected error: {e}")


# Example 7.2: FileExistsError with 'x' mode
existing_file_for_x = "my_exclusive_file.txt" # This file was created earlier

try:
    with open(existing_file_for_x, "x") as file:
        file.write("This line should not be written.")
except FileExistsError:
    print(f"Caught FileExistsError: '{existing_file_for_x}' already exists, 'x' mode failed as expected.")
except IOError as e:
    print(f"Caught an IOError with 'x' mode: {e}")


# --- 8. Clean up created files ---
print("\n--- 8. Cleaning up created files ---")
files_to_clean = [
    "my_output_file.txt",
    "my_append_file.txt",
    "my_exclusive_file.txt",
    "write_example.txt",
    "append_example.txt",
    "writelines_example.txt",
    "my_binary_output.bin",
    "wplus_example.txt"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")

# Remove the dummy protected_path if it was created (unlikely)
if os.path.exists("/nonexistent_protected_dir"):
    shutil.rmtree("/nonexistent_protected_dir")
    print("Cleaned up '/nonexistent_protected_dir' (if it was created).")