# A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle.
# This means the last element added to the stack is the first one to be removed.
# A stack can be implemented using a list in Python.

class Stack:
    """A simple implementation of a stack data structure."""

    def __init__(self):
        """Initializes an empty list to store the stack elements."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty.
        Returns True if the stack is empty, False otherwise.
        """
        return not self.items

    def push(self, item):
        """Adds a new item to the top of the stack.
        This operation has a time complexity of O(1).
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Raises an IndexError if the stack is empty.
        This operation also has a time complexity of O(1).
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the item at the top of the stack without removing it.
        Raises an IndexError if the stack is empty.
        This operation is also O(1).
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        """Returns the number of items in the stack.
        This operation is O(1).
        """
        return len(self.items)

# --- Example Usage ---

# Create a new stack instance
my_stack = Stack()

# Check if the stack is empty
print(f"Is the stack empty? {my_stack.is_empty()}")  # Output: Is the stack empty? True

# Push some items onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check the size of the stack
print(f"The size of the stack is: {my_stack.size()}")  # Output: The size of the stack is: 3

# Peek at the top item
print(f"The item at the top is: {my_stack.peek()}")  # Output: The item at the top is: 30

# Pop an item from the stack
popped_item = my_stack.pop()
print(f"Popped item: {popped_item}")  # Output: Popped item: 30

# Check the new size and top item
print(f"The new size of the stack is: {my_stack.size()}")  # Output: The new size of the stack is: 2
print(f"The new top item is: {my_stack.peek()}")  # Output: The new top item is: 20

# Pop all remaining items
my_stack.pop()
my_stack.pop()

# Check if the stack is now empty
print(f"Is the stack empty now? {my_stack.is_empty()}")  # Output: Is the stack empty now? True

# Demonstrate error handling
try:
    my_stack.pop()
except IndexError as e:
    print(f"Error: {e}")  # Output: Error: pop from empty stack


# -----------------------------
# 1️⃣ Using a Python List as a Stack
# -----------------------------

# A stack is a LIFO (Last In First Out) data structure.
# In Python, we can use a list's append() to push and pop() to remove the last element.

stack = []  # empty stack

# Push elements
stack.append(10)  # stack = [10]
stack.append(20)  # stack = [10, 20]
stack.append(30)  # stack = [10, 20, 30]

# Pop elements
last_item = stack.pop()  # Removes 30, stack = [10, 20]

# Peek (check top element without removing)
top_item = stack[-1]  # 20

# Check if stack is empty
is_empty = len(stack) == 0  # False

# -----------------------------
# 2️⃣ Stack Implementation Using a Class
# -----------------------------

class Stack:
    def __init__(self):
        self.items = []  # internal list to store elements
    
    def push(self, item):
        self.items.append(item)  # add item to top
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # remove top item
        return None  # if stack is empty
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # return top without removing
        return None
    
    def is_empty(self):
        return len(self.items) == 0  # check if empty
    
    def size(self):
        return len(self.items)  # total items in stack

# Using the Stack class
s = Stack()
s.push(5)
s.push(15)
s.push(25)
top = s.peek()      # 25
removed = s.pop()   # removes 25
empty_check = s.is_empty()  # False

# -----------------------------
# 3️⃣ Stack Using collections.deque (Faster)
# -----------------------------

from collections import deque

stack_deque = deque()  # double-ended queue used as stack
stack_deque.append(100)  # push
stack_deque.append(200)
stack_deque.pop()        # pop (200 removed)

# -----------------------------
# 4️⃣ Stack Using queue.LifoQueue (Thread-Safe)
# -----------------------------

from queue import LifoQueue

stack_queue = LifoQueue(maxsize=5)  # max size optional
stack_queue.put(1)  # push
stack_queue.put(2)
stack_queue.get()   # pop (removes 2)
stack_queue.empty() # check if empty (False)

# -----------------------------
# 5️⃣ Example: Reverse a String Using a Stack
# -----------------------------

def reverse_string(text):
    stack = []
    for char in text:
        stack.append(char)  # push each character
    
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()  # pop to reverse order
    return reversed_text

result = reverse_string("STACK")  # "KCATS"
# Stack Implementation in Python

"""
Stack is a linear data structure that follows the LIFO (Last In First Out) principle.
Basic operations:
- push(item): Add an item to the top of the stack
- pop(): Remove and return the item from the top of the stack
- peek(): Return the top item without removing it
- is_empty(): Check if the stack is empty
- size(): Return the number of items in the stack
"""

# 1. Stack Implementation using List (Dynamic Array)
class StackList:
    def __init__(self):
        """Initialize an empty stack using Python list"""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack - O(1) amortized"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack - O(1)"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it - O(1)"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack - O(1)"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the stack"""
        return f"Stack({self.items})"


# 2. Stack Implementation using collections.deque
from collections import deque

class StackDeque:
    def __init__(self):
        """Initialize an empty stack using deque (more efficient for large stacks)"""
        self.items = deque()
    
    def push(self, item):
        """Add an item to the top of the stack - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack - O(1)"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it - O(1)"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack - O(1)"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the stack"""
        return f"Stack({list(self.items)})"


# 3. Stack Implementation using Linked List
class Node:
    """Node class for linked list implementation"""
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        """Initialize an empty stack using linked list"""
        self.top = None
        self._size = 0
    
    def push(self, item):
        """Add an item to the top of the stack - O(1)"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """Remove and return the top item from the stack - O(1)"""
        if not self.is_empty():
            popped_value = self.top.value
            self.top = self.top.next
            self._size -= 1
            return popped_value
        raise IndexError("pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it - O(1)"""
        if not self.is_empty():
            return self.top.value
        raise IndexError("peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty - O(1)"""
        return self.top is None
    
    def size(self):
        """Return the number of items in the stack - O(1)"""
        return self._size
    
    def __str__(self):
        """Return string representation of the stack"""
        items = []
        current = self.top
        while current:
            items.append(current.value)
            current = current.next
        return f"Stack({items[::-1]})"  # Reverse to show top first


# Example Usage
if __name__ == "__main__":
    print("Stack using List Implementation:")
    stack = StackList()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)            # Stack([10, 20, 30])
    print(stack.peek())     # 30
    print(stack.pop())      # 30
    print(stack.size())     # 2
    print(stack.is_empty()) # False
    
    print("\nStack using Deque Implementation:")
    stack = StackDeque()
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    print(stack)            # Stack(['apple', 'banana', 'cherry'])
    print(stack.pop())      # cherry
    print(stack.peek())     # banana
    
    print("\nStack using Linked List Implementation:")
    stack = StackLinkedList()
    stack.push(100)
    stack.push(200)
    stack.push(300)
    print(stack)            # Stack([300, 200, 100])
    print(stack.pop())      # 300
    print(stack.peek())     # 200
    print(stack.size())     # 2

def get_second_element(stack):
    """
    Returns the second element from the top of the stack without modifying the stack.
    Raises IndexError if stack has fewer than 2 elements.
    """
    if stack.size() < 2:
        raise IndexError("Stack has fewer than 2 elements")
    
    # Temporarily remove the top element
    top_element = stack.pop()
    
    # The new top is now the second element
    second_element = stack.peek()
    
    # Restore the original top element
    stack.push(top_element)
    
    return second_element


# Example usage with all three stack implementations
if __name__ == "__main__":
    print("List Implementation:")
    sl = StackList()
    sl.push(10)
    sl.push(20)
    sl.push(30)
    print(f"Full stack: {sl}")
    print(f"Second element: {get_second_element(sl)}")
    print(f"Stack after operation: {sl}")  # Unchanged
    
    print("\nDeque Implementation:")
    sd = StackDeque()
    sd.push("A")
    sd.push("B")
    sd.push("C")
    print(f"Full stack: {sd}")
    print(f"Second element: {get_second_element(sd)}")
    print(f"Stack after operation: {sd}")  # Unchanged
    
    print("\nLinked List Implementation:")
    sll = StackLinkedList()
    sll.push(100)
    sll.push(200)
    sll.push(300)
    print(f"Full stack: {sll}")
    print(f"Second element: {get_second_element(sll)}")
    print(f"Stack after operation: {sll}")  # Unchanged