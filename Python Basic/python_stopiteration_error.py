# 1. How StopIteration is raised implicitly by for loops

my_list = [1, 2, 3]
iterator = iter(my_list) # Get an iterator for the list

print("--- Demonstrating StopIteration with a 'for' loop (implicit) ---")
for item in my_list:
    print(item)
# The 'for' loop handles StopIteration internally when the iterator is exhausted.
# You will not see a StopIteration error here.

print("\n--- Demonstrating StopIteration manually with next() ---")
# 2. How to observe StopIteration directly using next()

my_list_2 = ['a', 'b']
iterator_2 = iter(my_list_2)

try:
    print(next(iterator_2)) # Output: a
    print(next(iterator_2)) # Output: b
    print(next(iterator_2)) # This will raise StopIteration
except StopIteration:
    print("Caught StopIteration: The iterator is exhausted.")

print("\n--- Implementing a custom iterator that raises StopIteration ---")
# 3. Creating a custom iterator that explicitly raises StopIteration

class MyCustomIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration # Signal that there are no more items

custom_iter = MyCustomIterator(1, 4)

print("Iterating through MyCustomIterator:")
for num in custom_iter:
    print(num)

print("\n--- Using a generator function which implicitly handles StopIteration ---")
# 4. Generator functions and StopIteration

def my_generator():
    yield 10
    yield 20
    yield 30

gen = my_generator()

print("Iterating through my_generator:")
for val in gen:
    print(val)
# Generator functions automatically raise StopIteration when they run out of 'yield' statements.

print("\n--- What happens if you try to call next() on an exhausted generator ---")
exhausted_gen = my_generator()
try:
    next(exhausted_gen) # 10
    next(exhausted_gen) # 20
    next(exhausted_gen) # 30
    next(exhausted_gen) # This will raise StopIteration
except StopIteration:
    print("Caught StopIteration from an exhausted generator.")






class Countdown:
    """
    A simple iterator class that counts down from a given number to 1.
    It raises StopIteration when the countdown is complete.
    """
    def __init__(self, start):
        if not isinstance(start, int) or start < 1:
            raise ValueError("Countdown must start from a positive integer.")
        self.current = start

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the iterator.
        Raises StopIteration when there are no more items.
        """
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            # When self.current becomes 0 or less, we've exhausted the countdown.
            # We signal this by raising StopIteration.
            raise StopIteration

# --- Demonstration of the Countdown iterator ---

print("--- Using 'for' loop (handles StopIteration implicitly) ---")
countdown_for = Countdown(5)
for number in countdown_for:
    print(number)
# The 'for' loop catches the StopIteration internally, so you won't see it as an error.

print("\n--- Using next() directly (demonstrates StopIteration explicitly) ---")
countdown_next = Countdown(3)
try:
    print(next(countdown_next)) # Output: 3
    print(next(countdown_next)) # Output: 2
    print(next(countdown_next)) # Output: 1
    print(next(countdown_next)) # This call will raise StopIteration
except StopIteration:
    print("Caught StopIteration: The countdown has finished.")

print("\n--- What happens if you try to iterate an exhausted iterator ---")
# Once an iterator is exhausted (StopIteration has been raised),
# subsequent calls to next() will continue to raise StopIteration.
countdown_exhausted = Countdown(1)
try:
    print(next(countdown_exhausted)) # Output: 1
    print(next(countdown_exhausted)) # This will raise StopIteration
except StopIteration:
    print("Caught StopIteration again from an exhausted iterator.")
    try:
        print(next(countdown_exhausted)) # And again...
    except StopIteration:
        print("Still caught StopIteration, as expected.")

print("\n--- Creating a new instance to restart iteration ---")
# To start the countdown again, you need a new instance of the iterator.
new_countdown = Countdown(2)
for num in new_countdown:
    print(f"New countdown: {num}")