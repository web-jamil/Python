# --- Python open() Function: All About in Code ---

# The `open()` function is a fundamental built-in function in Python
# used to open a file. It returns a file object, which provides methods
# for reading, writing, and manipulating files.

# Syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# - file: The path to the file (string or path-like object).
# - mode: Specifies how the file is opened (string). Defaults to 'r'.
#         Common modes: 'r', 'w', 'a', 'x', 'rb', 'wb', 'ab', 'r+', 'w+', 'a+'.
# - buffering: Controls the buffering policy (e.g., line-buffered, block-buffered).
#              Defaults to -1 (system default).
# - encoding: For text mode, the name of the encoding used to decode or encode the file.
#             Defaults to platform-dependent encoding (e.g., 'utf-8' on many systems).
#             Crucial for handling text files correctly.
# - errors: Specifies how encoding/decoding errors are to be handled.
#           Common options: 'strict', 'ignore', 'replace', 'xmlcharrefreplace'.
# - newline: Controls how universal newlines work (for text mode).
#            '': For CSV files, to prevent extra blank rows.
#            '\n', '\r', '\r\n': Specific newline characters.
#            None (default): Universal newline mode.
# - closefd: If True (default), the file descriptor is closed when the file object is closed.
# - opener: A custom opener callback.

import os

# --- 1. Basic File Opening: Read Mode ('r') ---

print("--- 1. Basic File Opening: Read Mode ('r') ---")

# Create a dummy file for reading
try:
    with open("read_demo.txt", "w", encoding="utf-8") as f:
        f.write("Line 1: Hello from read_demo.txt\n")
        f.write("Line 2: This file is for reading examples.\n")
except IOError as e:
    print(f"Error creating read_demo.txt: {e}")

# Best practice: Use `with` statement for automatic file closing.
# The file is automatically closed when the block is exited, even if errors occur.
try:
    with open("read_demo.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"Content of 'read_demo.txt':\n{content}")
    print("File 'read_demo.txt' opened and read successfully (and automatically closed).\n")
except FileNotFoundError:
    print("Error: 'read_demo.txt' not found.")
except IOError as e:
    print(f"Error reading 'read_demo.txt': {e}")


# --- 2. File Modes (`mode` parameter) ---

print("--- 2. File Modes (`mode` parameter) ---")

# 2.1. 'w' (Write Mode)
# - Creates a new file if it doesn't exist.
# - If the file exists, it TRUNCATES (empties) the file.
# - File pointer is at the beginning.
write_file = "write_demo.txt"
try:
    with open(write_file, "w", encoding="utf-8") as file:
        file.write("This is the first line.\n")
        file.write("This line overwrites previous content if file existed.\n")
    print(f"Content written to '{write_file}' (mode 'w').")
except IOError as e:
    print(f"Error writing to '{write_file}': {e}")

# Verify content by reading
try:
    with open(write_file, "r", encoding="utf-8") as file:
        print(f"Content of '{write_file}':\n{file.read().strip()}\n")
except FileNotFoundError:
    pass # Already handled above


# 2.2. 'a' (Append Mode)
# - Creates a new file if it doesn't exist.
# - If the file exists, content is appended to the end.
# - File pointer is at the end.
append_file = "append_demo.txt"
try:
    # Initial write (or create)
    with open(append_file, "w", encoding="utf-8") as file:
        file.write("Initial content.\n")
    print(f"Created '{append_file}' with initial content.")

    # Now append
    with open(append_file, "a", encoding="utf-8") as file:
        file.write("This is appended content.\n")
        file.write("Another appended line.\n")
    print(f"Content appended to '{append_file}' (mode 'a').")
except IOError as e:
    print(f"Error appending to '{append_file}': {e}")

# Verify content
try:
    with open(append_file, "r", encoding="utf-8") as file:
        print(f"Content of '{append_file}':\n{file.read().strip()}\n")
except FileNotFoundError:
    pass


# 2.3. 'x' (Exclusive Creation Mode)
# - Creates a new file.
# - Raises `FileExistsError` if the file already exists.
exclusive_file = "exclusive_demo.txt"
try:
    with open(exclusive_file, "x", encoding="utf-8") as file:
        file.write("This file was created exclusively.\n")
    print(f"Successfully created '{exclusive_file}' (mode 'x').")
except FileExistsError:
    print(f"Error: '{exclusive_file}' already exists (expected if run multiple times).")
except IOError as e:
    print(f"Error creating '{exclusive_file}': {e}")
finally:
    # Attempt to remove if it was created, for re-running the demo
    if os.path.exists(exclusive_file):
        os.remove(exclusive_file)
        print(f"Removed '{exclusive_file}' for next run.")
    print("") # Newline for readability


# 2.4. 'r+', 'w+', 'a+' (Read and Write Modes)
# - 'r+': Opens for both reading and writing. Pointer at beginning. File must exist.
# - 'w+': Opens for both reading and writing. TRUNCATES file if exists, creates if not. Pointer at beginning.
# - 'a+': Opens for both reading and writing. Appends if exists, creates if not. Pointer at end.

# Example 'w+'
wplus_file = "wplus_demo.txt"
try:
    with open(wplus_file, "w+", encoding="utf-8") as file:
        file.write("First line w+.\n")
        file.write("Second line w+.\n")
        file.seek(0) # Move cursor to beginning to read
        content = file.read()
        print(f"Content after writing and seeking (w+):\n{content.strip()}\n")
except IOError as e:
    print(f"Error with '{wplus_file}' in 'w+' mode: {e}")


# --- 3. Binary Modes ('rb', 'wb', 'ab', etc.) ---

print("--- 3. Binary Modes ('rb', 'wb', 'ab', etc.) ---")

# - Used for non-text files (images, audio, executables, serialized objects).
# - Data is handled as raw bytes.
# - `encoding` parameter is NOT used and will cause an error if provided.

binary_file = "binary_demo.bin"
try:
    with open(binary_file, "wb") as file:
        # Write bytes literal
        file.write(b'\xDE\xAD\xBE\xEF')
        # Encode string to bytes
        file.write("Hello Binary!".encode('utf-8'))
    print(f"Content written to '{binary_file}' in 'wb' mode.")

    with open(binary_file, "rb") as file:
        content_bytes = file.read()
        print(f"Content of '{binary_file}' (binary):\n{content_bytes}")
        print(f"Type of content: {type(content_bytes)}\n")
except IOError as e:
    print(f"Error with '{binary_file}' in binary mode: {e}")


# --- 4. Encoding (`encoding` parameter) ---

print("--- 4. Encoding (`encoding` parameter) ---")

# Crucial for text files to ensure characters are correctly interpreted
# when reading and correctly stored when writing.
# Default encoding is platform-dependent (often UTF-8 on modern systems,
# but can be problematic on Windows with old default encodings).
# Always specify 'utf-8' for portability and best practice.

unicode_text = "안녕하세요 (Annyeonghaseyo) - こんにちは (Konnichiwa)"
encoding_file = "encoded_text.txt"

# Example 4.1: Writing with UTF-8 (recommended)
try:
    with open(encoding_file, "w", encoding="utf-8") as file:
        file.write(unicode_text)
    print(f"Wrote Unicode text to '{encoding_file}' with UTF-8 encoding.")
    with open(encoding_file, "r", encoding="utf-8") as file:
        read_text = file.read()
        print(f"Read with UTF-8 (correct): '{read_text}'\n")
except IOError as e:
    print(f"Error with UTF-8 encoding: {e}")

# Example 4.2: Reading with incorrect encoding (will cause UnicodeDecodeError)
# To demonstrate, let's create a file with UTF-8 but try to read it as Latin-1
try:
    # Ensure file is UTF-8
    with open("utf8_for_decode_test.txt", "w", encoding="utf-8") as f:
        f.write("Some UTF-8 character: éàü\n")
    print("Created 'utf8_for_decode_test.txt' with UTF-8 content.")

    with open("utf8_for_decode_test.txt", "r", encoding="latin-1") as file:
        content = file.read()
        print(f"Read with Latin-1 (might show mojibake): '{content.strip()}'")
except UnicodeDecodeError as e:
    print(f"Caught UnicodeDecodeError: {e} - because of wrong encoding.")
except IOError as e:
    print(f"Error during encoding test: {e}")
finally:
    if os.path.exists("utf8_for_decode_test.txt"):
        os.remove("utf8_for_decode_test.txt")


# --- 5. Newline Handling (`newline` parameter) ---

print("\n--- 5. Newline Handling (`newline` parameter) ---")

# The `newline` parameter controls universal newlines mode (default `None`).
# Important for cross-platform compatibility, especially for CSV files.

# `newline=''` is crucial for `csv` module to prevent extra blank rows.
csv_data = [
    ["Name", "Age"],
    ["Alice", 30],
    ["Bob", 24]
]
csv_file = "my_data.csv"
try:
    import csv
    with open(csv_file, "w", newline='', encoding="utf-8") as file: # `newline=''` here
        writer = csv.writer(file)
        writer.writerows(csv_data)
    print(f"Wrote CSV to '{csv_file}' with newline=''.")

    # Read back to show no extra lines
    with open(csv_file, "r", encoding="utf-8") as file:
        print(f"Content of '{csv_file}' (raw):\n{file.read().strip()}")
except IOError as e:
    print(f"Error with CSV file: {e}")


# --- 6. Error Handling with `open()` ---

print("\n--- 6. Error Handling with `open()` ---")

non_existent_path = "path/to/non_existent_dir/file.txt"
permission_denied_path = "/root/restricted_file.txt" # Requires specific OS setup to trigger

# 6.1. FileNotFoundError (most common)
try:
    with open(non_existent_path, "r") as f:
        pass
except FileNotFoundError:
    print(f"Caught FileNotFoundError: Directory or file '{non_existent_path}' does not exist.")

# 6.2. PermissionError
# This error occurs if your program doesn't have the necessary permissions
# to read/write to the specified location. Often seen when trying to write
# to system directories.
try:
    # Attempting to open a path where permissions might be denied.
    # Note: This line might still raise FileNotFoundError if the /root/ directory
    # itself isn't accessible or is empty. It's illustrative.
    with open(permission_denied_path, "w") as f:
        f.write("Attempting to write to a restricted area.")
except FileNotFoundError:
    print(f"Caught FileNotFoundError: Parent directory for '{permission_denied_path}' does not exist.")
except PermissionError:
    print(f"Caught PermissionError: Insufficient permissions to access '{permission_denied_path}'.")
except IOError as e: # General I/O errors
    print(f"Caught an IOError: {e}")


# --- 7. Clean up created files ---
print("\n--- 7. Cleaning up created files ---")
files_to_clean = [
    "read_demo.txt",
    "write_demo.txt",
    "append_demo.txt",
    # "exclusive_demo.txt", # Already handled in its section
    "wplus_demo.txt",
    "binary_demo.bin",
    "encoded_text.txt",
    "my_data.csv"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")