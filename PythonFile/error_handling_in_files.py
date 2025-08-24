# --- Python File System Operations: All About in Code ---

# The `os` module provides a way of using operating system dependent
# functionality, such as reading or writing to the file system.
# The `shutil` module provides higher-level file operations, like copying
# entire directories, which are not available in the `os` module.

import os
import shutil
import time # For demonstrating modification times

# --- 1. Getting Current Working Directory ---

print("--- 1. Getting Current Working Directory ---")
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")


# --- 2. Changing Directory ---

print("\n--- 2. Changing Directory ---")
# Create a temporary directory to change into
temp_dir = "my_temp_fs_dir"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
    print(f"Created directory: {temp_dir}")

original_dir = os.getcwd() # Store original directory to return later
try:
    os.chdir(temp_dir)
    print(f"Changed current directory to: {os.getcwd()}")
    # Now operations like open("file.txt", "w") would create file inside my_temp_fs_dir
except OSError as e:
    print(f"Error changing directory: {e}")
finally:
    os.chdir(original_dir) # Change back to original directory
    print(f"Changed back to original directory: {os.getcwd()}")


# --- 3. Listing Directory Contents ---

print("\n--- 3. Listing Directory Contents ---")

# Create some dummy files and directories for demonstration
os.makedirs("my_dir_to_list/subdir1", exist_ok=True)
os.makedirs("my_dir_to_list/subdir2", exist_ok=True)
with open("my_dir_to_list/file1.txt", "w") as f: f.write("content")
with open("my_dir_to_list/file2.log", "w") as f: f.write("log content")

# os.listdir(path='.') - Returns a list containing the names of the entries in the directory.
# Does not include '.' and '..'. Names are listed in arbitrary order.
print(f"Contents of '{os.path.join(os.getcwd(), 'my_dir_to_list')}':")
for item in os.listdir("my_dir_to_list"):
    print(f"  - {item}")

# os.walk(top) - Generates the file names in a directory tree by walking the tree
# top-down or bottom-up. For each directory in the tree rooted at directory `top`
# (including `top` itself), it yields a 3-tuple: (dirpath, dirnames, filenames).
print("\nWalking through 'my_dir_to_list' using os.walk():")
for dirpath, dirnames, filenames in os.walk("my_dir_to_list"):
    print(f"  Directory: {dirpath}")
    print(f"    Subdirectories: {dirnames}")
    print(f"    Files: {filenames}")


# --- 4. Creating Directories ---

print("\n--- 4. Creating Directories ---")

# os.mkdir(path) - Creates a single directory. Raises FileExistsError if it already exists.
try:
    os.mkdir("single_new_dir")
    print("Created 'single_new_dir'.")
except FileExistsError:
    print("'single_new_dir' already exists.")
except OSError as e:
    print(f"Error creating single directory: {e}")

# os.makedirs(path, exist_ok=False) - Creates all intermediate-level directories needed.
# If `exist_ok` is True, no error is raised if the target directory already exists.
try:
    os.makedirs("path/to/nested/new_dir", exist_ok=True)
    print("Created 'path/to/nested/new_dir' (including intermediate directories).")
except FileExistsError: # Only raised if exist_ok=False
    print("'path/to/nested/new_dir' already exists (should not happen with exist_ok=True).")
except OSError as e:
    print(f"Error creating nested directories: {e}")


# --- 5. Removing Files and Directories ---

print("\n--- 5. Removing Files and Directories ---")

# Create dummy files/dirs for removal
with open("file_to_delete.txt", "w") as f: f.write("delete me")
os.makedirs("empty_dir_to_remove", exist_ok=True)
os.makedirs("non_empty_dir_to_remove/subdir", exist_ok=True)
with open("non_empty_dir_to_remove/file_in_dir.txt", "w") as f: f.write("content")


# os.remove(path) - Removes (deletes) a file.
try:
    os.remove("file_to_delete.txt")
    print("Removed 'file_to_delete.txt'.")
except FileNotFoundError:
    print("'file_to_delete.txt' not found (already removed or never existed).")
except OSError as e:
    print(f"Error removing file: {e}")


# os.rmdir(path) - Removes an EMPTY directory. Raises OSError if directory is not empty.
try:
    os.rmdir("empty_dir_to_remove")
    print("Removed 'empty_dir_to_remove'.")
except OSError as e:
    print(f"Error removing empty directory: {e}")


# shutil.rmtree(path) - Recursively deletes a directory and all its contents. Use with extreme caution!
try:
    shutil.rmtree("non_empty_dir_to_remove")
    print("Removed 'non_empty_dir_to_remove' and its contents using shutil.rmtree().")
except FileNotFoundError:
    print("'non_empty_dir_to_remove' not found.")
except OSError as e:
    print(f"Error removing non-empty directory with shutil.rmtree(): {e}")


# --- 6. Renaming and Moving Files/Directories ---

print("\n--- 6. Renaming and Moving Files/Directories ---")

# Create dummy for rename/move
with open("old_name.txt", "w") as f: f.write("rename me")
os.makedirs("original_location/sub", exist_ok=True)
with open("original_location/sub/file_to_move.txt", "w") as f: f.write("move me")


# os.rename(src, dst) - Renames a file or directory. If dst exists and is a file, it will be overwritten.
try:
    os.rename("old_name.txt", "new_name.txt")
    print("Renamed 'old_name.txt' to 'new_name.txt'.")
except FileNotFoundError:
    print("Original file for rename 'old_name.txt' not found.")
except OSError as e:
    print(f"Error renaming file: {e}")


# shutil.move(src, dst) - Recursively moves a file or directory (src) to another location (dst).
# If dst is an existing directory, src is moved inside it.
# If dst does not exist or is a file, src is renamed to dst.
try:
    shutil.move("original_location/sub/file_to_move.txt", "new_location_for_file.txt")
    print("Moved 'original_location/sub/file_to_move.txt' to 'new_location_for_file.txt'.")
    # Clean up the now empty sub-directory
    os.rmdir("original_location/sub")
    os.rmdir("original_location")
except FileNotFoundError:
    print("Source file for move 'original_location/sub/file_to_move.txt' not found.")
except OSError as e:
    print(f"Error moving file: {e}")


# --- 7. Copying Files and Directories ---

print("\n--- 7. Copying Files and Directories ---")

# Create dummy for copy
with open("file_to_copy.txt", "w") as f: f.write("copy me")
os.makedirs("dir_to_copy/nested", exist_ok=True)
with open("dir_to_copy/nested/file_in_nested.txt", "w") as f: f.write("nested copy")


# shutil.copy(src, dst) - Copies the file `src` to the file or directory `dst`.
# If `dst` is a directory, the file will be copied into `dst` with the same basename.
# If `dst` is a file, it will be overwritten.
try:
    shutil.copy("file_to_copy.txt", "copied_file.txt") # Copy to a new file name
    print("Copied 'file_to_copy.txt' to 'copied_file.txt'.")
    shutil.copy("file_to_copy.txt", "my_temp_fs_dir/") # Copy into an existing directory
    print("Copied 'file_to_copy.txt' into 'my_temp_fs_dir/'.")
except FileNotFoundError:
    print("Source file for copy 'file_to_copy.txt' not found.")
except OSError as e:
    print(f"Error copying file: {e}")


# shutil.copytree(src, dst) - Recursively copies an entire directory tree.
# `dst` must not already exist. Raises FileExistsError if `dst` exists.
try:
    shutil.copytree("dir_to_copy", "copied_directory_tree")
    print("Copied 'dir_to_copy' to 'copied_directory_tree' using shutil.copytree().")
except FileExistsError:
    print("Destination directory 'copied_directory_tree' already exists for copytree.")
except OSError as e:
    print(f"Error copying directory tree: {e}")


# --- 8. Checking Path Existence and Types ---

print("\n--- 8. Checking Path Existence and Types ---")

# os.path module has various utility functions for path manipulation and checks.

# os.path.exists(path) - Returns True if path refers to an existing path or an open file descriptor.
print(f"Does 'new_name.txt' exist? {os.path.exists('new_name.txt')}")
print(f"Does 'non_existent_file.txt' exist? {os.path.exists('non_existent_file.txt')}")
print(f"Does 'copied_directory_tree' exist? {os.path.exists('copied_directory_tree')}")

# os.path.isfile(path) - Returns True if path is an existing regular file.
print(f"Is 'new_name.txt' a file? {os.path.isfile('new_name.txt')}")
print(f"Is 'copied_directory_tree' a file? {os.path.isfile('copied_directory_tree')}")

# os.path.isdir(path) - Returns True if path is an existing directory.
print(f"Is 'new_name.txt' a directory? {os.path.isdir('new_name.txt')}")
print(f"Is 'copied_directory_tree' a directory? {os.path.isdir('copied_directory_tree')}")

# os.path.islink(path) - Returns True if path refers to a symbolic link.
# (Requires creating a symlink for demonstration)
symlink_target = "new_name.txt"
symlink_name = "mylink.txt"
if hasattr(os, 'symlink') and os.path.exists(symlink_target): # Check if symlinks are supported
    try:
        os.symlink(symlink_target, symlink_name)
        print(f"Created symlink '{symlink_name}' pointing to '{symlink_target}'.")
        print(f"Is '{symlink_name}' a symlink? {os.path.islink(symlink_name)}")
    except OSError as e:
        print(f"Could not create symlink (e.g., permissions, Windows non-admin): {e}")
else:
    print("Symlinks not supported or target does not exist for symlink creation.")


# --- 9. Getting Path Components ---

print("\n--- 9. Getting Path Components ---")

full_path_example = "/home/user/documents/report.pdf" # Linux/macOS style
# full_path_example = "C:\\Users\\user\\Documents\\report.pdf" # Windows style

# os.path.basename(path) - Returns the final component of a pathname.
print(f"Basename of '{full_path_example}': {os.path.basename(full_path_example)}")

# os.path.dirname(path) - Returns the directory portion of a pathname.
print(f"Dirname of '{full_path_example}': {os.path.dirname(full_path_example)}")

# os.path.split(path) - Splits the pathname into a pair (head, tail).
head, tail = os.path.split(full_path_example)
print(f"Split of '{full_path_example}': head='{head}', tail='{tail}'")

# os.path.splitext(path) - Splits the pathname into a pair (root, ext) where ext is empty or starts with a dot.
root, ext = os.path.splitext(full_path_example)
print(f"Splitext of '{full_path_example}': root='{root}', ext='{ext}'")

# os.path.join(path, ...) - Joins one or more path components intelligently.
# It handles separators correctly for the current OS.
joined_path = os.path.join("my_new_folder", "subfolder", "data.csv")
print(f"Joined path: {joined_path}") # Will be 'my_new_folder/subfolder/data.csv' on Linux, 'my_new_folder\subfolder\data.csv' on Windows


# --- 10. Getting File/Directory Metadata (Stats) ---

print("\n--- 10. Getting File/Directory Metadata (Stats) ---")

# os.stat(path) - Returns a stat_result object with information about the path.
# Contains: st_size (size in bytes), st_mtime (last modification time), st_ctime (creation/last metadata change time), etc.
try:
    file_stat = os.stat("new_name.txt")
    print(f"\nStats for 'new_name.txt':")
    print(f"  Size: {file_stat.st_size} bytes")
    # st_mtime, st_ctime are timestamps (seconds since epoch), convert to readable format
    print(f"  Last modified: {time.ctime(file_stat.st_mtime)}")
    print(f"  Creation time (or last metadata change): {time.ctime(file_stat.st_ctime)}")
    print(f"  Is it a directory? {os.path.isdir('new_name.txt')}") # This uses os.path directly
    print(f"  Is it a regular file? {os.path.isfile('new_name.txt')}") # This uses os.path directly

    dir_stat = os.stat("my_temp_fs_dir")
    print(f"\nStats for 'my_temp_fs_dir':")
    print(f"  Last modified: {time.ctime(dir_stat.st_mtime)}")
except FileNotFoundError:
    print("File/directory for stats not found.")
except OSError as e:
    print(f"Error getting file stats: {e}")

# os.path.getsize(path) - Returns the size of the file in bytes.
try:
    print(f"\nSize of 'new_name.txt': {os.path.getsize('new_name.txt')} bytes")
except FileNotFoundError:
    print("File 'new_name.txt' not found for getsize.")

# os.path.getmtime(path) - Returns the time of last modification of path.
try:
    mtime = os.path.getmtime("new_name.txt")
    print(f"Last modification time of 'new_name.txt': {time.ctime(mtime)}")
except FileNotFoundError:
    print("File 'new_name.txt' not found for getmtime.")


# --- 11. Error Handling in File System Operations ---

print("\n--- 11. Error Handling ---")

# Always use try-except blocks to handle potential OS errors.
try:
    os.remove("definitely_non_existent_file_for_error_test.txt")
except FileNotFoundError:
    print("Caught FileNotFoundError: Tried to remove a non-existent file.")
except OSError as e:
    print(f"Caught an OSError during file removal: {e}")

try:
    os.rmdir("non_empty_dir_cannot_rmdir")
except OSError as e: # This will be OSError if it's not empty
    print(f"Caught OSError: Tried to rmdir a non-empty directory. Error: {e}")


# --- 12. Clean up created files and directories ---
print("\n--- 12. Cleaning up created files and directories ---")

files_and_dirs_to_clean = [
    "my_temp_fs_dir",
    "my_dir_to_list",
    "single_new_dir",
    "path", # This will remove 'path/to/nested/new_dir' recursively
    "new_name.txt", # Was old_name.txt
    "new_location_for_file.txt", # Was original_location/sub/file_to_move.txt
    "file_to_copy.txt",
    "copied_file.txt",
    "dir_to_copy",
    "copied_directory_tree",
    "mylink.txt" # If symlink was created
]

for item in files_and_dirs_to_clean:
    if os.path.exists(item):
        if os.path.isfile(item) or os.path.islink(item):
            os.remove(item)
            print(f"Cleaned up file/symlink: {item}")
        elif os.path.isdir(item):
            shutil.rmtree(item) # Use rmtree for directories, as they might be non-empty
            print(f"Cleaned up directory: {item}")

print("All temporary files and directories cleaned up.")