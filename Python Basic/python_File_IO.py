import os # For checking file existence and deleting files
import json # For JSON file operations
import csv # For CSV file operations

print("--- Python File I/O: Practice Code ---")

# --- 1. Opening a File (`open()` function) ---
print("\n--- 1. Opening a File (`open()` function) ---")
print("The `open()` function is the primary way to interact with files.")
print("Syntax: `open(file, mode='r', encoding=None)`")

# `file`: The path to the file (can be relative or absolute).
# `mode`: A string indicating how the file is to be opened. Common modes:
#   - 'r': Read (default). Opens for reading. Raises FileNotFoundError if file doesn't exist.
#   - 'w': Write. Opens for writing. Creates file if it doesn't exist, **truncates (empties)** if it does.
#   - 'a': Append. Opens for writing. Creates file if it doesn't exist, appends to end if it does.
#   - 'x': Exclusive creation. Creates a new file and opens it for writing. Raises FileExistsError if file already exists.
#   - 'b': Binary mode (e.g., 'rb', 'wb'). For non-text files (images, executables).
#   - 't': Text mode (default). For text files (explicitly 'rt', 'wt').

# `encoding`: Specifies the encoding of the file (e.g., 'utf-8', 'latin-1'). Default is platform-dependent.
#             Always explicitly specify encoding for text files to avoid issues.

file_path_write = "my_first_file.txt"
file_path_read = "my_read_file.txt"
file_path_append = "my_append_file.txt"
file_path_binary = "my_binary_data.bin"
file_path_json = "my_data.json"
file_path_csv = "my_data.csv"

# Ensure files from previous runs are clean
for f_path in [file_path_write, file_path_read, file_path_append,
               file_path_binary, file_path_json, file_path_csv]:
    if os.path.exists(f_path):
        os.remove(f_path)


# --- 2. Writing to a Text File ---
print("\n--- 2. Writing to a Text File ---")

# Mode 'w': Creates or overwrites the file
print(f"Opening '{file_path_write}' in 'w' mode to write.")
try:
    with open(file_path_write, 'w', encoding='utf-8') as f:
        f.write("This is the first line.\n")
        f.write("This is the second line.\n")
        f.write("Python makes file writing easy!\n")
    print(f"Successfully wrote to '{file_path_write}'.")
except IOError as e:
    print(f"Error writing to file: {e}")

# Mode 'a': Appends to the end of the file
print(f"\nOpening '{file_path_append}' in 'a' mode to append.")
try:
    with open(file_path_append, 'a', encoding='utf-8') as f:
        f.write("This is the first line for appending.\n")
    print(f"Successfully wrote initial content to '{file_path_append}'.")

    with open(file_path_append, 'a', encoding='utf-8') as f:
        f.write("This line is appended later.\n")
        f.write("Another appended line.\n")
    print(f"Successfully appended more content to '{file_path_append}'.")
except IOError as e:
    print(f"Error appending to file: {e}")


# --- 3. Reading from a Text File ---
print("\n--- 3. Reading from a Text File ---")

# First, create a file to read from
with open(file_path_read, 'w', encoding='utf-8') as f:
    f.write("Line 1: Hello Python!\n")
    f.write("Line 2: File I/O is fun.\n")
    f.write("Line 3: Read me carefully.\n")
print(f"Created '{file_path_read}' for reading demonstration.")

# Mode 'r': Reads from the file
print(f"\nOpening '{file_path_read}' in 'r' mode to read.")
try:
    with open(file_path_read, 'r', encoding='utf-8') as f:
        # 3.1 `f.read()`: Reads the entire content as a single string
        content = f.read()
        print("\n--- Content using f.read() ---")
        print(content)

    # Reopen to demonstrate other methods, as f.read() consumes the file pointer
    with open(file_path_read, 'r', encoding='utf-8') as f:
        # 3.2 `f.readline()`: Reads one line at a time
        print("\n--- Content using f.readline() ---")
        first_line = f.readline()
        second_line = f.readline()
        print(f"First line: {first_line.strip()}") # .strip() removes trailing newline
        print(f"Second line: {second_line.strip()}")

    with open(file_path_read, 'r', encoding='utf-8') as f:
        # 3.3 `f.readlines()`: Reads all lines into a list of strings
        print("\n--- Content using f.readlines() ---")
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"Line {i+1}: {line.strip()}")

    with open(file_path_read, 'r', encoding='utf-8') as f:
        # 3.4 Iterating directly over the file object (most memory efficient for large files)
        print("\n--- Content by iterating over file object ---")
        for i, line in enumerate(f): # File object is its own iterator
            print(f"Iterated line {i+1}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: File '{file_path_read}' not found.")
except IOError as e:
    print(f"Error reading file: {e}")


# --- 4. The `with` Statement (Context Manager) ---
print("\n--- 4. The `with` Statement (Context Manager) ---")
print("Using `with open(...) as f:` is the recommended way to handle files.")
print("It ensures that the file is automatically closed, even if errors occur, preventing resource leaks.")
print("You don't need `f.close()` explicitly.")

# All examples above already used `with` statement.
print("All examples above already demonstrated the `with` statement, which automatically closes the file.")
print("Without `with`, you'd need `f = open(...); try: ... finally: f.close()` which is more verbose.")


# --- 5. Binary File I/O (`'b'` mode) ---
print("\n--- 5. Binary File I/O (`'b'` mode) ---")
print("For non-text files (images, audio, pickled data, executables), use binary modes ('rb', 'wb', 'ab').")
print("Data is read/written as bytes, not strings.")

sample_bytes = b'\x00\x01\x02\x03\xff\xfe\xfd' # Example bytes data

print(f"\nWriting to '{file_path_binary}' in 'wb' mode.")
try:
    with open(file_path_binary, 'wb') as f:
        f.write(sample_bytes)
    print(f"Successfully wrote bytes to '{file_path_binary}'.")

    print(f"\nReading from '{file_path_binary}' in 'rb' mode.")
    with open(file_path_binary, 'rb') as f:
        read_bytes = f.read()
        print(f"Read bytes: {read_bytes}")
except IOError as e:
    print(f"Error in binary file operation: {e}")


# --- 6. Working with JSON Files ---
print("\n--- 6. Working with JSON Files ---")
print("Python's `json` module makes it easy to read/write JSON data.")

data_to_json = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"],
    "address": None
}

print(f"\nWriting JSON data to '{file_path_json}'.")
try:
    with open(file_path_json, 'w', encoding='utf-8') as f:
        json.dump(data_to_json, f, indent=4) # indent=4 for pretty printing
    print(f"Successfully wrote JSON to '{file_path_json}'.")

    print(f"\nReading JSON data from '{file_path_json}'.")
    with open(file_path_json, 'r', encoding='utf-8') as f:
        read_json_data = json.load(f)
        print(f"Read JSON data: {read_json_data}")
        print(f"Accessing 'name': {read_json_data['name']}")
except (IOError, json.JSONDecodeError) as e:
    print(f"Error with JSON file: {e}")


# --- 7. Working with CSV Files ---
print("\n--- 7. Working with CSV Files ---")
print("Python's `csv` module simplifies reading/writing comma-separated values.")

csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "24", "London"],
    ["Charlie", "35", "Paris"]
]

print(f"\nWriting CSV data to '{file_path_csv}'.")
try:
    with open(file_path_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    print(f"Successfully wrote CSV to '{file_path_csv}'.")

    print(f"\nReading CSV data from '{file_path_csv}'.")
    with open(file_path_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        read_csv_data = list(reader) # Read all rows into a list of lists
        print(f"Read CSV data:")
        for row in read_csv_data:
            print(row)
except (IOError, csv.Error) as e:
    print(f"Error with CSV file: {e}")


# --- 8. File Pointers (`f.tell()`, `f.seek()`) ---
print("\n--- 8. File Pointers (`f.tell()`, `f.seek()`) ---")
print("When reading/writing, there's an internal file pointer that indicates current position.")
print("`f.tell()`: Returns the current position of the file pointer (bytes from beginning).")
print("`f.seek(offset, whence=0)`: Changes the file pointer's position.")
print("  - `offset`: Number of bytes to move.")
print("  - `whence`: 0 (start of file, default), 1 (current position), 2 (end of file).")

with open(file_path_read, 'r+', encoding='utf-8') as f: # 'r+' mode for read and write
    print(f"\nInitial file pointer position: {f.tell()}") # 0

    content = f.read(5) # Read first 5 characters
    print(f"Read '{content}'")
    print(f"File pointer after reading 5 chars: {f.tell()}") # 5

    f.seek(0) # Move pointer back to the beginning
    print(f"File pointer after seeking to 0: {f.tell()}") # 0

    full_content = f.read()
    print(f"Read full content after seek: {full_content.strip()}")

    f.seek(0, 2) # Seek to end of file (for appending)
    print(f"File pointer after seeking to end: {f.tell()}")
    f.write("\nThis line was added at the end using seek.")
    print("Added line at the end using seek.")


# --- 9. Checking File Existence and Deleting Files ---
print("\n--- 9. Checking File Existence and Deleting Files ---")
print("The `os` module provides utilities for file system operations.")

dummy_file = "temp_delete_me.txt"
with open(dummy_file, 'w') as f:
    f.write("This file will be deleted.")

print(f"\nDoes '{dummy_file}' exist? {os.path.exists(dummy_file)}")

if os.path.exists(dummy_file):
    os.remove(dummy_file)
    print(f"Deleted '{dummy_file}'.")

print(f"Does '{dummy_file}' exist after deletion? {os.path.exists(dummy_file)}")


# --- 10. Best Practices for File I/O ---
print("\n--- 10. Best Practices for File I/O ---")
print("- **Always use `with open(...)`**: Ensures files are closed properly.")
print("- **Specify `encoding` for text files**: Prevents encoding errors across different systems.")
print("- **Handle `IOError` or `FileNotFoundError`**: Use `try...except` blocks.")
print("- **Iterate over file objects**: For large text files, `for line in f:` is most memory-efficient.")
print("- **Use appropriate modes**: `w` for new/overwrite, `a` for append, `r` for read, `b` for binary.")
print("- **Use `json` and `csv` modules**: For structured data, don't reinvent the wheel.")

print("\n--- End of Python File I/O Practice Code ---")

# Clean up all created files
for f_path in [file_path_write, file_path_read, file_path_append,
               file_path_binary, file_path_json, file_path_csv, "temp_delete_me.txt"]:
    if os.path.exists(f_path):
        os.remove(f_path)
print("\nAll demonstration files have been cleaned up.")