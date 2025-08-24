# --- 1. Opening and Closing Files ---

# The 'open()' function is used to open files.
# It returns a file object, which is then used to access methods for reading/writing.
# The 'with' statement is the recommended way to handle files, as it ensures
# the file is automatically closed even if errors occur.

print("--- 1. Opening and Closing Files ---")

# 'w' mode: write mode. Creates a new file or overwrites an existing one.
try:
    with open("my_text_file.txt", "w") as file:
        file.write("Hello, this is a test file.\n")
        file.write("This is the second line.\n")
    print("'my_text_file.txt' created and written to.")
except IOError as e:
    print(f"Error writing to file: {e}")

# 'r' mode: read mode. (default)
try:
    with open("my_text_file.txt", "r") as file:
        content = file.read()
        print("\nContent of 'my_text_file.txt':")
        print(content)
except FileNotFoundError:
    print("'my_text_file.txt' not found.")
except IOError as e:
    print(f"Error reading file: {e}")

# 'a' mode: append mode. Appends content to the end of the file. Creates if not exists.
try:
    with open("my_text_file.txt", "a") as file:
        file.write("This line was appended.\n")
    print("\nContent appended to 'my_text_file.txt'.")
except IOError as e:
    print(f"Error appending to file: {e}")

# Verify append
try:
    with open("my_text_file.txt", "r") as file:
        content = file.read()
        print("Updated content of 'my_text_file.txt':")
        print(content)
except IOError as e:
    print(f"Error reading file: {e}")


# --- 2. Reading from Files ---

print("\n--- 2. Reading from Files ---")

# read() - Reads the entire content of the file
try:
    with open("my_text_file.txt", "r") as file:
        full_content = file.read()
        print("\nUsing .read():")
        print(full_content)
except IOError as e:
    print(f"Error reading file: {e}")

# readline() - Reads a single line
try:
    with open("my_text_file.txt", "r") as file:
        first_line = file.readline()
        second_line = file.readline()
        print("\nUsing .readline():")
        print(f"First line: {first_line.strip()}") # .strip() removes leading/trailing whitespace including newline
        print(f"Second line: {second_line.strip()}")
except IOError as e:
    print(f"Error reading file: {e}")

# readlines() - Reads all lines into a list
try:
    with open("my_text_file.txt", "r") as file:
        all_lines = file.readlines()
        print("\nUsing .readlines():")
        for i, line in enumerate(all_lines):
            print(f"Line {i+1}: {line.strip()}")
except IOError as e:
    print(f"Error reading file: {e}")

# Iterating over a file object (most memory-efficient for large files)
try:
    print("\nIterating over file object (line by line):")
    with open("my_text_file.txt", "r") as file:
        for line_num, line in enumerate(file):
            print(f"Line {line_num+1}: {line.strip()}")
except IOError as e:
    print(f"Error reading file: {e}")


# --- 3. Writing to Files ---

print("\n--- 3. Writing to Files ---")

# write() - Writes a string to the file
try:
    with open("new_output.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("And this is the second line.\n")
    print("\n'new_output.txt' created with two lines.")
except IOError as e:
    print(f"Error writing to file: {e}")

# writelines() - Writes a list of strings to the file (each string should end with '\n')
try:
    lines_to_write = [
        "Line 1 from writelines\n",
        "Line 2 from writelines\n",
        "Line 3 from writelines\n"
    ]
    with open("writelines_example.txt", "w") as file:
        file.writelines(lines_to_write)
    print("\n'writelines_example.txt' created using writelines.")
except IOError as e:
    print(f"Error writing to file: {e}")


# --- 4. Binary Files (Example: Image Copy) ---
# 'rb' for read binary, 'wb' for write binary
print("\n--- 4. Binary Files (Example: Image Copy) ---")

# Create a dummy binary file for demonstration (not a real image)
try:
    with open("dummy_binary.bin", "wb") as f:
        f.write(b'\x01\x02\x03\x04\x05\xFF\xFE\xFD')
    print("Created 'dummy_binary.bin'.")
except IOError as e:
    print(f"Error creating dummy binary file: {e}")

# Copying a binary file (e.g., an image)
try:
    source_file = "dummy_binary.bin"
    destination_file = "copied_binary.bin"

    with open(source_file, "rb") as source:
        with open(destination_file, "wb") as destination:
            while True:
                chunk = source.read(4096) # Read in chunks (e.g., 4KB)
                if not chunk:
                    break
                destination.write(chunk)
    print(f"'{source_file}' copied to '{destination_file}'.")
except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
except IOError as e:
    print(f"Error handling binary file: {e}")


# --- 5. File System Operations (using os module) ---
import os

print("\n--- 5. File System Operations ---")

# Check if a file exists
file_to_check = "my_text_file.txt"
if os.path.exists(file_to_check):
    print(f"'{file_to_check}' exists.")
else:
    print(f"'{file_to_check}' does not exist.")

# Get file size
if os.path.exists(file_to_check):
    size_bytes = os.path.getsize(file_to_check)
    print(f"Size of '{file_to_check}': {size_bytes} bytes.")
else:
    print(f"Cannot get size, '{file_to_check}' does not exist.")

# Renaming a file
old_name = "new_output.txt"
new_name = "renamed_output.txt"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File '{old_name}' renamed to '{new_name}'.")
else:
    print(f"Cannot rename, '{old_name}' does not exist.")

# Deleting a file
file_to_delete = "writelines_example.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"File '{file_to_delete}' deleted.")
else:
    print(f"Cannot delete, '{file_to_delete}' does not exist.")

# Creating and removing directories
dir_name = "my_new_directory"
if not os.path.exists(dir_name):
    os.makedirs(dir_name) # Use makedirs to create intermediate directories if needed
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' already exists.")

# Clean up the created directory
if os.path.exists(dir_name):
    os.rmdir(dir_name) # rmdir only removes empty directories
    print(f"Directory '{dir_name}' removed.")


# --- 6. Error Handling ---
print("\n--- 6. Error Handling ---")

# Using try-except for robust file operations
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'non_existent_file.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")

# Example of permission error (might need to run as non-admin in a protected directory)
# try:
#     # Attempt to write to a protected system path (e.g., root on Linux, Program Files on Windows)
#     with open("/root/test_protected.txt", "w") as file: # This will likely fail due to permissions
#         file.write("Trying to write to a protected area.")
# except PermissionError:
#     print("Permission denied: Cannot write to this location.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")


# --- 7. Working with CSV Files (using csv module) ---
import csv

print("\n--- 7. Working with CSV Files ---")

# Writing to a CSV file
try:
    data_to_write = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 24, "London"],
        ["Charlie", 35, "Paris"]
    ]
    with open("my_data.csv", "w", newline='') as csvfile: # newline='' is important for CSV
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data_to_write)
    print("'my_data.csv' created.")
except IOError as e:
    print(f"Error writing CSV file: {e}")

# Reading from a CSV file
try:
    with open("my_data.csv", "r", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        print("\nContent of 'my_data.csv':")
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("'my_data.csv' not found.")
except IOError as e:
    print(f"Error reading CSV file: {e}")

# Reading CSV into a dictionary (using DictReader)
try:
    with open("my_data.csv", "r", newline='') as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        print("\nContent of 'my_data.csv' (DictReader):")
        for row in csv_dict_reader:
            print(row)
            # You can access data by column name
            # print(f"Name: {row['Name']}, Age: {row['Age']}")
except FileNotFoundError:
    print("'my_data.csv' not found.")
except IOError as e:
    print(f"Error reading CSV file with DictReader: {e}")


# --- 8. Working with JSON Files (using json module) ---
import json

print("\n--- 8. Working with JSON Files ---")

# Writing to a JSON file
data_to_json = {
    "name": "John Doe",
    "age": 40,
    "isStudent": False,
    "courses": ["History", "Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}
try:
    with open("my_data.json", "w") as jsonfile:
        json.dump(data_to_json, jsonfile, indent=4) # indent for pretty-printing
    print("'my_data.json' created.")
except IOError as e:
    print(f"Error writing JSON file: {e}")

# Reading from a JSON file
try:
    with open("my_data.json", "r") as jsonfile:
        loaded_data = json.load(jsonfile)
        print("\nContent of 'my_data.json':")
        print(loaded_data)
        print(f"Loaded name: {loaded_data['name']}")
        print(f"Loaded city: {loaded_data['address']['city']}")
except FileNotFoundError:
    print("'my_data.json' not found.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from 'my_data.json'. File might be corrupted.")
except IOError as e:
    print(f"Error reading JSON file: {e}")


# --- 9. Clean up created files ---
print("\n--- 9. Cleaning up created files ---")
files_to_clean = [
    "my_text_file.txt",
    "renamed_output.txt", # Was new_output.txt
    "dummy_binary.bin",
    "copied_binary.bin",
    "my_data.csv",
    "my_data.json"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")