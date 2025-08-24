# 🔑 Keyword arguments in Python functions

# Function using keyword arguments with default values
def describe_pet(animal_type, pet_name="Unknown", age=0):
    print(f"Type: {animal_type}, Name: {pet_name}, Age: {age}")

describe_pet(animal_type="Cat", pet_name="Whiskers", age=3)
describe_pet("Dog", age=5)  # mixed positional + keyword usage


# 🌈 Keyword arguments allow flexible ordering
def log_message(level="INFO", message="No message", timestamp=None):
    print(f"[{level}] {timestamp}: {message}")

log_message(message="System rebooted", timestamp="2025-08-05 13:00")


# 🛑 Using keyword arguments after positional ones
def add(a, b=10):
    return a + b

print(add(5))            # Output: 15
print(add(a=5, b=7))     # Output: 12


# 🔨 Using keyword arguments in classes

class Rectangle:
    def __init__(self, width=1, height=1, color="blue"):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.width * self.height

rect1 = Rectangle(width=5, height=3)
rect2 = Rectangle(color="green", height=2)

print(rect1.area())   # Output: 15
print(rect2.color)    # Output: green


# ✅ Keyword arguments with **kwargs for dynamic input

def flexible_logger(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

flexible_logger(level="DEBUG", timestamp="13:15", user="admin")


class Signal:
    def __init__(self, **components):
        self.components = components

    def summary(self):
        return ", ".join(f"{k}={v}" for k, v in self.components.items())

signal1 = Signal(freq=440, amp=0.8, phase=0)
print(signal1.summary())  # Output: freq=440, amp=0.8, phase=0