# --- Python Writing to Files: All About in Code ---

# The primary way to write to a file in Python involves opening it
# in a write mode ('w', 'a', 'x', 'w+') and then using methods
# like .write() or .writelines() on the file object.

# --- 1. Writing to a File in 'w' (Write) Mode ---

print("--- 1. Writing in 'w' (Write) Mode ---")

# 'w' mode:
# - Creates a new file if it doesn't exist.
# - If the file already exists, its content is TRUNCATED (emptied)
#   before any new writing occurs. Use with caution!
# - Writes strings (in text mode) or bytes (in binary mode).

# Example 1.1: Basic write - creating a new file
try:
    with open("write_example_new.txt", "w", encoding="utf-8") as file:
        file.write("This is the first line written to a new file.\n")
        file.write("This is the second line.\n")
        file.write("And this is the final line.\n")
    print("Content written to 'write_example_new.txt' (new file created).")
except IOError as e:
    print(f"Error writing to 'write_example_new.txt': {e}")

# Example 1.2: Overwriting an existing file
# Let's verify the content first
try:
    with open("write_example_new.txt", "r", encoding="utf-8") as file:
        print("\nContent before overwrite:")
        print(file.read().strip())
except FileNotFoundError:
    print("Original file 'write_example_new.txt' not found for verification.")

try:
    with open("write_example_new.txt", "w", encoding="utf-8") as file:
        file.write("This content COMPLETELY REPLACES the old content.\n")
        file.write("Only these two lines will be in the file now.\n")
    print("Content overwritten in 'write_example_new.txt'.")
except IOError as e:
    print(f"Error overwriting 'write_example_new.txt': {e}")

# Verify the overwritten content
try:
    with open("write_example_new.txt", "r", encoding="utf-8") as file:
        print("\nContent AFTER overwrite:")
        print(file.read().strip())
except FileNotFoundError:
    print("Overwritten file 'write_example_new.txt' not found for verification.")


# --- 2. Appending to a File in 'a' (Append) Mode ---

print("\n--- 2. Appending in 'a' (Append) Mode ---")

# 'a' mode:
# - Creates a new file if it doesn't exist.
# - If the file exists, new content is ADDED to the end of the file.
# - The file pointer is automatically positioned at the end of the file.

# Example 2.1: Appending to an existing file
try:
    with open("append_example.txt", "w", encoding="utf-8") as file: # First, create it with some content
        file.write("Initial content for appending.\n")
    print("Created 'append_example.txt' with initial content.")

    with open("append_example.txt", "a", encoding="utf-8") as file:
        file.write("This line is appended.\n")
        file.write("Another line appended.\n")
    print("Content appended to 'append_example.txt'.")
except IOError as e:
    print(f"Error appending to 'append_example.txt': {e}")

# Verify the appended content
try:
    with open("append_example.txt", "r", encoding="utf-8") as file:
        print("\nContent AFTER appending:")
        print(file.read().strip())
except FileNotFoundError:
    print("Appended file 'append_example.txt' not found for verification.")


# --- 3. Exclusive Creation in 'x' Mode ---

print("\n--- 3. Exclusive Creation in 'x' Mode ---")

# 'x' mode:
# - Creates a new file.
# - Raises a FileExistsError if the file already exists.
# - Useful to ensure you are not accidentally overwriting an important file.

# Example 3.1: Successfully creating a new file
try:
    with open("exclusive_new_file.txt", "x", encoding="utf-8") as file:
        file.write("This file was created using 'x' mode.\n")
    print("Successfully created 'exclusive_new_file.txt' using 'x' mode.")
except FileExistsError:
    print("Error: 'exclusive_new_file.txt' already exists (expected if run twice).")
except IOError as e:
    print(f"Error creating 'exclusive_new_file.txt' with 'x' mode: {e}")

# Example 3.2: Attempting to create an existing file (will raise FileExistsError)
try:
    with open("exclusive_new_file.txt", "x", encoding="utf-8") as file:
        file.write("This line will never be written.\n")
except FileExistsError:
    print("Caught expected FileExistsError when trying to create 'exclusive_new_file.txt' again with 'x' mode.")
except IOError as e:
    print(f"An unexpected I/O error occurred: {e}")


# --- 4. Read/Write ('+') Modes ---

print("\n--- 4. Read/Write ('+') Modes ---")

# '+' modes allow both reading and writing. The behavior of writing depends
# on the base mode ('r', 'w', 'a').

# 4.1 'w+' mode: Write and Read
# - Truncates the file (empties it) if it exists, creates if not.
# - The file pointer starts at the beginning (index 0).
# - You can read immediately after writing (if you seek back to the beginning).
try:
    with open("write_read_wplus.txt", "w+", encoding="utf-8") as file:
        file.write("Hello from w+ mode!\n")
        file.write("Second line for w+.\n")
        file.seek(0) # Move cursor to the beginning to read
        content = file.read()
        print("\nContent from 'write_read_wplus.txt' (w+ mode after writing and seeking):")
        print(content.strip())
except IOError as e:
    print(f"Error with 'w+' mode: {e}")

# 4.2 'a+' mode: Append and Read
# - Appends content to the end of the file.
# - File pointer starts at the end for writing.
# - To read, you must explicitly `seek(0)` to go to the beginning.
try:
    with open("append_read_aplus.txt", "w", encoding="utf-8") as file: # Initialize file
        file.write("Existing content.\n")

    with open("append_read_aplus.txt", "a+", encoding="utf-8") as file:
        file.write("New line appended by a+.\n")
        print(f"Current cursor position after writing in a+: {file.tell()}")
        file.seek(0) # Move cursor to the beginning to read everything
        content = file.read()
        print("\nContent from 'append_read_aplus.txt' (a+ mode after appending and seeking):")
        print(content.strip())
except IOError as e:
    print(f"Error with 'a+' mode: {e}")


# --- 5. Writing Lists of Strings with .writelines() ---

print("\n--- 5. Writing Lists with .writelines() ---")

# .writelines(iterable_of_strings):
# - Writes an iterable (like a list or tuple) of strings to the file.
# - IMPORTANT: It does NOT automatically add newline characters.
#   You must include '\n' at the end of each string if you want them on separate lines.
try:
    lines_to_write = [
        "Item 1 from writelines\n",
        "Item 2 from writelines\n",
        "Item 3 from writelines\n",
        "Item 4 (without newline - will be on same line as 3)" # This won't start a new line
    ]
    with open("writelines_output.txt", "w", encoding="utf-8") as file:
        file.writelines(lines_to_write)
    print("'writelines_output.txt' created using .writelines().")

    with open("writelines_output.txt", "r", encoding="utf-8") as file:
        print("\nContent of 'writelines_output.txt':")
        print(file.read().strip())
except IOError as e:
    print(f"Error with .writelines(): {e}")


# --- 6. Writing Binary Files ('wb', 'ab', 'xb', 'wb+', 'ab+') ---

print("\n--- 6. Writing Binary Files ---")

# Use 'b' in the mode (e.g., 'wb', 'ab') for binary files.
# - Data must be bytes objects (prefixed with `b''` or created via .encode()).
# - No encoding argument is used for binary modes.

try:
    with open("binary_output.bin", "wb") as file:
        file.write(b'Hello') # Write bytes literal
        file.write(bytes([0x01, 0x02, 0x03])) # Write bytes from a list of integers
        text_as_bytes = "Binary Data End".encode("utf-8") # Encode a string to bytes
        file.write(text_as_bytes)
    print("'binary_output.bin' created with binary content.")

    with open("binary_output.bin", "rb") as file:
        content = file.read()
        print(f"Content of 'binary_output.bin': {content}")
        print(f"Length of binary content: {len(content)} bytes")
except IOError as e:
    print(f"Error writing/reading binary file: {e}")


# --- 7. Error Handling During Writing ---

print("\n--- 7. Error Handling During Writing ---")

# Always use try-except blocks to gracefully handle potential errors.

try:
    # Attempt to write to a protected system path (will likely cause PermissionError)
    # This path might not exist or be writable on your system.
    # On Linux/macOS: try "/root/forbidden_write.txt" or "/etc/forbidden_write.txt"
    # On Windows: try "C:\\Program Files\\forbidden_write.txt"
    # For demonstration, we'll use a path that might just be non-existent.
    # To truly test PermissionError, you need to run this code in an environment
    # where you lack write permissions to the target directory.
    # For now, let's simulate a case where the directory doesn't exist
    # and we're not using os.makedirs.
    path_to_non_existent_dir = "non_existent_folder/protected_file.txt"
    with open(path_to_non_existent_dir, "w") as file:
        file.write("Trying to write to a potentially protected/non-existent path.")
    print("Successfully wrote to a potentially non-existent path (this might not print).")
except FileNotFoundError:
    print(f"Caught Error: Directory for '{path_to_non_existent_dir}' does not exist.")
except PermissionError:
    print(f"Caught Error: Permission denied when trying to write to '{path_to_non_existent_dir}'.")
except IOError as e: # Catch other I/O related errors
    print(f"Caught an I/O error during write: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"Caught an unexpected error: {e}")


# --- 8. Clean up created files ---
import os

print("\n--- 8. Cleaning up created files ---")
files_to_clean = [
    "write_example_new.txt",
    "append_example.txt",
    "exclusive_new_file.txt",
    "write_read_wplus.txt",
    "append_read_aplus.txt",
    "writelines_output.txt",
    "binary_output.bin"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")