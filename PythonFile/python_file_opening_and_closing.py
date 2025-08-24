# --- Python File Opening and Closing: All About in Code ---

# The fundamental way to open a file in Python is using the `open()` function.
# It returns a file object, which you then use for reading, writing, or other operations.

# Syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# The most common arguments are 'file' (the path to the file) and 'mode'.

# --- 1. Basic File Opening and Manual Closing (Not Recommended for most cases) ---

print("--- 1. Basic File Opening and Manual Closing ---")

# 'w' mode: write mode.
# - If the file exists, its content will be truncated (emptied) before writing.
# - If the file does not exist, a new file will be created.
# - It's crucial to close the file manually using .close() to ensure all data is written
#   and resources are released. If not closed, data might be buffered and lost.
try:
    file_object_write = open("manual_close_example.txt", "w")
    file_object_write.write("This is the first line.\n")
    file_object_write.write("This is the second line.\n")
    print("Content written to 'manual_close_example.txt'.")
except IOError as e:
    print(f"Error writing to file (manual close): {e}")
finally:
    # Always ensure the file is closed, even if errors occur during writing.
    if 'file_object_write' in locals() and not file_object_write.closed:
        file_object_write.close()
        print("'manual_close_example.txt' closed manually.")


# 'r' mode: read mode. (This is the default mode if not specified)
# - The file must exist for this mode, otherwise, a FileNotFoundError occurs.
try:
    file_object_read = open("manual_close_example.txt", "r")
    content = file_object_read.read()
    print("\nContent read from 'manual_close_example.txt' (manual close):")
    print(content)
except FileNotFoundError:
    print("Error: 'manual_close_example.txt' not found (manual read).")
except IOError as e:
    print(f"Error reading file (manual close): {e}")
finally:
    if 'file_object_read' in locals() and not file_object_read.closed:
        file_object_read.close()
        print("'manual_close_example.txt' closed manually.")

# --- 2. Using the 'with' Statement (THE RECOMMENDED WAY) ---

print("\n--- 2. Using the 'with' Statement (Recommended) ---")

# The 'with' statement creates a context manager.
# - It automatically handles opening and closing the file, even if errors occur.
# - This prevents resource leaks and ensures data integrity.

# Writing with 'with' (mode 'w')
try:
    with open("with_statement_example.txt", "w") as file:
        file.write("Hello from the 'with' statement!\n")
        file.write("This line is also written.\n")
    print("Content written to 'with_statement_example.txt' using 'with'.")
    # File is automatically closed here, outside the 'with' block.
except IOError as e:
    print(f"Error writing to file (with statement): {e}")


# Reading with 'with' (mode 'r')
try:
    with open("with_statement_example.txt", "r") as file:
        content = file.read()
        print("\nContent read from 'with_statement_example.txt' using 'with':")
        print(content)
    # File is automatically closed here.
except FileNotFoundError:
    print("Error: 'with_statement_example.txt' not found (with statement read).")
except IOError as e:
    print(f"Error reading file (with statement): {e}")


# Appending with 'with' (mode 'a')
# - Adds content to the end of the file.
# - Creates the file if it doesn't exist.
try:
    with open("with_statement_example.txt", "a") as file:
        file.write("This line was appended by the 'a' mode.\n")
    print("Content appended to 'with_statement_example.txt' using 'with'.")
except IOError as e:
    print(f"Error appending to file (with statement): {e}")

# Verify appended content
try:
    with open("with_statement_example.txt", "r") as file:
        content = file.read()
        print("\nUpdated content of 'with_statement_example.txt':")
        print(content)
except IOError as e:
    print(f"Error verifying appended content: {e}")


# --- 3. Different File Modes for Opening ---

print("\n--- 3. Different File Modes ---")

# 'x' mode: exclusive creation mode.
# - Creates a new file but raises FileExistsError if the file already exists.
try:
    with open("exclusive_create_test.txt", "x") as file:
        file.write("This file was exclusively created.\n")
    print("'exclusive_create_test.txt' created successfully (x mode).")
except FileExistsError:
    print("'exclusive_create_test.txt' already exists (x mode failed to create).")
except IOError as e:
    print(f"Error during exclusive creation: {e}")


# 'b' mode: binary mode.
# - Used for non-text files like images, audio, or compiled data.
# - Data is read/written as bytes, not strings.
# - Combine with 'r', 'w', 'a', 'x' (e.g., 'rb', 'wb', 'ab', 'xb').
try:
    with open("binary_example.bin", "wb") as file:
        # b'' prefix denotes a bytes literal
        file.write(b'\x48\x65\x6c\x6c\x6f\x20\x42\x69\x6e\x61\x72\x79\x21') # "Hello Binary!" in hex bytes
    print("'binary_example.bin' created in binary mode.")

    with open("binary_example.bin", "rb") as file:
        binary_content = file.read()
        print(f"Content from 'binary_example.bin' (bytes): {binary_content}")
except IOError as e:
    print(f"Error with binary file operations: {e}")


# '+' mode: update mode.
# - Allows both reading and writing.
# - Combine with 'r', 'w', 'a', 'x' (e.g., 'r+', 'w+', 'a+', 'x+').

# 'r+' mode: read and write.
# - File must exist. Cursor starts at the beginning.
# - Writing overwrites from the current cursor position.
try:
    with open("read_write_rplus.txt", "w") as file: # First create a file
        file.write("0123456789")
    print("\n'read_write_rplus.txt' initialized with '0123456789'.")

    with open("read_write_rplus.txt", "r+") as file:
        print(f"Initial content (r+): {file.read()}") # Read all
        file.seek(0) # Move cursor to the beginning
        file.write("ABC") # Overwrite first 3 chars
        file.seek(0) # Move cursor to the beginning to read again
        print(f"Content after 'ABC' overwrite (r+): {file.read()}")
except IOError as e:
    print(f"Error with 'r+' mode: {e}")


# 'w+' mode: write and read.
# - Truncates (empties) the file if it exists, creates if not.
# - Cursor starts at the beginning.
try:
    with open("read_write_wplus.txt", "w+") as file:
        file.write("First write with w+.\n")
        file.seek(0) # Move cursor to the beginning to read what was just written
        content = file.read()
        print(f"\nContent from 'w+' after writing and seeking: {content.strip()}")
        file.write("Second write.\n") # Will write after previous content
        file.seek(0)
        print(f"Content after second write: {file.read().strip()}")
except IOError as e:
    print(f"Error with 'w+' mode: {e}")

# 'a+' mode: append and read.
# - Appends content to the end. Cursor starts at the end for writing.
# - For reading, you must `seek(0)` to go to the beginning.
try:
    with open("read_write_aplus.txt", "w") as file: # Initialize
        file.write("Initial content.\n")

    with open("read_write_aplus.txt", "a+") as file:
        file.write("Appended line with a+.\n")
        file.seek(0) # Move cursor to the beginning to read everything
        content = file.read()
        print(f"\nContent from 'a+' after appending and seeking: {content.strip()}")
except IOError as e:
    print(f"Error with 'a+' mode: {e}")


# --- 4. Encoding ---

print("\n--- 4. Encoding ---")

# Encoding specifies how characters are converted to bytes and vice-versa.
# 'utf-8' is the most common and recommended encoding for text files.
# If not specified, the default system encoding is used, which can lead to issues
# when files are moved between different operating systems.
try:
    with open("utf8_example.txt", "w", encoding="utf-8") as file:
        file.write("Hello, World! This includes some special characters: æøåñé\n")
    print("'utf8_example.txt' written with UTF-8 encoding.")

    with open("utf8_example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"Read with UTF-8 encoding: {content.strip()}")
except IOError as e:
    print(f"Error with UTF-8 encoding: {e}")

# Example of an encoding error if you try to read a UTF-8 file with the wrong encoding
try:
    with open("utf8_example.txt", "r", encoding="latin-1") as file: # Incorrect encoding
        content = file.read()
        print(f"Read with LATIN-1 encoding (might show mojibake): {content.strip()}")
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: Could not decode with LATIN-1. Use correct encoding (e.g., UTF-8). {e}")
except IOError as e:
    print(f"Error with encoding example: {e}")


# --- 5. Clean up created files ---
import os

print("\n--- 5. Cleaning up created files ---")
files_to_clean = [
    "manual_close_example.txt",
    "with_statement_example.txt",
    "exclusive_create_test.txt",
    "binary_example.bin",
    "read_write_rplus.txt",
    "read_write_wplus.txt",
    "read_write_aplus.txt",
    "utf8_example.txt"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")