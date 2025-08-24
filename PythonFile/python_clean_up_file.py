# --- Python File Cleanup: All About in Code ---

# Cleaning up created files and directories is important for:
# - Keeping your project directory tidy.
# - Freeing up disk space.
# - Ensuring subsequent runs of your script behave consistently
#   (e.g., if a script expects a file not to exist initially).

# We primarily use the `os` module for basic file operations (remove, rmdir)
# and the `shutil` module for higher-level directory operations (rmtree).

import os
import shutil

# --- 1. Setting up for Cleanup (Creating Dummy Files/Folders) ---

print("--- 1. Setting up for Cleanup (Creating Dummy Files/Folders) ---")

# Create a single file
try:
    with open("temp_file_1.txt", "w") as f:
        f.write("This is a temporary file.")
    print("Created 'temp_file_1.txt'.")
except IOError as e:
    print(f"Error creating temp_file_1.txt: {e}")

# Create another file
try:
    with open("temp_file_2.log", "w") as f:
        f.write("Another temporary file.")
    print("Created 'temp_file_2.log'.")
except IOError as e:
    print(f"Error creating temp_file_2.log: {e}")

# Create an empty directory
empty_dir = "empty_folder_to_remove"
try:
    os.makedirs(empty_dir, exist_ok=True)
    print(f"Created empty directory '{empty_dir}'.")
except OSError as e:
    print(f"Error creating '{empty_dir}': {e}")

# Create a non-empty directory with subdirectories and files
non_empty_dir = "project_temp_data"
nested_dir = os.path.join(non_empty_dir, "reports", "daily")
try:
    os.makedirs(nested_dir, exist_ok=True)
    with open(os.path.join(non_empty_dir, "config.ini"), "w") as f:
        f.write("[settings]\nkey=value")
    with open(os.path.join(nested_dir, "report_july_04_2025.txt"), "w") as f:
        f.write("Daily report data.")
    print(f"Created complex directory structure '{non_empty_dir}'.")
except IOError as e:
    print(f"Error creating complex structure: {e}")
except OSError as e:
    print(f"Error creating complex structure: {e}")

# Create a file that we'll attempt to remove but might not exist
non_existent_file = "non_existent_file_for_removal_test.tmp"
print("Will attempt to clean up 'non_existent_file_for_removal_test.tmp'.")

# --- 2. Cleaning Up Files ---

print("\n--- 2. Cleaning Up Files ---")

# os.remove(path) - Deletes a regular file.
# Raises FileNotFoundError if the file does not exist.
# Raises IsADirectoryError if the path is a directory.

# Example 2.1: Removing an existing file
try:
    os.remove("temp_file_1.txt")
    print("Removed 'temp_file_1.txt'.")
except FileNotFoundError:
    print("Error: 'temp_file_1.txt' not found (already removed or never existed).")
except OSError as e:
    print(f"Error removing 'temp_file_1.txt': {e}")


# Example 2.2: Attempting to remove a non-existent file (good practice for error handling)
try:
    os.remove(non_existent_file)
    print(f"Removed '{non_existent_file}'. (This line should not print if file didn't exist).")
except FileNotFoundError:
    print(f"Caught FileNotFoundError: '{non_existent_file}' does not exist, so cannot be removed.")
except OSError as e:
    print(f"Error removing '{non_existent_file}': {e}")


# --- 3. Cleaning Up Empty Directories ---

print("\n--- 3. Cleaning Up Empty Directories ---")

# os.rmdir(path) - Deletes an EMPTY directory.
# Raises OSError if the directory is not empty or if it does not exist.

# Example 3.1: Removing an existing empty directory
try:
    os.rmdir(empty_dir)
    print(f"Removed empty directory '{empty_dir}'.")
except FileNotFoundError:
    print(f"Error: '{empty_dir}' not found.")
except OSError as e: # This will catch if the directory is not empty
    print(f"Error removing '{empty_dir}': {e} (e.g., directory might not be empty).")


# --- 4. Cleaning Up Non-Empty Directories (Recursive Deletion) ---

print("\n--- 4. Cleaning Up Non-Empty Directories (Recursive Deletion) ---")

# shutil.rmtree(path) - Recursively deletes a directory and all its contents.
# This is a powerful function; use with EXTREME CAUTION as it cannot be undone!
# It will delete all files and subdirectories within the specified path.

# Example 4.1: Removing the complex, non-empty directory structure
try:
    shutil.rmtree(non_empty_dir)
    print(f"Removed non-empty directory '{non_empty_dir}' and all its contents using shutil.rmtree().")
except FileNotFoundError:
    print(f"Error: '{non_empty_dir}' not found for recursive removal.")
except OSError as e:
    print(f"Error removing '{non_empty_dir}' with shutil.rmtree(): {e}")


# --- 5. A General Cleanup Function/Block ---

print("\n--- 5. A General Cleanup Function/Block ---")

# It's common to have a list of files/directories to clean up at the end of a script
# or in a test suite's teardown phase.

files_and_dirs_to_clean = [
    "temp_file_2.log",
    # "empty_folder_to_remove", # Already removed in section 3
    # "project_temp_data",      # Already removed in section 4
    "another_temp_file.csv",  # Example of a file that might be created later
    "another_temp_dir"        # Example of a dir that might be created later
]

# Create some of these for the final cleanup loop
try:
    with open("another_temp_file.csv", "w") as f: f.write("a,b,c\n1,2,3")
    os.makedirs("another_temp_dir/sub", exist_ok=True)
    with open("another_temp_dir/data.txt", "w") as f: f.write("more temp data")
    print("Created additional items for general cleanup loop.")
except (IOError, OSError) as e:
    print(f"Error during setup for general cleanup: {e}")


print("\nInitiating general cleanup loop:")
for item in files_and_dirs_to_clean:
    if os.path.exists(item):
        if os.path.isfile(item):
            try:
                os.remove(item)
                print(f"  Cleaned up file: '{item}'")
            except OSError as e:
                print(f"  Error cleaning up file '{item}': {e}")
        elif os.path.isdir(item):
            try:
                # Use shutil.rmtree for directories, as they might be non-empty
                shutil.rmtree(item)
                print(f"  Cleaned up directory: '{item}'")
            except OSError as e:
                print(f"  Error cleaning up directory '{item}': {e}")
        else:
            print(f"  '{item}' exists but is not a file or directory (e.g., symlink, special file). Skipping.")
    else:
        print(f"  '{item}' does not exist. No cleanup needed.")

print("\nAll specified temporary files and directories processed for cleanup.")