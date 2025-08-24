# ===========================================================
# 📌 DEQUE (Double-Ended Queue) from collections module
# ===========================================================

# Import syntax
from collections import deque

# ===========================================================
# 1️⃣ Creating a Deque
# ===========================================================
# Syntax:
# deque(iterable=None, maxlen=None)
# iterable → optional starting values (list, tuple, etc.)
# maxlen   → optional fixed maximum size (oldest elements removed when full)

# Empty deque
dq = deque()

# Deque from a list
dq_list = deque([1, 2, 3])

# Deque with a max size
dq_limit = deque([10, 20, 30], maxlen=5)

# ===========================================================
# 2️⃣ Basic Operations
# ===========================================================

dq = deque()

# Append to right (end)
dq.append(1)      # deque([1])
dq.append(2)      # deque([1, 2])

# Append to left (front)
dq.appendleft(0)  # deque([0, 1, 2])

# Pop from right (end)
dq.pop()          # removes 2 → deque([0, 1])

# Pop from left (front)
dq.popleft()      # removes 0 → deque([1])

# ===========================================================
# 3️⃣ Peek Elements
# ===========================================================
dq = deque([10, 20, 30])
first = dq[0]   # Peek first element (10)
last = dq[-1]   # Peek last element  (30)

# ===========================================================
# 4️⃣ Extend Operations
# ===========================================================

dq = deque([1, 2])

# Extend right
dq.extend([3, 4])       # deque([1, 2, 3, 4])

# Extend left (adds elements in reverse order at the front)
dq.extendleft([-1, -2]) # deque([-2, -1, 1, 2, 3, 4])

# ===========================================================
# 5️⃣ Rotation
# ===========================================================

dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)   # Right rotation by 2 → deque([4, 5, 1, 2, 3])
dq.rotate(-1)  # Left rotation by 1  → deque([5, 1, 2, 3, 4])

# ===========================================================
# 6️⃣ Maxlen Behavior
# ===========================================================
dq = deque(maxlen=3)  # Only 3 elements allowed
dq.extend([1, 2, 3])  # deque([1, 2, 3])
dq.append(4)          # deque([2, 3, 4]) → 1 removed automatically

# ===========================================================
# 7️⃣ Clearing and Counting
# ===========================================================
dq = deque([1, 2, 2, 3])

# Count occurrences
count_2 = dq.count(2)  # 2

# Remove first occurrence
dq.remove(2)           # deque([1, 2, 3])

# Clear all elements
dq.clear()             # deque([])

# ===========================================================
# 8️⃣ Example: Palindrome Check using Deque
# ===========================================================

def is_palindrome(s):
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():  # compare front and end
            return False
    return True

print(is_palindrome("level"))  # True
print(is_palindrome("python")) # False



from collections import deque

# A deque (double-ended queue) is a versatile data structure that allows for
# efficient appending and popping from both ends of a sequence.
# It's a generalization of stacks and queues.
# Deques are implemented in Python's `collections` module.

# --- Creating a Deque ---

# Syntax: deque([iterable], [maxlen])
# The optional 'iterable' argument can be any sequence (like a list or tuple).
# The optional 'maxlen' argument sets a fixed size for the deque.
# If maxlen is not specified, the deque can grow to any size.

# Example 1: Create an empty deque
my_deque = deque()
print(f"Empty deque: {my_deque}")

# Example 2: Create a deque from a list
my_deque_from_list = deque([10, 20, 30])
print(f"Deque from list: {my_deque_from_list}")

# Example 3: Create a deque with a max length
fixed_size_deque = deque(maxlen=3)
print(f"Fixed size deque: {fixed_size_deque}")

# --- Common Operations ---

# append(x): Add an element to the right end of the deque.
my_deque.append(40)
print(f"After appending 40 to the right: {my_deque}")

# appendleft(x): Add an element to the left end of the deque.
my_deque.appendleft(5)
print(f"After appending 5 to the left: {my_deque}")

# pop(): Remove and return an element from the right end of the deque.
popped_right = my_deque.pop()
print(f"Popped from the right: {popped_right}, Deque is now: {my_deque}")

# popleft(): Remove and return an element from the left end of the deque.
popped_left = my_deque.popleft()
print(f"Popped from the left: {popped_left}, Deque is now: {my_deque}")

# The fixed size deque automatically discards elements from the opposite end
# when it reaches its maximum length.
fixed_size_deque.append(1)
fixed_size_deque.append(2)
fixed_size_deque.append(3)
print(f"Fixed size deque filled: {fixed_size_deque}")
fixed_size_deque.append(4)  # '1' is automatically discarded from the left
print(f"Fixed size deque after appending 4: {fixed_size_deque}")

# --- Other Useful Methods ---

# extend(iterable): Extend the deque by appending elements from the iterable to the right.
my_deque.extend([50, 60])
print(f"After extending with [50, 60]: {my_deque}")

# extendleft(iterable): Extend the deque by prepending elements from the iterable to the left.
# Note: The iterable's elements are added one by one, so their order is reversed.
my_deque.extendleft([1, 2])
print(f"After extendingleft with [1, 2]: {my_deque}")  # Output will be deque([2, 1, ...])

# rotate(n): Rotate the deque n steps to the right (if n > 0) or left (if n < 0).
my_deque.rotate(1)
print(f"After rotating 1 step to the right: {my_deque}")

my_deque.rotate(-1)
print(f"After rotating 1 step to the left: {my_deque}")

# count(x): Count the number of occurrences of an element x.
my_deque.append(10)
print(f"Count of 10 in the deque: {my_deque.count(10)}")

# clear(): Remove all elements from the deque.
my_deque.clear()
print(f"After clearing the deque: {my_deque}")


from collections import deque

# A deque (double-ended queue) is a versatile data structure that allows for
# efficient appending and popping from both ends of a sequence.
# It's a generalization of stacks and queues.
# Deques are implemented in Python's `collections` module.

# --- Creating a Deque ---

# Syntax: deque([iterable], [maxlen])
# The optional 'iterable' argument can be any sequence (like a list or tuple).
# The optional 'maxlen' argument sets a fixed size for the deque.
# If maxlen is not specified, the deque can grow to any size.

# Example 1: Create an empty deque
my_deque = deque()
print(f"Empty deque: {my_deque}")

# Example 2: Create a deque from a list
my_deque_from_list = deque([10, 20, 30])
print(f"Deque from list: {my_deque_from_list}")

# Example 3: Create a deque with a max length
fixed_size_deque = deque(maxlen=3)
print(f"Fixed size deque: {fixed_size_deque}")

# --- Common Operations ---

# append(x): Add an element to the right end of the deque.
my_deque.append(40)
print(f"After appending 40 to the right: {my_deque}")

# appendleft(x): Add an element to the left end of the deque.
my_deque.appendleft(5)
print(f"After appending 5 to the left: {my_deque}")

# pop(): Remove and return an element from the right end of the deque.
popped_right = my_deque.pop()
print(f"Popped from the right: {popped_right}, Deque is now: {my_deque}")

# popleft(): Remove and return an element from the left end of the deque.
popped_left = my_deque.popleft()
print(f"Popped from the left: {popped_left}, Deque is now: {my_deque}")

# The fixed size deque automatically discards elements from the opposite end
# when it reaches its maximum length.
fixed_size_deque.append(1)
fixed_size_deque.append(2)
fixed_size_deque.append(3)
print(f"Fixed size deque filled: {fixed_size_deque}")
fixed_size_deque.append(4)  # '1' is automatically discarded from the left
print(f"Fixed size deque after appending 4: {fixed_size_deque}")

# --- Other Useful Methods ---

# extend(iterable): Extend the deque by appending elements from the iterable to the right.
my_deque.extend([50, 60])
print(f"After extending with [50, 60]: {my_deque}")

# extendleft(iterable): Extend the deque by prepending elements from the iterable to the left.
# Note: The iterable's elements are added one by one, so their order is reversed.
my_deque.extendleft([1, 2])
print(f"After extendingleft with [1, 2]: {my_deque}")  # Output will be deque([2, 1, ...])

# rotate(n): Rotate the deque n steps to the right (if n > 0) or left (if n < 0).
my_deque.rotate(1)
print(f"After rotating 1 step to the right: {my_deque}")

my_deque.rotate(-1)
print(f"After rotating 1 step to the left: {my_deque}")

# count(x): Count the number of occurrences of an element x.
my_deque.append(10)
print(f"Count of 10 in the deque: {my_deque.count(10)}")

# clear(): Remove all elements from the deque.
my_deque.clear()
print(f"After clearing the deque: {my_deque}")