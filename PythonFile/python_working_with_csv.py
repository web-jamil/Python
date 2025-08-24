# --- Python Working with CSV Files: All About in Code ---

# The `csv` module in Python provides functionality to work with CSV files,
# making it easy to read and write tabular data.

import csv
import os

# --- 1. Writing to a CSV File ---

print("--- 1. Writing to a CSV File ---")

# 1.1. Writing a list of lists using csv.writer
# When opening a CSV file, always use `newline=''` to prevent extra blank rows.

output_csv_file_basic = "output_data_basic.csv"
header_basic = ["Name", "Age", "City"]
data_basic = [
    ["Alice", 30, "New York"],
    ["Bob", 24, "London"],
    ["Charlie", 35, "Paris"]
]

try:
    with open(output_csv_file_basic, "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(header_basic)

        # Write multiple data rows
        csv_writer.writerows(data_basic)
    print(f"'{output_csv_file_basic}' created and written successfully.")
except IOError as e:
    print(f"Error writing to '{output_csv_file_basic}': {e}")


# 1.2. Writing a list of dictionaries using csv.DictWriter
# DictWriter maps dictionaries to rows. The `fieldnames` parameter is crucial.

output_csv_file_dict = "output_data_dict.csv"
fieldnames_dict = ["Product", "Price", "Quantity"]
data_dict = [
    {"Product": "Laptop", "Price": 1200, "Quantity": 5},
    {"Product": "Mouse", "Price": 25, "Quantity": 50},
    {"Product": "Keyboard", "Price": 75, "Quantity": 20}
]

try:
    with open(output_csv_file_dict, "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames_dict)

        # Write the header row (using fieldnames)
        csv_writer.writeheader()

        # Write the data rows
        csv_writer.writerows(data_dict)
    print(f"'{output_csv_file_dict}' created and written successfully using DictWriter.")
except IOError as e:
    print(f"Error writing to '{output_csv_file_dict}': {e}")


# --- 2. Reading from a CSV File ---

print("\n--- 2. Reading from a CSV File ---")

# 2.1. Reading row by row using csv.reader (yields lists)
# Each row is returned as a list of strings.

try:
    with open(output_csv_file_basic, "r", newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)

        print(f"\nContent of '{output_csv_file_basic}' (csv.reader):")
        header_read = next(csv_reader) # Read the header row
        print(f"Header: {header_read}")

        for row in csv_reader:
            print(f"Row: {row}")
            # You can access elements by index:
            # print(f"  Name: {row[0]}, Age: {row[1]}")
except FileNotFoundError:
    print(f"Error: '{output_csv_file_basic}' not found for reading.")
except IOError as e:
    print(f"Error reading '{output_csv_file_basic}': {e}")


# 2.2. Reading into dictionaries using csv.DictReader (yields dictionaries)
# Each row is returned as a dictionary where keys are the column headers.

try:
    with open(output_csv_file_dict, "r", newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        print(f"\nContent of '{output_csv_file_dict}' (csv.DictReader):")
        # DictReader automatically uses the first row as fieldnames (keys)
        print(f"Fieldnames (Keys): {csv_reader.fieldnames}")

        for row_dict in csv_reader:
            print(f"Row (Dict): {row_dict}")
            # Access elements by column name:
            # print(f"  Product: {row_dict['Product']}, Price: {row_dict['Price']}")
except FileNotFoundError:
    print(f"Error: '{output_csv_file_dict}' not found for DictReader.")
except IOError as e:
    print(f"Error reading '{output_csv_file_dict}' with DictReader: {e}")


# --- 3. CSV Dialects and Delimiters ---

print("\n--- 3. CSV Dialects and Delimiters ---")

# CSV files can use different delimiters (e.g., tab, semicolon) and quoting rules.
# A 'dialect' encapsulates these rules.

# Example: Tab-separated values (TSV)
tsv_file = "output_data.tsv"
tsv_data = [
    ["ID", "Description", "Value"],
    ["A001", "First Item", "100"],
    ["B002", "Second Item, with comma", "250"],
    ["C003", "Third Item", "50"]
]

# Writing TSV
try:
    with open(tsv_file, "w", newline='', encoding="utf-8") as tsvfile:
        # Specify delimiter='\t' for tab-separated
        tsv_writer = csv.writer(tsvfile, delimiter='\t')
        tsv_writer.writerows(tsv_data)
    print(f"'{tsv_file}' created as a tab-separated file.")
except IOError as e:
    print(f"Error writing TSV file: {e}")

# Reading TSV
try:
    with open(tsv_file, "r", newline='', encoding="utf-8") as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        print(f"\nContent of '{tsv_file}' (TSV reader):")
        for row in tsv_reader:
            print(f"TSV Row: {row}")
except FileNotFoundError:
    print(f"Error: '{tsv_file}' not found for TSV reading.")
except IOError as e:
    print(f"Error reading TSV file: {e}")


# Example: Handling quotes (default is QUOTE_MINIMAL)
# QUOTE_ALL: Always quote fields.
# QUOTE_NONNUMERIC: Quote all non-numeric fields.
# QUOTE_NONE: Never quote fields (can be problematic if fields contain delimiters).
# QUOTE_MINIMAL (default): Only quote fields containing special characters (delimiter, quotechar, line terminator).

quotes_csv_file = "quotes_example.csv"
quotes_data = [
    ["ID", "Text with, comma", "Number"],
    [1, "Another, text with 'quotes'", 10],
    [2, "No special chars", 20]
]

try:
    with open(quotes_csv_file, "w", newline='', encoding="utf-8") as csvfile:
        csv_writer_minimal = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer_minimal.writerow(["Default Quoting (MINIMAL)"])
        csv_writer_minimal.writerows(quotes_data)

        # Reopen in append mode to show another quoting
        csv_writer_all = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer_all.writerow([]) # Empty line for separation
        csv_writer_all.writerow(["All Fields Quoted (ALL)"])
        csv_writer_all.writerows(quotes_data)

    print(f"'{quotes_csv_file}' created with different quoting styles.")
except IOError as e:
    print(f"Error writing quotes example: {e}")

# Read and print raw content to see quoting
try:
    with open(quotes_csv_file, "r", encoding="utf-8") as csvfile:
        print(f"\nRaw content of '{quotes_csv_file}' to observe quoting:")
        print(csvfile.read())
except FileNotFoundError:
    print(f"Error: '{quotes_csv_file}' not found for raw reading.")


# --- 4. Error Handling with CSV Files ---

print("\n--- 4. Error Handling with CSV Files ---")

# FileNotFoundError: If the file doesn't exist for reading.
try:
    with open("non_existent.csv", "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Caught FileNotFoundError: 'non_existent.csv' not found.")
except IOError as e:
    print(f"Caught generic IOError: {e}")

# Bad csv format (e.g., too many fields in a row, unclosed quotes)
# This can sometimes cause `_csv.Error` or `csv.Error` (subclass of Exception)

# Create a malformed CSV for demonstration
malformed_csv = "malformed.csv"
try:
    with open(malformed_csv, "w", newline='') as f:
        f.write("Header1,Header2\n")
        f.write("Data1,Data2,ExtraData\n") # Too many fields
        f.write("Unclosed quote,\"text with\n") # Unclosed quote
except IOError as e:
    print(f"Error creating malformed CSV: {e}")


try:
    with open(malformed_csv, "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except csv.Error as e: # Specific error for CSV parsing issues
    print(f"Caught csv.Error: Malformed CSV detected: {e}")
except IOError as e:
    print(f"Caught generic IOError during malformed CSV read: {e}")
except Exception as e:
    print(f"Caught unexpected error: {e}")


# --- 5. Clean up created files ---

print("\n--- 5. Cleaning up created files ---")
files_to_clean = [
    output_csv_file_basic,
    output_csv_file_dict,
    tsv_file,
    quotes_csv_file,
    malformed_csv
]

for f in files_to_clean:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")