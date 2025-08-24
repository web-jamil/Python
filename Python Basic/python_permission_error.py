import os
import sys
import stat # For changing file permissions

# --- 1. Basic PermissionError when trying to write to a read-only file ---

def basic_permission_error_write_readonly():
    print("\n--- 1. Basic PermissionError (Write to Read-Only) ---")
    
    # Create a test file
    test_file = "test_read_only.txt"
    with open(test_file, 'w') as f:
        f.write("Original content.")
    print(f"  Created '{test_file}'.")

    # Change permissions to read-only for the owner
    # os.chmod(path, mode): mode uses octal numbers like 0o444
    # 0o444 means read-only for owner, group, others
    # 0o666 means read/write for owner, group, others (default for new files)
    try:
        os.chmod(test_file, 0o444) 
        print(f"  Changed '{test_file}' to read-only (0o444).")
    except OSError as e:
        print(f"  [WARNING] Could not change permissions to read-only: {e}")
        print("  Skipping this part of the demo, as permissions might not be settable as expected.")
        # On Windows, os.chmod might not fully restrict write access for owner this way.
        # It's more about "read-only attribute" than Unix-like permissions.
        return # Exit the function if chmod failed

    try:
        print(f"  Attempting to write to '{test_file}'...")
        with open(test_file, 'a') as f: # 'a' for append, 'w' for write
            f.write("\nAttempted to append new content.")
        print("  Successfully wrote to file (this might happen on Windows despite chmod 0o444).")
    except PermissionError:
        print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to write to '{test_file}'.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        # Clean up: Make writable before deleting on Unix-like systems
        try:
            os.chmod(test_file, 0o666) 
            os.remove(test_file)
            print(f"  Cleaned up '{test_file}'.")
        except OSError as e:
            print(f"  [ERROR] Could not clean up '{test_file}': {e}")
        print("  Basic write-to-read-only demonstration finished.")

# --- 2. PermissionError when trying to delete a file without delete permission ---
# (More subtle, often tied to directory permissions or file being in use)

def permission_error_delete_no_permission():
    print("\n--- 2. PermissionError (Delete No Permission) ---")
    
    test_dir = "protected_dir"
    test_file_in_dir = os.path.join(test_dir, "protected_file.txt")
    
    try:
        os.makedirs(test_dir, exist_ok=True)
        with open(test_file_in_dir, 'w') as f:
            f.write("Content of protected file.")
        print(f"  Created '{test_dir}' and '{test_file_in_dir}'.")

        # On Unix-like systems, if a directory is read-only, you can't delete files within it.
        # Or if the file itself has immutable flags set (rare via os.chmod).
        # We'll make the DIRECTORY unwritable for owner to prevent file deletion within it.
        try:
            os.chmod(test_dir, 0o555) # Read-only, execute for directory (no write permission for owner)
            print(f"  Changed '{test_dir}' permissions to 0o555 (read/execute only).")
        except OSError as e:
            print(f"  [WARNING] Could not set directory permissions to 0o555: {e}")
            print("  Skipping this part of the demo due to permission setting issue.")
            # Ensure cleanup if this warning occurs before returning
            os.chmod(test_dir, 0o777)
            os.remove(test_file_in_dir)
            os.rmdir(test_dir)
            return

        try:
            print(f"  Attempting to delete '{test_file_in_dir}'...")
            os.remove(test_file_in_dir)
            print("  Successfully deleted file (this should not happen if permissions are set).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to delete '{test_file_in_dir}'.")
            print("    This often happens if the directory containing the file is not writable.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            # Clean up: Make directory writable again, then delete file and directory
            try:
                os.chmod(test_dir, 0o777) # Make writable
                if os.path.exists(test_file_in_dir):
                    os.remove(test_file_in_dir)
                    print(f"  Cleaned up '{test_file_in_dir}'.")
                if os.path.exists(test_dir):
                    os.rmdir(test_dir)
                    print(f"  Cleaned up '{test_dir}'.")
            except OSError as e:
                print(f"  [ERROR] Could not clean up '{test_dir}': {e}")
            print("  Delete no permission demonstration finished.")

    except Exception as e:
        print(f"  [SETUP ERROR] An error occurred during setup: {e}")
        # Ensure cleanup even if setup fails
        if os.path.exists(test_file_in_dir):
            os.remove(test_file_in_dir)
        if os.path.exists(test_dir):
            os.rmdir(test_dir)


# --- 3. PermissionError when trying to rename/move files between protected locations ---

def permission_error_rename():
    print("\n--- 3. PermissionError (Rename/Move) ---")
    
    src_dir = "src_writable"
    dest_dir = "dest_protected"
    src_file = os.path.join(src_dir, "file_to_move.txt")
    dest_file = os.path.join(dest_dir, "file_to_move.txt")

    try:
        os.makedirs(src_dir, exist_ok=True)
        os.makedirs(dest_dir, exist_ok=True)
        with open(src_file, 'w') as f:
            f.write("Content to be moved.")
        print(f"  Created '{src_dir}' and '{src_file}'.")
        print(f"  Created '{dest_dir}'.")

        # Make destination directory read-only (no write permission)
        try:
            os.chmod(dest_dir, 0o555) # r-x for all, no write
            print(f"  Changed '{dest_dir}' permissions to 0o555 (read/execute only).")
        except OSError as e:
            print(f"  [WARNING] Could not set '{dest_dir}' permissions: {e}")
            print("  Skipping this part of the demo due to permission setting issue.")
            # Ensure cleanup if this warning occurs before returning
            os.chmod(dest_dir, 0o777)
            os.remove(src_file)
            os.rmdir(src_dir)
            os.rmdir(dest_dir)
            return

        try:
            print(f"  Attempting to rename/move '{src_file}' to '{dest_file}'...")
            os.rename(src_file, dest_file)
            print("  Successfully renamed/moved file (this should not happen).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to write to '{dest_dir}' for rename.")
        except FileNotFoundError:
            print(f"  [ERROR] FileNotFoundError (unexpected): Source file not found.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            # Clean up: Make dest_dir writable, then remove files/dirs
            try:
                os.chmod(dest_dir, 0o777)
                if os.path.exists(src_file):
                    os.remove(src_file)
                if os.path.exists(dest_file):
                    os.remove(dest_file)
                if os.path.exists(src_dir):
                    os.rmdir(src_dir)
                if os.path.exists(dest_dir):
                    os.rmdir(dest_dir)
                print("  Cleaned up directories and files.")
            except OSError as e:
                print(f"  [ERROR] Could not clean up: {e}")
            print("  Rename/move permission demonstration finished.")

    except Exception as e:
        print(f"  [SETUP ERROR] An error occurred during setup: {e}")
        # Ensure cleanup even if setup fails
        if os.path.exists(src_file): os.remove(src_file)
        if os.path.exists(dest_file): os.remove(dest_file)
        if os.path.exists(src_dir): os.rmdir(src_dir)
        if os.path.exists(dest_dir): os.rmdir(dest_dir)


# --- 4. PermissionError when trying to access a blocked network share / protected system file ---
# This is hard to simulate generically without actual system setup, so we'll
# use a non-existent, typically protected system path as an example.
# On Windows, you might use 'C:\Windows\System32\config\SAM' (requires admin)
# On Unix, you might use '/etc/sudoers' or a root-owned directory.

def permission_error_system_access():
    print("\n--- 4. PermissionError (System File Access) ---")
    
    # Choose a path that usually requires elevated privileges
    if sys.platform.startswith('win'):
        protected_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'System32', 'config', 'SAM')
    else: # Unix-like systems
        protected_path = '/etc/sudoers'
    
    print(f"  Attempting to read a highly protected system file: '{protected_path}'...")
    try:
        with open(protected_path, 'r') as f:
            content = f.read(100) # Read only first 100 bytes
            print(f"  Successfully read (partial) content from '{protected_path}':\n{content}...")
            print("  [WARNING] You might be running with elevated privileges if this succeeded unexpectedly.")
    except FileNotFoundError:
        print(f"  [INFO] File '{protected_path}' not found (expected on some systems or virtual environments).")
    except PermissionError:
        print(f"  [CAUGHT ERROR] PermissionError: Access denied to '{protected_path}'.")
        print("    This is the expected behavior for protected system files without elevated permissions.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  System file access demonstration finished.")

# --- 5. Handling PermissionError Gracefully ---

def handle_permission_error_gracefully():
    print("\n--- 5. Handling PermissionError Gracefully ---")
    
    safe_file = "my_app_log.txt"
    protected_file = "protected_log.txt" # This will be made read-only

    # Create safe file
    with open(safe_file, 'w') as f:
        f.write("Log start.")
    print(f"  Created '{safe_file}'.")

    # Create protected file and make it read-only
    try:
        with open(protected_file, 'w') as f:
            f.write("Important system log.")
        os.chmod(protected_file, 0o444)
        print(f"  Created and set '{protected_file}' to read-only.")
    except OSError as e:
        print(f"  [WARNING] Could not set '{protected_file}' to read-only: {e}")
        # Proceed anyway, the write attempt might still fail or succeed depending on OS
        pass 

    files_to_try = [safe_file, protected_file]

    for file_path in files_to_try:
        try:
            print(f"\n  Attempting to append to '{file_path}'...")
            with open(file_path, 'a') as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\nLog entry at {timestamp}.")
            print(f"  [SUCCESS] Appended to '{file_path}'.")
        except PermissionError:
            print(f"  [HANDLED] PermissionError: Cannot write to '{file_path}'. Check file permissions or run as administrator.")
            # Log the error, notify user, try alternative, etc.
        except FileNotFoundError:
            print(f"  [HANDLED] FileNotFoundError: '{file_path}' does not exist. Creating it...")
            try:
                with open(file_path, 'w') as f:
                    f.write("New file created.")
                print(f"  Successfully created new file '{file_path}'.")
            except PermissionError:
                print(f"  [ERROR] Even creating '{file_path}' failed due to permissions.")
            except Exception as e:
                print(f"  [ERROR] Failed to create '{file_path}': {e}")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] While processing '{file_path}': {type(e).__name__} - {e}")
    finally:
        # Clean up all files
        for f_path in files_to_try:
            if os.path.exists(f_path):
                # Ensure writable before deleting
                try:
                    os.chmod(f_path, 0o666)
                    os.remove(f_path)
                    print(f"  Cleaned up '{f_path}'.")
                except OSError as e:
                    print(f"  [ERROR] Could not clean up '{f_path}': {e}")
        print("  Graceful handling demonstration finished.")

# --- Main execution block ---
if __name__ == "__main__":
    import time

    basic_permission_error_write_readonly()
    input("\nPress Enter to run the next example: PermissionError (Delete No Permission)...")
    
    permission_error_delete_no_permission()
    input("\nPress Enter to run the next example: PermissionError (Rename/Move)...")
    
    permission_error_rename()
    input("\nPress Enter to run the next example: PermissionError (System Access)...")
    
    permission_error_system_access()
    input("\nPress Enter to run the next example: Handling PermissionError Gracefully...")

    handle_permission_error_gracefully()
    
    print("\nAll PermissionError demonstrations concluded.")


import os
import sys
import stat # For changing file permissions
import time # For timestamping logs

# --- Base Class for File System Operations ---
class FileSystemDemoBase:
    def __init__(self, demo_name):
        self.demo_name = demo_name
        print(f"\n--- {self.demo_name} ---")

    def _create_file(self, path, content="Default content."):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            print(f"  Created file: '{path}'.")
            return True
        except Exception as e:
            print(f"  [ERROR] Failed to create '{path}': {e}")
            return False

    def _cleanup_path(self, path):
        if os.path.exists(path):
            try:
                # For directories, try rmdir, for files, try remove
                if os.path.isfile(path):
                    # Ensure writeable before removing if it was made read-only
                    try:
                        os.chmod(path, 0o666) 
                    except OSError:
                        pass # Ignore if already writable or cannot change
                    os.remove(path)
                    print(f"  Cleaned up file: '{path}'.")
                elif os.path.isdir(path):
                    # Make directory writable to delete its contents and itself
                    try:
                        os.chmod(path, 0o777) 
                    except OSError:
                        pass 
                    # If directory is not empty, rmdir will fail.
                    # For a full recursive delete, use shutil.rmtree (not used here for simplicity).
                    if not os.listdir(path): # Check if empty before rmdir
                        os.rmdir(path)
                        print(f"  Cleaned up directory: '{path}'.")
                    else:
                        print(f"  [WARNING] Directory '{path}' not empty, skipping rmdir cleanup.")
            except Exception as e:
                print(f"  [ERROR] Failed to clean up '{path}': {e}")

# --- 1. Class for Basic PermissionError (Write to Read-Only) ---
class ReadOnlyWriteDemo(FileSystemDemoBase):
    def __init__(self):
        super().__init__("1. Basic PermissionError (Write to Read-Only)")
        self.test_file = "read_only_demo_file.txt"

    def run(self):
        self._create_file(self.test_file, "Original content for read-only test.")

        # Change permissions to read-only for the owner
        try:
            os.chmod(self.test_file, 0o444) # r--r--r--
            print(f"  Changed '{self.test_file}' to read-only (0o444).")
        except OSError as e:
            print(f"  [WARNING] Could not set '{self.test_file}' to read-only: {e}")
            print("  Skipping write attempt as permissions might not be settable as expected.")
            self._cleanup_path(self.test_file)
            return

        try:
            print(f"  Attempting to write to '{self.test_file}'...")
            with open(self.test_file, 'a') as f: # 'a' for append, 'w' for write
                f.write(f"\nAttempted append at {time.strftime('%H:%M:%S')}.")
            print("  [SUCCESS] Successfully wrote to file (unexpected on Unix-like, possible on Windows).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to write to '{self.test_file}'.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            self._cleanup_path(self.test_file)
            print(f"  {self.demo_name} finished.")

# --- 2. Class for PermissionError (Delete No Permission) ---
class NoDeletePermissionDemo(FileSystemDemoBase):
    def __init__(self):
        super().__init__("2. PermissionError (Delete No Permission)")
        self.test_dir = "protected_delete_dir"
        self.test_file_in_dir = os.path.join(self.test_dir, "protected_file.txt")

    def run(self):
        self._create_file(self.test_file_in_dir, "Content of protected file.")

        # Make the parent directory unwritable to prevent deletion of contents
        try:
            # r-xr-xr-x (read, execute, but no write for owner)
            os.chmod(self.test_dir, 0o555) 
            print(f"  Changed directory '{self.test_dir}' permissions to 0o555 (no write).")
        except OSError as e:
            print(f"  [WARNING] Could not set directory permissions to 0o555: {e}")
            print("  Skipping delete attempt due to permission setting issue.")
            self._cleanup_path(self.test_file_in_dir)
            self._cleanup_path(self.test_dir)
            return

        try:
            print(f"  Attempting to delete '{self.test_file_in_dir}'...")
            os.remove(self.test_file_in_dir)
            print("  [SUCCESS] Successfully deleted file (this should not happen).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to delete '{self.test_file_in_dir}'.")
            print("    This is typically because the parent directory is not writable.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            # Restore directory write permission for cleanup
            os.chmod(self.test_dir, 0o777)
            self._cleanup_path(self.test_file_in_dir)
            self._cleanup_path(self.test_dir)
            print(f"  {self.demo_name} finished.")

# --- 3. Class for PermissionError (Rename/Move) ---
class RenamePermissionDemo(FileSystemDemoBase):
    def __init__(self):
        super().__init__("3. PermissionError (Rename/Move)")
        self.src_dir = "src_writable_for_rename"
        self.dest_dir = "dest_protected_for_rename"
        self.src_file = os.path.join(self.src_dir, "file_to_move.txt")
        self.dest_file = os.path.join(self.dest_dir, "file_to_move.txt")

    def run(self):
        self._create_file(self.src_file, "Content to be moved.")
        os.makedirs(self.dest_dir, exist_ok=True)
        print(f"  Created directory: '{self.dest_dir}'.")

        # Make destination directory read-only to prevent writing into it (for rename/move)
        try:
            os.chmod(self.dest_dir, 0o555) 
            print(f"  Changed destination directory '{self.dest_dir}' to 0o555 (read/execute only).")
        except OSError as e:
            print(f"  [WARNING] Could not set '{self.dest_dir}' permissions: {e}")
            print("  Skipping rename attempt due to permission setting issue.")
            self._cleanup_path(self.src_file)
            self._cleanup_path(self.dest_dir)
            self._cleanup_path(self.src_dir)
            return

        try:
            print(f"  Attempting to rename/move '{self.src_file}' to '{self.dest_file}'...")
            os.rename(self.src_file, self.dest_file)
            print("  [SUCCESS] Successfully renamed/moved file (this should not happen).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Insufficient permissions to write to '{self.dest_dir}' for rename.")
        except FileNotFoundError:
            print(f"  [ERROR] FileNotFoundError (unexpected): Source file not found.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            # Restore permissions for cleanup
            os.chmod(self.dest_dir, 0o777)
            self._cleanup_path(self.src_file)
            self._cleanup_path(self.dest_file)
            self._cleanup_path(self.src_dir)
            self._cleanup_path(self.dest_dir)
            print(f"  {self.demo_name} finished.")

# --- 4. Class for PermissionError (System File Access) ---
class SystemAccessDemo(FileSystemDemoBase):
    def __init__(self):
        super().__init__("4. PermissionError (System File Access)")
        if sys.platform.startswith('win'):
            # Path to a typically protected system file on Windows
            self.protected_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'System32', 'config', 'SAM')
        else: # Unix-like systems
            # Path to a typically protected system file on Unix/Linux
            self.protected_path = '/etc/sudoers'

    def run(self):
        print(f"  Attempting to read a highly protected system file: '{self.protected_path}'...")
        try:
            with open(self.protected_path, 'r') as f:
                content = f.read(100) # Read only first 100 bytes
                print(f"  [SUCCESS] Successfully read (partial) content from '{self.protected_path}':\n{content}...")
                print("  [WARNING] You might be running with elevated privileges if this succeeded unexpectedly.")
        except FileNotFoundError:
            print(f"  [INFO] File '{self.protected_path}' not found (expected on some systems or in restricted environments).")
        except PermissionError:
            print(f"  [CAUGHT ERROR] PermissionError: Access denied to '{self.protected_path}'.")
            print("    This is the expected behavior for protected system files without elevated permissions.")
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
        finally:
            print(f"  {self.demo_name} finished.")

# --- 5. Class for Handling PermissionError Gracefully ---
class GracefulPermissionHandler(FileSystemDemoBase):
    def __init__(self):
        super().__init__("5. Handling PermissionError Gracefully")
        self.safe_file = "my_app_log.txt"
        self.protected_file = "protected_app_log.txt"

    def run(self):
        # Create safe file
        self._create_file(self.safe_file, "Log start.")

        # Create protected file and make it read-only
        self._create_file(self.protected_file, "Important system log.")
        try:
            os.chmod(self.protected_file, 0o444)
            print(f"  Set '{self.protected_file}' to read-only.")
        except OSError as e:
            print(f"  [WARNING] Could not set '{self.protected_file}' to read-only: {e}")
            # Continue anyway, the write attempt might still fail or succeed depending on OS
            pass 

        files_to_try = [self.safe_file, self.protected_file, "non_existent_yet.txt"]

        for file_path in files_to_try:
            try:
                print(f"\n  Attempting to append to '{file_path}'...")
                with open(file_path, 'a') as f:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"\nLog entry at {timestamp}.")
                print(f"  [SUCCESS] Appended to '{file_path}'.")
            except PermissionError:
                print(f"  [HANDLED] PermissionError: Cannot write to '{file_path}'. Please check file permissions or run with necessary privileges.")
                # Practical response: log, notify user, skip operation, or retry after fixing permissions
            except FileNotFoundError:
                print(f"  [HANDLED] FileNotFoundError: '{file_path}' does not exist. Attempting to create it...")
                if self._create_file(file_path, "New file created due to non-existence."):
                    print(f"  Successfully created new file '{file_path}'.")
                else:
                    print(f"  [ERROR] Failed to create '{file_path}' (possibly due to parent directory permissions).")
            except Exception as e:
                print(f"  [UNEXPECTED ERROR] While processing '{file_path}': {type(e).__name__} - {e}")
        finally:
            self._cleanup_path(self.safe_file)
            self._cleanup_path(self.protected_file)
            self._cleanup_path("non_existent_yet.txt") # Clean up if created
            print(f"  {self.demo_name} finished.")


# --- Main execution block ---
if __name__ == "__main__":
    
    # Instantiate and run each demo
    ReadOnlyWriteDemo().run()
    input("\nPress Enter to run the next example...")
    
    NoDeletePermissionDemo().run()
    input("\nPress Enter to run the next example...")
    
    RenamePermissionDemo().run()
    input("\nPress Enter to run the next example...")
    
    SystemAccessDemo().run()
    input("\nPress Enter to run the next example...")

    GracefulPermissionHandler().run()
    
    print("\nAll PermissionError demonstrations using classes concluded.")