import itertools

print("--- Python's Built-in enumerate() and zip() Functions (Advanced Use Cases) ---")
print("----------------------------------------------------------------------------\n")

# --- Advanced enumerate() Use Cases ---

print("--- Advanced enumerate() Use Cases ---\n")

# 1. enumerate() with List Comprehensions for Conditional Indexing/Modification
print("1. enumerate() with List Comprehensions for Conditional Indexing/Modification:")
data = [10, 5, 20, 15, 30, 8]

# Create a new list where values greater than 15 are replaced with 'HIGH'
# and keep track of their original index.
processed_data_with_indices = [
    (i, 'HIGH') if x > 15 else (i, x)
    for i, x in enumerate(data)
]
print(f"Original data: {data}")
print(f"Processed data with indices: {processed_data_with_indices}\n")

# Get indices of all even numbers
even_indices = [
    i for i, x in enumerate(data) if x % 2 == 0
]
print(f"Indices of even numbers in {data}: {even_indices}\n")


# 2. enumerate() for Creating Indexed Data Structures
print("2. enumerate() for Creating Indexed Data Structures:")

# Create a dictionary mapping item name to its original index
items = ['laptop', 'mouse', 'keyboard', 'monitor']
item_to_index = {item: idx for idx, item in enumerate(items)}
print(f"Item to index mapping: {item_to_index}")
print(f"Index of 'keyboard': {item_to_index['keyboard']}\n")

# Create a list of dictionaries with index and value
products = ['milk', 'bread', 'eggs']
product_details = [{'id': i, 'name': p} for i, p in enumerate(products, start=101)]
print(f"Product details with custom IDs: {product_details}\n")


# 3. enumerate() for Implementing "Roll Over" or Cyclic Behavior (less common, but possible)
print("3. enumerate() for Implementing 'Roll Over' or Cyclic Behavior:")
# Assign colors to items cyclically based on index and modulo operator
colors = ['red', 'green', 'blue']
items_to_color = ['itemA', 'itemB', 'itemC', 'itemD', 'itemE']

# Assign colors in a repeating pattern
colored_items = [
    (item, colors[i % len(colors)])
    for i, item in enumerate(items_to_color)
]
print(f"Items assigned cyclic colors: {colored_items}\n")


# 4. enumerate() in Complex Iteration Logic (e.g., finding sequences)
print("4. enumerate() in Complex Iteration Logic (e.g., finding sequences):")
sequence = [1, 5, 3, 5, 8, 5, 12, 5, 20]
target = 5
consecutive_count = 0
found_indices = []

for i, num in enumerate(sequence):
    if num == target:
        consecutive_count += 1
        if consecutive_count >= 2: # Found at least two consecutive
            # Adjust index to reflect the start of the consecutive sequence
            found_indices.append(i - consecutive_count + 1)
    else:
        consecutive_count = 0 # Reset count if not consecutive

# This example specifically looks for *consecutive* sequences of a target
# If you just wanted all indices of a target:
all_target_indices = [i for i, x in enumerate(sequence) if x == target]
print(f"All indices where {target} appears in {sequence}: {all_target_indices}\n")


# --- Advanced zip() Use Cases ---

print("--- Advanced zip() Use Cases ---\n")

# 1. zip() for Transposing Matrices/Lists of Lists
print("1. zip() for Transposing Matrices/Lists of Lists:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Original Matrix: {matrix}")

# The magic of zip(*matrix) unpacks the rows as arguments to zip
transposed_matrix = list(zip(*matrix))
print(f"Transposed Matrix: {transposed_matrix}\n")

# This works for any number of inner lists and their elements
matrix_variable_rows = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
transposed_variable_rows = list(zip(*matrix_variable_rows))
print(f"Original Variable Row Matrix: {matrix_variable_rows}")
print(f"Transposed Variable Row Matrix: {transposed_variable_rows}\n")


# 2. zip() for Parallel Iteration and Data Alignment
print("2. zip() for Parallel Iteration and Data Alignment:")
product_ids = ['P001', 'P002', 'P003']
product_names = ['Laptop', 'Mouse', 'Keyboard']
product_prices = [1200.00, 25.50, 75.00]
product_stock = [10, 50, 30]

print("Product Inventory Report:")
for pid, name, price, stock in zip(product_ids, product_names, product_prices, product_stock):
    print(f"ID: {pid}, Name: {name}, Price: ${price:.2f}, Stock: {stock}")
print("\n")


# 3. zip() with Iterators (e.g., from files or generators)
print("3. zip() with Iterators:")

# Simulate reading from two large files line by line
def read_lines(filename):
    # This is a generator function
    lines = {
        'file1.txt': ["Header A", "Data A1", "Data A2"],
        'file2.txt': ["Header B", "Data B1", "Data B2"]
    }
    for line in lines.get(filename, []):
        yield line

# Process lines from two "files" in parallel
print("Processing lines from simulated files:")
file1_lines = read_lines('file1.txt')
file2_lines = read_lines('file2.txt')

for line1, line2 in zip(file1_lines, file2_lines):
    print(f"File1: '{line1}', File2: '{line2}'")
print("\n")


# 4. zip() for Creating Paired Dictionaries (from two lists)
print("4. zip() for Creating Paired Dictionaries:")
headers = ['Name', 'Age', 'City']
row_data = ['John Doe', 30, 'New York']

# Create a dictionary for a single row
row_dict = dict(zip(headers, row_data))
print(f"Single row dictionary: {row_dict}\n")

# Example: Processing multiple rows
all_headers = ['ID', 'Product', 'Price', 'Quantity']
all_rows_data = [
    (1, 'Apple', 1.50, 100),
    (2, 'Banana', 0.75, 150),
    (3, 'Orange', 1.20, 80)
]

# Create a list of dictionaries, one for each row
parsed_records = [
    dict(zip(all_headers, row))
    for row in all_rows_data
]
print(f"Parsed records: {parsed_records}\n")


# 5. zip() and itertools.zip_longest for Robust Data Alignment
print("5. zip() and itertools.zip_longest for Robust Data Alignment:")
# zip_longest is crucial when iterables might have different lengths and you don't
# want to lose data from the longer one.

student_names_long = ['Alice', 'Bob', 'Charlie', 'David']
student_grades_short = ['A', 'B', 'C']

# Using zip_longest, 'N/A' will be filled for missing grades
student_grade_pairs_long = list(itertools.zip_longest(student_names_long, student_grades_short, fillvalue='N/A'))
print(f"Students and their grades (zip_longest): {student_grade_pairs_long}\n")

# This is useful for merging datasets where some entries might be incomplete.


# 6. Combining enumerate() and zip()
print("6. Combining enumerate() and zip():")

tasks = ['Clean room', 'Buy groceries', 'Pay bills']
priorities = ['High', 'Medium', 'Low']

# Enumerate tasks with their priorities, starting from 1
print("Numbered Tasks with Priorities:")
for i, (task, priority) in enumerate(zip(tasks, priorities), start=1):
    print(f"{i}. {task} (Priority: {priority})")
print("\n")

# Example: Process sensor readings with timestamps and device IDs
timestamps = ['2025-06-05 10:00:00', '2025-06-05 10:00:01', '2025-06-05 10:00:02']
device_ids = ['DEV_001', 'DEV_002', 'DEV_001']
readings = [23.5, 24.1, 23.9]

print("Indexed Sensor Data:")
for index, (ts, dev_id, reading) in enumerate(zip(timestamps, device_ids, readings)):
    print(f"Record {index}: Timestamp={ts}, Device={dev_id}, Reading={reading}°C")
print("\n")


print("--- End of Advanced enumerate() and zip() Demonstration ---")