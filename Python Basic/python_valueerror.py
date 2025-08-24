# --- ValueError: All About in Code ---

# A ValueError is raised when a function or operation receives an argument
# of the correct type, but an inappropriate value.
# This means the value itself is problematic for the specific operation.

# --- 1. Basic ValueError: Invalid Argument Value ---
print("--- 1. Basic ValueError: Invalid Argument Value ---")

# 1.1 `int()` conversion for non-numeric strings
try:
    num = int("hello") # "hello" cannot be converted to an integer
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: invalid literal for int() with base 10: 'hello'.")

# 1.2 `float()` conversion for non-numeric strings
try:
    f_num = float("abc.def") # "abc.def" cannot be converted to a float
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: could not convert string to float: 'abc.def'.")

# 1.3 `list.remove()` for non-existent value
my_list = [10, 20, 30]
try:
    my_list.remove(40) # 40 is not in the list
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: list.remove(x): x not in list.")

print("-" * 50 + "\n")


# --- 2. ValueError: Unpacking Iterables with Wrong Number of Elements ---
print("--- 2. ValueError: Unpacking Iterables with Wrong Number of Elements ---")

# When unpacking an iterable into variables, the number of variables must match
# the number of elements in the iterable.

# 2.1 Too many values to unpack (iterable has fewer elements than variables)
data = (1, 2)
try:
    a, b, c = data # Trying to unpack 2 elements into 3 variables
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: not enough values to unpack (expected 3, got 2).")

# 2.2 Not enough values to unpack (iterable has more elements than variables)
data_too_many = (1, 2, 3, 4)
try:
    x, y = data_too_many # Trying to unpack 4 elements into 2 variables
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: too many values to unpack (expected 2).")

# Correct unpacking
d, e = data
print(f"Correct unpacking: d={d}, e={e}")
f, *rest, g = data_too_many # Using starred assignment for flexible unpacking
print(f"Flexible unpacking: f={f}, rest={rest}, g={g}")

print("-" * 50 + "\n")


# --- 3. ValueError: Invalid Value for Built-in Functions/Methods ---
print("--- 3. ValueError: Invalid Value for Built-in Functions/Methods ---")

# 3.1 `math.sqrt()` for negative numbers
import math
try:
    result = math.sqrt(-4) # Cannot take square root of a negative number
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: math domain error (for sqrt of negative number).")

# 3.2 `datetime.datetime.strptime()` for incorrect format
import datetime
date_string = "2023-13-01" # Invalid month (13)
try:
    dt_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: time data '2023-13-01' does not match format '%Y-%m-%d'.")

# Also incorrect format string
date_string_ok = "2023-12-01"
try:
    dt_obj = datetime.datetime.strptime(date_string_ok, "%Y/%m/%d") # Format mismatch
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: time data '2023-12-01' does not match format '%Y/%m/%d'.")


# 3.3 `index()` method (strings, lists, tuples) for non-existent item
my_string = "python"
try:
    idx = my_string.index('z') # 'z' is not in the string
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: substring not found.")

print("-" * 50 + "\n")


# --- 4. ValueError: Invalid Base for `int()` Conversion ---
print("--- 4. ValueError: Invalid Base for `int()` Conversion ---")

# The `int(string, base)` function requires the base to be valid (2-36).
try:
    binary_num = int("101", base=1) # Base must be >= 2
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: int() base must be >= 2 and <= 36, or 0.")

try:
    hex_num = int("G", base=16) # 'G' is not a valid hexadecimal digit
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: invalid literal for int() with base 16: 'G'.")

print("-" * 50 + "\n")


# --- 5. ValueError in Custom Functions ---
print("--- 5. ValueError in Custom Functions ---")

# It's good practice to raise ValueError in your own functions when arguments
# are of the correct type but contain invalid data.

def calculate_discount(price, discount_percentage):
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price

# Valid call
print(f"Discounted price (valid): {calculate_discount(100, 10)}")

# Invalid discount percentage
try:
    print(f"Discounted price: {calculate_discount(50, 120)}")
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")

# Invalid price
try:
    print(f"Discounted price: {calculate_discount(-20, 10)}")
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")

print("-" * 50 + "\n")


# --- 6. ValueError in JSON Operations (`json.loads`, `json.dumps`) ---
print("--- 6. ValueError in JSON Operations ---")

# `json.loads()` can raise ValueError if `allow_nan=False` and NaN/Infinity are present.
# (Note: `json.JSONDecodeError` is a subclass of `ValueError`, so catching `ValueError` will work for both).

json_with_nan = '{"value": NaN}'
try:
    # By default, json.loads allows NaN/Infinity. To make it raise ValueError:
    # You generally control this via the dumping side with allow_nan=False.
    # For `loads`, `parse_constant` is where you'd intervene if you wanted to disallow it.
    # However, if the JSON itself is malformed in a way that includes special constants
    # *not* as `NaN`, `Infinity`, `-Infinity`, it could cause `JSONDecodeError` (which is a ValueError subclass).
    loaded_data = json.loads(json_with_nan)
    print(f"Loaded JSON with NaN (default behavior allows): {loaded_data}")
except ValueError as e:
    print(f"Caught ValueError (expected only if parse_constant disallows or strict parsing): {e}")
    # In standard json.loads(), this would pass unless parse_constant is defined to raise.

# json.dumps() with `allow_nan=False` when NaN/Infinity are present
import json
data_with_special_floats = {
    "num": 1.0,
    "not_a_number": float('nan'),
    "positive_infinity": float('inf')
}
try:
    # This will raise ValueError because allow_nan is False
    json_output = json.dumps(data_with_special_floats, allow_nan=False)
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: Out of range float values are not JSON compliant.")

print("-" * 50 + "\n")


# --- 7. ValueError with Enum (Invalid Member Access) ---
print("--- 7. ValueError with Enum (Invalid Member Access) ---")

from enum import Enum

class Status(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3

# Accessing an existing member (OK)
print(f"Status: {Status.PENDING}")

# Trying to get an enum member by an invalid value
try:
    invalid_status = Status(4) # 4 is not a defined value for Status
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: 4 is not a valid Status.")

# Trying to get an enum member by an invalid name
try:
    invalid_status_name = Status['UNKNOWN'] # 'UNKNOWN' is not a defined name
except KeyError as e: # This is a KeyError, not ValueError, when accessing by name
    print(f"Caught KeyError (expected): {e}")
    print("Reason: 'UNKNOWN' is not a valid Status member name.")

print("-" * 50 + "\n")


# --- 8. ValueError in String Methods ---
print("--- 8. ValueError in String Methods ---")

# 8.1 `str.find()` vs `str.index()`
# `find()` returns -1 if not found. `index()` raises ValueError if not found.
my_sentence = "The quick brown fox"

# `find()` (safe)
pos_quick = my_sentence.find("quick")
print(f"Position of 'quick': {pos_quick}")
pos_zebra = my_sentence.find("zebra")
print(f"Position of 'zebra' (not found): {pos_zebra}") # Returns -1

# `index()` (raises ValueError)
try:
    idx_zebra = my_sentence.index("zebra")
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: substring not found.")

# 8.2 `str.split()` with empty separator
try:
    "hello".split('') # Splitting by empty string is not allowed
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: empty separator.")

print("-" * 50 + "\n")


# --- 9. Common Troubleshooting Tips for ValueError ---
print("--- 9. Common Troubleshooting Tips for ValueError ---")

# 9.1 **Validate Inputs**: Always check function arguments for valid ranges or formats
#     *before* performing operations that might fail.
# 9.2 **Use `try-except`**: Wrap operations that are prone to `ValueError` in `try-except` blocks.
# 9.3 **Check Data Sources**: If reading from files, APIs, or user input, assume data might be malformed.
#     Implement robust parsing with `.get()`, `try-except`, and data validation.
# 9.4 **Read Error Messages Carefully**: The message `ValueError: invalid literal for int() with base 10: 'hello'`
#     clearly indicates what went wrong and where.

print("--- End of ValueError demonstration ---")


# --- ValueError: More Examples (Continued) ---

# This section provides even more scenarios where ValueError might occur,
# including less common built-in functions, custom object validation, and data parsing.

# --- 10. ValueError with `range()` Function ---
print("--- 10. ValueError with `range()` Function ---")

# While `range()` typically raises `TypeError` for non-integer arguments,
# it can implicitly cause a `ValueError` in certain contexts if the input is valid in type
# but results in an invalid range *conceptually* for other operations.
# More commonly, the arguments for `range` are validated at function call time,
# and if the type is wrong, it's `TypeError`. If the value leads to an invalid sequence,
# it's more about the subsequent use of that sequence.

# Example: `range` itself doesn't typically raise ValueError unless base is invalid in int()
# The common errors for range are TypeError (non-int args).
# However, if you pass a float that Python internally tries to cast to int and it fails,
# it might manifest as a ValueError or TypeError depending on the exact context.
# Let's stick to the direct `int()` conversion where ValueError is explicit.
try:
    # This is a TypeError, as covered before.
    list(range(5.0))
except TypeError as e:
    print(f"Caught TypeError (expected for float in range): {e}")

# This section is more about "invalid value" after type is confirmed.
# For `range`, all valid integer values result in a valid (though possibly empty) range.
# No specific ValueError from `range` itself for numerical bounds that are integers.
print("`range()` function typically raises TypeError for non-integer arguments, not ValueError for numeric bounds.")

print("-" * 50 + "\n")


# --- 11. ValueError in String Formatting with `str.format()` / f-strings ---
print("--- 11. ValueError in String Formatting with `str.format()` / f-strings ---")

# When using format specifiers, providing an invalid specifier can lead to ValueError.

value = 123.456

# Valid format specifier (2 decimal places)
print(f"Formatted float: {value:.2f}")

try:
    # Invalid format specifier: 'x' is for hexadecimal integers
    print(f"Formatted float with invalid specifier: {value:x}")
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: Unknown format code 'x' for object of type 'float'.")

# For `str.format()`
try:
    "Formatted float with invalid specifier: {:.x}".format(value)
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: Unknown format code 'x' for object of type 'float'.")

print("-" * 50 + "\n")


# --- 12. ValueError with `time.strptime()` (Similar to datetime) ---
print("--- 12. ValueError with `time.strptime()` ---")

import time

# Valid parse
time_string = "09:30:00"
format_string = "%H:%M:%S"
parsed_time = time.strptime(time_string, format_string)
print(f"Parsed time: {parsed_time}")

# Invalid hour (25)
invalid_time_string = "25:00:00"
try:
    time.strptime(invalid_time_string, format_string)
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: time data '25:00:00' does not match format '%H:%M:%S'.")
    print("Note: The error message often indicates a format mismatch, but it's really about the value being out of range for the format.")

# Mismatch between string and format
misaligned_time_string = "09-30-00"
try:
    time.strptime(misaligned_time_string, format_string)
except ValueError as e:
    print(f"Caught ValueError (expected): {e}")
    print("Reason: time data '09-30-00' does not match format '%H:%M:%S'.")

print("-" * 50 + "\n")


# --- 13. ValueError in List/Tuple Comprehensions (Conditional Logic) ---
print("--- 13. ValueError in List/Tuple Comprehensions (Conditional Logic) ---")

# While comprehensions themselves are generally safe, a `ValueError` can occur
# if an operation within the comprehension is applied to an element that causes it.

data_strings = ["1", "2", "invalid", "4"]

try:
    numbers = [int(s) for s in data_strings]
    print(f"Numbers from strings: {numbers}")
except ValueError as e:
    print(f"Caught ValueError in list comprehension (expected): {e}")
    print("Reason: 'invalid' cannot be converted to int.")

# Safe way using conditional filtering (excluding invalid values)
safe_numbers = []
for s in data_strings:
    try:
        safe_numbers.append(int(s))
    except ValueError:
        print(f"Skipping invalid number string: '{s}'")
print(f"Safe numbers: {safe_numbers}")

# Alternative with generator expression and filter (for more complex validation)
def is_int_convertible(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# You would typically filter first, then convert.
valid_number_strings = [s for s in data_strings if is_int_convertible(s)]
converted_numbers = [int(s) for s in valid_number_strings]
print(f"Converted numbers (filtered first): {converted_numbers}")

print("-" * 50 + "\n")


# --- 14. ValueError in Custom Data Validation (Input from User/File) ---
print("--- 14. ValueError in Custom Data Validation (Input from User/File) ---")

# When parsing user input or data from files, explicitly raising ValueError is crucial.

def get_age_from_input():
    while True:
        user_input = input("Please enter your age (a positive integer): ")
        try:
            age = int(user_input)
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Uncomment the line below to interact with the input prompt
# user_age = get_age_from_input()
# print(f"Your age is: {user_age}")

print("Demonstrating custom validation (no interactive input here):")
test_inputs = ["abc", "-5", "30", "0"]
for test_input in test_inputs:
    try:
        age = int(test_input)
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        print(f"Input '{test_input}' -> Valid Age: {age}")
    except ValueError as e:
        print(f"Input '{test_input}' -> Caught ValueError: {e}")

print("-" * 50 + "\n")


# --- 15. ValueError with `bytes.decode()` / `str.encode()` ---
print("--- 15. ValueError with `bytes.decode()` / `str.encode()` ---")

# Encoding/decoding operations can raise ValueError if the data is not valid for the specified encoding.

# Decoding bytes that are not valid UTF-8
invalid_bytes = b'\x80\x81\x82' # These bytes are not valid in UTF-8
try:
    decoded_string = invalid_bytes.decode('utf-8')
except ValueError as e:
    print(f"Caught ValueError (expected for decode): {e}")
    print("Reason: invalid start byte or continuation byte in UTF-8 sequence.")

# Encoding a string that cannot be represented in a specific encoding
# (e.g., trying to encode a character not present in 'ascii')
japanese_char = "こんにちは" # "konnichiwa"
try:
    encoded_bytes = japanese_char.encode('ascii')
except UnicodeEncodeError as e: # This specifically raises UnicodeEncodeError, a subclass of ValueError
    print(f"Caught UnicodeEncodeError (expected for encode): {e}")
    print("Reason: 'ascii' codec can't encode characters.")

print("-" * 50 + "\n")


print("--- End of More ValueError Examples ---")
