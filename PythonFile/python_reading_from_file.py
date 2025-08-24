# --- Python Reading From Files: All About in Code ---

# The primary way to read from a file in Python involves opening it
# in a read mode and then using various methods available on the file object.

# --- 1. Basic Reading with 'with' Statement (Recommended) ---

print("--- 1. Basic Reading with 'with' Statement ---")

# First, let's create a sample file to read from
sample_content = (
    "Line 1: This is the first line of the sample file.\n"
    "Line 2: Python file handling is quite versatile.\n"
    "Line 3: You can read line by line, or the entire content.\n"
    "Line 4: This is the final line for our reading examples.\n"
)
try:
    with open("sample_read_file.txt", "w", encoding="utf-8") as file:
        file.write(sample_content)
    print("Created 'sample_read_file.txt' for reading examples.")
except IOError as e:
    print(f"Error creating sample file: {e}")


# 1.1. Reading the entire content using .read()
# - Reads the entire file into a single string.
# - The file cursor moves to the end of the file.
try:
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        full_text = file.read()
        print("\n1.1. Content using .read():")
        print(full_text)
        # Try reading again - it will be empty because cursor is at the end
        empty_read = file.read()
        print(f"Attempt to read again (should be empty): '{empty_read}'")
except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for .read() example.")
except IOError as e:
    print(f"Error reading file with .read(): {e}")


# 1.2. Reading line by line using .readline()
# - Reads one line at a time, including the newline character '\n'.
# - Returns an empty string '' when the end of the file is reached.
try:
    print("\n1.2. Content using .readline():")
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        print(f"First line: '{line1.strip()}'") # .strip() removes leading/trailing whitespace including '\n'
        print(f"Second line: '{line2.strip()}'")
        print(f"Third line: '{line3.strip()}'")
        # Read the next line, and then the one after, until empty string
        line_n = file.readline()
        while line_n:
            print(f"Next line: '{line_n.strip()}'")
            line_n = file.readline()
        print("End of file reached with .readline().")
except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for .readline() example.")
except IOError as e:
    print(f"Error reading file with .readline(): {e}")


# 1.3. Reading all lines into a list using .readlines()
# - Reads all lines from the file and returns them as a list of strings.
# - Each string in the list includes the newline character '\n'.
try:
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        all_lines_list = file.readlines()
        print("\n1.3. Content using .readlines() (list of strings):")
        for i, line in enumerate(all_lines_list):
            print(f"Line {i+1} (raw): '{line.strip()}'")
except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for .readlines() example.")
except IOError as e:
    print(f"Error reading file with .readlines(): {e}")


# --- 2. Iterating Through a File Object (Most Memory Efficient) ---

print("\n--- 2. Iterating Through a File Object ---")

# Iterating directly over the file object is the most memory-efficient way
# to read large files, as it reads one line at a time without loading the
# entire file into memory at once.
try:
    print("Iterating directly over 'sample_read_file.txt':")
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        for line_number, line_content in enumerate(file):
            print(f"Line {line_number + 1}: {line_content.strip()}")
except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for iteration example.")
except IOError as e:
    print(f"Error iterating file: {e}")


# --- 3. Reading Specific Number of Characters/Bytes ---

print("\n--- 3. Reading Specific Number of Characters/Bytes ---")

# .read(size) - Reads 'size' number of characters (in text mode) or bytes (in binary mode).
try:
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        chunk1 = file.read(10) # Read first 10 characters
        print(f"\nFirst 10 characters: '{chunk1}'")
        chunk2 = file.read(5)  # Read next 5 characters
        print(f"Next 5 characters: '{chunk2}'")
        remaining = file.read() # Read the rest
        print(f"Remaining content: '{remaining.strip()}'")
except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for .read(size) example.")
except IOError as e:
    print(f"Error reading specific size: {e}")


# --- 4. File Pointer (Cursor) Manipulation: .seek() and .tell() ---

print("\n--- 4. File Pointer Manipulation ---")

# .tell() - Returns the current position of the file pointer (cursor) in bytes.
# .seek(offset, whence=0) - Moves the file pointer to a new position.
#   - offset: Number of bytes to move.
#   - whence: 0 (start of file), 1 (current position), 2 (end of file).
#     Note: 'whence=1' or 'whence=2' with text mode can be problematic or restricted.
#           It's generally safer to use 'whence=0' or binary mode for these.

try:
    with open("sample_read_file.txt", "r", encoding="utf-8") as file:
        print(f"\nInitial cursor position: {file.tell()} bytes") # Should be 0

        content_chunk = file.read(15)
        print(f"Read 15 chars: '{content_chunk}'")
        print(f"Cursor after reading 15 chars: {file.tell()} bytes")

        file.seek(0) # Move cursor back to the beginning
        print(f"Cursor after seeking to 0: {file.tell()} bytes")
        full_content_again = file.read()
        print(f"Read entire content after seeking to 0:\n{full_content_again.strip()}")

        # Seek to a specific byte offset (e.g., to the beginning of a specific line)
        # Note: In text mode, 'seek' offsets are character counts, not necessarily bytes,
        #       unless using an encoding like 'latin-1' where 1 char = 1 byte.
        #       For precise byte seeking, binary mode ('rb') is better.
        file.seek(0) # Reset to beginning
        # Let's find the start of 'Line 3'
        file.readline() # Read Line 1
        file.readline() # Read Line 2
        print(f"Cursor after reading two lines: {file.tell()} bytes")
        line3_content = file.readline()
        print(f"Content from what should be Line 3: '{line3_content.strip()}'")

except FileNotFoundError:
    print("Error: 'sample_read_file.txt' not found for seek/tell example.")
except IOError as e:
    print(f"Error with seek/tell: {e}")


# --- 5. Reading Binary Files ---

print("\n--- 5. Reading Binary Files ---")

# 'rb' mode: read binary.
# - Data is read as bytes objects, not strings.
# - This is essential for non-text files (images, executables, compressed data).

# Create a dummy binary file
try:
    with open("dummy_binary_read.bin", "wb") as f:
        f.write(b'\x01\x02\x03\x41\x42\x43\xFF\xFE\xFD') # Some arbitrary bytes
    print("Created 'dummy_binary_read.bin' for binary reading.")
except IOError as e:
    print(f"Error creating dummy binary file: {e}")

try:
    with open("dummy_binary_read.bin", "rb") as file:
        binary_data = file.read()
        print(f"\nFull binary content: {binary_data}")

        file.seek(3) # Move to the 4th byte (index 3)
        specific_bytes = file.read(3) # Read 3 bytes from there
        print(f"Bytes after seeking to 3 and reading 3: {specific_bytes}")
        # To convert bytes to something readable (if they represent ASCII, for example)
        try:
            print(f"Decoded these bytes: {specific_bytes.decode('ascii')}")
        except UnicodeDecodeError:
            print("Bytes are not simple ASCII.")

except FileNotFoundError:
    print("Error: 'dummy_binary_read.bin' not found for binary read example.")
except IOError as e:
    print(f"Error reading binary file: {e}")


# --- 6. Error Handling During Reading ---

print("\n--- 6. Error Handling During Reading ---")

# Always use try-except blocks to gracefully handle potential errors
# like FileNotFoundError or IOError.

try:
    # Attempt to open a file that does not exist
    with open("non_existent_file_for_read.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Caught Error: 'non_existent_file_for_read.txt' was not found as expected.")
except IOError as e: # Catch other I/O related errors (e.g., permission issues)
    print(f"Caught an I/O error during read: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"Caught an unexpected error: {e}")

# --- 7. Clean up created files ---
import os

print("\n--- 7. Cleaning up created files ---")
files_to_clean = [
    "sample_read_file.txt",
    "dummy_binary_read.bin"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")