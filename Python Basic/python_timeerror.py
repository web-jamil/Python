import time
import socket
import threading
import datetime

# --- 1. Functions for Handling Time-Related Issues ---

def demonstrate_timeout_error_function(duration_seconds):
    """
    Demonstrates TimeoutError, often raised by system-level functions
    when an operation exceeds a timeout.
    """
    print(f"\n--- Function: Demonstrating TimeoutError (for {duration_seconds}s timeout) ---")
    
    # Simulate a network operation with a timeout
    host = "10.255.255.1"  # A non-routable IP, likely to cause a timeout
    port = 80
    
    try:
        print(f"  Attempting to connect to {host}:{port} with a {duration_seconds}-second timeout...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(duration_seconds)
        s.connect((host, port))
        print(f"  [SUCCESS] Connected to {host}:{port} (this is unexpected for a non-routable IP).")
        s.close()
    except socket.timeout: # TimeoutError is a subclass of OSError, and socket.timeout is specific
        print(f"  [CAUGHT ERROR] socket.timeout: Connection to {host} timed out after {duration_seconds} seconds.")
    except TimeoutError: # Catch general TimeoutError if socket.timeout isn't caught
        print(f"  [CAUGHT ERROR] TimeoutError: A generic timeout occurred.")
    except ConnectionRefusedError:
        print(f"  [INFO] Connection refused by {host} (less common for non-routable).")
    except OSError as e: # Broader OS-related errors
        print(f"  [CAUGHT ERROR] OSError: An OS-related error occurred: {e}")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  TimeoutError demonstration finished.")

def demonstrate_time_value_errors_function():
    """
    Demonstrates common errors when dealing with time values (ValueError, TypeError).
    """
    print("\n--- Function: Demonstrating Time Value Errors ---")

    # Case 1: ValueError - Invalid format string for strptime
    date_string = "2023-13-01" # Month 13 is invalid
    format_string = "%Y-%m-%d"
    try:
        print(f"  Attempting to parse '{date_string}' with format '{format_string}'...")
        datetime.datetime.strptime(date_string, format_string)
        print(f"  [SUCCESS] Parsed date: {date_string} (unexpected).")
    except ValueError as e:
        print(f"  [CAUGHT ERROR] ValueError: Failed to parse date string due to invalid value or format: {e}")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    # Case 2: TypeError - Incorrect argument type for time.sleep()
    sleep_duration = "5" # Should be int or float, not string
    try:
        print(f"  Attempting to sleep for '{sleep_duration}' seconds...")
        time.sleep(sleep_duration)
        print(f"  [SUCCESS] Slept for {sleep_duration} seconds (unexpected).")
    except TypeError as e:
        print(f"  [CAUGHT ERROR] TypeError: Invalid type for sleep duration: {e}")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    # Case 3: ValueError - Out of range time components (e.g., day 32)
    try:
        print(f"  Attempting to create datetime with invalid day (32)...")
        datetime.datetime(2023, 1, 32) # Day 32 is invalid
        print(f"  [SUCCESS] Created invalid datetime (unexpected).")
    except ValueError as e:
        print(f"  [CAUGHT ERROR] ValueError: Invalid date component: {e}")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Time value errors demonstration finished.")

# --- 2. Classes for Handling Time-Related Issues ---

class TimedOperation:
    """
    A class to encapsulate an operation that might time out.
    """
    def __init__(self, host, port, timeout_seconds):
        self.host = host
        self.port = port
        self.timeout_seconds = timeout_seconds

    def connect_with_timeout(self):
        print(f"\n--- Class: TimedOperation - Connecting to {self.host}:{self.port} with {self.timeout_seconds}s timeout ---")
        try:
            print(f"  Attempting to connect...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout_seconds)
            s.connect((self.host, self.port))
            print(f"  [SUCCESS] Connected to {self.host}:{self.port}.")
            s.close()
            return True
        except socket.timeout:
            print(f"  [CAUGHT ERROR] socket.timeout: Connection to {self.host} timed out.")
            return False
        except TimeoutError:
            print(f"  [CAUGHT ERROR] TimeoutError: A generic timeout occurred during connection.")
            return False
        except ConnectionRefusedError:
            print(f"  [INFO] Connection refused by {self.host}.")
            return False
        except OSError as e:
            print(f"  [CAUGHT ERROR] OSError: An OS-level network error: {e}")
            return False
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return False
        finally:
            print("  Connection attempt finished.")

class TimeValueHandler:
    """
    A class to demonstrate and handle various time-related value and type errors.
    """
    def parse_date_string(self, date_str, format_str):
        """Attempts to parse a date string, handling ValueError."""
        print(f"\n--- Class: TimeValueHandler - Parsing '{date_str}' with format '{format_str}' ---")
        try:
            dt_object = datetime.datetime.strptime(date_str, format_str)
            print(f"  [SUCCESS] Parsed date: {dt_object}")
            return dt_object
        except ValueError as e:
            print(f"  [CAUGHT ERROR] ValueError: Could not parse '{date_str}': {e}")
            return None
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return None

    def pause_execution(self, seconds_to_sleep):
        """Attempts to pause execution, handling TypeError."""
        print(f"\n--- Class: TimeValueHandler - Pausing execution for '{seconds_to_sleep}' seconds ---")
        try:
            time.sleep(seconds_to_sleep)
            print(f"  [SUCCESS] Paused for {seconds_to_sleep} seconds.")
            return True
        except TypeError as e:
            print(f"  [CAUGHT ERROR] TypeError: Invalid sleep duration type: {e}")
            return False
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return False

    def create_specific_datetime(self, year, month, day, hour=0, minute=0, second=0):
        """Attempts to create a datetime object, handling ValueError."""
        print(f"\n--- Class: TimeValueHandler - Creating datetime for {year}-{month}-{day} {hour}:{minute}:{second} ---")
        try:
            dt_obj = datetime.datetime(year, month, day, hour, minute, second)
            print(f"  [SUCCESS] Created datetime: {dt_obj}")
            return dt_obj
        except ValueError as e:
            print(f"  [CAUGHT ERROR] ValueError: Invalid datetime component: {e}")
            return None
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return None

# --- Main Execution Block ---
if __name__ == "__main__":
    
    # --- Function-based Demonstrations ---
    demonstrate_timeout_error_function(2) # 2-second timeout
    demonstrate_timeout_error_function(0.001) # Very short timeout

    demonstrate_time_value_errors_function()

    input("\nPress Enter to run the Class-based demonstrations...")

    # --- Class-based Demonstrations ---

    # TimeoutError Demo using Class
    timeout_op1 = TimedOperation("10.255.255.1", 80, 3) # Non-routable IP, should time out
    timeout_op1.connect_with_timeout()

    # Another timeout example (very short)
    timeout_op2 = TimedOperation("www.google.com", 80, 0.01) # Real host, but very short timeout
    timeout_op2.connect_with_timeout()
    
    # TimeValue Errors Demo using Class
    time_handler = TimeValueHandler()

    # Invalid date string format
    time_handler.parse_date_string("2024/02/30", "%Y-%m-%d") # Day 30 in Feb is invalid
    time_handler.parse_date_string("Invalid-Date", "%Y-%m-%d")

    # Invalid sleep duration type
    time_handler.pause_execution("2") # String instead of number
    time_handler.pause_execution(1) # Correct usage

    # Invalid datetime components
    time_handler.create_specific_datetime(2025, 2, 30) # February 30th
    time_handler.create_specific_datetime(2025, 1, 1, hour=25) # Hour 25

    print("\nAll Time-related error demonstrations concluded.")