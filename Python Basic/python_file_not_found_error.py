import os
import sys

# --- 1. Basic FileNotFoundError when trying to open a non-existent file ---

def basic_file_not_found_example():
    print("\n--- 1. Basic FileNotFoundError ---")
    
    non_existent_file = "non_existent_document.txt"
    
    try:
        print(f"Attempting to open '{non_existent_file}' for reading...")
        with open(non_existent_file, 'r') as f:
            content = f.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The file '{non_existent_file}' does not exist at the specified path.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("Basic FileNotFoundError example finished.")

# --- 2. FileNotFoundError when trying to execute a non-existent program (subprocess) ---

def subprocess_file_not_found_example():
    print("\n--- 2. Subprocess FileNotFoundError ---")
    
    # Try to run a command that doesn't exist on the system's PATH
    non_existent_command = "this_is_not_a_real_command_12345"
    
    try:
        print(f"Attempting to run external command: '{non_existent_command}'...")
        # For cross-platform compatibility, use shell=True with caution, or ensure pathing
        import subprocess
        subprocess.run([non_existent_command, "arg1", "arg2"], check=True)
        print("Command executed successfully (this line should not be reached).")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The command '{non_existent_command}' was not found.")
        print("  This typically means the executable doesn't exist or isn't in your system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[UNEXPECTED ERROR] Subprocess exited with non-zero status: {e.returncode}")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("Subprocess FileNotFoundError example finished.")

# --- 3. FileNotFoundError with incorrect path or permissions (simulated) ---

def incorrect_path_or_permissions_example():
    print("\n--- 3. Incorrect Path or Permissions (simulated) ---")
    
    # Simulate a scenario where the directory exists but the file path is wrong
    existing_dir = "temp_data_dir"
    os.makedirs(existing_dir, exist_ok=True)
    
    correct_file_path = os.path.join(existing_dir, "data.txt")
    incorrect_file_path = os.path.join(existing_dir, "non_existent_data.txt")
    
    # Create the actual file
    with open(correct_file_path, 'w') as f:
        f.write("Some sample data.")
    print(f"Created '{correct_file_path}' for testing.")

    try:
        print(f"Attempting to open incorrect path: '{incorrect_file_path}'...")
        with open(incorrect_file_path, 'r') as f:
            content = f.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The file '{incorrect_file_path}' was not found.")
        print("  Even if the directory exists, the file itself might be misspelled or missing.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        # Clean up the created directory and file
        if os.path.exists(correct_file_path):
            os.remove(correct_file_path)
            print(f"Cleaned up '{correct_file_path}'.")
        if os.path.exists(existing_dir):
            os.rmdir(existing_dir)
            print(f"Cleaned up directory '{existing_dir}'.")
        print("Incorrect path/permissions example finished.")

# --- 4. Preventing FileNotFoundError: Checking Existence Before Opening ---

def preventing_file_not_found_example():
    print("\n--- 4. Preventing FileNotFoundError: Checking Existence ---")
    
    existing_file = "my_important_config.ini"
    non_existing_file = "another_missing_file.log"
    
    # Create an existing file for this demo
    with open(existing_file, 'w') as f:
        f.write("[Settings]\nversion=1.0")
    print(f"Created '{existing_file}' for testing.")

    # Check for existing file
    if os.path.exists(existing_file):
        print(f"'{existing_file}' exists. Proceeding to open.")
        try:
            with open(existing_file, 'r') as f:
                content = f.read()
                print(f"Content of '{existing_file}':\n{content}")
        except IOError as e: # Catch IOError for permission issues, etc.
            print(f"[ERROR] Could not open '{existing_file}' due to IOError: {e}")
    else:
        print(f"'{existing_file}' does NOT exist. Will not attempt to open.")

    print("\nChecking for non-existing file:")
    if os.path.exists(non_existing_file):
        print(f"'{non_existing_file}' exists. Proceeding to open. (This should not happen).")
    else:
        print(f"'{non_existing_file}' does NOT exist. Will not attempt to open.")
        # Instead of opening, you might create it or inform the user
        try:
            with open(non_existing_file, 'w') as f:
                f.write("New log file created.")
            print(f"Successfully created '{non_existing_file}'.")
        except Exception as e:
            print(f"[ERROR] Could not create '{non_existing_file}': {e}")
    
    # Clean up
    if os.path.exists(existing_file):
        os.remove(existing_file)
        print(f"Cleaned up '{existing_file}'.")
    if os.path.exists(non_existing_file):
        os.remove(non_existing_file)
        print(f"Cleaned up '{non_existing_file}'.")
    print("Prevention example finished.")

# --- 5. Handling FileNotFoundError specifically for different operations ---

def specific_operation_error_handling():
    print("\n--- 5. Specific Operation Error Handling ---")
    
    source_file = "source_data.txt"
    dest_file = "destination_data.txt"
    
    # Simulate the source file existing sometimes, and sometimes not.
    create_source = True # Change to False to see FileNotFoundError on os.rename
    if create_source:
        with open(source_file, 'w') as f:
            f.write("Data to move.")
        print(f"Created '{source_file}' for demo.")

    try:
        print(f"Attempting to rename '{source_file}' to '{dest_file}'...")
        os.rename(source_file, dest_file)
        print(f"Successfully renamed '{source_file}' to '{dest_file}'.")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: Cannot rename '{source_file}' because it does not exist.")
    except PermissionError:
        print(f"[ERROR] PermissionError: Insufficient permissions to rename '{source_file}'.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        # Clean up
        if os.path.exists(source_file):
            os.remove(source_file)
            print(f"Cleaned up leftover '{source_file}'.")
        if os.path.exists(dest_file):
            os.remove(dest_file)
            print(f"Cleaned up '{dest_file}'.")
        print("Specific operation example finished.")


# --- Main execution block ---
if __name__ == "__main__":
    basic_file_not_found_example()
    input("\nPress Enter to run the next example: Subprocess FileNotFoundError...")
    
    subprocess_file_not_found_example()
    input("\nPress Enter to run the next example: Incorrect Path or Permissions (simulated)...")
    
    incorrect_path_or_permissions_example()
    input("\nPress Enter to run the next example: Preventing FileNotFoundError...")
    
    prevention_file_not_found_example()
    input("\nPress Enter to run the next example: Specific Operation Error Handling...")

    specific_operation_error_handling()
    
    print("\nAll FileNotFoundError demonstrations concluded.")


    import os
import sys

# --- 1. Basic FileNotFoundError when trying to open a non-existent file ---

def basic_file_not_found_example():
    print("\n--- 1. Basic FileNotFoundError ---")
    
    non_existent_file = "non_existent_document.txt"
    
    try:
        print(f"Attempting to open '{non_existent_file}' for reading...")
        with open(non_existent_file, 'r') as f:
            content = f.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The file '{non_existent_file}' does not exist at the specified path.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("Basic FileNotFoundError example finished.")

# --- 2. FileNotFoundError when trying to execute a non-existent program (subprocess) ---

def subprocess_file_not_found_example():
    print("\n--- 2. Subprocess FileNotFoundError ---")
    
    # Try to run a command that doesn't exist on the system's PATH
    non_existent_command = "this_is_not_a_real_command_12345"
    
    try:
        print(f"Attempting to run external command: '{non_existent_command}'...")
        # For cross-platform compatibility, use shell=True with caution, or ensure pathing
        import subprocess
        subprocess.run([non_existent_command, "arg1", "arg2"], check=True)
        print("Command executed successfully (this line should not be reached).")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The command '{non_existent_command}' was not found.")
        print("  This typically means the executable doesn't exist or isn't in your system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[UNEXPECTED ERROR] Subprocess exited with non-zero status: {e.returncode}")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("Subprocess FileNotFoundError example finished.")

# --- 3. FileNotFoundError with incorrect path or permissions (simulated) ---

def incorrect_path_or_permissions_example():
    print("\n--- 3. Incorrect Path or Permissions (simulated) ---")
    
    # Simulate a scenario where the directory exists but the file path is wrong
    existing_dir = "temp_data_dir"
    os.makedirs(existing_dir, exist_ok=True)
    
    correct_file_path = os.path.join(existing_dir, "data.txt")
    incorrect_file_path = os.path.join(existing_dir, "non_existent_data.txt")
    
    # Create the actual file
    with open(correct_file_path, 'w') as f:
        f.write("Some sample data.")
    print(f"Created '{correct_file_path}' for testing.")

    try:
        print(f"Attempting to open incorrect path: '{incorrect_file_path}'...")
        with open(incorrect_file_path, 'r') as f:
            content = f.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: The file '{incorrect_file_path}' was not found.")
        print("  Even if the directory exists, the file itself might be misspelled or missing.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        # Clean up the created directory and file
        if os.path.exists(correct_file_path):
            os.remove(correct_file_path)
            print(f"Cleaned up '{correct_file_path}'.")
        if os.path.exists(existing_dir):
            os.rmdir(existing_dir)
            print(f"Cleaned up directory '{existing_dir}'.")
        print("Incorrect path/permissions example finished.")

# --- 4. Preventing FileNotFoundError: Checking Existence Before Opening ---

def preventing_file_not_found_example():
    print("\n--- 4. Preventing FileNotFoundError: Checking Existence ---")
    
    existing_file = "my_important_config.ini"
    non_existing_file = "another_missing_file.log"
    
    # Create an existing file for this demo
    with open(existing_file, 'w') as f:
        f.write("[Settings]\nversion=1.0")
    print(f"Created '{existing_file}' for testing.")

    # Check for existing file
    if os.path.exists(existing_file):
        print(f"'{existing_file}' exists. Proceeding to open.")
        try:
            with open(existing_file, 'r') as f:
                content = f.read()
                print(f"Content of '{existing_file}':\n{content}")
        except IOError as e: # Catch IOError for permission issues, etc.
            print(f"[ERROR] Could not open '{existing_file}' due to IOError: {e}")
    else:
        print(f"'{existing_file}' does NOT exist. Will not attempt to open.")

    print("\nChecking for non-existing file:")
    if os.path.exists(non_existing_file):
        print(f"'{non_existing_file}' exists. Proceeding to open. (This should not happen).")
    else:
        print(f"'{non_existing_file}' does NOT exist. Will not attempt to open.")
        # Instead of opening, you might create it or inform the user
        try:
            with open(non_existing_file, 'w') as f:
                f.write("New log file created.")
            print(f"Successfully created '{non_existing_file}'.")
        except Exception as e:
            print(f"[ERROR] Could not create '{non_existing_file}': {e}")
    
    # Clean up
    if os.path.exists(existing_file):
        os.remove(existing_file)
        print(f"Cleaned up '{existing_file}'.")
    if os.path.exists(non_existing_file):
        os.remove(non_existing_file)
        print(f"Cleaned up '{non_existing_file}'.")
    print("Prevention example finished.")

# --- 5. Handling FileNotFoundError specifically for different operations ---

def specific_operation_error_handling():
    print("\n--- 5. Specific Operation Error Handling ---")
    
    source_file = "source_data.txt"
    dest_file = "destination_data.txt"
    
    # Simulate the source file existing sometimes, and sometimes not.
    create_source = True # Change to False to see FileNotFoundError on os.rename
    if create_source:
        with open(source_file, 'w') as f:
            f.write("Data to move.")
        print(f"Created '{source_file}' for demo.")

    try:
        print(f"Attempting to rename '{source_file}' to '{dest_file}'...")
        os.rename(source_file, dest_file)
        print(f"Successfully renamed '{source_file}' to '{dest_file}'.")
    except FileNotFoundError:
        print(f"[CAUGHT ERROR] FileNotFoundError: Cannot rename '{source_file}' because it does not exist.")
    except PermissionError:
        print(f"[ERROR] PermissionError: Insufficient permissions to rename '{source_file}'.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        # Clean up
        if os.path.exists(source_file):
            os.remove(source_file)
            print(f"Cleaned up leftover '{source_file}'.")
        if os.path.exists(dest_file):
            os.remove(dest_file)
            print(f"Cleaned up '{dest_file}'.")
        print("Specific operation example finished.")


# --- Main execution block ---
if __name__ == "__main__":
    basic_file_not_found_example()
    input("\nPress Enter to run the next example: Subprocess FileNotFoundError...")
    
    subprocess_file_not_found_example()
    input("\nPress Enter to run the next example: Incorrect Path or Permissions (simulated)...")
    
    incorrect_path_or_permissions_example()
    input("\nPress Enter to run the next example: Preventing FileNotFoundError...")
    
    prevention_file_not_found_example()
    input("\nPress Enter to run the next example: Specific Operation Error Handling...")

    specific_operation_error_handling()
    
    print("\nAll FileNotFoundError demonstrations concluded.")