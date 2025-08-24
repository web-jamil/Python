import os

print("--- Python File Operations: Practice Code ---")

# Define a directory for temporary files
output_dir = "python_file_examples"
os.makedirs(output_dir, exist_ok=True)
print(f"Temporary files will be created in: {output_dir}")


# --- 1. Opening and Closing Files (`open()` and `close()`) ---
print("\n--- 1. Opening and Closing Files ---")
print("Files must be opened before reading from or writing to them, and closed afterwards.")

file_path_basic = os.path.join(output_dir, "basic_file.txt")

# 1.1 Writing to a file (write mode 'w')
# 'w' mode: If the file exists, it's truncated (emptied). If it doesn't exist, it's created.
print(f"\nWriting to {file_path_basic} using 'w' mode...")
file_obj = open(file_path_basic, 'w')
file_obj.write("Hello, Python!\n")
file_obj.write("This is a basic file write operation.\n")
file_obj.close() # Crucial to close the file to ensure data is saved and resources are released.
print("Write complete. File closed.")

# 1.2 Reading from a file (read mode 'r')
# 'r' mode: File must exist, otherwise FileNotFoundError.
print(f"\nReading from {file_path_basic} using 'r' mode...")
file_obj = open(file_path_basic, 'r')
content = file_obj.read() # Reads the entire content of the file as a single string
print(f"Content:\n{content}")
file_obj.close()
print("Read complete. File closed.")

# 1.3 Appending to a file (append mode 'a')
# 'a' mode: If the file exists, new data is written to the end. If it doesn't exist, it's created.
print(f"\nAppending to {file_path_basic} using 'a' mode...")
file_obj = open(file_path_basic, 'a')
file_obj.write("This line was appended.\n")
file_obj.close()
print("Append complete. File closed.")

print(f"\nReading updated content from {file_path_basic}:")
with open(file_path_basic, 'r') as f:
    print(f.read())


# --- 2. Using `with` statement (Recommended for File Operations) ---
print("\n--- 2. Using `with` statement (Recommended) ---")
print("The `with` statement ensures files are properly closed, even if errors occur.")
print("It automatically handles `file_obj.close()` for you.")

file_path_with = os.path.join(output_dir, "with_file.txt")

# 2.1 Writing with `with`
print(f"\nWriting to {file_path_with} using 'w' mode with 'with' statement...")
with open(file_path_with, 'w') as f:
    f.write("This is the first line.\n")
    f.write("And this is the second line.\n")
print("Write complete. File automatically closed.")

# 2.2 Reading with `with`
print(f"\nReading from {file_path_with} using 'r' mode with 'with' statement...")
with open(file_path_with, 'r') as f:
    read_content = f.read()
    print(f"Content:\n{read_content}")
print("Read complete. File automatically closed.")


# --- 3. File Modes ---
print("\n--- 3. File Modes ---")
print("Common modes for `open(filename, mode)`:")
print(" 'r' : Read (default). Error if file doesn't exist.")
print(" 'w' : Write. Creates file if not exists. Truncates (empties) if exists.")
print(" 'a' : Append. Creates file if not exists. Appends to end if exists.")
print(" 'x' : Exclusive creation. Creates file, error if file already exists.")
print(" 'b' : Binary mode. Used with 'r', 'w', 'a' (e.g., 'rb', 'wb'). For non-text files.")
print(" '+' : Update mode. Used with 'r', 'w', 'a' to allow both reading and writing (e.g., 'r+', 'w+', 'a+').")

file_path_x = os.path.join(output_dir, "exclusive_file.txt")

# 'x' mode example
print(f"\nUsing 'x' mode for {file_path_x} (exclusive creation)...")
try:
    with open(file_path_x, 'x') as f:
        f.write("This file was created exclusively.\n")
    print("File created successfully with 'x' mode.")
except FileExistsError:
    print(f"Error: {file_path_x} already exists. 'x' mode prevented overwrite.")

# 'r+' mode example (read and write)
file_path_rplus = os.path.join(output_dir, "rplus_file.txt")
with open(file_path_rplus, 'w') as f: # First create the file
    f.write("Line 1\nLine 2\nLine 3\n")
print(f"\nInitial content of {file_path_rplus}:\nLine 1\nLine 2\nLine 3")

with open(file_path_rplus, 'r+') as f:
    f.seek(0) # Go to the beginning of the file
    first_line = f.readline()
    print(f"Read first line: '{first_line.strip()}'")
    f.write("NEW_LINE\n") # Overwrites "Line 1"
    f.seek(0) # Go back to beginning to read all
    print(f"Content after writing with 'r+':\n{f.read()}")
# Expected output for `r+`: NEW_LINE, then remaining original content

# 'wb' and 'rb' for binary files
print("\n--- 3.1 Binary File Operations ---")
# Useful for images, audio, serialized objects (e.g., pickle)
binary_file_path = os.path.join(output_dir, "binary_data.bin")
byte_data = b'\x00\x01\x02\xff\x80' # Example bytes

with open(binary_file_path, 'wb') as f:
    f.write(byte_data)
print(f"Binary data written to: {binary_file_path}")

with open(binary_file_path, 'rb') as f:
    read_bytes = f.read()
    print(f"Read binary data: {read_bytes}")
    print(f"Are read bytes equal to original? {read_bytes == byte_data}")


# --- 4. Reading File Content ---
print("\n--- 4. Reading File Content ---")
read_file_path = os.path.join(output_dir, "read_methods.txt")
sample_text = "Alpha\nBeta\nGamma\nDelta\n"
with open(read_file_path, 'w') as f:
    f.write(sample_text)
print(f"\nSample content written to {read_file_path}:")
print(sample_text.strip())

# 4.1 `read()`: Reads entire file content as a single string
with open(read_file_path, 'r') as f:
    content_all = f.read()
    print(f"read():\n'{content_all.strip()}'")

# 4.2 `readline()`: Reads one line at a time
with open(read_file_path, 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"readline() Line 1: '{line1.strip()}'")
    print(f"readline() Line 2: '{line2.strip()}'")

# 4.3 `readlines()`: Reads all lines into a list of strings
with open(read_file_path, 'r') as f:
    list_of_lines = f.readlines()
    print(f"readlines(): {list_of_lines}") # Includes newline characters
    print(f"Processed readlines(): {[line.strip() for line in list_of_lines]}")

# 4.4 Iterating over file object (most memory efficient for large files)
print("\nIterating over file object (memory efficient for large files):")
with open(read_file_path, 'r') as f:
    for i, line in enumerate(f):
        print(f"Line {i+1} (from iteration): '{line.strip()}'")


# --- 5. File Pointers and `seek()` / `tell()` ---
print("\n--- 5. File Pointers and `seek()` / `tell()` ---")
print("`tell()`: Returns the current position of the file pointer (in bytes).")
print("`seek(offset, whence)`: Changes the file pointer's position.")
print("  - `offset`: Number of bytes to move.")
print("  - `whence`: 0 (start of file), 1 (current position), 2 (end of file). Default is 0.")

seek_file_path = os.path.join(output_dir, "seek_file.txt")
with open(seek_file_path, 'w') as f:
    f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"\nContent of {seek_file_path}: ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open(seek_file_path, 'r+') as f:
    print(f"Initial position: {f.tell()}") # 0

    f.read(5) # Read 'ABCDE'
    print(f"Position after reading 5 bytes: {f.tell()}") # 5

    f.seek(10) # Move to 10th byte (index 9, character 'J')
    print(f"Position after seek(10): {f.tell()}") # 10
    print(f"Read from current position: {f.read(3)}") # Reads 'KLM'

    f.seek(0) # Go to beginning
    f.write("123") # Overwrites 'ABC'
    print(f"Position after writing '123': {f.tell()}") # 3

    f.seek(0) # Go to beginning to read all
    print(f"Final content after seek and write: {f.read()}")


# --- 6. OS Module for File and Directory Management ---
print("\n--- 6. OS Module for File and Directory Management ---")
print("The `os` module provides functions for interacting with the operating system, including file system operations.")

new_dir = os.path.join(output_dir, "new_sub_dir")
new_file_in_dir = os.path.join(new_dir, "inner_file.txt")

# 6.1 Creating Directories
if not os.path.exists(new_dir):
    os.mkdir(new_dir) # Creates a single directory
    print(f"Created directory: {new_dir}")
else:
    print(f"Directory already exists: {new_dir}")

# 6.2 Writing to a file within a created directory
with open(new_file_in_dir, 'w') as f:
    f.write("This file is in a new directory.")
print(f"Created file: {new_file_in_dir}")

# 6.3 Checking if a file/directory exists
print(f"Does '{file_path_basic}' exist? {os.path.exists(file_path_basic)}")
print(f"Is '{new_dir}' a directory? {os.path.isdir(new_dir)}")
print(f"Is '{new_file_in_dir}' a file? {os.path.isfile(new_file_in_dir)}")

# 6.4 Listing contents of a directory
print(f"Contents of '{output_dir}': {os.listdir(output_dir)}")

# 6.5 Renaming files
old_name = os.path.join(output_dir, "basic_file.txt")
new_name = os.path.join(output_dir, "renamed_file.txt")
os.rename(old_name, new_name)
print(f"Renamed '{os.path.basename(old_name)}' to '{os.path.basename(new_name)}'")

# 6.6 Deleting Files and Directories
# os.remove(file_path) for files
# os.rmdir(dir_path) for empty directories
# shutil.rmtree(dir_path) for non-empty directories (requires import shutil)

# Clean up the specific files created in this section
os.remove(new_file_in_dir)
print(f"Deleted file: {new_file_in_dir}")
os.rmdir(new_dir)
print(f"Deleted directory: {new_dir}")


# --- Cleanup All Generated Files ---
print("\n--- Cleaning up all generated files and directories ---")
try:
    for root, dirs, files in os.walk(output_dir, topdown=False):
        for name in files:
            file_to_remove = os.path.join(root, name)
            os.remove(file_to_remove)
            # print(f"Removed file: {file_to_remove}")
        for name in dirs:
            dir_to_remove = os.path.join(root, name)
            os.rmdir(dir_to_remove)
            # print(f"Removed directory: {dir_to_remove}")
    os.rmdir(output_dir)
    print(f"Successfully cleaned up '{output_dir}'.")
except OSError as e:
    print(f"Error during cleanup: {e}")

print("\n--- End of Python File Operations Practice Code ---")