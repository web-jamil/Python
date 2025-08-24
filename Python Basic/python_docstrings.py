print("--- Python Docstrings: All About Methods ---")
print("--------------------------------------------\n")

# Docstrings (documentation strings) are multi-line string literals that occur
# as the first statement in a module, function, class, or method definition.
# They are used to explain what the code does and how to use it.
# Unlike comments, docstrings are preserved at runtime and can be accessed
# using the `__doc__` attribute of the object.

# For methods, docstrings typically describe:
# - What the method does.
# - Its parameters (args).
# - What it returns (returns).
# - Any exceptions it might raise (raises).
# - Any side effects it has.
# - Examples of usage (often in more complex docstring formats).

# There are various formats for docstrings, but the most common are:
# 1. One-line docstrings (for simple, concise descriptions).
# 2. Multi-line docstrings (for more detailed explanations).
# 3. Specific formats like reStructuredText, NumPy/SciPy style, Google style.

# --- 1. One-line Docstrings for Methods ---
print("1. One-line Docstrings for Methods:\n")

class SimpleCalculator:
    """A basic calculator class."""

    def add(self, a, b):
        """Adds two numbers and returns their sum."""
        return a + b

    def subtract(self, a, b):
        """Subtracts b from a and returns the difference."""
        return a - b

calc = SimpleCalculator()
print(f"Adding 5 and 3: {calc.add(5, 3)}")
print(f"Subtracting 5 from 10: {calc.subtract(10, 5)}")

# Accessing docstrings
print(f"\nDocstring for add method: {calc.add.__doc__}")
print(f"Docstring for subtract method: {SimpleCalculator.subtract.__doc__}\n")


# --- 2. Multi-line Docstrings for Methods ---
print("2. Multi-line Docstrings for Methods:\n")

class UserManager:
    """
    Manages user data within the system.

    This class provides methods for creating, retrieving, updating, and deleting
    user records.
    """

    def __init__(self, admin_email="admin@example.com"):
        """
        Initializes the UserManager with an optional admin email.

        Args:
            admin_email (str, optional): The email address of the administrator.
                                         Defaults to "admin@example.com".
        """
        self.users = {}
        self.admin_email = admin_email
        print(f"UserManager initialized with admin email: {self.admin_email}")

    def create_user(self, user_id, username, email):
        """
        Creates a new user record in the system.

        Args:
            user_id (int): The unique identifier for the user.
            username (str): The username for the new user.
            email (str): The email address of the new user.

        Returns:
            bool: True if the user was created successfully, False if user_id
                  already exists.
        """
        if user_id in self.users:
            print(f"Error: User with ID {user_id} already exists.")
            return False
        self.users[user_id] = {"username": username, "email": email}
        print(f"User {username} (ID: {user_id}) created.")
        return True

    def get_user(self, user_id):
        """
        Retrieves user information by their ID.

        Args:
            user_id (int): The unique identifier of the user to retrieve.

        Returns:
            dict or None: A dictionary containing user data if found,
                          otherwise None.
        """
        return self.users.get(user_id)

    def update_user_email(self, user_id, new_email):
        """
        Updates the email address for an existing user.

        Args:
            user_id (int): The ID of the user whose email to update.
            new_email (str): The new email address.

        Raises:
            ValueError: If the user_id does not exist.

        Returns:
            bool: True if the email was updated, False otherwise.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        old_email = self.users[user_id]["email"]
        self.users[user_id]["email"] = new_email
        print(f"User {user_id}'s email updated from {old_email} to {new_email}.")
        return True

    def delete_user(self, user_id):
        """
        Deletes a user record from the system.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, False if user_id was not found.
        """
        if user_id in self.users:
            del self.users[user_id]
            print(f"User with ID {user_id} deleted.")
            return True
        print(f"User with ID {user_id} not found for deletion.")
        return False

# Demonstrate usage and access docstrings
manager = UserManager()
manager.create_user(1, "john_d", "john@example.com")
manager.create_user(2, "jane_d", "jane@example.com")

print(f"\nUser 1 details: {manager.get_user(1)}")

manager.update_user_email(1, "john.doe@newmail.com")

try:
    manager.update_user_email(99, "nonexistent@example.com")
except ValueError as e:
    print(f"Caught expected error: {e}")

manager.delete_user(2)

print("\n--- Accessing Multi-line Docstrings ---")
print(f"Docstring for UserManager class:\n{UserManager.__doc__}")
print(f"\nDocstring for create_user method:\n{manager.create_user.__doc__}")
print(f"\nDocstring for update_user_email method:\n{UserManager.update_user_email.__doc__}")


# --- 3. Docstring Conventions (Briefly) ---
print("\n--- 3. Docstring Conventions (Briefly) ---")

# Python has no official standard for docstring *content*, but PEP 257
# provides guidelines, and common community standards exist (e.g., Google, NumPy).

# Common elements in multi-line method docstrings:
# - A brief summary line.
# - A blank line.
# - A more elaborate description (optional).
# - Sections for:
#   - `Args`: List of arguments, their types, and descriptions.
#   - `Returns`: Description of the return value and its type.
#   - `Yields`: For generator functions.
#   - `Raises`: Any exceptions that might be raised.
#   - `Example`: Code examples showing how to use the method.
#   - `Notes`: Any additional important information.
#   - `See Also`: References to related functions/methods.

# Example of a method docstring following a common style (e.g., Google Style)
class DataProcessor:
    def process_data(self, data: List[int], strategy: str = "sum") -> float:
        """
        Processes a list of numerical data based on a given strategy.

        This method supports 'sum' and 'average' strategies for processing
        the input data.

        Args:
            data (List[int]): A list of integers to be processed.
            strategy (str, optional): The processing method to apply.
                                      Can be "sum" or "average".
                                      Defaults to "sum".

        Returns:
            float: The result of the processing (sum or average).

        Raises:
            ValueError: If an unsupported strategy is provided or data is empty
                        for 'average' strategy.

        Example:
            >>> processor = DataProcessor()
            >>> processor.process_data([1, 2, 3])
            6.0
            >>> processor.process_data([10, 20, 30], strategy="average")
            20.0
        """
        if not data:
            if strategy == "average":
                raise ValueError("Cannot calculate average of an empty list.")
            return 0.0 # Sum of empty list is 0

        if strategy == "sum":
            return float(sum(data))
        elif strategy == "average":
            return float(sum(data)) / len(data)
        else:
            raise ValueError(f"Unsupported strategy: {strategy}. Choose 'sum' or 'average'.")

processor = DataProcessor()
print(f"\nProcessing [1,2,3]: {processor.process_data([1,2,3])}")
print(f"Processing [10,20,30] with 'average': {processor.process_data([10,20,30], 'average')}")

try:
    processor.process_data([], strategy="average")
except ValueError as e:
    print(f"Caught error: {e}")

# Accessing the docstring of the `process_data` method
print(f"\nDocstring for process_data method:\n{DataProcessor.process_data.__doc__}")


# --- 4. Tools and Docstrings ---
print("\n--- 4. Tools and Docstrings ---")

# Docstrings are vital for automated documentation generation tools like Sphinx.
# They are also used by IDEs (like VS Code, PyCharm) to provide inline help
# and autocompletion suggestions.

# Example using `help()` function:
# help(UserManager.create_user)
# help(DataProcessor.process_data)
# (Uncomment the lines above to see the output from help() - it formats the docstring nicely)

print("\n--- End of Python Docstrings Demonstration ---")



import math
from typing import List, Union, Tuple, Dict, Any

print("--- Python Docstrings: Comprehensive Guide ---")
print("----------------------------------------------\n")

# Docstrings (documentation strings) are string literals that appear
# immediately after the definition of a function, method, class, or module.
# They are used to document the purpose and usage of code.
# Unlike comments, docstrings are accessible at runtime via the __doc__ attribute.

# --- 1. Triple-Quoted Strings for Docstrings ---
print("1. Triple-Quoted Strings for Docstrings:\n")

# Docstrings are almost always enclosed in triple quotes (either single `'''` or double `"""`).
# This allows them to span multiple lines naturally without needing escape characters,
# and it's the standard convention for readability.

def example_function_with_triple_quotes(param1, param2):
    """
    This is a docstring using triple double quotes.
    It can span multiple lines.
    
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    """
    return f"{param1} - {param2}"

def another_function_with_triple_single_quotes(x):
    '''
    This is a docstring using triple single quotes.
    It works exactly the same way as triple double quotes.
    
    Args:
        x (float): A numeric value.
    '''
    return x * 2

print(f"Calling example_function: {example_function_with_triple_quotes(1, 'test')}")
print(f"Calling another_function: {another_function_with_triple_single_quotes(3.14)}")

print("\nAccessing docstrings using .__doc__:")
print(f"Docstring of example_function_with_triple_quotes:\n{example_function_with_triple_quotes.__doc__}")
print(f"Docstring of another_function_with_triple_single_quotes:\n{another_function_with_triple_single_quotes.__doc__}\n")


# --- 2. One-Line Docstrings ---
print("2. One-Line Docstrings:\n")

# Used for very concise explanations, typically when the function/method/class
# is simple and its purpose is immediately obvious from its name or arguments.
# They should fit on one line and end with a period.

class SimpleGreeter:
    """A simple class for greeting people."""

    def greet_user(self, name: str):
        """Greets the user by their name."""
        return f"Hello, {name}!"

def calculate_square_root(number: Union[int, float]):
    """Calculates the square root of a given number."""
    return math.sqrt(number)

greeter = SimpleGreeter()
print(f"Greeting: {greeter.greet_user('Alice')}")
print(f"Square root of 25: {calculate_square_root(25)}")

print(f"\nDocstring of greet_user method: {greeter.greet_user.__doc__}")
print(f"Docstring of calculate_square_root function: {calculate_square_root.__doc__}\n")


# --- 3. Multi-Line Docstrings ---
print("3. Multi-Line Docstrings:\n")

# Used for more complex functions, methods, or classes that require detailed
# explanations of their purpose, arguments, return values, and potential side effects.
# The first line is a concise summary, followed by a blank line, then the detailed description.

def get_prime_numbers_in_range(start: int, end: int) -> List[int]:
    """
    Finds all prime numbers within a specified inclusive range.

    This function iterates through each number in the given range and
    checks for primality. It uses a basic primality test algorithm.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Returns:
        List[int]: A list containing all prime numbers found in the range.
                   Returns an empty list if no primes are found or if the
                   range is invalid.
    """
    if start > end:
        return []
    
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(f"Primes from 1 to 20: {get_prime_numbers_in_range(1, 20)}")
print(f"Primes from 20 to 30: {get_prime_numbers_in_range(20, 30)}")

print(f"\nDocstring for get_prime_numbers_in_range:\n{get_prime_numbers_in_range.__doc__}\n")


# --- 4. Indentation in Docstrings ---
print("4. Indentation in Docstrings:\n")

# The indentation of the docstring body should match the indentation level
# of the function/method signature. The closing triple quotes should be on
# a line by themselves and align with the first non-whitespace character
# of the docstring's first line (or the code below it).

class UserManager:
    def get_user_profile(self, user_id: int) -> Dict[str, Any]:
        """
        Retrieves the profile information for a given user ID.

        This method queries the database (simulated) to fetch user details
        such as name, email, and registration date.

        Args:
            user_id (int): The unique identifier of the user.

        Returns:
            Dict[str, Any]: A dictionary containing the user's profile data.
                            Returns an empty dictionary if the user is not found.
        """
        # Simulate database lookup
        if user_id == 1:
            return {"id": 1, "name": "Alice", "email": "alice@example.com"}
        elif user_id == 2:
            return {"id": 2, "name": "Bob", "email": "bob@example.com"}
        return {}

manager = UserManager()
print(f"User profile for ID 1: {manager.get_user_profile(1)}")
print(f"\nDocstring for get_user_profile:\n{UserManager.get_user_profile.__doc__}\n")


# --- 5. Docstrings in Classes ---
print("5. Docstrings in Classes:\n")

# Classes should also have docstrings, placed immediately after the class definition line.
# They describe the purpose of the class, its main responsibilities, and any
# important attributes it might have.

class BankAccount:
    """
    Represents a simple bank account with basic functionalities.

    Attributes:
        account_number (str): Unique identifier for the account.
        balance (float): The current monetary balance in the account.
        owner_name (str): The name of the account holder.
    """

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        """
        Initializes a new BankAccount instance.

        Args:
            account_number (str): The unique account identifier.
            owner_name (str): The name of the account holder.
            initial_balance (float, optional): The starting balance for the account.
                                                Defaults to 0.0.
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        print(f"Account {self.account_number} created for {self.owner_name} with balance {self.balance:.2f}.")

    def deposit(self, amount: float):
        """
        Deposits funds into the account.

        Args:
            amount (float): The amount of money to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}.")

    def withdraw(self, amount: float):
        """
        Withdraws funds from the account.

        Args:
            amount (float): The amount of money to withdraw. Must be positive.

        Raises:
            ValueError: If the withdrawal amount is not positive.
            RuntimeError: If there are insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise RuntimeError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}.")

# Demonstrate class and method usage
my_account = BankAccount("12345", "Alice Smith", 100.0)
my_account.deposit(50.0)
try:
    my_account.withdraw(200.0)
except RuntimeError as e:
    print(f"Error withdrawing: {e}")
my_account.withdraw(30.0)

print(f"\nDocstring for BankAccount class:\n{BankAccount.__doc__}")
print(f"\nDocstring for deposit method:\n{BankAccount.deposit.__doc__}\n")


# --- 6. Google Style Docstrings ---
print("6. Google Style Docstrings:\n")

# A popular and readable docstring format.
# Key sections: Args, Returns, Raises, Examples.
# Uses colons for type hints and descriptions.

def process_data_google_style(data: List[Union[int, float]], threshold: float = 0.5) -> List[float]:
    """
    Applies a filtering and transformation process to a list of numerical data.

    This function filters out elements below a given threshold and then
    squares the remaining elements.

    Args:
        data (list[int | float]): A list of numerical values to process.
        threshold (float, optional): The minimum value an element must have
                                     to be included in the processing. Defaults to 0.5.

    Returns:
        list[float]: A new list containing the squared values of elements
                     that met the threshold. Returns an empty list if no
                     elements meet the criteria.

    Raises:
        TypeError: If `data` is not a list.
        ValueError: If any element in `data` is not a number.

    Examples:
        >>> process_data_google_style([1, 0.2, 3])
        [1.0, 9.0]
        >>> process_data_google_style([-1, 5], threshold=2.0)
        [25.0]
        >>> process_data_google_style([0.1, 0.2])
        []
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    processed_list = []
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError(f"All elements in 'data' must be numbers, got {type(item)}")
        if item >= threshold:
            processed_list.append(float(item ** 2))
    return processed_list

print(f"Processed with Google Style: {process_data_google_style([1, 0.2, 3])}")
print(f"Processed with Google Style and threshold: {process_data_google_style([-1, 5], threshold=2.0)}")
try:
    process_data_google_style("not a list")
except TypeError as e:
    print(f"Caught expected error (Google Style): {e}")

print(f"\nDocstring for process_data_google_style:\n{process_data_google_style.__doc__}\n")


# --- 7. NumPyDoc Style Docstrings ---
print("7. NumPyDoc Style Docstrings:\n")

# Widely used in scientific computing libraries (NumPy, SciPy, Pandas).
# Uses specific Sphinx-compatible reStructuredText sections (e.g., Parameters, Returns).
# Often formatted with underlined section headers.

def calculate_mean_numpydoc_style(data: List[Union[int, float]]) -> float:
    """
    Calculates the arithmetic mean of a list of numbers.

    Parameters
    ----------
    data : list[int | float]
        A list of numerical values for which to calculate the mean.

    Returns
    -------
    float
        The calculated arithmetic mean of the input data.

    Raises
    ------
    ValueError
        If the input `data` list is empty.

    See Also
    --------
    sum : Built-in function for summing numbers.
    statistics.mean : Standard library function for mean calculation.

    Examples
    --------
    >>> calculate_mean_numpydoc_style([1, 2, 3, 4, 5])
    3.0
    >>> calculate_mean_numpydoc_style([10, 20, 30])
    20.0
    """
    if not data:
        raise ValueError("Input data list cannot be empty for mean calculation.")
    return sum(data) / len(data)

print(f"Mean with NumPyDoc Style: {calculate_mean_numpydoc_style([1, 2, 3, 4, 5])}")
try:
    calculate_mean_numpydoc_style([])
except ValueError as e:
    print(f"Caught expected error (NumPyDoc Style): {e}")

print(f"\nDocstring for calculate_mean_numpydoc_style:\n{calculate_mean_numpydoc_style.__doc__}\n")


# --- Best Practices for Docstrings ---
print("--- Best Practices for Docstrings ---")

print("\n1. Be Concise and Clear:")
print("   - The first line should be a brief, imperative summary.")
print("   - Elaborate only when necessary.")

print("\n2. Keep Them Up-to-Date:")
print("   - Docstrings should evolve with the code. Outdated docstrings are worse than no docstrings.")

print("\n3. Use Type Hints (Python 3.5+):")
print("   - While docstrings describe types, Python's type hints are for static analysis.")
print("   - Use both! Type hints in the signature, descriptions in the docstring.")

print("\n4. Follow a Consistent Style:")
print("   - Choose one style (Google, NumPy, reStructuredText) and stick to it throughout your project.")
print("   - Tools like `pydocstyle` and linters can help enforce this.")

print("\n5. What to Document:")
print("   - **Functions/Methods:** Purpose, arguments, return value, side effects, exceptions.")
print("   - **Classes:** Purpose, important attributes, how to instantiate/use.")
print("   - **Modules:** Overall purpose, main classes/functions, example usage.")

print("\n6. `help()` and IDE Integration:")
print("   - Docstrings are primarily for humans (developers) and documentation tools.")
print("   - Use `help(your_function)` in the interpreter to see how Python formats them.")
# Example using help (uncomment to see output in console)
# help(get_prime_numbers_in_range)
# help(BankAccount)


print("\n--- End of Python Docstrings Comprehensive Guide ---")