import os
import datetime
import math
import random
import re
import collections
import statistics
import json # Already covered in File I/O, but worth mentioning here for data handling
import csv # Already covered in File I/O, but worth mentioning here for data handling

# Libraries that usually require installation (pip install library_name)
# To avoid errors in this interpreter, I'll only import and demonstrate usage
# if they are commonly part of standard environments or have a simple fallback.
# For complex libraries like NumPy, Pandas, Matplotlib, Requests, I'll explain their use cases
# and provide conceptual code snippets rather than runnable examples here.
try:
    import numpy as np
except ImportError:
    np = None # Indicate that numpy is not available
    print("Warning: NumPy not installed. Some examples will be skipped.")

try:
    import pandas as pd
except ImportError:
    pd = None
    print("Warning: Pandas not installed. Some examples will be skipped.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print("Warning: Matplotlib not installed. Some examples will be skipped.")

try:
    import requests
except ImportError:
    requests = None
    print("Warning: Requests not installed. Some examples will be skipped.")

print("--- Python's Useful Libraries: Practice Code ---")

# --- 1. Standard Library (Built-in or Ships with Python) ---
print("\n--- 1. Standard Library ---")
print("These libraries are part of the Python installation itself. No `pip install` needed.")

# 1.1 `os` (Operating System Interface)
print("\n1.1 `os` - Interacting with the Operating System:")
print("Used for file system operations, environment variables, etc.")
print(f"Current working directory: {os.getcwd()}")
# os.mkdir("temp_dir") # Create a directory (uncomment to test)
# os.rmdir("temp_dir") # Remove a directory (uncomment to test)
print(f"List files in current directory (first 3): {os.listdir('.')[:3]}...")
print(f"Path join: {os.path.join('my_folder', 'my_file.txt')}")
print(f"File exists ('{__file__}'): {os.path.exists(__file__)}")

# 1.2 `sys` (System-specific parameters and functions)
print("\n1.2 `sys` - System Interactions:")
print("Provides access to system-specific parameters and functions.")
print(f"Python version: {sys.version.split(' ')[0]}")
# sys.exit() # Exit the program (uncomment to test)

# 1.3 `datetime` (Date and Time handling)
print("\n1.3 `datetime` - Working with Dates and Times:")
print("Classes for manipulating dates and times.")
now = datetime.datetime.now()
print(f"Current date and time: {now}")
today = datetime.date.today()
print(f"Today's date: {today}")
future_date = datetime.date(2025, 12, 25)
delta = future_date - today
print(f"Days until Dec 25, 2025: {delta.days} days")
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 1.4 `math` (Mathematical functions)
print("\n1.4 `math` - Mathematical Operations:")
print("Provides mathematical functions not available in built-in operators.")
print(f"PI: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.9: {math.floor(4.9)}")
print(f"Factorial of 5: {math.factorial(5)}")

# 1.5 `random` (Generate pseudo-random numbers)
print("\n1.5 `random` - Generating Randomness:")
print("Functions for generating pseudo-random numbers.")
print(f"Random float (0.0 to 1.0): {random.random()}")
print(f"Random integer (1 to 10): {random.randint(1, 10)}")
my_list = ['apple', 'banana', 'cherry']
print(f"Random choice from list: {random.choice(my_list)}")
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# 1.6 `re` (Regular Expressions)
print("\n1.6 `re` - Regular Expressions:")
print("Operations for matching and manipulating strings with regular expressions.")
text = "The quick brown fox jumps over the lazy dog."
match = re.search(r"fox", text)
if match:
    print(f"Found 'fox' at index: {match.start()}")
all_words = re.findall(r"\b\w+\b", text) # Find all words
print(f"All words: {all_words}")
new_text = re.sub(r"lazy", "sleepy", text)
print(f"Text after substitution: {new_text}")

# 1.7 `collections` (Specialized container datatypes)
print("\n1.7 `collections` - Enhanced Data Structures:")
print("Provides alternatives to built-in types like dict, list, tuple.")
# `Counter`
from collections import Counter
sentence = "apple banana apple orange banana apple"
word_counts = Counter(sentence.split())
print(f"Word counts: {word_counts}")
# `defaultdict`
from collections import defaultdict
scores = defaultdict(int) # Default value for new keys is 0
scores['Alice'] += 10
scores['Bob'] += 5
scores['Alice'] += 7
print(f"Scores using defaultdict: {scores}")
# `deque` (double-ended queue)
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(f"Deque: {d}")
d.popleft()
print(f"Deque after popleft: {d}")

# 1.8 `statistics` (Mathematical statistics functions)
print("\n1.8 `statistics` - Basic Statistics:")
print("Functions for common mathematical statistics of numeric data.")
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Standard Deviation: {statistics.stdev(data):.2f}")


# 1.9 `json` and `csv` (Already covered in File I/O, but worth reinforcing for data handling)
print("\n1.9 `json` and `csv` - Data Serialization/Deserialization:")
print("Essential for working with structured text data.")
print("See previous 'Python File I/O' section for detailed examples.")
sample_dict = {"name": "Test", "value": 100}
json_string = json.dumps(sample_dict)
print(f"Dict to JSON string: {json_string}")
loaded_dict = json.loads(json_string)
print(f"JSON string to Dict: {loaded_dict}")


# --- 2. Third-Party Libraries (Require `pip install`) ---
print("\n--- 2. Third-Party Libraries (Require `pip install library_name`) ---")
print("These libraries are not part of the standard Python distribution but are widely used.")
print("You typically install them using Python's package installer, `pip`.")
print("Example: `pip install numpy pandas requests matplotlib`")

# 2.1 `NumPy` (Numerical Python)
print("\n2.1 `NumPy` - Numerical Computing (Arrays):")
print("Foundation for numerical computing in Python. Provides powerful N-dimensional array object.")
print("Used extensively in data science, machine learning, scientific computing.")
if np:
    arr = np.array([1, 2, 3, 4])
    print(f"NumPy Array: {arr}")
    print(f"Array + 5: {arr + 5}")
    matrix = np.array([[1, 2], [3, 4]])
    print(f"Matrix multiplication: {matrix @ matrix}") # Or np.dot(matrix, matrix)
else:
    print("NumPy not available. Install with `pip install numpy`.")


# 2.2 `Pandas` (Data Manipulation and Analysis)
print("\n2.2 `Pandas` - Data Analysis (DataFrames):")
print("Built on NumPy, provides high-performance, easy-to-use data structures and data analysis tools.")
print("Key structures: Series (1D), DataFrame (2D, like a spreadsheet).")
if pd:
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print(f"Pandas DataFrame:\n{df}")
    print(f"\nAverage Age: {df['Age'].mean()}")
    print(f"Filtered (Age > 28):\n{df[df['Age'] > 28]}")
else:
    print("Pandas not available. Install with `pip install pandas`.")


# 2.3 `Matplotlib` (Plotting and Visualization)
print("\n2.3 `Matplotlib` - Plotting and Visualization:")
print("A comprehensive library for creating static, animated, and interactive visualizations.")
if plt:
    print("Conceptual Matplotlib usage (requires a display to show plot):")
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    # plt.plot(x, y)
    # plt.title("Sine Wave")
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.show() # This would open a plot window
else:
    print("Matplotlib not available. Install with `pip install matplotlib`.")


# 2.4 `Requests` (HTTP for Humans)
print("\n2.4 `Requests` - HTTP Communication:")
print("Simplifies making HTTP requests (GET, POST, etc.) to web services.")
print("Used for web scraping, interacting with APIs.")
if requests:
    print("\nConceptual Requests usage:")
    # try:
    #     response = requests.get('https://api.github.com/events')
    #     response.raise_for_status() # Raise an exception for HTTP errors
    #     data = response.json()
    #     print(f"First event from GitHub API: {data[0]['type']}")
    # except requests.exceptions.RequestException as e:
    #     print(f"Error fetching data: {e}")
else:
    print("Requests not available. Install with `pip install requests`.")


# 2.5 `Scikit-learn` (Machine Learning)
print("\n2.5 `Scikit-learn` - Machine Learning:")
print("A powerful and user-friendly library for various machine learning algorithms.")
print("Includes tools for classification, regression, clustering, model selection, etc.")
print("Conceptual usage: (Requires NumPy/SciPy)")
print("  `from sklearn.linear_model import LinearRegression`")
print("  `model = LinearRegression()`")
print("  `model.fit(X_train, y_train)`")
print("  `predictions = model.predict(X_test)`")


# 2.6 `Flask` / `Django` (Web Frameworks)
print("\n2.6 `Flask` / `Django` - Web Development:")
print("Libraries for building web applications.")
print("  - `Flask`: A lightweight micro-framework, good for small projects/APIs.")
print("  - `Django`: A full-stack framework, includes ORM, admin panel, etc., for larger projects.")
print("Conceptual Flask usage:")
print("  `from flask import Flask`")
print("  `app = Flask(__name__)`")
print("  `@app.route('/')`")
print("  `def hello_world(): return 'Hello, World!'`")
print("  `if __name__ == '__main__': app.run(debug=True)`")


# 2.7 `BeautifulSoup` (Web Scraping)
print("\n2.7 `BeautifulSoup` - Web Scraping (HTML/XML Parsing):")
print("A library for pulling data out of HTML and XML files.")
print("Conceptual usage: (Often used with `requests`)")
print("  `from bs4 import BeautifulSoup`")
print("  `html_doc = requests.get('http://example.com').text`")
print("  `soup = BeautifulSoup(html_doc, 'html.parser')`")
print("  `title = soup.title.string`")


# --- 3. How to Discover More Libraries ---
print("\n--- 3. How to Discover More Libraries ---")
print(" - **PyPI (Python Package Index):** The official third-party software repository for Python. (pypi.org)")
print(" - **Awesome Python List:** A curated list of awesome Python frameworks, libraries, software and resources. (github.com/vinta/awesome-python)")
print(" - **Community:** Stack Overflow, Reddit (r/Python), developer blogs.")
print(" - **Project Needs:** Often, your specific problem will lead you to the right library.")

print("\n--- End of Python's Useful Libraries Practice Code ---")