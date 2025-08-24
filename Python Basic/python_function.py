print("--- Python Functions: Practice Code ---")

# --- 1. What is a Function? ---
print("\n--- 1. What is a Function? ---")
print("A function is a block of organized, reusable code that performs a single, related action.")
print("Functions provide better modularity for your application and a high degree of code reusing.")
print("You define functions once and can call them multiple times.")

# --- 2. Defining a Simple Function ---
print("\n--- 2. Defining a Simple Function ---")

# Use the 'def' keyword, followed by the function name, parentheses (), and a colon :
# The code block is indented.
def greet():
    """This function prints a simple greeting.""" # This is a docstring (documentation)
    print("Hello from a function!")

# --- 3. Calling a Function ---
print("\n--- 3. Calling a Function ---")

# To execute the code inside a function, you 'call' it by its name followed by parentheses.
greet() # Call the greet function

# --- 4. Function Parameters (Arguments) ---
print("\n--- 4. Function Parameters (Arguments) ---")
print("Parameters are placeholders that a function accepts.")
print("When you call the function, you pass 'arguments' to these parameters.")

# 4.1 Positional Arguments: Passed in the order they are defined.
def greet_person(name):
    """This function greets the person passed in as an argument."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

def add_numbers(num1, num2):
    """Adds two numbers and prints the sum."""
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")

add_numbers(10, 5) # num1 gets 10, num2 gets 5

# 4.2 Keyword Arguments: Passed by name, allowing out-of-order passing.
print("\n4.2 Keyword Arguments:")
def describe_pet(animal_type, pet_name):
    """Describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat") # Order doesn't matter with keywords

# 4.3 Default Parameter Values: Assign a default if no argument is provided.
print("\n4.3 Default Parameter Values:")
def greet_default(name="Guest"):
    """Greets a person, defaulting to 'Guest' if no name is given."""
    print(f"Welcome, {name}!")

greet_default("Charlie") # Uses provided argument
greet_default()        # Uses default value "Guest"

def power(base, exponent=2):
    """Calculates base raised to the power of exponent (default is 2)."""
    result = base ** exponent
    print(f"{base} to the power of {exponent} is {result}")

power(5)    # 5 to the power of 2 (default)
power(2, 3) # 2 to the power of 3

# --- 5. Return Statement ---
print("\n--- 5. Return Statement ---")
print("The `return` statement sends a value back to the caller of the function.")
print("If a function doesn't have an explicit return statement, it implicitly returns `None`.")

def multiply(a, b):
    """Multiplies two numbers and returns the product."""
    product = a * b
    return product # Return the calculated product

result_mult = multiply(7, 3)
print(f"The product is: {result_mult}")

def get_status(is_online):
    """Returns a status string based on a boolean."""
    if is_online:
        return "User is online."
    else:
        return "User is offline."

status1 = get_status(True)
status2 = get_status(False)
print(status1)
print(status2)

# Function with no explicit return (returns None)
def no_return_func():
    print("This function prints something but doesn't return a value.")

returned_value = no_return_func()
print(f"Value returned by no_return_func(): {returned_value} (which is None)")


# --- 6. Arbitrary Arguments (*args and **kwargs) ---
print("\n--- 6. Arbitrary Arguments (*args and **kwargs) ---")
print("Useful when you don't know how many arguments will be passed.")

# 6.1 *args (Arbitrary Positional Arguments): Collects arguments into a tuple.
print("\n6.1 *args:")
def sum_all_numbers(*numbers):
    """Sums all numbers passed as arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all_numbers(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40, 50: {sum_all_numbers(10, 20, 30, 40, 50)}")
print(f"Sum of no numbers: {sum_all_numbers()}")

# 6.2 **kwargs (Arbitrary Keyword Arguments): Collects arguments into a dictionary.
print("\n6.2 **kwargs:")
def display_profile(**details):
    """Displays user profile details."""
    print("\nUser Profile:")
    for key, value in details.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

display_profile(name="Sarah", age=30, city="New York")
display_profile(product="Laptop", price=1200, category="Electronics", brand="TechCorp")


# --- 7. Scope of Variables (Local vs. Global) ---
print("\n--- 7. Scope of Variables (Local vs. Global) ---")

# Global variable
global_var = "I am a global variable."

def scope_example():
    local_var = "I am a local variable."
    print(f"Inside function: {local_var}")   # Accesses local_var
    print(f"Inside function: {global_var}")  # Accesses global_var

scope_example()
# print(local_var) # This would cause a NameError, local_var is not accessible outside

# Modifying global variable (use 'global' keyword - generally avoided for clarity)
glob_count = 0
def increment_global_count():
    global glob_count # Declare intent to modify the global variable
    glob_count += 1
    print(f"Global count inside function: {glob_count}")

print(f"Global count before: {glob_count}")
increment_global_count()
increment_global_count()
print(f"Global count after: {glob_count}")


# --- 8. Lambda Functions (Anonymous Functions) ---
print("\n--- 8. Lambda Functions (Anonymous Functions) ---")
print("Small, anonymous functions defined with the `lambda` keyword.")
print("They can take any number of arguments but can only have one expression.")

# Syntax: lambda arguments: expression
add_lambda = lambda x, y: x + y
print(f"Lambda add(2, 3): {add_lambda(2, 3)}")

# Often used for short-term functions, e.g., with `map()`, `filter()`, `sort()`'s `key`.
numbers = [1, 5, 2, 8, 3]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers (using map and lambda): {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using filter and lambda): {even_numbers}")

# Sorting a list of dictionaries by a specific key using lambda
students = [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}, {'name': 'Charlie', 'grade': 78}]
students.sort(key=lambda s: s['grade'])
print(f"Students sorted by grade: {students}")


# --- 9. Docstrings (Function Documentation) ---
print("\n--- 9. Docstrings (Function Documentation) ---")
print("Docstrings (documentation strings) explain what a function does.")
print("They are enclosed in triple quotes and placed right after the `def` line.")

def calculate_average(data_list):
    """
    Calculates the average of a list of numbers.

    Args:
        data_list (list): A list of numerical values.

    Returns:
        float: The average of the numbers in the list.
               Returns 0.0 if the list is empty to avoid division by zero.
    """
    if not data_list:
        return 0.0
    return sum(data_list) / len(data_list)

# Accessing the docstring
print(f"Docstring for calculate_average:\n{calculate_average.__doc__}")

avg = calculate_average([10, 20, 30, 40])
print(f"Average of [10, 20, 30, 40]: {avg}")
avg_empty = calculate_average([])
print(f"Average of empty list: {avg_empty}")

# --- 10. Type Hinting (Optional but Recommended) ---
print("\n--- 10. Type Hinting (Optional but Recommended) ---")
print("Type hints improve code readability and allow static analysis tools (like linters, IDEs) to catch type-related errors.")

def add_typed(a: int, b: int) -> int:
    """Adds two integers and returns an integer."""
    return a + b

print(f"Result of add_typed(5, 7): {add_typed(5, 7)}")

# Although Python doesn't enforce types at runtime, tools will warn you:
# print(f"Result of add_typed('hello', 'world'): {add_typed('hello', 'world')}") # Would typically trigger a warning in an IDE


print("\n--- End of Python Functions Practice Code ---")



# --- 1. Defining a Simple Function ---
# Functions are blocks of organized, reusable code that perform a single, related action.

def greet():
    """
    This function prints a simple greeting message.
    It takes no arguments and returns nothing.
    """
    print("Hello, World!")

def add_numbers(a, b):
    """
    This function takes two arguments and returns their sum.
    Arguments:
        a (int/float): The first number.
        b (int/float): The second number.
    Returns:
        (int/float): The sum of a and b.
    """
    return a + b

def simple_function_demonstration():
    print("\n--- 1. Defining and Calling Simple Functions ---")
    greet() # Calling the function
    
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    result_float = add_numbers(10.5, 2.3)
    print(f"10.5 + 2.3 = {result_float}")

# --- 2. Function Arguments ---
# Functions can accept different types of arguments:
# - Positional arguments
# - Keyword arguments
# - Default arguments
# - Arbitrary positional arguments (*args)
# - Arbitrary keyword arguments (**kwargs)

def describe_person(name, age, city="Unknown", profession="Developer"):
    """
    Describes a person with positional, keyword, and default arguments.
    """
    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Profession: {profession}")

def calculate_average(*numbers):
    """
    Calculates the average of an arbitrary number of positional arguments.
    `*numbers` collects all passed positional arguments into a tuple.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def create_profile(name, **details):
    """
    Creates a user profile with arbitrary keyword arguments.
    `**details` collects all passed keyword arguments into a dictionary.
    """
    profile = {"name": name}
    profile.update(details)
    print("\n--- User Profile ---")
    for key, value in profile.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def function_arguments_demonstration():
    print("\n--- 2. Function Arguments ---")
    
    # Positional arguments
    describe_person("Alice", 30) 
    
    # Keyword arguments (order doesn't matter)
    describe_person(age=25, name="Bob") 
    
    # Mixing positional and keyword (positional first)
    describe_person("Charlie", 35, profession="Artist")
    
    # Using default arguments
    describe_person("David", 40) # City and Profession use defaults
    describe_person("Eve", 28, city="New York") # City overridden, Profession uses default
    
    # Arbitrary positional arguments (*args)
    avg1 = calculate_average(1, 2, 3)
    print(f"\nAverage of (1, 2, 3): {avg1}")
    avg2 = calculate_average(10, 20, 30, 40, 50)
    print(f"Average of (10, 20, 30, 40, 50): {avg2}")
    avg3 = calculate_average()
    print(f"Average of no numbers: {avg3}")
    
    # Arbitrary keyword arguments (**kwargs)
    create_profile("Frank", email="frank@example.com", is_active=True, role="Admin")
    create_profile("Grace", hobbies=["reading", "hiking"])

# --- 3. Return Values ---
# Functions can return single values, multiple values (as a tuple), or nothing (None).

def get_full_name(first, last):
    """Returns a single string."""
    return f"{first} {last}"

def get_coordinates():
    """Returns multiple values as a tuple."""
    return 10.0, 20.0 # This is implicitly a tuple (10.0, 20.0)

def print_message(message):
    """Returns None explicitly or implicitly."""
    print(message)
    # return None # This is implicit if no return statement

def return_values_demonstration():
    print("\n--- 3. Function Return Values ---")
    
    full_name = get_full_name("John", "Doe")
    print(f"Full name: {full_name}")
    
    x, y = get_coordinates() # Tuple unpacking
    print(f"Coordinates: x={x}, y={y}")
    
    result = print_message("Hello from print_message!")
    print(f"Return value of print_message: {result} (which is None)")

# --- 4. Function Scope (Local vs. Global Variables) ---

global_var = "I am a global variable."

def scope_example():
    local_var = "I am a local variable."
    print(f"\nInside function: {global_var}") # Can access global
    print(f"Inside function: {local_var}")   # Can access local
    
    # Modifying global variable (bad practice without 'global' keyword)
    # global_var = "Modified global in function (creates new local scope var)"
    # To modify the true global variable:
    # global global_var
    # global_var = "Modified global in function (actual global)"

def scope_demonstration():
    print("\n--- 4. Function Scope ---")
    scope_example()
    # print(local_var) # This would raise NameError: local_var is not defined in global scope
    print(f"Outside function: {global_var}")

# --- 5. Nested Functions (Closures) ---
# Functions defined inside other functions. The inner function can access
# variables from the outer (enclosing) function's scope.

def outer_function(message):
    def inner_function():
        print(f"Inner function received: {message}")
    return inner_function # Return the inner function itself

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

def nested_functions_demonstration():
    print("\n--- 5. Nested Functions (Closures) ---")
    
    my_closure = outer_function("Hello from outer!")
    my_closure() # Calls inner_function, which remembers 'message' from outer_function's scope
    
    # Create different multipliers
    double = multiplier(2)
    triple = multiplier(3)
    
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")

# --- 6. Lambda Functions (Anonymous Functions) ---
# Small, anonymous functions created with the `lambda` keyword.
# They can only contain a single expression.

def lambda_functions_demonstration():
    print("\n--- 6. Lambda Functions ---")
    
    # Simple lambda for addition
    add_lambda = lambda x, y: x + y
    print(f"Lambda add(2, 3): {add_lambda(2, 3)}")
    
    # Lambda used with filter()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers from list: {even_numbers}")
    
    # Lambda used with map()
    squared_numbers = list(map(lambda x: x * x, numbers))
    print(f"Squared numbers from list: {squared_numbers}")
    
    # Lambda for sorting (e.g., list of tuples by second element)
    pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
    print(f"Sorted pairs by second element: {sorted_pairs}")

# --- 7. Function Documentation (Docstrings) ---
# Docstrings are used to explain what a function does. Accessible via help() or .__doc__.

def example_with_docstring(param1, param2):
    """
    This is an example function demonstrating a docstring.
    
    It takes two parameters and does nothing useful, but shows documentation.
    
    Args:
        param1 (str): The first parameter.
        param2 (int): The second parameter, an integer.
        
    Returns:
        bool: Always returns True for demonstration.
    
    Raises:
        ValueError: If param2 is negative (just an example).
    """
    if param2 < 0:
        raise ValueError("param2 cannot be negative.")
    print(f"Param1: {param1}, Param2: {param2}")
    return True

def docstring_demonstration():
    print("\n--- 7. Function Documentation (Docstrings) ---")
    print(example_with_docstring.__doc__) # Accessing the docstring
    help(example_with_docstring)        # Using help() for full documentation

# --- 8. Type Hinting ---
# Provides hints about the expected types of arguments and return values.
# Used for static analysis (linters, IDEs) and better readability, not runtime enforcement.

from typing import List, Union

def calculate_sum(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the sum of numbers in a list."""
    return sum(numbers)

def greet_person(name: str, age: int) -> str:
    """Greets a person by name and age."""
    return f"Hello, {name}! You are {age} years old."

def type_hinting_demonstration():
    print("\n--- 8. Type Hinting ---")
    
    total = calculate_sum([1, 2, 3, 4.5])
    print(f"Sum of [1, 2, 3, 4.5]: {total}")
    
    greeting = greet_person("Alice", 30)
    print(greeting)
    
    # Type checkers (like MyPy) would flag this:
    # greet_person("Bob", "thirty") 
    
# --- Main Execution Block ---
if __name__ == "__main__":
    simple_function_demonstration()
    function_arguments_demonstration()
    return_values_demonstration()
    scope_demonstration()
    nested_functions_demonstration()
    lambda_functions_demonstration()
    docstring_demonstration()
    type_hinting_demonstration()
    
    print("\nAll Python functions demonstrations concluded.")


# --- 1. Class with Simple Functions (Methods) ---
class BasicCalculator:
    def greet(self):
        """A simple method that prints a greeting."""
        print("Hello from BasicCalculator!")

    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers."""
        return a - b

    def demonstrate_basics(self):
        print("\n--- 1. Class with Simple Functions (Methods) ---")
        self.greet()
        print(f"5 + 3 = {self.add(5, 3)}")
        print(f"10 - 4 = {self.subtract(10, 4)}")


# --- 2. Class with Different Types of Arguments ---
class PersonManager:
    def __init__(self, default_city="Unknown", default_profession="Generalist"):
        self.default_city = default_city
        self.default_profession = default_profession

    def describe_person(self, name, age, city=None, profession=None):
        """
        Describes a person using positional, keyword, and default arguments.
        city and profession can be overridden or use class defaults.
        """
        actual_city = city if city is not None else self.default_city
        actual_profession = profession if profession is not None else self.default_profession
        print(f"\n  Name: {name}, Age: {age}, City: {actual_city}, Profession: {actual_profession}")

    def calculate_average(self, *numbers):
        """
        Calculates the average of an arbitrary number of positional arguments.
        """
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

    def create_detailed_profile(self, name, **details):
        """
        Creates a detailed profile using arbitrary keyword arguments.
        """
        profile = {"name": name}
        profile.update(details)
        print("\n  --- Detailed Profile ---")
        for key, value in profile.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

    def demonstrate_arguments(self):
        print("\n--- 2. Class with Different Types of Arguments ---")
        self.describe_person("Alice", 30) # Uses class defaults
        self.describe_person("Bob", 25, city="Dhaka") # Overrides city
        self.describe_person(age=40, name="Charlie", profession="Engineer") # Keyword args

        print(f"\n  Average of (1, 2, 3): {self.calculate_average(1, 2, 3)}")
        print(f"  Average of (10, 20, 30, 40, 50): {self.calculate_average(10, 20, 30, 40, 50)}")
        print(f"  Average of no numbers: {self.calculate_average()}")

        self.create_detailed_profile("David", email="david@example.com", status="Active", role="User")
        self.create_detailed_profile("Eve", hobbies=["Reading", "Coding"], location="Chattogram")


# --- 3. Class with Return Values ---
class DataProcessor:
    def get_full_name(self, first_name, last_name):
        """Returns a concatenated full name."""
        return f"{first_name} {last_name}"

    def get_coordinates(self):
        """Returns a tuple of coordinates."""
        return (10.5, 20.3)

    def print_and_log(self, message):
        """Prints a message and implicitly returns None."""
        print(f"\n  Log: {message}")

    def demonstrate_returns(self):
        print("\n--- 3. Class with Return Values ---")
        full_name = self.get_full_name("Siam", "Ahmed")
        print(f"  Full name: {full_name}")

        x, y = self.get_coordinates()
        print(f"  Coordinates: X={x}, Y={y}")

        result_none = self.print_and_log("Processing complete.")
        print(f"  Return value of print_and_log: {result_none} (which is None)")


# --- 4. Class for Demonstrating Scope (Instance vs. Local vs. Class Variables) ---
class ScopeDemonstrator:
    class_level_data = "I am class-level data." # Class variable

    def __init__(self, instance_id):
        self.instance_id = instance_id # Instance variable
        self.instance_data = f"Instance data for {instance_id}."

    def show_scope(self):
        local_data = "I am local data." # Local variable
        print(f"\n  --- Inside show_scope() for {self.instance_id} ---")
        print(f"  Local data: {local_data}")
        print(f"  Instance data: {self.instance_data}")
        print(f"  Class-level data (via self): {self.class_level_data}")
        print(f"  Class-level data (via class): {ScopeDemonstrator.class_level_data}")

        # Changing instance variable
        self.instance_data = "Instance data changed locally."
        print(f"  Instance data after change: {self.instance_data}")

        # Attempting to change class variable directly (creates instance variable)
        # self.class_level_data = "Changed class-level data (but made it instance-level for this object)"
        # Use ScopeDemonstrator.class_level_data = "New value" to change for all instances

    @classmethod
    def show_class_scope(cls):
        print(f"\n  --- Inside show_class_scope() (Class Method) ---")
        print(f"  Class-level data (via cls): {cls.class_level_data}")
        # print(cls.instance_data) # Would raise AttributeError: Cannot access instance data via class method
        # local_var_in_class_method = "Local here too"

    def demonstrate_scope(self):
        print("\n--- 4. Class for Demonstrating Scope ---")
        self.show_scope()
        
        # Accessing class variable from instance
        print(f"\n  Outside show_scope(), instance data: {self.instance_data}")
        print(f"  Outside show_scope(), class data: {self.class_level_data}")

        # Demonstrating class method
        ScopeDemonstrator.show_class_scope()
        # print(local_data) # NameError: local_data is not defined


# --- 5. Class with Nested Functions (Methods as Closures) ---
class FunctionFactory:
    def create_greeting_generator(self, greeting_prefix):
        """
        Returns an inner function (closure) that generates greetings
        using the provided prefix.
        """
        def generate_greeting(name):
            return f"{greeting_prefix}, {name}!"
        return generate_greeting

    def create_multiplier(self, factor):
        """
        Returns an inner function (closure) that multiplies a number by the factor.
        """
        def multiply(number):
            return number * factor
        return multiply

    def demonstrate_nested_functions(self):
        print("\n--- 5. Class with Nested Functions (Methods as Closures) ---")
        
        # Create a specific greeting generator
        formal_greeter = self.create_greeting_generator("Good day")
        casual_greeter = self.create_greeting_generator("Hey there")
        
        print(f"  Formal greeting: {formal_greeter('Mr. Smith')}")
        print(f"  Casual greeting: {casual_greeter('Alex')}")

        # Create different multipliers
        double_func = self.create_multiplier(2)
        triple_func = self.create_multiplier(3)
        
        print(f"  Double 7: {double_func(7)}")
        print(f"  Triple 7: {triple_func(7)}")


# --- 6. Class Using Lambda Functions (Anonymous Functions) ---
class LambdaOperations:
    def __init__(self, numbers_list):
        self.numbers = numbers_list

    def filter_even(self):
        """Filters even numbers using lambda with filter()."""
        return list(filter(lambda x: x % 2 == 0, self.numbers))

    def square_numbers(self):
        """Squares all numbers using lambda with map()."""
        return list(map(lambda x: x * x, self.numbers))

    def sort_pairs_by_second_element(self, pairs):
        """Sorts a list of tuples by their second element using lambda."""
        return sorted(pairs, key=lambda pair: pair[1])

    def demonstrate_lambdas(self):
        print("\n--- 6. Class Using Lambda Functions ---")
        print(f"  Original numbers: {self.numbers}")
        print(f"  Even numbers: {self.filter_even()}")
        print(f"  Squared numbers: {self.square_numbers()}")
        
        sample_pairs = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
        print(f"  Original pairs: {sample_pairs}")
        print(f"  Sorted pairs by fruit name: {self.sort_pairs_by_second_element(sample_pairs)}")


# --- 7. Class with Function Documentation (Docstrings) ---
class DocumentedUtility:
    def __init__(self, name):
        self.name = name

    def perform_task(self, data_input: str, repetitions: int) -> str:
        """
        Performs a repetitive task with the given input data.

        This method demonstrates how to write a docstring for a class method.
        It processes a string by repeating it.

        Args:
            data_input (str): The string data to be processed.
            repetitions (int): The number of times to repeat the data.

        Returns:
            str: The concatenated string based on repetitions.

        Raises:
            ValueError: If repetitions is negative.
        """
        if repetitions < 0:
            raise ValueError("Repetitions cannot be negative.")
        print(f"  Performing task '{data_input}' {repetitions} times.")
        return data_input * repetitions

    def demonstrate_docstrings(self):
        print("\n--- 7. Class with Function Documentation (Docstrings) ---")
        print("  Docstring for perform_task method:")
        print(self.perform_task.__doc__)
        
        # You can also use help() for methods
        # help(self.perform_task)
        
        try:
            result = self.perform_task("Python", 3)
            print(f"  Result: {result}")
            self.perform_task("Error", -1)
        except ValueError as e:
            print(f"  [CAUGHT ERROR] {type(e).__name__}: {e}")


# --- 8. Class with Type Hinting ---
from typing import List, Union

class TypeHintedProcessor:
    def process_list(self, items: List[Union[int, str]]) -> str:
        """
        Processes a list of integers or strings and returns a summary string.
        Demonstrates type hints for list elements and return type.
        """
        summary_parts = []
        for item in items:
            if isinstance(item, int):
                summary_parts.append(f"Int: {item * 2}")
            elif isinstance(item, str):
                summary_parts.append(f"Str: {item.upper()}")
        return " | ".join(summary_parts)

    def calculate_total_amount(self, quantity: int, price_per_unit: float) -> float:
        """
        Calculates total amount with type hints for numerical arguments and return.
        """
        return quantity * price_per_unit

    def demonstrate_type_hinting(self):
        print("\n--- 8. Class with Type Hinting ---")
        
        list_result = self.process_list([10, "apple", 20, "banana"])
        print(f"  Processed list: {list_result}")
        
        total = self.calculate_total_amount(5, 12.75)
        print(f"  Total amount for 5 units at 12.75: {total:.2f}")

        # Static type checkers (like MyPy) would flag these:
        # self.process_list([10, {"bad_type": True}])
        # self.calculate_total_amount("five", 10.0)


# --- Main Execution Block ---
if __name__ == "__main__":
    
    calc = BasicCalculator()
    calc.demonstrate_basics()

    mgr = PersonManager(default_city="Sylhet", default_profession="Student")
    mgr.demonstrate_arguments()

    data_proc = DataProcessor()
    data_proc.demonstrate_returns()

    scope_demo_instance1 = ScopeDemonstrator("InstanceA")
    scope_demo_instance1.demonstrate_scope()
    
    scope_demo_instance2 = ScopeDemonstrator("InstanceB")
    print(f"\n  Accessing instance data from InstanceB after A's change: {scope_demo_instance2.instance_data}")
    # Note: InstanceA's instance_data was changed, but InstanceB's was not.
    # If ScopeDemonstrator.class_level_data was changed, it would affect all.

    func_factory = FunctionFactory()
    func_factory.demonstrate_nested_functions()

    lambda_ops = LambdaOperations([1, 2, 3, 4, 5, 6])
    lambda_ops.demonstrate_lambdas()

    doc_util = DocumentedUtility("ReportGenerator")
    doc_util.demonstrate_docstrings()

    type_proc = TypeHintedProcessor()
    type_proc.demonstrate_type_hinting()

    print("\nAll Python functions demonstrations using classes concluded.")