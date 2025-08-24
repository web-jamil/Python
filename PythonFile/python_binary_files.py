# --- Python Binary Files: All About in Code ---

# Binary files store data as a sequence of bytes, unlike text files
# which store human-readable characters.
# Examples: images, audio, video, executable programs, compressed archives.

# Key Differences from Text Files:
# 1. Mode: Must include 'b' (e.g., 'rb', 'wb', 'ab').
# 2. Data Type: Read/written data is `bytes` objects, not `str` (strings).
# 3. Encoding: No `encoding` parameter is used for binary modes.
# 4. Newlines: No automatic newline translation. '\n' is just byte 0x0A.

import os

# --- 1. Writing to a Binary File ('wb' - Write Binary) ---

print("--- 1. Writing to a Binary File ('wb') ---")

# 'wb' mode:
# - Creates a new file if it doesn't exist.
# - If the file exists, its content is TRUNCATED (emptied).
# - Writes `bytes` objects.

try:
    with open("my_binary_file.bin", "wb") as f:
        # Write bytes literals (prefix 'b')
        f.write(b"Hello Binary World!\n") # 'H' is 0x48, 'e' is 0x65, '\n' is 0x0A etc.

        # Write bytes from a list of integers (each integer must be 0-255)
        f.write(bytes([0x01, 0x02, 0x03, 0xFF, 0x00, 0x7F]))

        # Encode a string to bytes (e.g., UTF-8)
        message = "This is a string encoded to bytes."
        f.write(message.encode('utf-8'))

        # Write some null bytes or specific control characters
        f.write(b'\x00\x00\x00') # Three null bytes

    print("Successfully wrote to 'my_binary_file.bin' using 'wb' mode.")
except IOError as e:
    print(f"Error writing binary file: {e}")


# --- 2. Reading from a Binary File ('rb' - Read Binary) ---

print("\n--- 2. Reading from a Binary File ('rb') ---")

# 'rb' mode:
# - Reads `bytes` objects.
# - File must exist.

try:
    with open("my_binary_file.bin", "rb") as f:
        # 2.1. Reading the entire content
        full_binary_content = f.read()
        print(f"Full binary content: {full_binary_content}")
        print(f"Type of content: {type(full_binary_content)}")
        print(f"Length of content: {len(full_binary_content)} bytes")

        # Decode a portion if you know its original encoding
        # (Be careful, decoding arbitrary bytes can lead to UnicodeDecodeError)
        try:
            # Assuming "Hello Binary World!\n" was UTF-8
            decoded_part = full_binary_content[0:len(b"Hello Binary World!\n")].decode('utf-8')
            print(f"Decoded 'Hello Binary World!': '{decoded_part.strip()}'")
        except UnicodeDecodeError:
            print("Could not decode the first part as UTF-8.")

        # 2.2. Reading specific number of bytes
        f.seek(0) # Reset cursor to the beginning
        first_5_bytes = f.read(5)
        print(f"\nFirst 5 bytes: {first_5_bytes}")

        next_2_bytes = f.read(2)
        print(f"Next 2 bytes: {next_2_bytes}")

        # 2.3. Reading in chunks (important for large files)
        f.seek(0) # Reset cursor again
        print("\nReading binary file in chunks (e.g., 8 bytes at a time):")
        while True:
            chunk = f.read(8) # Read 8 bytes at a time
            if not chunk: # If chunk is empty, end of file is reached
                break
            print(f"  Chunk: {chunk}")
except FileNotFoundError:
    print("Error: 'my_binary_file.bin' not found for reading.")
except IOError as e:
    print(f"Error reading binary file: {e}")


# --- 3. Appending to a Binary File ('ab' - Append Binary) ---

print("\n--- 3. Appending to a Binary File ('ab') ---")

# 'ab' mode:
# - Creates a new file if it doesn't exist.
# - If the file exists, new content is ADDED to the end of the file.
# - The file pointer is automatically positioned at the end for writing.

try:
    with open("my_binary_file.bin", "ab") as f:
        f.write(b'\xDE\xAD\xBE\xEF') # Append some more bytes
        f.write("Appended string".encode('ascii')) # Append encoded string
    print("Successfully appended to 'my_binary_file.bin' using 'ab' mode.")

    # Verify content after appending
    with open("my_binary_file.bin", "rb") as f:
        print(f"Full content after appending: {f.read()}")
except IOError as e:
    print(f"Error appending binary file: {e}")


# --- 4. Read/Write Binary Modes ('r+b', 'w+b', 'a+b', 'x+b') ---

print("\n--- 4. Read/Write Binary Modes ('+b') ---")

# These modes allow both reading and writing of bytes.

# 4.1. 'w+b' mode: Write and Read Binary
# - Truncates (empties) the file if it exists, creates if not.
# - Cursor starts at the beginning.
try:
    with open("wplus_binary_file.bin", "w+b") as f:
        f.write(b'\x01\x02\x03\x04\x05')
        print(f"Cursor after write (w+b): {f.tell()} bytes") # Should be 5
        f.seek(0) # Move cursor to the beginning
        content = f.read()
        print(f"Content read from 'wplus_binary_file.bin': {content}")
        f.write(b'\xAA\xBB') # Overwrites bytes at current cursor position (start)
        f.seek(0)
        print(f"Content after overwrite: {f.read()}")
except IOError as e:
    print(f"Error with 'w+b' mode: {e}")

# 4.2. 'a+b' mode: Append and Read Binary
# - Appends content to the end. Cursor starts at the end for writing.
# - To read, you must `seek(0)` to go to the beginning.
try:
    with open("aplus_binary_file.bin", "wb") as f: # Initialize with some data
        f.write(b'OriginalData')

    with open("aplus_binary_file.bin", "a+b") as f:
        f.write(b'AppendedData')
        print(f"Cursor after append (a+b): {f.tell()} bytes") # Should be 24 (12 + 12)
        f.seek(0) # Move cursor to beginning to read all
        content = f.read()
        print(f"Content from 'aplus_binary_file.bin' after append and seek: {content}")
except IOError as e:
    print(f"Error with 'a+b' mode: {e}")

# 4.3. 'x+b' mode: Exclusive Create and Read/Write Binary
# - Creates a new binary file for reading and writing.
# - Raises FileExistsError if the file already exists.
try:
    with open("xplus_binary_file.bin", "x+b") as f:
        f.write(b'Only if new!')
        f.seek(0)
        print(f"\nContent from 'xplus_binary_file.bin' (x+b): {f.read()}")
except FileExistsError:
    print("Caught expected FileExistsError for 'xplus_binary_file.bin' (already exists).")
except IOError as e:
    print(f"Error with 'x+b' mode: {e}")


# --- 5. Working with Specific Bytes and Bytearray ---

print("\n--- 5. Working with Specific Bytes and Bytearray ---")

# Bytes objects are immutable. `bytearray` objects are mutable.
data_bytes = b'\x01\x02\x03\x04'
print(f"Original bytes: {data_bytes}")

# Convert bytes to bytearray for modification
mutable_bytes = bytearray(data_bytes)
mutable_bytes[0] = 0xFF # Change the first byte
print(f"Modified bytearray: {mutable_bytes}")

# Write a bytearray to a binary file
try:
    with open("mutable_binary.bin", "wb") as f:
        f.write(mutable_bytes)
    print("Wrote mutable_bytes to 'mutable_binary.bin'.")

    with open("mutable_binary.bin", "rb") as f:
        read_back = f.read()
        print(f"Read back from 'mutable_binary.bin': {read_back}")
except IOError as e:
    print(f"Error with mutable binary file: {e}")


# --- 6. Common Use Case: Copying Binary Files ---

print("\n--- 6. Common Use Case: Copying Binary Files ---")

# Copying a binary file (e.g., an image, PDF) without corruption.
# Read in chunks to handle very large files efficiently.

# Create a dummy source file
try:
    with open("source_image.jpg", "wb") as f:
        f.write(b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x01\x00\x48\x00\x48\x00\x00' + b'\x00' * 1000) # Simple dummy JPEG header + some nulls
    print("Created 'source_image.jpg' (dummy).")
except IOError as e:
    print(f"Error creating source dummy image: {e}")

try:
    source_file_path = "source_image.jpg"
    destination_file_path = "copied_image.jpg"
    buffer_size = 4096 # Read/write in 4KB chunks

    with open(source_file_path, "rb") as source:
        with open(destination_file_path, "wb") as destination:
            while True:
                chunk = source.read(buffer_size)
                if not chunk: # No more data to read
                    break
                destination.write(chunk)
    print(f"'{source_file_path}' successfully copied to '{destination_file_path}'.")
except FileNotFoundError:
    print(f"Error: Source file '{source_file_path}' not found for copying.")
except IOError as e:
    print(f"Error during binary file copy: {e}")


# --- 7. Clean up created files ---

print("\n--- 7. Cleaning up created files ---")
files_to_clean = [
    "my_binary_file.bin",
    "wplus_binary_file.bin",
    "aplus_binary_file.bin",
    "xplus_binary_file.bin",
    "mutable_binary.bin",
    "source_image.jpg",
    "copied_image.jpg"
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")