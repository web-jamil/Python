# --- Python File readlines() Method: All About in Code ---

# The `readlines()` method is a method of file objects in Python.
# It reads all lines from the file and returns them as a list of strings.
# Each string in the list represents a line from the file,
# including the newline character at the end of each line (e.g., '\n', '\r\n').

import os

# --- 1. Setting up for Demo (Creating a Dummy File) ---

print("--- 1. Setting up for Demo (Creating a Dummy File) ---")

demo_file = "my_multiline_data.txt"
file_content = (
    "This is the first line.\n"
    "This is the second line with some more text.\r\n" # CRLF newline
    "Third line, short.\n"
    "\n" # An empty line
    "Fifth and final line." # No newline at the end of the last line
)

try:
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"Created '{demo_file}' for demonstration.")
except IOError as e:
    print(f"Error creating '{demo_file}': {e}")


# --- 2. Basic Usage: Reading All Lines with readlines() ---

print("\n--- 2. Basic Usage: Reading All Lines with readlines() ---")

try:
    with open(demo_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print(f"Content read using readlines() from '{demo_file}':")
    for i, line in enumerate(lines):
        # The `repr()` function shows the actual string representation, including '\n', '\r\n'
        # The `strip()` method can be used to remove leading/trailing whitespace, including newlines.
        print(f"  Line {i+1} (raw): {repr(line)}")
        print(f"  Line {i+1} (stripped): '{line.strip()}'")

    print(f"\nType of 'lines' variable: {type(lines)}")
    print(f"Number of lines read: {len(lines)}")
except FileNotFoundError:
    print(f"Error: '{demo_file}' not found.")
except IOError as e:
    print(f"Error reading '{demo_file}': {e}")


# --- 3. Memory Considerations with readlines() ---

print("\n--- 3. Memory Considerations with readlines() ---")

# `readlines()` reads the *entire* file into memory as a list of strings.
# For very large files (e.g., gigabytes), this can consume a lot of RAM
# and potentially lead to `MemoryError`.

large_file_name = "large_temp_file.txt"
num_large_lines = 100_000 # 100,000 lines
line_size_kb = 0.1 # Approximate size per line (100 bytes)
estimated_size_mb = (num_large_lines * line_size_kb) / 1024 # Convert KB to MB
print(f"Creating a simulated large file with {num_large_lines} lines (~{estimated_size_mb:.2f} MB)...")

try:
    with open(large_file_name, "w") as f:
        for i in range(num_large_lines):
            f.write(f"Line {i:07d}: This is some sample content for a large file.\n")
    print(f"Simulated large file '{large_file_name}' created.")

    # Attempt to read the large file with readlines()
    print(f"Attempting to read '{large_file_name}' with readlines()...")
    # For *extremely* large files, the following line could cause MemoryError.
    # We'll put it in a try-except block just in case, but it might run fine for 100k lines.
    try:
        with open(large_file_name, "r") as f:
            large_lines = f.readlines()
        print(f"Successfully read {len(large_lines)} lines from '{large_file_name}'.")
        # print(f"First 3 lines: {large_lines[:3]}") # Uncomment to see lines
    except MemoryError:
        print(f"Caught MemoryError: '{large_file_name}' is too large for readlines().")
    except IOError as e:
        print(f"Error reading large file: {e}")

except IOError as e:
    print(f"Error creating large_temp_file.txt: {e}")


# --- 4. Alternatives for Reading Files (Memory Efficiently) ---

print("\n--- 4. Alternatives for Reading Files (Memory Efficiently) ---")

# For large files, iterating over the file object directly or using `readline()`
# is more memory-efficient as they process line by line.

# 4.1. Iterating directly over the file object (most Pythonic and efficient)
print("\n4.1. Reading line by line by iterating over the file object:")
try:
    with open(large_file_name, "r") as file:
        line_count = 0
        for line in file: # `line` variable includes the newline character
            # Process each line here
            # print(f"  Read line (stripped): '{line.strip()}'") # Uncomment to see lines being read
            line_count += 1
            if line_count > 5: # Just print first few lines for brevity
                # print("  (truncated for brevity)...")
                pass # Continue processing without printing
        print(f"Finished iterating through {line_count} lines of '{large_file_name}'.")
except FileNotFoundError:
    print(f"Error: '{large_file_name}' not found for iteration.")
except IOError as e:
    print(f"Error iterating '{large_file_name}': {e}")


# 4.2. Using `readline()` to read one line at a time
print("\n4.2. Reading line by line using file.readline():")
try:
    with open(demo_file, "r", encoding="utf-8") as file:
        line_num = 1
        while True:
            line = file.readline() # Reads one line
            if not line: # readline() returns an empty string at EOF
                break
            print(f"  Read line {line_num}: {repr(line)}")
            line_num += 1
    print(f"Finished reading '{demo_file}' using readline().")
except FileNotFoundError:
    print(f"Error: '{demo_file}' not found for readline().")
except IOError as e:
    print(f"Error reading '{demo_file}' with readline(): {e}")


# --- 5. When to Use readlines() ---

print("\n--- 5. When to Use readlines() ---")

# `readlines()` is appropriate when:
# - The file is relatively small and can comfortably fit into memory.
# - You need to perform operations that require all lines to be available
#   simultaneously (e.g., sorting all lines, then writing them back).
# - You want to quickly get all lines into a list for further list-based processing.

# Example: Reading, sorting, and writing back
sort_file = "lines_to_sort.txt"
try:
    with open(sort_file, "w") as f:
        f.write("zebra\n")
        f.write("apple\n")
        f.write("banana\n")
        f.write("cat\n")
    print(f"Created '{sort_file}' for sorting demo.")

    with open(sort_file, "r") as f:
        all_lines = f.readlines() # Read all into memory
    print(f"Original lines: {all_lines}")

    all_lines.sort() # Sort the list of lines
    print(f"Sorted lines: {all_lines}")

    with open(sort_file, "w") as f:
        f.writelines(all_lines) # Write sorted lines back (writelines expects iterable of strings)
    print(f"Sorted lines written back to '{sort_file}'.")

    # Verify content
    with open(sort_file, "r") as f:
        print(f"Content of '{sort_file}' after sort: {f.read().strip()}")
except IOError as e:
    print(f"Error during sort demo: {e}")


# --- 6. Clean up created files ---

print("\n--- 6. Cleaning up created files ---")
files_to_clean = [
    demo_file,
    large_file_name,
    sort_file
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")