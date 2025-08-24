import time
import os
import sys

# --- Basic KeyboardInterrupt Handling ---
def basic_interrupt_handling():
    print("\n--- Basic KeyboardInterrupt Handling ---")
    print("Press Ctrl+C to stop this loop.")
    try:
        while True:
            print("Program is running...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SUCCESS] KeyboardInterrupt caught! Exiting gracefully from basic_interrupt_handling.")

# --- KeyboardInterrupt with Cleanup using finally ---
def cleanup_interrupt_handling():
    print("\n--- KeyboardInterrupt with Cleanup ---")
    file_handle = None
    try:
        log_file = "cleanup_log.txt"
        file_handle = open(log_file, "a")
        print(f"Writing to '{log_file}'. Press Ctrl+C to stop and close the file.")
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f"Log entry at {timestamp}\n"
            file_handle.write(message)
            print(f"Wrote: {message.strip()}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt detected. Initiating cleanup.")
    finally:
        if file_handle:
            file_handle.close()
            print(f"[SUCCESS] File '{log_file}' successfully closed.")
        if os.path.exists(log_file):
            print(f"[INFO] Content of '{log_file}':")
            with open(log_file, "r") as f:
                for line in f.readlines():
                    print(f"  {line.strip()}")
            os.remove(log_file)
            print(f"[SUCCESS] Cleaned up: '{log_file}' deleted.")
        print("Cleanup complete for cleanup_interrupt_handling.")

# --- Demonstrating why `except Exception` doesn't catch KeyboardInterrupt ---
def exception_vs_keyboardinterrupt():
    print("\n--- Exception vs. KeyboardInterrupt ---")
    print("This block will NOT catch KeyboardInterrupt with `except Exception`.")
    print("Press Ctrl+C to observe the behavior.")
    try:
        i = 0
        while True:
            print(f"Loop iteration {i}...")
            if i == 5:
                # Simulate another type of error, which 'except Exception' would catch
                if random.random() < 0.2: # Occasionally raise a ValueError
                    raise ValueError("Simulated random error!")
            time.sleep(0.8)
            i += 1
    except ValueError as e:
        print(f"\n[INFO] Caught a ValueError: {e}")
    except Exception as e: # This will NOT catch KeyboardInterrupt
        print(f"\n[UNEXPECTED] Caught a generic Exception: {type(e).__name__} - {e}")
    finally:
        print("Finally block executes in exception_vs_keyboardinterrupt, even on KeyboardInterrupt if not explicitly caught earlier.")

# --- Explicitly Catching BaseException (Generally Discouraged for just KeyboardInterrupt) ---
def baseexception_catch():
    print("\n--- Explicitly Catching BaseException ---")
    print("This block WILL catch KeyboardInterrupt using `except BaseException`.")
    print("Press Ctrl+C.")
    try:
        while True:
            print("Monitoring process... Press Ctrl+C.")
            time.sleep(1.2)
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            print("\n[SUCCESS] KeyboardInterrupt caught via BaseException!")
        else:
            print(f"\n[INFO] Another BaseException caught: {type(e).__name__} - {e}")
    finally:
        print("Finally block for baseexception_catch.")

# --- Re-raising KeyboardInterrupt after partial cleanup/logging ---
def re_raise_keyboardinterrupt():
    print("\n--- Re-raising KeyboardInterrupt ---")
    def intermediate_function():
        try:
            print("  [Intermediate] Starting task. Press Ctrl+C.")
            for _ in range(10):
                print("  [Intermediate] Working...")
                time.sleep(0.7)
        except KeyboardInterrupt:
            print("\n  [INFO] KeyboardInterrupt caught in intermediate_function for local log/cleanup.")
            # Perform specific cleanup for this function's resources
            print("  [INFO] Local cleanup in intermediate_function complete.")
            raise # Re-raise the exception to propagate it up the call stack

    try:
        print("  [Main] Calling intermediate_function.")
        intermediate_function()
        print("  [Main] This line will NOT be reached if KeyboardInterrupt was re-raised.")
    except KeyboardInterrupt:
        print("[SUCCESS] KeyboardInterrupt caught in main block after being re-raised.")
    finally:
        print("[Main] Finally block for re_raise_keyboardinterrupt.")

# --- Main execution block ---
if __name__ == "__main__":
    import random

    basic_interrupt_handling()
    print("-" * 50)
    cleanup_interrupt_handling()
    print("-" * 50)
    exception_vs_keyboardinterrupt()
    print("-" * 50)
    baseexception_catch()
    print("-" * 50)
    re_raise_keyboardinterrupt()
    print("-" * 50)

    print("\nAll demonstrations complete.")



'''

A `KeyboardInterrupt` is a Python exception that is raised when the user manually interrupts the execution of a program, typically by pressing `Ctrl+C` in the terminal. It's a `BaseException`, not a direct subclass of `Exception`, which is why it usually bypasses generic `except Exception:` blocks.

Here's all about `KeyboardInterrupt` errors within the context of code:

### What is `KeyboardInterrupt`?

  * **Type:** It's a built-in exception in Python.
  * **Purpose:** It signals an external request to stop the program's execution. It's often used by developers to gracefully shut down long-running processes or infinite loops.
  * **Behavior:** When `Ctrl+C` is pressed, the Python interpreter raises this exception at the point in the code where it receives the signal. If not handled, it will terminate the program.

### Why does it occur?

The `KeyboardInterrupt` occurs when:

1.  **User Action:** The user presses `Ctrl+C` (or `Cmd+C` on macOS) in the terminal where the Python script is running.
2.  **External Signal:** On some systems, other signals might also trigger it, though `Ctrl+C` is the most common.

### How to Handle `KeyboardInterrupt`

You handle `KeyboardInterrupt` using `try...except` blocks, just like other exceptions. However, because it's a `BaseException`, it's good practice to catch it explicitly or separately from a general `Exception` catch.

**1. Basic Handling:**

```python
import time

try:
    while True:
        print("Program running... Press Ctrl+C to stop.")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected! Exiting gracefully.")
```

**2. Handling with Cleanup:**

This is crucial for ensuring resources (like open files, network connections, or threads) are properly closed or cleaned up before the program terminates.

```python
import time
import os

file_handle = None
try:
    file_handle = open("temp_log.txt", "w")
    while True:
        file_handle.write(f"Logging at {time.time()}\n")
        print("Writing to file... Press Ctrl+C to stop.")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Cleaning up and exiting.")
finally:
    if file_handle:
        file_handle.close()
        print("File closed.")
    # Additional cleanup like closing database connections, stopping threads, etc.
    print("Cleanup complete.")
```

**3. Avoiding Catching it with `except Exception:` (Best Practice):**

If you use a broad `except Exception as e:` block, it will **not** catch `KeyboardInterrupt` because `KeyboardInterrupt` inherits from `BaseException`, not `Exception`. This is by design, as it allows the user to always interrupt a program, even if it has a very general error handler.

If you *do* want to catch it along with other exceptions (which is generally discouraged for `KeyboardInterrupt` as it can make your program unresponsive to `Ctrl+C`), you would need to catch `BaseException`:

```python
try:
    while True:
        print("Running...")
        time.sleep(1)
except BaseException as e: # This will catch KeyboardInterrupt and other system exit signals
    if isinstance(e, KeyboardInterrupt):
        print("\nKeyboardInterrupt caught by BaseException!")
    else:
        print(f"Other BaseException caught: {type(e).__name__}")
finally:
    print("Always runs, even after interrupt.")
```

**It's highly recommended to handle `KeyboardInterrupt` explicitly.**

**4. When to Re-raise `KeyboardInterrupt`:**

Sometimes you might catch `KeyboardInterrupt` to perform a small cleanup, but then you want the program to terminate. In such cases, you can re-raise the exception.

```python
import time

def do_work():
    try:
        print("Doing some work...")
        time.sleep(5)
    except KeyboardInterrupt:
        print("Inner KeyboardInterrupt caught for local cleanup.")
        # Perform specific cleanup for do_work()
        raise # Re-raise the exception to propagate it up

try:
    do_work()
    print("This line will not be reached if KeyboardInterrupt is re-raised.")
except KeyboardInterrupt:
    print("Outer KeyboardInterrupt caught, program terminating.")
```

### Common Scenarios and Considerations:

  * **Infinite Loops:** `KeyboardInterrupt` is essential for breaking out of `while True:` loops.
  * **Long-Running Computations:** For scripts that perform lengthy operations, a `try...except KeyboardInterrupt` block allows for a clean exit without leaving corrupted files or processes.
  * **Multithreading/Multiprocessing:** Handling `KeyboardInterrupt` in concurrent programming can be more complex. The signal is typically sent to the main thread, and you might need mechanisms (like flags or queues) to signal other threads/processes to shut down gracefully.
  * **Daemon Processes:** For processes running in the background, `Ctrl+C` might not be applicable. Other signal handling (e.g., `signal` module in Unix-like systems) would be used.
  * **Testing:** When developing, `KeyboardInterrupt` is invaluable for quickly stopping and restarting scripts during debugging.

### `KeyboardInterrupt` vs. `SystemExit`:

  * **`KeyboardInterrupt`:** Raised by the user (`Ctrl+C`).
  * **`SystemExit`:** Raised by the `sys.exit()` function, or implicitly when the interpreter exits (e.g., after the main script finishes). Both inherit from `BaseException`.

### Summary:

The `KeyboardInterrupt` is a vital mechanism for user control over running Python scripts. Understanding how and when to handle it (or not handle it) is a key part of writing robust and user-friendly applications. Always prioritize graceful shutdown and resource cleanup when anticipating user interruptions. '''


import time
import sys
import threading
import subprocess
import signal # For more advanced signal handling, primarily on Unix-like systems

# --- Example 1: Long-running Data Processing Loop ---
def data_processing_example():
    print("\n--- Example 1: Long-running Data Processing ---")
    data_points_processed = 0
    start_time = time.time()
    try:
        print("Simulating data processing. Press Ctrl+C to stop.")
        while True:
            # Simulate processing a batch of data
            time.sleep(0.1) # Simulates work
            data_points_processed += 100
            if data_points_processed % 1000 == 0:
                print(f"Processed {data_points_processed} data points...")

    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        print(f"\n[INFO] KeyboardInterrupt received during data processing.")
        print(f"Processed {data_points_processed} data points in {elapsed_time:.2f} seconds.")
        print("[SUCCESS] Data processing stopped gracefully.")

# --- Example 2: Interactive Input Loop ---
def interactive_input_example():
    print("\n--- Example 2: Interactive Input Loop ---")
    print("Type something and press Enter, or press Ctrl+C to exit.")
    messages = []
    try:
        while True:
            user_input = input("Enter message (or Ctrl+C to quit): ")
            if user_input.lower() == 'quit': # Allow explicit 'quit' command
                print("Exiting normally via 'quit' command.")
                break
            messages.append(user_input)
            print(f"You entered: '{user_input}'")
            print(f"Current messages: {messages}")
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received.")
        print(f"Exiting interactive input. Collected messages: {messages}")
        print("[SUCCESS] Interactive session ended gracefully.")

# --- Example 3: Downloading a File with Progress ---
# (Simplified simulation, actual download would use requests or similar)
def file_download_example():
    print("\n--- Example 3: Simulated File Download ---")
    file_size = 5000 # KB
    downloaded_size = 0
    try:
        print(f"Simulating download of a {file_size}KB file. Press Ctrl+C to cancel.")
        while downloaded_size < file_size:
            chunk_size = 100 # KB per iteration
            time.sleep(0.2) # Simulate network delay
            downloaded_size += chunk_size
            progress = (downloaded_size / file_size) * 100
            print(f"Downloading: {downloaded_size}/{file_size} KB ({progress:.1f}%)", end='\r')
            sys.stdout.flush() # Ensure immediate print update

        print(f"\n[SUCCESS] Download complete! {downloaded_size} KB downloaded.")

    except KeyboardInterrupt:
        print(f"\n[INFO] KeyboardInterrupt received. Cancelling download.")
        print(f"Partially downloaded: {downloaded_size} KB. Cleaning up incomplete file...")
        # In a real scenario, you'd delete the partial file here
        print("[SUCCESS] Download cancelled and cleaned up.")

# --- Example 4: Threading and KeyboardInterrupt (Important!) ---
# KeyboardInterrupt typically targets the main thread. Other threads might continue
# running unless explicitly told to stop.
class WorkerThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.stop_event = event

    def run(self):
        print(f"  [{self.name}] Worker started.")
        while not self.stop_event.is_set():
            print(f"  [{self.name}] Working...")
            time.sleep(1) # Simulate work
        print(f"  [{self.name}] Worker received stop signal. Exiting.")

def threading_interrupt_example():
    print("\n--- Example 4: Threading and KeyboardInterrupt ---")
    print("The main thread will catch Ctrl+C. The worker thread needs a signal to stop.")
    stop_event = threading.Event()
    worker1 = WorkerThread("Worker-1", stop_event)
    worker2 = WorkerThread("Worker-2", stop_event)

    try:
        worker1.start()
        worker2.start()
        print("Main thread running. Workers are active. Press Ctrl+C to stop both.")
        # Keep main thread alive
        while not stop_event.is_set():
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received in main thread.")
        print("Signaling worker threads to stop...")
        stop_event.set() # Set the event to tell workers to stop
        print("Waiting for worker threads to finish...")
        worker1.join() # Wait for worker threads to complete their shutdown
        worker2.join()
        print("[SUCCESS] All threads stopped gracefully.")

# --- Example 5: Running an External Command (subprocess) ---
def subprocess_interrupt_example():
    print("\n--- Example 5: Subprocess and KeyboardInterrupt ---")
    command = [sys.executable, "-c", "import time; print('Subprocess started...'); time.sleep(10); print('Subprocess finished.')"]
    process = None
    try:
        print(f"Running external command: {' '.join(command)}")
        print("Press Ctrl+C to terminate the subprocess and this script.")
        process = subprocess.Popen(command)
        process.wait() # Wait for the subprocess to complete
        print("\n[SUCCESS] Subprocess finished normally.")
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received. Terminating subprocess...")
        if process and process.poll() is None: # Check if subprocess is still running
            process.terminate() # Send SIGTERM
            time.sleep(0.5)
            if process.poll() is None: # If still running, force kill
                process.kill() # Send SIGKILL
            print("[SUCCESS] Subprocess terminated.")
        else:
            print("[INFO] Subprocess was already finished or not started.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
    finally:
        print("Subprocess example cleanup complete.")

# --- Example 6: Avoiding KeyboardInterrupt (NOT RECOMMENDED!) ---
# This demonstrates how to "block" KeyboardInterrupt (don't do this in production)
def block_keyboard_interrupt():
    print("\n--- Example 6: Blocking KeyboardInterrupt (DO NOT USE IN PRODUCTION) ---")
    print("This will catch ALL BaseExceptions, making Ctrl+C ineffective.")
    print("You might need to forcefully close your terminal or process if it gets stuck.")
    try:
        while True:
            print("Trying to block Ctrl+C. You might struggle to stop me now!")
            time.sleep(1)
            sys.stdout.flush() # Ensure print appears
    except BaseException as e:
        print(f"\n[DANGER] Caught BaseException: {type(e).__name__}. This means Ctrl+C was caught!")
        print("If this was not intended, you've made your program hard to stop.")
    finally:
        print("Blocked KeyboardInterrupt example finished.")

# --- Example 7: Using `signal` module for graceful shutdown (Unix-like systems) ---
# This is more robust for daemons or services
def signal_handler_example():
    print("\n--- Example 7: Using signal module (Unix-like systems) ---")
    # This example specifically registers a handler for SIGINT (Ctrl+C)
    # It might behave differently or not work on Windows as directly
    # For Windows, subprocess.Popen().terminate() is generally used for external processes

    if sys.platform.startswith('win'):
        print("Skipping signal handler example on Windows for direct demonstration.")
        print("On Windows, Ctrl+C directly raises KeyboardInterrupt.")
        return

    running = True

    def signal_handler(sig, frame):
        nonlocal running
        print(f"\n[INFO] Caught signal {sig} ({signal.SIGINT.name}). Initiating graceful shutdown...")
        running = False

    # Register the signal handler for SIGINT (Ctrl+C)
    # In some cases, this can prevent KeyboardInterrupt from being raised,
    # and instead, your handler is called.
    signal.signal(signal.SIGINT, signal_handler)

    try:
        print("Monitoring with signal handler. Press Ctrl+C.")
        while running:
            print("Application running...")
            time.sleep(1)
        print("[SUCCESS] Application gracefully shut down by signal handler.")
    except KeyboardInterrupt:
        # This block might still be hit if the signal isn't caught immediately
        # or if multiple Ctrl+C presses happen.
        print("\n[WARNING] KeyboardInterrupt also occurred, possibly due to multiple Ctrl+C or timing.")
    finally:
        print("Signal handler example cleanup complete.")
        # Restore default signal handler to avoid interfering with subsequent tests
        signal.signal(signal.SIGINT, signal.SIG_DFL)


# --- Main execution block to run all examples ---
if __name__ == "__main__":
    data_processing_example()
    input("\nPress Enter to run the next example: Interactive Input...")
    interactive_input_example()
    input("\nPress Enter to run the next example: File Download Simulation...")
    file_download_example()
    input("\nPress Enter to run the next example: Threading Interrupt...")
    threading_interrupt_example()
    input("\nPress Enter to run the next example: Subprocess Interrupt...")
    subprocess_interrupt_example()
    input("\nPress Enter to run the next example: Blocking KeyboardInterrupt (CAUTION!)...")
    block_keyboard_interrupt()
    input("\nPress Enter to run the next example: Signal Handler (Unix-like only)...")
    signal_handler_example()

    print("\nAll KeyboardInterrupt examples concluded.")