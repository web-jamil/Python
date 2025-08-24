print("--- Python Special Operators ---")
print("--------------------------------\n")

# Python has several operators that don't fit neatly into arithmetic,k
# comparison, logical, assignment, membership, or identity categories.
# These often perform specific, unique functions.

# 1. Walrus Operator (Assignment Expression) (:=) - Python 3.8+
print("1. Walrus Operator (Assignment Expression) (:=):")
# Allows you to assign a value to a variable as part of a larger expression.
# Useful for reducing redundant code, especially in conditional statements or loops.

# Without walrus operator:
print("  Without walrus operator:")
data = [1, 2, 3, 4, 5]
n = len(data)
if n > 3:
    print(f"    List is long: {n} elements.")

# With walrus operator:
print("  With walrus operator:")
if (n := len(data)) > 3: # Assigns len(data) to n, then evaluates the condition
    print(f"    List is long: {n} elements.")




# Another common use case: processing stream of data
# while True:
#     line = input("Enter something (or 'quit'): ")
#     if line == 'quit':
#         break
#     print(f"You entered: {line}")

# Using walrus operator:
print("  Using walrus operator in a loop (conceptual):")
# while (line := input("Enter something (or 'quit'): ")) != 'quit':
#     print(f"    You entered: {line}")
print("    (Example code not runnable in this static block, but demonstrates concept)\n")


# 2. Ternary Operator (Conditional Expression) (if-else)
print("2. Ternary Operator (Conditional Expression):")
# Allows assigning a value to a variable based on a condition in a single line.
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

temperature = 28
weather = "Hot" if temperature > 25 else ("Warm" if temperature > 15 else "Cold")
print(f"Temperature: {temperature}°C, Weather: {weather}\n")


# 3. Tuple Packing and Unpacking (implicit use of comma and assignment)
print("3. Tuple Packing and Unpacking:")
# Packing: Multiple values on the right side of an assignment are "packed" into a tuple.
packed_tuple = 10, 20, "hello"
print(f"Packed tuple: {packed_tuple} (type: {type(packed_tuple)})")

# Unpacking: Elements of an iterable (like a tuple or list) are "unpacked" into variables.
x, y, message = packed_tuple
print(f"Unpacked: x={x}, y={y}, message='{message}'")

# Swapping variables (classic Pythonic use of unpacking)
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a # The right side (b, a) creates a temporary tuple (10, 5), then unpacks it.
print(f"After swap: a={a}, b={b}\n")


# 4. Starred Assignment / Extended Iterable Unpacking (*) - Python 3.x
print("4. Starred Assignment / Extended Iterable Unpacking (*):")
# Allows you to "catch" multiple values from an iterable into a list.
# Only one starred expression is allowed in an unpacking assignment.

numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(f"Original: {numbers}")
print(f"  first={first}, middle={middle}, last={last}")

first, *rest = numbers
print(f"  first={first}, rest={rest}")

*start, end = numbers
print(f"  start={start}, end={end}\n")

# Can also be used in function calls (unpacking arguments)
def sum_all(*args):
    return sum(args)

my_nums = [1, 2, 3, 4]
total = sum_all(*my_nums) # Unpacks the list into individual arguments
print(f"sum_all(*{my_nums}) = {total}\n")


# 5. `isinstance()` and `issubclass()` (Functions, not strictly operators, but often used as such)
print("5. `isinstance()` and `issubclass()` (Type checking):")
# `isinstance(object, classinfo)`: Checks if an object is an instance of a class or a tuple of classes.
# `issubclass(class, classinfo)`: Checks if a class is a subclass of another class or a tuple of classes.

class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

my_dog = Dog()
my_cat = Cat()

print(f"my_dog is Dog instance: {isinstance(my_dog, Dog)}")
print(f"my_dog is Animal instance: {isinstance(my_dog, Animal)}")
print(f"my_dog is Cat instance: {isinstance(my_dog, Cat)}")
print(f"my_dog is (Dog, Cat) instance: {isinstance(my_dog, (Dog, Cat))}\n") # Check against multiple types

print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
print(f"Cat is subclass of Dog: {issubclass(Cat, Dog)}")
print(f"Animal is subclass of object: {issubclass(Animal, object)}\n")


# 6. `callable()` (Function, checks if an object can be called)
print("6. `callable()` (Checks if an object can be called):")
def my_function():
    pass

class MyClass:
    def __call__(self):
        pass

my_object = MyClass()

print(f"my_function is callable: {callable(my_function)}")
print(f"my_object is callable: {callable(my_object)}") # True because it has __call__ method
print(f"123 is callable: {callable(123)}\n")


print("--- End of Python Special Operators Demonstration ---")