# #python docstrings

#  When it comes to writing clean, well-documented code, Python developers have a secret weapon at their disposal – docstrings. Docstrings, short for documentation strings, are vital in conveying the purpose and functionality of Python functions, modules, and classes. 


""" What are the docstrings in Python?
Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods. It’s specified in source code that is used, like a comment, to document a specific segment of code. Unlike conventional source code comments, the docstring should describe what the function does, not how.

Declaring Docstrings:-> The docstrings are declared using ”’triple single quotes”’ or “”” triple double quotes “”” just below the class, method, or function declaration. All functions should have a docstring.

Accessing Docstrings:-> The docstrings can be accessed using the __doc__ method of the object or using the help function. The below examples demonstrate how to declare and access a docstring.


What should a docstring look like?

1.The doc string line should begin with a capital letter and end with a period.
2.The first line should be a short description.
3.If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
4.The following lines should be one or more paragraphs describing the object’s calling conventions, side effects, etc.
Docstrings in Python
Below are the topics that we will cover in this article:

Triple-Quoted Strings

Google Style Docstrings

Numpydoc Style Docstrings

One-line Docstrings

Multi-line Docstrings

Indentation in Docstrings

Docstrings in Classes

Difference between Python comments and docstrings

Triple-Quoted Strings
This is the most common docstring format in Python. It involves using triple quotes (either single or double) to enclose the documentation text. Triple-quoted strings can span multiple lines and are often placed immediately below the function, class, or module definition """



def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    return None

print("Using **doc**:")
print(my_function.__doc__)

print("Using help:")
help(my_function)



def my_function():
    ' ' 'Demonstrates triple double quotes docstrings and does nothing really' ' '
 
    return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)


""" Google Style Docstrings

Google style docstrings follow a specific format and are inspired by Google’s documentation style guide. They provide a structured way to document Python code, including parameters, return values, and descriptions.
 """
 

def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b
print(multiply_numbers(3,5))


""" Numpydoc Style Docstrings

Numpydoc-style docstrings are widely used in the scientific and data analysis community, particularly for documenting functions and classes related to numerical computations and data manipulation. It is an extension of Google-style docstrings, with some additional conventions for documenting parameters and return values.
 """
 

def divide_numbers(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.

    Returns
    -------
    float
        The quotient of the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
print(divide_numbers(3,6))


""" One-line Docstrings


As the name suggests, one-line docstrings fit in one line. They are used in obvious cases. The closing quotes are on the same line as the opening quotes. This looks better for one-liners. For example: """


def power(a, b):
    ' ' 'Returns arg1 raised to power arg2.' ' '
 
    return a**b

print(power.__doc__)


""" Multi-line Docstrings

Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description. The summary line may be on the same line as the opening quotes or on the next line. The example below shows a multi-line docstring.



 """
 

def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b
print(add_numbers(3, 5))


""" Indentation in Docstrings


The entire docstring is indented the same as the quotes in its first line. Docstring processing tools will strip a uniform amount of indentation from the second and further lines of the docstring, equal to the minimum indentation of all non-blank lines after the first line. Any indentation in the first line of the docstring (i.e., up to the first new line) is insignificant and removed. Relative indentation of later lines in the docstring is retained.



 """
 

class Employee:
    """
    A class representing an employee.

    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        department (str): The department the employee works in.
        salary (float): The salary of the employee.
    """

    def __init__(self, name, age, department, salary):
        """
        Initializes an Employee object.

        Parameters:
            name (str): The name of the employee.
            age (int): The age of the employee.
            department (str): The department the employee works in.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def promote(self, raise_amount):
        """
        Promotes the employee and increases their salary.

        Parameters:
            raise_amount (float): The raise amount to increase the salary.

        Returns:
            str: A message indicating the promotion and new salary.
        """
        self.salary += raise_amount
        return f"{self.name} has been promoted! New salary: ${self.salary:.2f}"

    def retire(self):
        """
        Marks the employee as retired.

        Returns:
            str: A message indicating the retirement status.
        """
        # Some implementation for retiring an employee
        return f"{self.name} has retired. Thank you for your service!"

# Access the Class docstring using help()
help(Employee)

""" Docstrings in Classes """



class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
        real (int): The real part of the complex number.
        imag (int): The imaginary part of the complex number.
    """

    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.

        Parameters:
            real (int): The real part of the complex number.
            imag (int): The imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag

    def add(self, num):
        """
        The function to add two Complex Numbers.

        Parameters:
            num (ComplexNumber): The complex number to be added.

        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
        re = self.real + num.real
        im = self.imag + num.imag

        return ComplexNumber(re, im)

# Access the Class docstring using help()
help(ComplexNumber)

# Access the method docstring using help()
help(ComplexNumber.add)



""" Python Docstrings – FAQs

What are docstrings in Python?

Docstrings in Python are string literals that appear right after the definition of a function, method, class, or module. They are used to document what the object does. Enclosed in triple quotes, docstrings can be one line or multiline and are accessible via the .__doc__ attribute of the object.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

print(add.__doc__)  

"""# Output: Add two numbers and return the result.
What is the difference between comments and docstrings in Python?
Comments: Comments in Python start with a hash mark (#) and are intended to explain the code to developers. They are ignored by the Python interpreter.
Docstrings: Docstrings provide a description of the function, method, class, or module. Unlike comments, they are not ignored by the interpreter and can be accessed at runtime using the .__doc__ attribute.
What is the best format for docstrings in Python?
The best format for docstrings depends on the project and any related style guidelines. However, commonly accepted formats are outlined by PEP 257, which recommends a concise summary line followed by a more detailed description. The Google and NumPy/SciPy formats are also widely used, particularly in projects involving scientific computing.
"""

def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

"""
What is the difference between docstring and multiline string?
Docstring: A docstring is a string literal that describes a module, function, class, or method. It is accessible via the .__doc__ attribute.
Multiline String: A multiline string can be used for any purpose where a string spanning multiple lines is needed, including as data, in file I/O operations, or just within the code for complex string constructions. It is not used for documentation accessible via the .__doc__ attribute.
Should Python classes have docstrings?
Yes, Python classes should have docstrings. Including a docstring in a Python class improves code readability and provides a convenient place to document the class’s purpose, constructor, attributes, and methods. This is especially helpful for larger projects or for API documentation generation tools such as Sphinx.


Docstrings like these are crucial for maintaining clear and comprehensible code, especially as projects grow and evolve.

 """
 


# I am single line comment

""" Multi-line comment used
print("Python Comments") 

Multi-Line Comments
Python does not provide the option for multiline comments. However, there are different ways through which we can write multiline comments.

Multiline comments using multiple hashtags (#)

We can multiple hashtags (#) to write multiline comments in Python. Each and every line will be considered as a single-line comment.


Multi-Line Comments
Python does not provide the option for multiline comments. However, there are different ways through which we can write multiline comments.

Multiline comments using multiple hashtags (#)

We can multiple hashtags (#) to write multiline comments in Python. Each and every line will be considered as a single-line comment.


"""


# Python program to demonstrate
# multiline comments
print("Multiline comments")



""" Using String Literals as Comment
Python ignores the string literals that are not assigned to a variable. So, we can use these string literals as Python Comments. 

"""

1
'Single-line comments using string literals'
"""
Python program to demonstrate

 multiline comments"""

print("Multiline comments")

"""
Best Practice to Write Comments
These are some of the tips you can follow, to make your comments effective are:

Comments should be short and precise.
Use comments only when necessary, don’t clutter your code with comments.
Avoid writing generic or basic comments.
Write comments that are self explanatory. """