"""A `MemoryError` in Python occurs when an operation runs out of available memory. This can happen for various reasons, such as trying to load a very large file into memory, creating excessively large data structures (lists, dictionaries, arrays), or due to an inefficient algorithm that consumes memory exponentially.

Here's all about `MemoryError` in the context of Python code:

### What is `MemoryError`?

  * **Type:** It's a built-in exception in Python, inheriting from `Exception`.
  * **Purpose:** It signals that the Python interpreter was unable to allocate enough memory to complete an operation. This is distinct from a `RecursionError` (stack overflow) or `OverflowError` (numerical overflow).
  * **Behavior:** When a `MemoryError` occurs, the program will terminate if the error is not handled using a `try...except` block.

### Why does it occur?

`MemoryError` typically occurs due to:

1.  **Loading Large Data:** Attempting to read entire very large files (e.g., multi-gigabyte CSVs, huge images) into RAM at once.
2.  **Creating Large Data Structures:**
      * Lists with millions or billions of elements.
      * Dictionaries with a vast number of key-value pairs.
      * Numpy arrays or Pandas DataFrames that exceed available RAM.
3.  **Infinite Data Generation:** Loops that continuously append data to a list or similar structure without bound.
4.  **Deep Recursion (less common for `MemoryError`):** While deep recursion usually causes `RecursionError` (stack overflow), in some edge cases or specific Python implementations, extremely deep recursion could contribute to general memory exhaustion.
5.  **Memory Leaks:** Although Python has automatic garbage collection, poorly managed external resources (like C extensions not releasing memory) or circular references that are not properly collected can lead to gradual memory exhaustion.
6.  **Inefficient Algorithms:** Algorithms that require storing too much intermediate data.

### How to Handle `MemoryError`

You can catch `MemoryError` using a `try...except` block, similar to other exceptions. However, handling it often means redesigning the code rather than simply catching and continuing, as the underlying problem (lack of memory) usually persists.

**1. Basic Handling (Catch and Log):**

```python
import sys

def basic_memory_error_handling():
    print("\n--- Basic MemoryError Handling ---")
    large_list = []
    try:
        print("Attempting to allocate a very large list...")
        # This loop will eventually cause a MemoryError on most systems
        # The actual number of iterations depends on available RAM
        for i in range(10**9): # Trying to add a billion integers
            large_list.append(i)
        print(f"Successfully created a list of {len(large_list)} elements.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught! Unable to allocate enough memory for the list.")
        print(f"List size reached approximately {sys.getsizeof(large_list) / (1024**3):.2f} GB before error.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        # Cleanup if necessary (e.g., delete partial structures)
        del large_list
        print("Basic MemoryError handling complete. Large list deleted from memory.")

# --- Strategies to Prevent/Mitigate MemoryError ---

# 2. Process Data in Chunks/Streams (Iterators/Generators)
def process_data_in_chunks():
    print("\n--- Strategy 1: Process Data in Chunks/Streams (Generators) ---")

    # Simulate reading a very large file line by line using a generator
    def read_large_file_line_by_line(filename, num_lines=10**7):
        print(f"Simulating reading {num_lines} lines from '{filename}'...")
        # In a real scenario, this would be `with open(filename, 'r') as f:`
        for i in range(num_lines):
            # Simulate a line of data
            if i % (num_lines // 10) == 0:
                print(f"  Yielding line {i}...")
            yield f"This is line number {i}\n"
        print(f"  Finished simulating reading {num_lines} lines.")

    processed_count = 0
    try:
        # This will not load all lines into memory at once
        for line in read_large_file_line_by_line("simulated_large_file.txt", num_lines=5 * 10**6):
            # Process each line here (e.g., parse, store in a database, write to another file)
            # print(f"Processing: {line.strip()}") # Uncomment to see lines
            processed_count += 1
            if processed_count % 1000000 == 0:
                print(f"  Processed {processed_count} lines...")
            # Simulate an external memory check if needed
            # if psutil.virtual_memory().percent > 90:
            #     raise MemoryError("System memory critically low during processing.")
        print(f"[SUCCESS] Successfully processed {processed_count} lines without MemoryError.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during chunked processing! This might indicate other issues.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("Chunked processing example complete.")

# 3. Use Data Structures Optimized for Memory (e.g., `array`, `numpy`, `pandas`)
# Note: These can still cause MemoryError if data is too large, but they are more efficient.
def optimized_data_structures_example():
    print("\n--- Strategy 2: Use Memory-Efficient Data Structures ---")
    try:
        import array
        import numpy as np
        # import pandas as pd # For very large datasets, Pandas might still hit MemoryError

        # Python list of integers (can be memory-intensive for large numbers)
        print("Creating a large Python list (less efficient for numbers):")
        # integers_list = list(range(50 * 10**6)) # This might still cause MemoryError on some systems
        # print(f"  List size: {sys.getsizeof(integers_list) / (1024**2):.2f} MB")
        # del integers_list

        # 'array' module for basic types (more memory-efficient than lists)
        print("Creating a large 'array.array' (more efficient for homogeneous types):")
        # 'i' means signed integer (2 bytes on most systems)
        my_array = array.array('i', range(50 * 10**6))
        print(f"  Array.array size: {sys.getsizeof(my_array) / (1024**2):.2f} MB")
        del my_array

        # NumPy arrays (highly optimized for numerical data)
        print("Creating a large NumPy array (most efficient for numerical data):")
        # dtype='int32' ensures fixed memory per element
        np_array = np.arange(500 * 10**6, dtype='int32') # 500 million 4-byte integers
        print(f"  NumPy array size: {np_array.nbytes / (1024**2):.2f} MB")
        del np_array

        print("[SUCCESS] Demonstrated memory-efficient data structure creation.")

    except MemoryError:
        print("\n[ERROR] MemoryError caught during optimized data structure creation! Data was still too large.")
    except ImportError:
        print("\n[WARNING] NumPy or Array module not installed/available for this example.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("Optimized data structures example complete.")

# 4. Clear Unused Variables / Use Context Managers
def clear_variables_example():
    print("\n--- Strategy 3: Clear Unused Variables / Use Context Managers ---")
    data = []
    try:
        # Simulate loading some data that's only needed for a specific task
        print("Creating temporary large data structure...")
        temp_data = [i for i in range(10**7)] # 10 million integers
        print(f"  Temporary data size: {sys.getsizeof(temp_data) / (1024**2):.2f} MB")

        # Perform a task that uses temp_data
        print("  Performing task with temporary data...")
        result = sum(temp_data[:100]) # Only using a small part for demonstration
        print(f"  Task result: {result}")

        # Explicitly delete the temporary data to free memory
        del temp_data
        print("  Temporary data deleted to free memory.")

        # Continue with other operations without the large temporary data
        data.append("Some small persistent data.")
        print("  Continuing with other operations.")
        # Attempt to allocate something else that might have failed before deletion
        # small_list = [0] * (10**6) # This might now succeed
        # print(f"  Small list created after cleanup: {sys.getsizeof(small_list) / (1024**2):.2f} MB")

        print("[SUCCESS] Demonstrated explicit variable deletion.")

    except MemoryError:
        print("\n[ERROR] MemoryError caught even after trying to clear variables.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("Clear variables example complete.")

# 5. Iterators for File Operations (Context Managers `with open(...)`)
def file_iterator_example():
    print("\n--- Strategy 4: File Iterators (Context Managers) ---")
    large_file_name = "large_log_simulation.txt"
    num_lines = 10**6 # 1 million lines

    # Create a simulated large file
    print(f"Creating simulated large file '{large_file_name}' with {num_lines} lines...")
    with open(large_file_name, 'w') as f:
        for i in range(num_lines):
            f.write(f"Log entry {i}: This is a sample line for a very large log file.\n")
    print("Simulated file created.")

    line_count = 0
    try:
        # Using 'with' statement ensures the file is closed, and iterating directly
        # over the file object processes line by line, not loading all into memory.
        print(f"Reading '{large_file_name}' line by line (memory efficient)...")
        with open(large_file_name, 'r') as f:
            for line in f: # This is the memory-efficient way
                # Process each line here
                line_count += 1
                if line_count % 100000 == 0:
                    print(f"  Processed {line_count} lines...")
        print(f"[SUCCESS] Successfully read {line_count} lines without MemoryError.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during file iteration! (Unexpected with this method).")
    except FileNotFoundError:
        print(f"\n[ERROR] File '{large_file_name}' not found.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        if os.path.exists(large_file_name):
            os.remove(large_file_name)
            print(f"Cleaned up simulated file: '{large_file_name}'.")
        print("File iterator example complete.")

# --- Main execution block ---
if __name__ == "__main__":
    import os
    # import psutil # Uncomment if you want to use psutil for system memory checks

    basic_memory_error_handling()
    input("\nPress Enter to run the next example: Process Data in Chunks...")
    process_data_in_chunks()
    input("\nPress Enter to run the next example: Optimized Data Structures...")
    optimized_data_structures_example()
    input("\nPress Enter to run the next example: Clear Unused Variables...")
    clear_variables_example()
    input("\nPress Enter to run the next example: File Iterators...")
    file_iterator_example()

    print("\nAll MemoryError examples and strategies concluded.")
```"""


import sys
import os
import time

# --- Example 1: Basic MemoryError Generation and Handling ---
# This function attempts to create an extremely large list,
# likely leading to a MemoryError on most systems.
def generate_and_handle_memory_error():
    print("\n--- Example 1: Generating and Handling MemoryError ---")
    large_list = []
    try:
        print("Attempting to allocate a very large list (can cause MemoryError)...")
        # Attempt to append a billion integers. This will exhaust RAM.
        for i in range(1_000_000_000):
            large_list.append(i)
        print(f"Successfully created a list of {len(large_list)} elements.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught! The system ran out of memory.")
        print(f"  List approximately consumed: {sys.getsizeof(large_list) / (1024**3):.2f} GB before error.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        # Crucial for freeing memory: delete the large object
        del large_list
        print("  Large list reference deleted (memory potentially freed).")
        print("Example 1 completed.")

# --- Example 2: Preventing MemoryError with Generators (Stream Processing) ---
# This demonstrates processing a large "data stream" without loading it all into memory.
def prevent_memory_error_with_generators():
    print("\n--- Example 2: Preventing MemoryError with Generators ---")

    # A generator function that simulates reading lines from a very large file.
    # It yields one line at a time, keeping memory usage low.
    def read_large_data_stream(num_lines=5_000_000):
        print(f"  Simulating a data stream of {num_lines} lines...")
        for i in range(num_lines):
            # Simulate a complex data line
            if i % (num_lines // 5) == 0:
                print(f"    Yielding line {i}...")
            yield f"Data entry {i}: Some extensive log information and calculations.\n"

    processed_records = 0
    try:
        print("Processing data stream using a generator (memory efficient)...")
        for record_line in read_large_data_stream():
            # In a real application, you'd process (e.g., parse, store in DB, aggregate)
            # each record_line here. Only one line is in memory at a time.
            processed_records += 1
            if processed_records % 1_000_000 == 0:
                print(f"  Processed {processed_records} records.")
        print(f"[SUCCESS] Successfully processed {processed_records} records using generators.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught unexpectedly during generator usage! (Should not happen if implemented correctly).")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("Example 2 completed.")


# --- Example 3: Using Memory-Efficient Data Structures (array, numpy) ---
# Demonstrates built-in Python 'array' module and external 'numpy' library
# for more compact storage of homogeneous numerical data.
def use_memory_efficient_structures():
    print("\n--- Example 3: Using Memory-Efficient Data Structures ---")

    try:
        # Python's built-in 'array' module for basic types
        import array
        print("  Creating an 'array.array' (more memory-efficient than a list for numbers):")
        # 'i' type code for signed int, typically 2 or 4 bytes
        large_array = array.array('i', range(50_000_000)) # 50 million integers
        print(f"    array.array size: {sys.getsizeof(large_array) / (1024**2):.2f} MB")
        del large_array # Release memory

        # NumPy arrays (requires `pip install numpy`)
        try:
            import numpy as np
            print("  Creating a NumPy array (highly optimized for numerical data):")
            # Create 500 million 32-bit integers.
            # `nbytes` gives exact memory usage.
            large_numpy_array = np.arange(500_000_000, dtype='int32')
            print(f"    NumPy array size: {large_numpy_array.nbytes / (1024**2):.2f} MB")
            del large_numpy_array # Release memory
        except ImportError:
            print("    NumPy not installed. Skipping NumPy array example (`pip install numpy`).")

        print("[SUCCESS] Demonstrated use of memory-efficient data structures.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during optimized data structure creation! Data was still too large for available RAM.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("Example 3 completed.")


# --- Example 4: Clearing Unused References / Scope Management ---
# Shows how explicitly deleting large objects or letting them go out of scope
# can help manage memory, especially in long-running processes.
def clear_unused_references():
    print("\n--- Example 4: Clearing Unused References ---")
    
    overall_results = []
    
    try:
        print("  Step 1: Creating a large temporary data structure...")
        temp_large_data = [x * 2 for x in range(20_000_000)] # 20 million elements
        print(f"    Temp data size: {sys.getsizeof(temp_large_data) / (1024**2):.2f} MB")

        print("  Step 2: Performing a task that uses the temporary data...")
        # Simulate some processing with temp_large_data
        intermediate_result = sum(temp_large_data[:1000])
        print(f"    Intermediate result: {intermediate_result}")
        overall_results.append(intermediate_result)

        print("  Step 3: Explicitly deleting the large temporary data...")
        # Explicitly delete the reference to free memory immediately
        del temp_large_data
        print("    Reference to temp_large_data deleted.")
        
        print("  Step 4: Attempting to allocate new large data after cleanup (more likely to succeed)...")
        # Now, try to allocate something else large, which might have failed before deletion
        another_large_object = [f"item_{i}" for i in range(15_000_000)] # 15 million strings
        print(f"    Another large object size: {sys.getsizeof(another_large_object) / (1024**2):.2f} MB")
        
        overall_results.append(len(another_large_object))
        del another_large_object # Cleanup
        
        print("[SUCCESS] Successfully managed memory by clearing references.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during reference clearing example! Still too much memory needed sequentially.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        del overall_results # Ensure final cleanup
        print("Example 4 completed.")

# --- Example 5: Efficient File Reading (Line by Line) ---
# Demonstrates using `with open(...)` and iterating directly over a file object
# to read large files line by line without loading the entire file into memory.
def efficient_file_reading():
    print("\n--- Example 5: Efficient File Reading (Line by Line) ---")
    large_test_file = "simulated_very_large_file.txt"
    num_lines_in_file = 2_000_000 # 2 million lines

    # Create a simulated large file for demonstration
    print(f"  Creating a simulated large file '{large_test_file}' with {num_lines_in_file} lines...")
    with open(large_test_file, 'w') as f:
        for i in range(num_lines_in_file):
            f.write(f"This is line number {i} with some generated content to make it long enough.\n")
    print("  Simulated file created.")

    lines_processed = 0
    try:
        print(f"  Reading '{large_test_file}' line by line (memory efficient)...")
        # The 'with' statement ensures the file is properly closed.
        # Iterating directly over 'f' reads one line at a time.
        with open(large_test_file, 'r') as f:
            for line in f:
                # Process each 'line' here. Only 'line' is in memory at any given time.
                lines_processed += 1
                if lines_processed % 500_000 == 0:
                    print(f"    Processed {lines_processed} lines...")
        print(f"[SUCCESS] Successfully processed {lines_processed} lines from file without MemoryError.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during file iteration! (Highly unlikely with this method).")
    except FileNotFoundError:
        print(f"\n[ERROR] The simulated file '{large_test_file}' was not found.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        # Clean up the simulated file
        if os.path.exists(large_test_file):
            os.remove(large_test_file)
            print(f"  Cleaned up simulated file: '{large_test_file}'.")
        print("Example 5 completed.")

# --- Main execution block ---
if __name__ == "__main__":
    print("Starting MemoryError demonstrations...")

    generate_and_handle_memory_error()
    time.sleep(1) # Give time for memory cleanup
    input("\nPress Enter to run the next example: Preventing with Generators...")

    prevent_memory_error_with_generators()
    time.sleep(1)
    input("\nPress Enter to run the next example: Memory-Efficient Data Structures...")

    use_memory_efficient_structures()
    time.sleep(1)
    input("\nPress Enter to run the next example: Clearing Unused References...")

    clear_unused_references()
    time.sleep(1)
    input("\nPress Enter to run the next example: Efficient File Reading...")

    efficient_file_reading()

    print("\nAll MemoryError demonstrations concluded.")



import sys
import os
import time
import gc # Garbage Collector interface

# --- Example 6: Image Processing (Simulated) ---
# Real image processing can easily hit MemoryError with large images.
# This simulates loading pixel data.
def image_processing_memory_error():
    print("\n--- Example 6: Image Processing MemoryError (Simulated) ---")
    # Simulate a very large image: 100,000 x 100,000 pixels, 3 bytes per pixel (RGB)
    # This is 30 Gigabytes if stored naively!
    width, height = 100_000, 100_000
    pixel_size_bytes = 3 # RGB

    try:
        print(f"  Attempting to load a simulated image of {width}x{height} pixels ({pixel_size_bytes} bytes/pixel)...")
        print(f"  Expected memory for full image: {(width * height * pixel_size_bytes) / (1024**3):.2f} GB")

        # This will almost certainly cause a MemoryError
        image_data = bytearray(width * height * pixel_size_bytes)
        print(f"  Successfully allocated image data of {len(image_data) / (1024**2):.2f} MB.")

        # Simulate some processing
        # image_data[0] = 255

    except MemoryError:
        print("\n[ERROR] MemoryError caught! Image data too large for available RAM.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        # Crucial to clean up large temporary objects
        try:
            del image_data
            print("  Simulated image data deleted.")
        except NameError:
            pass # Variable might not have been created if MemoryError occurred early
        gc.collect() # Force garbage collection
        print("Example 6 completed.")

# --- Example 7: Large Dictionaries / Hash Tables ---
# Dictionaries can consume significant memory due to hash table overhead and key/value storage.
def large_dictionary_memory_error():
    print("\n--- Example 7: Large Dictionaries MemoryError ---")
    large_dict = {}
    num_entries = 50_000_000 # 50 million entries

    try:
        print(f"  Attempting to create a dictionary with {num_entries} entries...")
        # Each entry stores an integer key and a small string value
        for i in range(num_entries):
            large_dict[i] = f"val_{i}" # String objects also consume memory
            if i % (num_entries // 10) == 0 and i > 0:
                print(f"    Added {i} entries. Approx size: {sys.getsizeof(large_dict) / (1024**2):.2f} MB")
        
        print(f"  Successfully created dictionary with {len(large_dict)} entries.")

    except MemoryError:
        print("\n[ERROR] MemoryError caught! Dictionary too large for available RAM.")
        print(f"  Dictionary size at error: {sys.getsizeof(large_dict) / (1024**2):.2f} MB")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        del large_dict
        gc.collect()
        print("Example 7 completed.")

# --- Example 8: Indirect MemoryError from Deep Recursion (Stack vs. Heap) ---
# While deep recursion typically causes RecursionError (stack overflow),
# extremely deep recursion might exhaust general memory (heap) in some Python versions/systems,
# or it might hold too many stack frames for long. This is less common than direct MemoryError.
def indirect_recursion_memory_error(depth, max_depth, data_storage):
    if depth > max_depth:
        return
    
    # Simulate allocating memory on each recursive call (e.g., local variables, closure captures)
    # This example aims to combine deep recursion with continuous memory allocation,
    # which can trigger MemoryError before RecursionError on some systems,
    # or make the RecursionError happen faster due to memory pressure.
    local_data = [i for i in range(100)] # Small allocation per frame
    data_storage.append(local_data) # Keep references, leading to heap growth

    indirect_recursion_memory_error(depth + 1, max_depth, data_storage)
    
    # Simulate cleaning up local data (won't happen until return, which is too late for deep recursion)
    # del local_data


def run_recursion_memory_example():
    print("\n--- Example 8: Indirect MemoryError from Deep Recursion ---")
    sys.setrecursionlimit(20000) # Increase recursion limit for demonstration
    print(f"  Recursion limit set to: {sys.getrecursionlimit()}")

    global_data_storage = [] # List to hold references from recursive calls
    try:
        print("  Attempting deep recursion with memory allocation per frame...")
        # Try a depth that might stress memory before hitting typical recursion limit
        indirect_recursion_memory_error(0, 15000, global_data_storage) 
        print(f"  Recursion completed successfully to depth {len(global_data_storage)}. (Unexpected, if error was expected).")
    except RecursionError:
        print("\n[ERROR] RecursionError caught! The recursion depth limit was exceeded.")
        print("  This is the more common outcome for very deep recursion.")
    except MemoryError:
        print("\n[ERROR] MemoryError caught during deep recursion! This indicates heap exhaustion (less common).")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        del global_data_storage
        gc.collect()
        sys.setrecursionlimit(1000) # Reset to default
        print("Example 8 completed. Recursion limit reset.")

# --- Example 9: Large Set Creation ---
# Sets, like dictionaries, have overhead for hashing and can consume significant memory.
def large_set_memory_error():
    print("\n--- Example 9: Large Set Creation MemoryError ---")
    large_set = set()
    num_elements = 50_000_000 # 50 million unique elements

    try:
        print(f"  Attempting to create a set with {num_elements} unique integer elements...")
        for i in range(num_elements):
            large_set.add(i)
            if i % (num_elements // 10) == 0 and i > 0:
                print(f"    Added {i} elements. Approx size: {sys.getsizeof(large_set) / (1024**2):.2f} MB")
        
        print(f"  Successfully created set with {len(large_set)} elements.")

    except MemoryError:
        print("\n[ERROR] MemoryError caught! Set too large for available RAM.")
        print(f"  Set size at error: {sys.getsizeof(large_set) / (1024**2):.2f} MB")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        del large_set
        gc.collect()
        print("Example 9 completed.")

# --- Main execution block ---
if __name__ == "__main__":
    print("Starting more MemoryError demonstrations...")

    image_processing_memory_error()
    time.sleep(1)
    input("\nPress Enter to run the next example: Large Dictionary...")

    large_dictionary_memory_error()
    time.sleep(1)
    input("\nPress Enter to run the next example: Indirect Recursion...")

    run_recursion_memory_example()
    time.sleep(1)
    input("\nPress Enter to run the next example: Large Set Creation...")

    large_set_memory_error()

    print("\nAll additional MemoryError demonstrations concluded.")


