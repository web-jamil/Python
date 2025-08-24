# --- IndexError: All About in Code ---

# An IndexError is raised when you try to access an index that is outside
# the valid range of indices for a sequence (like a list, tuple, or string).
# It means the index is too small (negative and out of bounds) or too large.

# --- 1. Basic IndexError: Accessing an Out-of-Bounds Index ---
print("--- 1. Basic IndexError: Accessing an Out-of-Bounds Index ---")

my_list = ['apple', 'banana', 'cherry']
my_tuple = (10, 20, 30, 40)
my_string = "Python"

# Valid indices
print(f"Accessing list[0]: {my_list[0]}")     # First element
print(f"Accessing list[-1]: {my_list[-1]}")   # Last element
print(f"Accessing tuple[2]: {my_tuple[2]}")   # Third element
print(f"Accessing string[3]: {my_string[3]}") # Fourth character

# Attempting to access an index beyond the length (causes IndexError)
try:
    print(my_list[3]) # Length is 3, valid indices are 0, 1, 2
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range.")

try:
    print(my_tuple[4]) # Length is 4, valid indices are 0, 1, 2, 3
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: tuple index out of range.")

try:
    print(my_string[6]) # Length is 6, valid indices are 0 to 5
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: string index out of range.")

# Attempting to access a negative index that is out of bounds
try:
    print(my_list[-4]) # Valid negative indices are -1, -2, -3
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range (too small).")

print("-" * 50 + "\n")


# --- 2. IndexError in Loops and Iteration ---
print("--- 2. IndexError in Loops and Iteration ---")

# A common mistake is to loop using a range that exceeds the sequence's length.

data = [100, 200, 300]
print(f"List 'data': {data}")

# Incorrect loop: `range(len(data) + 1)` goes one index too far
print("Incorrect loop (will cause IndexError):")
try:
    for i in range(len(data) + 1):
        print(f"  Accessing data[{i}]: {data[i]}")
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: loop tried to access index 3, but list length is 3 (max index 2).")

# Correct loop using `range(len(sequence))`
print("\nCorrect loop using `range(len(data))`: ")
for i in range(len(data)):
    print(f"  Accessing data[{i}]: {data[i]}")

# Pythonic way to iterate with index: `enumerate` (safer)
print("\nCorrect loop using `enumerate` (most Pythonic and safe):")
for index, value in enumerate(data):
    print(f"  Index: {index}, Value: {value}")

print("-" * 50 + "\n")


# --- 3. IndexError with Empty Sequences ---
print("--- 3. IndexError with Empty Sequences ---")

# Attempting to access any index on an empty sequence will always result in IndexError.

empty_list = []
empty_string = ""
empty_tuple = ()

try:
    print(empty_list[0])
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range for an empty list.")

try:
    print(empty_string[0])
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: string index out of range for an empty string.")

print("-" * 50 + "\n")


# --- 4. Preventing IndexError (Best Practices) ---
print("--- 4. Preventing IndexError (Best Practices) ---")

# 4.1 Check Length Before Accessing
my_items = ['A', 'B']
index_to_check = 2

if index_to_check < len(my_items):
    print(f"Item at index {index_to_check}: {my_items[index_to_check]}")
else:
    print(f"Index {index_to_check} is out of bounds for list of length {len(my_items)}.")

# 4.2 Use `try-except` blocks for robustness
def get_element_safely(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        print(f"Warning: Index {index} is out of range for sequence of length {len(sequence)}.")
        return None # Or raise a custom exception, or return a default value

print(f"Safe access at index 0: {get_element_safely(my_items, 0)}")
print(f"Safe access at index 2: {get_element_safely(my_items, 2)}")
print(f"Safe access for empty list: {get_element_safely([], 0)}")

# 4.3 Use `for...in` loops or `enumerate` for iteration (avoids manual indexing)
print("\nUsing `for...in` for values directly:")
for item in my_items:
    print(f"Item: {item}")

print("-" * 50 + "\n")


# --- 5. IndexError with Slicing (Slicing is generally safe) ---
print("--- 5. IndexError with Slicing (Slicing is generally safe) ---")

# Slicing is inherently more robust than direct indexing regarding out-of-bounds.
# It does *not* raise an IndexError if slice boundaries are out of range;
# it simply returns a partial or empty sequence.

long_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice within bounds (OK)
print(f"Slice [1:4]: {long_list[1:4]}")

# Slice extending beyond the end (OK, truncates)
print(f"Slice [5:20]: {long_list[5:20]}") # No IndexError, just takes up to the end

# Slice starting beyond the end (OK, returns empty)
print(f"Slice [15:20]: {long_list[15:20]}") # No IndexError, returns empty list

# Negative slices out of bounds (OK)
print(f"Slice [-15:-2]: {long_list[-15:-2]}") # Works as expected, effectively [0:-2]

print("-" * 50 + "\n")


# --- 6. IndexError with Nested Sequences ---
print("--- 6. IndexError with Nested Sequences ---")

# When dealing with lists of lists (matrices) or other nested structures,
# you can get an IndexError at any level of indexing.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valid access
print(f"Element at [1][1]: {matrix[1][1]}") # 5

# Invalid first index
try:
    print(matrix[3][0]) # Index 3 for row is out of range
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range for the outer list.")

# Invalid second index (after first index is valid)
try:
    print(matrix[0][3]) # Index 3 for column in row 0 is out of range
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range for the inner list.")

# What if a nested element is not a sequence? (This would be TypeError, not IndexError)
mixed_list = [10, [20, 30], 40]
try:
    print(mixed_list[0][0]) # Trying to index an integer (10)
except TypeError as e:
    print(f"Caught TypeError (expected, not IndexError): {e}")
    print("Reason: 'int' object is not subscriptable.")

print("-" * 50 + "\n")


# --- 7. IndexError in String Operations ---
print("--- 7. IndexError in String Operations ---")

# Strings behave like tuples for indexing.
my_word = "Python"

# Valid index
print(f"First character: {my_word[0]}")

# Out-of-bounds index
try:
    print(my_word[len(my_word)])
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: string index out of range.")

print("-" * 50 + "\n")


# --- 8. IndexError from Functions Returning Sequences ---
print("--- 8. IndexError from Functions Returning Sequences ---")

# If a function is expected to return a sequence, but it returns an empty one,
# or its length is not what's expected, subsequent indexing can cause IndexError.

def get_config_values(key):
    config_data = {
        "users": ["admin", "guest"],
        "roles": [] # Empty list
    }
    return config_data.get(key, []) # Return empty list if key not found

user_list = get_config_values("users")
print(f"First user: {user_list[0]}")

roles_list = get_config_values("roles")
try:
    print(f"First role: {roles_list[0]}") # Will fail as roles_list is empty
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list index out of range for empty list returned by function.")

# Safer way with check
permissions_list = get_config_values("permissions") # Key not found, returns empty list
if permissions_list:
    print(f"First permission: {permissions_list[0]}")
else:
    print("No permissions found.")

print("-" * 50 + "\n")


print("--- End of IndexError demonstration ---")



# --- IndexError: More Examples (Continued) ---

# This section provides further illustrations of IndexError, focusing on
# less common scenarios, interactions with specific data structures,
# and practical implications.

# --- 9. IndexError with Deletion (del statement) ---
print("--- 9. IndexError with Deletion (del statement) ---")

# The `del` statement can remove items by index. If the index is invalid,
# it will raise an IndexError.

task_list = ["Write report", "Send email", "Call client"]
print(f"Initial task list: {task_list}")

# Valid deletion
del task_list[1]
print(f"After deleting index 1: {task_list}")

# Attempt to delete an out-of-bounds index
try:
    del task_list[2] # List now has 2 elements (indices 0, 1)
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: list assignment index out of range (for del).")

print("-" * 50 + "\n")


# --- 10. IndexError in Tuple Unpacking with String/List Elements ---
print("--- 10. IndexError in Tuple Unpacking with String/List Elements ---")

# When unpacking elements from a sequence, if an element itself is a sequence
# and you try to unpack *it* with an out-of-bounds index, it's an IndexError.

records = [
    ("Alice", ["Math", "Physics"]),
    ("Bob", ["Chemistry"]),
    ("Charlie", []), # Empty list for courses
]

print("Processing student records:")
for name, courses in records:
    try:
        first_course = courses[0] # This will raise IndexError if 'courses' is empty
        print(f"  {name}'s first course: {first_course}")
    except IndexError as e:
        print(f"  Caught IndexError for {name}'s courses (expected): {e}")
        print(f"  Reason: 'courses' list for {name} is empty or index 0 is out of range.")

# Safer approach: check length or use .get() for dicts, or slicing for lists/tuples
print("\nProcessing student records (safer):")
for name, courses in records:
    if courses: # Check if the list is not empty
        print(f"  {name}'s first course (safe): {courses[0]}")
    else:
        print(f"  {name} has no courses listed.")

print("-" * 50 + "\n")


# --- 11. IndexError in String Operations (Accessing Characters) ---
print("--- 11. IndexError in String Operations (Accessing Characters) ---")

# While basic string indexing was covered, let's look at more dynamic examples.

user_input_word = "hello" # Imagine this comes from user input
# user_input_word = "" # Uncomment to test empty string

if user_input_word: # Check if string is not empty before accessing
    first_char = user_input_word[0]
    print(f"First character of '{user_input_word}': {first_char}")
else:
    print(f"Input word '{user_input_word}' is empty, cannot get first character.")

# Accessing a character based on a calculated or external index
sentence = "Python is fun"
index_to_extract = 7 # Corresponds to 's'
# index_to_extract = 100 # Uncomment to test out-of-bounds

try:
    char = sentence[index_to_extract]
    print(f"Character at index {index_to_extract}: '{char}'")
except IndexError as e:
    print(f"Caught IndexError for string (expected): {e}")
    print(f"Reason: Index {index_to_extract} is out of bounds for string of length {len(sentence)}.")

print("-" * 50 + "\n")


# --- 12. IndexError with `pop()` Method on Lists ---
print("--- 12. IndexError with `pop()` Method on Lists ---")

# The `pop(index)` method removes and returns the item at the given index.
# If no index is specified, it removes and returns the last item.
# If the list is empty or the index is out of range, it raises IndexError.

my_queue = ['task1', 'task2', 'task3']
print(f"Initial queue: {my_queue}")

# Pop last item (no index given)
removed_item = my_queue.pop()
print(f"Popped (last item): {removed_item}, Queue: {my_queue}")

# Pop specific item by index
removed_item_by_index = my_queue.pop(0)
print(f"Popped (index 0): {removed_item_by_index}, Queue: {my_queue}")

# Now queue is ['task3']
# Attempt to pop from an empty list (will become empty after next pop)
try:
    my_queue.pop() # Removes 'task3'
    print(f"Queue after one more pop: {my_queue}")
    my_queue.pop() # Now list is empty, this will cause error
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: pop from empty list.")

# Attempt to pop an invalid index from a non-empty list
my_numbers = [1, 2]
try:
    my_numbers.pop(2) # Index 2 is out of range (valid are 0, 1)
except IndexError as e:
    print(f"Caught IndexError (expected): {e}")
    print("Reason: pop index out of range.")

print("-" * 50 + "\n")


# --- 13. IndexError in Game Development / Grid Systems ---
print("--- 13. IndexError in Game Development / Grid Systems ---")

# In games or simulations with grids (like a board game, maze, or pixel grid),
# accessing coordinates outside the grid's boundaries is a common source of IndexError.

board = [
    ['.', 'X', '.'],
    ['O', '.', 'X'],
    ['.', 'O', '.']
]
BOARD_SIZE = 3 # 3x3 board

def get_board_piece(row, col):
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return board[row][col]
    else:
        # Instead of raising IndexError, handle it gracefully
        print(f"Warning: Coordinates ({row}, {col}) are out of board bounds.")
        return None

# Valid moves
print(f"Piece at (0, 1): {get_board_piece(0, 1)}") # X
print(f"Piece at (2, 2): {get_board_piece(2, 2)}") # .

# Invalid moves (would cause IndexError if not checked)
print(f"Piece at (3, 0): {get_board_piece(3, 0)}") # Out of bounds row
print(f"Piece at (1, -1): {get_board_piece(1, -1)}") # Out of bounds column (negative)

# Direct (unsafe) access for demonstration
try:
    print(board[3][0])
except IndexError as e:
    print(f"Caught IndexError (expected for direct access): {e}")
    print("Reason: list index out of range for row 3.")

print("-" * 50 + "\n")


# --- 14. IndexError with Queue/Stack Implementations using Lists ---
print("--- 14. IndexError with Queue/Stack Implementations using Lists ---")

# When implementing basic queues/stacks with lists, ensure operations
# like `pop(0)` (for queue) or accessing specific indices don't fail on empty lists.

class SimpleQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        try:
            return self._queue.pop(0) # Raises IndexError if queue is empty
        except IndexError:
            print("Error: Cannot dequeue from an empty queue.")
            return None

    def peek(self):
        try:
            return self._queue[0] # Raises IndexError if queue is empty
        except IndexError:
            print("Error: Queue is empty, cannot peek.")
            return None

    def is_empty(self):
        return len(self._queue) == 0

q = SimpleQueue()
q.enqueue("data1")
q.enqueue("data2")

print(f"Queue is empty? {q.is_empty()}")
print(f"Peek: {q.peek()}")
print(f"Dequeued: {q.dequeue()}")
print(f"Dequeued: {q.dequeue()}")

print("\nAttempting to dequeue from empty queue:")
print(f"Dequeued: {q.dequeue()}") # This will print the error message and return None
print(f"Peek: {q.peek()}")        # This will print the error message and return None

print("-" * 50 + "\n")

print("--- End of More IndexError Examples ---")