The `match` statement, introduced in **Python 3.10**, provides a **pattern matching** mechanism similar to a `switch` statement in other programming languages. It enables concise, readable, and flexible ways to handle conditional logic based on specific patterns of input.

Here’s a comprehensive guide to Python’s `match` statement:

---

## **1. Syntax of `match`**

```python
match subject:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (if no pattern matches)
```

- `subject`: The value or variable being matched.
- `pattern1`, `pattern2`, etc.: Patterns to match against the subject.
- `_`: A wildcard pattern that matches anything (like a default case).

---

## **2. Simple Example**

```python
value = 2

match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case _:
        print("Value is something else")
```

**Output**:

```
Value is 2
```

---

## **3. Pattern Matching Features**

### **a. Literal Patterns**

Match against specific values like numbers, strings, or booleans.

```python
match "hello":
    case "hello":
        print("Matched hello")
    case "world":
        print("Matched world")
```

---

### **b. Variable Patterns**

Assign the matched value to a variable.

```python
value = 42

match value:
    case x:
        print(f"Matched and assigned to x: {x}")
```

**Output**:

```
Matched and assigned to x: 42
```

---

### **c. Wildcard Pattern (`_`)**

Matches anything and does not bind the value.

```python
value = "anything"

match value:
    case _:
        print("This matches everything")
```

---

### **d. Sequence Patterns**

Match against lists, tuples, or other sequences.

```python
value = [1, 2, 3]

match value:
    case [1, 2, 3]:
        print("Matched the exact list")
    case [1, 2, _]:
        print("Matched list with first two elements as 1 and 2")
    case _:
        print("No match")
```

---

### **e. Dictionary Patterns**

Match dictionary structures.

```python
person = {"name": "Alice", "age": 30}

match person:
    case {"name": "Alice", "age": age}:
        print(f"Matched Alice with age {age}")
    case {"name": "Bob"}:
        print("Matched Bob")
    case _:
        print("No match")
```

---

### **f. Class Patterns**

Match based on object attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)

match point:
    case Point(x=1, y=2):
        print("Matched Point(1, 2)")
    case Point(x, y):
        print(f"Matched Point with x={x} and y={y}")
```

---

### **g. OR Patterns (`|`)**

Combine multiple patterns.

```python
value = 5

match value:
    case 1 | 2 | 3:
        print("Matched 1, 2, or 3")
    case 4 | 5 | 6:
        print("Matched 4, 5, or 6")
    case _:
        print("No match")
```

**Output**:

```
Matched 4, 5, or 6
```

---

### **h. Guard Patterns (`if`)**

Add a condition to patterns.

```python
value = 10

match value:
    case x if x > 5:
        print(f"Matched value greater than 5: {x}")
    case _:
        print("Value is 5 or less")
```

**Output**:

```
Matched value greater than 5: 10
```

---

### **i. Nested Patterns**

Match patterns within patterns.

```python
data = {"user": {"name": "Alice", "age": 30}}

match data:
    case {"user": {"name": "Alice", "age": age}}:
        print(f"Matched Alice with age {age}")
    case _:
        print("No match")
```

---

## **4. Limitations and Rules**

1. **Immutable Patterns**: Patterns must be immutable types like numbers, strings, or tuples.
2. **Exhaustive Matching**: Always include a `_` wildcard as a fallback case to avoid unhandled cases.
3. **Variable Binding**: Avoid shadowing existing variables unintentionally with pattern variables.

---

## **5. Advanced Examples**

### Example 1: Match JSON-like Data

```python
data = {"type": "error", "code": 404}

match data:
    case {"type": "error", "code": 404}:
        print("Not Found error")
    case {"type": "error", "code": code}:
        print(f"Error with code {code}")
    case _:
        print("Unknown type")
```

---

### Example 2: Match Against Tuples

```python
coords = (1, 2, 3)

match coords:
    case (1, 2, 3):
        print("Exact match")
    case (x, y, z):
        print(f"Coordinates are x={x}, y={y}, z={z}")
    case _:
        print("No match")
```

---

### Example 3: Combine Guards with Patterns

```python
value = 42

match value:
    case x if x % 2 == 0:
        print(f"{x} is even")
    case x if x % 2 != 0:
        print(f"{x} is odd")
    case _:
        print("Unknown value")
```

---

## **6. Why Use `match`?**

- **Improves Readability**: Makes code easier to read than nested `if-elif-else`.
- **Powerful Matching**: Allows matching against complex data structures (e.g., dictionaries, sequences).
- **Extensible**: Matches custom class objects, enabling robust conditional logic.

---

## **7. Comparison with `if-elif-else`**

### Using `if-elif-else`:

```python
value = 10
if value == 1:
    print("Value is 1")
elif value == 2:
    print("Value is 2")
else:
    print("Value is something else")
```

### Using `match`:

```python
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case _:
        print("Value is something else")
```

---

## **8. Conclusion**

The `match` statement is a versatile feature for handling complex conditional logic in Python. It's particularly useful when dealing with structured data, providing a cleaner and more concise alternative to nested `if-elif` statements.

Let me know if you'd like examples for a specific use case!

The **`match`** statement in Python is a structural pattern matching feature introduced in Python 3.10. It allows you to match variables against patterns, which can be complex data structures or simple literals, and execute code based on the match. It's similar to `switch` or `case` statements found in other programming languages but with more powerful matching capabilities.

### **Key Concepts of the `match` Statement:**

- **`match`**: The keyword used to start the pattern matching.
- **`case`**: Used to define a pattern to match against a value.

Pattern matching in Python with `match` is more flexible than traditional `switch`/`case` statements, allowing you to match more complex patterns, such as data structures, sequences, and objects.

---

### **Syntax:**

```python
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Default case (like "else" in if-else)
```

- `match` is followed by the value to be matched against.
- Each `case` provides a pattern that is checked against the value.
- The `_` wildcard is used to catch all unmatched cases (similar to `default` in other languages).
- The first `case` that matches the value will have its corresponding code executed, and the rest are skipped.

---

### **1. Matching Literal Values:**

You can match simple literal values such as integers, strings, and other constants.

**Example:**

```python
def match_number(x):
    match x:
        case 1:
            print("One")
        case 2:
            print("Two")
        case _:
            print("Other")

match_number(1)  # Output: One
match_number(5)  # Output: Other
```

---

### **2. Matching Data Structures (Lists, Tuples, etc.):**

You can match complex data structures like lists, tuples, and dictionaries.

**Example with Tuple:**

```python
def match_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On the x-axis at {x}")
        case (0, y):
            print(f"On the y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")

match_point((2, 3))  # Output: Point at (2, 3)
match_point((0, 3))  # Output: On the y-axis at 3
```

---

### **3. Matching with Conditions (Guards):**

You can add a condition (guard) to a case, which is checked in addition to the pattern match.

**Example:**

```python
def match_number(x):
    match x:
        case 1:
            print("One")
        case 2 | 3:  # Matching multiple values
            print("Two or Three")
        case x if x > 3:  # Guard condition
            print(f"Greater than 3: {x}")
        case _:
            print("Other")

match_number(5)  # Output: Greater than 3: 5
```

In this example, the case `x if x > 3` uses a guard condition to match only if the value is greater than 3.

---

### **4. Matching Sequences (Lists, Strings, etc.):**

You can match sequences (e.g., lists, strings) by specifying patterns that match the structure of the sequence.

**Example:**

```python
def match_list(lst):
    match lst:
        case [1, 2, 3]:  # Matches a list with elements 1, 2, 3
            print("Matched [1, 2, 3]")
        case [x, y, *rest]:  # Matches a list with at least 2 elements
            print(f"First: {x}, Second: {y}, Rest: {rest}")
        case _:
            print("No match")

match_list([1, 2, 3])  # Output: Matched [1, 2, 3]
match_list([5, 10, 15, 20])  # Output: First: 5, Second: 10, Rest: [15, 20]
```

Here, the pattern `[x, y, *rest]` matches lists with at least two elements and captures the first two elements in `x` and `y`, and the remaining elements in `rest`.

---

### **5. Matching Classes (Object Matching):**

You can match against the type of an object by specifying the class of the object in the pattern.

**Example:**

```python
class Animal:
    pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def match_animal(animal):
    match animal:
        case Dog():  # Matches objects of class Dog
            print("It's a dog!")
        case Cat():  # Matches objects of class Cat
            print("It's a cat!")
        case _:
            print("Unknown animal")

match_animal(Dog())  # Output: It's a dog!
match_animal(Cat())  # Output: It's a cat!
```

---

### **6. Nested Matching:**

You can also perform pattern matching inside other structures, like within a class or within another match block.

**Example:**

```python
def match_coordinates(coord):
    match coord:
        case (x, y):
            print(f"Coordinates: x={x}, y={y}")
            match x:
                case 0:
                    print("On the y-axis")
                case _:
                    print("Not on the y-axis")

match_coordinates((0, 5))  # Output: Coordinates: x=0, y=5, On the y-axis
```

---

### **7. `match` with Dictionaries:**

Python `match` can also match dictionaries, which is useful when working with structured data.

**Example:**

```python
def match_dict(data):
    match data:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case _:
            print("Unknown structure")

match_dict({"name": "Alice", "age": 30})  # Output: Name: Alice, Age: 30
match_dict({"name": "Bob"})  # Output: Unknown structure
```

---

### **8. Using `case _` (Wildcard):**

The `_` (underscore) in `case _` acts as a wildcard that matches anything that doesn't match the other patterns.

**Example:**

```python
def match_number(x):
    match x:
        case 1:
            print("Matched 1")
        case 2:
            print("Matched 2")
        case _:
            print("Matched something else")

match_number(3)  # Output: Matched something else
```

---

### **9. Pattern Matching with Type Guards:**

Pattern matching can also be combined with type guards to ensure that the matched value is of a specific type.

**Example:**

```python
def process(value):
    match value:
        case int() if value > 10:  # Only match integers greater than 10
            print(f"Large integer: {value}")
        case str():
            print(f"String: {value}")
        case _:
            print("Other")

process(15)  # Output: Large integer: 15
process("Hello")  # Output: String: Hello
```

---

### **Summary:**

- The `match` statement is a powerful pattern matching mechanism introduced in Python 3.10.
- It allows for sophisticated matching of values, data structures, classes, and more.
- Patterns can include literals, sequences, classes, and more complex structures.
- Guards (`if` conditions) can be applied to refine matches.
- The `_` wildcard is used as a catch-all, default case.

Pattern matching enhances code readability, making it easier to handle various scenarios with clear, structured patterns.

Let me know if you need any further clarification or examples!

The `match` statement, introduced in Python 3.10, is a powerful feature for pattern matching. It is similar to switch-case statements found in other programming languages, but much more flexible and sophisticated. The `match` statement can be used for matching specific patterns in data structures and performing actions based on these patterns.

### **Syntax of `match` Statement**

The basic syntax for the `match` statement is as follows:

```python
match expression:
    case pattern_1:
        # Code block executed when expression matches pattern_1
    case pattern_2:
        # Code block executed when expression matches pattern_2
    case _:
        # Code block executed when no other case matches (optional)
```

### **Key Components**

1. **`match` keyword**: Starts the pattern matching block, followed by the expression that you want to evaluate.
2. **`case` keyword**: Defines a specific pattern to match the expression against.
3. **`_` (underscore)**: A special pattern that acts as a "catch-all" or default case, similar to the `else` clause in an `if-else` structure.

---

### **Basic Example: Matching Literal Values**

The `match` statement can be used to match literal values, similar to how a switch-case works in other languages.

```python
def match_color(color):
    match color:
        case "red":
            return "You chose red."
        case "green":
            return "You chose green."
        case "blue":
            return "You chose blue."
        case _:
            return "Unknown color."

print(match_color("green"))  # Output: You chose green.
```

---

### **Pattern Matching with Variables**

You can also use variables in the patterns, which will capture the matched values.

```python
def match_value(value):
    match value:
        case int() as num:  # Matches any integer and assigns it to 'num'
            return f"Integer: {num}"
        case str() as text:  # Matches any string and assigns it to 'text'
            return f"String: {text}"
        case _:
            return "Unknown type"

print(match_value(42))     # Output: Integer: 42
print(match_value("hello")) # Output: String: hello
```

---

### **Matching with Sequences**

The `match` statement can be used to match sequences, such as lists or tuples. This allows you to destructure the sequence and capture specific elements.

```python
def match_sequence(seq):
    match seq:
        case [1, 2, 3]:  # Matches exactly [1, 2, 3]
            return "Matched [1, 2, 3]"
        case [1, *rest]:  # Matches [1, ...] and captures the rest of the sequence
            return f"Starts with 1, rest: {rest}"
        case _:
            return "No match"

print(match_sequence([1, 2, 3]))       # Output: Matched [1, 2, 3]
print(match_sequence([1, 4, 5, 6]))    # Output: Starts with 1, rest: [4, 5, 6]
```

---

### **Matching with Dictionaries**

You can match against dictionaries and even destructure them using `match`.

```python
def match_dict(d):
    match d:
        case {"name": name, "age": age}:  # Matches a dict with 'name' and 'age'
            return f"Name: {name}, Age: {age}"
        case {"name": name}:  # Matches a dict with only 'name'
            return f"Name: {name}"
        case _:
            return "Unknown dictionary structure"

print(match_dict({"name": "Alice", "age": 25}))  # Output: Name: Alice, Age: 25
print(match_dict({"name": "Bob"}))  # Output: Name: Bob
```

---

### **Matching with Classes and Instances**

You can match against classes and create patterns that match specific attributes of instances.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def match_instance(obj):
    match obj:
        case Person(name="Alice", age=25):  # Matches a Person with name Alice and age 25
            return "Matched Alice, 25 years old"
        case Person(name, age):  # Matches any Person and captures name and age
            return f"Matched {name}, {age} years old"
        case _:
            return "Not a person"

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(match_instance(p1))  # Output: Matched Alice, 25 years old
print(match_instance(p2))  # Output: Matched Bob, 30 years old
```

---

### **Guard Clauses in Pattern Matching**

You can add conditions (guards) to a case pattern using `if` to match more specific conditions.

```python
def match_with_guard(value):
    match value:
        case int() as num if num > 10:  # Matches integers greater than 10
            return f"Large integer: {num}"
        case int() as num:
            return f"Small integer: {num}"
        case _:
            return "Not an integer"

print(match_with_guard(15))  # Output: Large integer: 15
print(match_with_guard(5))   # Output: Small integer: 5
```

---

### **Match Case with Multiple Patterns**

A single `case` can match multiple patterns, separated by commas.

```python
def match_multiple_patterns(value):
    match value:
        case "apple" | "banana":  # Matches either "apple" or "banana"
            return "It's a fruit!"
        case "carrot" | "potato":  # Matches either "carrot" or "potato"
            return "It's a vegetable!"
        case _:
            return "Unknown"

print(match_multiple_patterns("apple"))  # Output: It's a fruit!
print(match_multiple_patterns("potato"))  # Output: It's a vegetable!
```

---

### **When to Use `match` Statements**

- **Pattern matching** in Python is great for cases where you want to destructure complex data structures, such as lists, dictionaries, or objects.
- **Readable conditional logic**: `match` is more expressive and cleaner than a series of `if-elif-else` statements when dealing with multiple cases, especially when pattern matching is involved.
- **Replacing switch-case**: In languages that lack pattern matching (like C or JavaScript), you often use switch-case for matching literals. In Python, `match` provides a more flexible and robust alternative.

---

### **Comparison with `if`-`elif`**

While the `match` statement is more expressive, sometimes simple `if`-`elif` conditions can be sufficient. The `match` statement shines when dealing with complex patterns or data structures.

**Example: Using `if`-`elif`:**

```python
def check_value(value):
    if value == "apple":
        return "It's an apple!"
    elif value == "banana":
        return "It's a banana!"
    else:
        return "Unknown fruit"

print(check_value("banana"))  # Output: It's a banana!
```

**Example: Using `match`-`case`:**

```python
def check_value(value):
    match value:
        case "apple":
            return "It's an apple!"
        case "banana":
            return "It's a banana!"
        case _:
            return "Unknown fruit"

print(check_value("banana"))  # Output: It's a banana!
```

---

### **Summary**

- The `match` statement allows you to match patterns in expressions and data structures.
- It is introduced in Python 3.10, making it a powerful tool for handling complex conditional logic.
- Supports matching on literals, sequences, classes, and dictionaries.
- Pattern matching can be enhanced with conditions and guards.
- Use `match` for cleaner, more readable code when dealing with multiple conditions or complex structures.

Let me know if you'd like more examples or clarification on any aspect of pattern matching!

The `match` statement is a powerful feature introduced in Python 3.10. It provides a way to match patterns against values, which can be used as a more flexible and readable alternative to traditional conditional logic like `if-elif-else`.

It is similar to the `switch` or `case` statement found in other programming languages. The `match` statement in Python allows for more advanced pattern matching, including matching against sequences, data structures, and even types.

### **Basic Syntax**

```python
match expression:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (like "else")
```

- `expression`: This is the value you're matching against.
- `pattern1`, `pattern2`: These are the patterns you're comparing the expression to.
- `_`: This is the default catch-all case, similar to `else`, used when no other patterns match.

### **Examples**

#### **Basic Matching**

```python
def describe_number(x):
    match x:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case _:
            print("Other number")

describe_number(2)  # Output: Two
```

#### **Matching with Sequences**

You can match sequences like lists or tuples.

```python
def handle_list(lst):
    match lst:
        case [x, y]:
            print(f"List has two elements: {x} and {y}")
        case [x, y, z]:
            print(f"List has three elements: {x}, {y}, and {z}")
        case _:
            print("Different length list")

handle_list([1, 2])  # Output: List has two elements: 1 and 2
handle_list([1, 2, 3])  # Output: List has three elements: 1, 2, and 3
```

#### **Matching with Dictionaries**

You can also match dictionaries and extract specific values.

```python
def match_dict(d):
    match d:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case _:
            print("No match")

match_dict({"name": "Alice", "age": 30})  # Output: Name: Alice, Age: 30
```

#### **Matching with Variables**

Patterns can bind variables to values, which you can use later in the block.

```python
def greet(name):
    match name:
        case "Alice":
            greeting = f"Hello, Alice!"
        case "Bob":
            greeting = f"Hello, Bob!"
        case _:
            greeting = "Hello, Stranger!"
    print(greeting)

greet("Bob")  # Output: Hello, Bob!
```

#### **Matching with Classes**

You can match instances of classes and extract attributes.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

def describe_pet(pet):
    match pet:
        case Dog(name, breed):
            print(f"A {breed} dog named {name}")
        case _:
            print("Unknown pet")

dog = Dog("Buddy", "Golden Retriever")
describe_pet(dog)  # Output: A Golden Retriever dog named Buddy
```

---

### **Advanced Features of Match**

#### **Guards (`if` conditions inside `case`)**

You can add conditions to a `case` using an `if` guard, which further refines the pattern.

```python
def describe_number(x):
    match x:
        case 1 | 2 | 3:
            print("Small number")
        case n if n > 10:
            print("Large number")
        case _:
            print("Other number")

describe_number(12)  # Output: Large number
```

#### **Nested Pattern Matching**

You can use nested patterns to match deeply structured data like lists of tuples or more complex objects.

```python
def handle_nested(data):
    match data:
        case ([x, y], z):
            print(f"First list: {x}, {y}, Second: {z}")
        case _:
            print("No match")

handle_nested(([1, 2], 3))  # Output: First list: 1, 2, Second: 3
```

#### **Type Matching**

You can match types using `type()` within the `case` pattern.

```python
def match_type(value):
    match value:
        case int():
            print("An integer")
        case str():
            print("A string")
        case list():
            print("A list")
        case _:
            print("Some other type")

match_type(42)  # Output: An integer
match_type("hello")  # Output: A string
```

---

### **The `_` (Wildcard) Pattern**

The `_` pattern is used as a wildcard to match any value, and it can also be used as a default catch-all for unmatched cases.

```python
def categorize_value(value):
    match value:
        case 1:
            print("One")
        case 2:
            print("Two")
        case _:
            print("Other")

categorize_value(5)  # Output: Other
```

---

### **Advantages of `match` Statement**

1. **Readability**: `match` statements are more readable, especially when dealing with complex conditions or nested structures, compared to multiple `if-elif-else` blocks.
2. **Pattern Matching**: It provides advanced pattern matching, including matching specific values, sequences, and class instances.
3. **More Elegant**: For cases that involve checking multiple conditions, `match` can simplify the code and make it more concise.

---

### **Limitations**

1. **Python 3.10+**: The `match` statement is available only in Python 3.10 and later versions, so it won't work in earlier versions.
2. **Performance Considerations**: For simple conditions, using `if` and `elif` might still be more efficient than `match`, though the difference is usually negligible unless working with extremely large datasets.

---

### **Summary**

The `match` statement is an advanced feature in Python that allows for pattern matching, making it easier to handle complex conditional logic. It supports matching against literals, sequences, classes, and even custom patterns, providing an elegant alternative to the traditional `if-elif-else` chains. With features like guards, nested patterns, and type matching, the `match` statement is a powerful tool for Python developers.

In Python, **`match`** is a powerful feature introduced in Python 3.10 as part of the **Structural Pattern Matching** functionality. The `match` statement is used to compare an expression against different patterns and execute the code block corresponding to the matching pattern. It's similar to a `switch` statement in other languages but more versatile due to its advanced pattern matching capabilities.

Here is a complete breakdown of how `match` works in Python:

### **Basic Syntax of `match`**

```python
match expression:
    case pattern_1:
        # Code block if pattern_1 matches
    case pattern_2:
        # Code block if pattern_2 matches
    case _:
        # Default case if no pattern matches
```

- **`match`**: Starts the pattern matching block, where the given expression will be matched against the patterns.
- **`case`**: Defines the specific pattern to check against the expression.
- **`_`**: The wildcard pattern that matches anything and acts as the default case (similar to `else`).

### **1. Basic Example**

The basic structure of a `match` statement is to match an expression against different patterns.

```python
def match_day(day):
    match day:
        case "Monday":
            return "Start of the week!"
        case "Tuesday":
            return "Second day of the week."
        case "Wednesday":
            return "Middle of the week."
        case _:
            return "Some other day."

print(match_day("Monday"))  # Output: Start of the week!
print(match_day("Sunday"))  # Output: Some other day.
```

### **2. Matching Literal Values**

You can match literal values such as strings, numbers, or any other constant value.

```python
def match_number(number):
    match number:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Unknown"

print(match_number(1))  # Output: One
print(match_number(5))  # Output: Unknown
```

### **3. Matching Variable Bindings**

You can bind values to variables within a pattern match, allowing you to capture parts of the expression that match a specific pattern.

```python
def match_color(color):
    match color:
        case "red":
            return "Red color"
        case "green":
            return "Green color"
        case other:  # Variable binding
            return f"Unknown color: {other}"

print(match_color("blue"))  # Output: Unknown color: blue
```

### **4. Matching Tuples**

You can match complex structures like tuples. When matching tuples, the number of elements in the tuple must be exactly the same as the pattern you're matching against.

```python
def match_coordinates(coord):
    match coord:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On the x-axis at {x}"
        case (0, y):
            return f"On the y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Unknown coordinate"

print(match_coordinates((0, 0)))  # Output: Origin
print(match_coordinates((5, 3)))  # Output: Point at (5, 3)
```

### **5. Matching Lists**

You can match lists, and you can even destructure lists into individual elements.

```python
def match_list(lst):
    match lst:
        case [1, 2, 3]:
            return "List is [1, 2, 3]"
        case [x, y, z]:
            return f"List has 3 elements: {x}, {y}, {z}"
        case [x, *rest]:  # The *rest syntax captures the remaining elements
            return f"List starts with {x}, and the rest is {rest}"
        case _:
            return "Unknown list"

print(match_list([1, 2, 3]))  # Output: List is [1, 2, 3]
print(match_list([5, 6, 7, 8]))  # Output: List starts with 5, and the rest is [6, 7, 8]
```

### **6. Matching with Guards**

Guards allow you to apply an additional condition to the pattern using the `if` clause.

```python
def match_number_with_guard(number):
    match number:
        case x if x > 10:
            return "Greater than 10"
        case x if x < 5:
            return "Less than 5"
        case _:
            return "Between 5 and 10"

print(match_number_with_guard(15))  # Output: Greater than 10
print(match_number_with_guard(2))   # Output: Less than 5
print(match_number_with_guard(7))   # Output: Between 5 and 10
```

### **7. Nested Matching**

You can nest `match` statements for more complex patterns, including matching objects and dictionaries.

```python
def match_person(person):
    match person:
        case {"name": name, "age": age} if age > 18:
            return f"{name} is an adult"
        case {"name": name, "age": age}:
            return f"{name} is a minor"
        case _:
            return "Unknown person"

print(match_person({"name": "Alice", "age": 20}))  # Output: Alice is an adult
print(match_person({"name": "Bob", "age": 15}))    # Output: Bob is a minor
```

### **8. Class Pattern Matching**

You can also match against class instances and destructure their attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def match_point(p):
    match p:
        case Point(0, 0):
            return "Origin"
        case Point(x, 0):
            return f"On the x-axis at {x}"
        case Point(0, y):
            return f"On the y-axis at {y}"
        case Point(x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Unknown"

p1 = Point(0, 0)
p2 = Point(3, 5)

print(match_point(p1))  # Output: Origin
print(match_point(p2))  # Output: Point at (3, 5)
```

### **9. The Wildcard (`_`)**

The `_` pattern matches anything, and it is typically used in the default case to catch any unmatched patterns.

```python
def match_animal(animal):
    match animal:
        case "dog":
            return "Woof!"
        case "cat":
            return "Meow!"
        case _:
            return "Unknown animal"

print(match_animal("dog"))  # Output: Woof!
print(match_animal("bird")) # Output: Unknown animal
```

### **Key Points about `match` Statements**

- **Patterns** can match literals, variables, sequences (like lists or tuples), objects, and more.
- **Guards** allow for conditions on patterns.
- **Wildcards (`_`)** act as the default catch-all.
- **Pattern Matching** is more expressive than traditional `if-elif-else` statements, especially when working with complex data structures.

### **Conclusion**

The `match` statement in Python is an incredibly powerful tool for structuring conditional logic, especially when working with more complex data structures or when you need a more readable alternative to multiple `if-elif` conditions. It supports **pattern matching**, **guards**, **wildcards**, and even **class instance matching**, making it a versatile feature to use in Python.

The `match` statement in Python, introduced in Python 3.10, is a powerful tool for pattern matching. It provides a more readable and concise way to handle conditional checks, especially when working with complex data structures like tuples, lists, dictionaries, or user-defined objects.

### **1. Basic Syntax of `match` Statement**

The `match` statement works similarly to a `switch` or `case` statement in other programming languages. It compares an expression against multiple patterns and executes the block of code associated with the first matching pattern.

**Basic Syntax**:

```python
match expression:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Code block for default case (wildcard)
```

- `expression`: The value you want to check.
- `case pattern`: The pattern to compare the expression with.
- `_`: The wildcard pattern that matches anything (acts as a default case).

---

### **2. Example: Simple Match Case**

Here’s a simple example that matches an integer with different cases:

```python
def describe_number(n):
    match n:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Other"

print(describe_number(2))  # Output: Two
```

In this example:

- `match n:` is comparing the value of `n` with the `case` patterns.
- The wildcard `_` serves as the default case and will match any value not explicitly handled by the other cases.

---

### **3. Pattern Matching with Literals**

You can match literals like integers, strings, or other constants directly in the `case` statements.

```python
def greeting(name):
    match name:
        case "Alice":
            return "Hello, Alice!"
        case "Bob":
            return "Hi, Bob!"
        case _:
            return "Hello, stranger!"

print(greeting("Alice"))  # Output: Hello, Alice!
```

---

### **4. Matching Data Types (Type Guards)**

Python’s `match` statement can be used to match types. You can check whether the expression is of a specific type.

```python
def process_data(data):
    match data:
        case int():
            return "Integer"
        case str():
            return "String"
        case list():
            return "List"
        case _:
            return "Unknown type"

print(process_data(123))    # Output: Integer
print(process_data("hello"))  # Output: String
```

- `case int()`: Matches an integer.
- `case str()`: Matches a string.
- `case list()`: Matches a list.

---

### **5. Matching Sequences (Lists, Tuples)**

You can match elements of sequences, such as lists or tuples. This allows you to match certain values at specific positions.

```python
def match_tuple(t):
    match t:
        case (x, y):
            return f"Tuple with two elements: {x}, {y}"
        case (x, y, z):
            return f"Tuple with three elements: {x}, {y}, {z}"
        case _:
            return "Other tuple shape"

print(match_tuple((1, 2)))  # Output: Tuple with two elements: 1, 2
print(match_tuple((1, 2, 3)))  # Output: Tuple with three elements: 1, 2, 3
```

---

### **6. Destructuring with Pattern Matching**

Pattern matching allows you to destructure complex data structures (e.g., lists, tuples, dictionaries) and bind variables to specific parts of the structure.

```python
def match_point(point):
    match point:
        case (x, y):  # Tuple with two elements, x and y
            return f"Point coordinates: x = {x}, y = {y}"
        case _:
            return "Not a valid point"

print(match_point((3, 4)))  # Output: Point coordinates: x = 3, y = 4
```

---

### **7. Matching with Named Patterns (Variable Binding)**

You can match and bind values to specific variables using pattern matching.

```python
def match_dict(d):
    match d:
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case _:
            return "Invalid data"

print(match_dict({"name": "Alice", "age": 30}))  # Output: Name: Alice, Age: 30
```

In this case:

- `{"name": name, "age": age}` matches dictionaries with specific keys (`name` and `age`) and binds their values to the variables `name` and `age`.

---

### **8. Combining Patterns**

You can combine multiple patterns to create more complex matches.

```python
def match_value(value):
    match value:
        case 1 | 2 | 3:
            return "Value is 1, 2, or 3"
        case 4 | 5 | 6:
            return "Value is 4, 5, or 6"
        case _:
            return "Other value"

print(match_value(2))  # Output: Value is 1, 2, or 3
```

In this example:

- `1 | 2 | 3` combines multiple literals into one case, matching if `value` is either `1`, `2`, or `3`.

---

### **9. Pattern Matching in Class Instances**

The `match` statement can also be used to match class instances.

```python
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat")
        self.breed = breed

def animal_sound(animal):
    match animal:
        case Dog(breed):
            return f"Woof! I am a {breed} dog."
        case Cat(breed):
            return f"Meow! I am a {breed} cat."
        case _:
            return "Unknown animal"

print(animal_sound(Dog("Labrador")))  # Output: Woof! I am a Labrador dog.
print(animal_sound(Cat("Siamese")))  # Output: Meow! I am a Siamese cat.
```

---

### **10. Wildcard `_`**

The `_` symbol is a wildcard that matches anything and is used as a catch-all when no other pattern matches.

```python
def match_value(value):
    match value:
        case 1:
            return "One"
        case _:
            return "Any other number"

print(match_value(5))  # Output: Any other number
```

---

### **11. Using `case` with Guard Clauses**

You can add a guard clause (`if` statement) to a `case` to further restrict the pattern match.

```python
def check_age(age):
    match age:
        case age if age < 18:
            return "Minor"
        case age if age >= 18:
            return "Adult"
        case _:
            return "Invalid age"

print(check_age(16))  # Output: Minor
```

---

### **12. Summary of `match` Features**

- **Pattern Matching**: Match against specific values, types, or structures.
- **Destructuring**: Bind variables to specific parts of complex data structures.
- **Guards**: Use conditions within the `case` to filter matches.
- **Class Matching**: Match class instances and their attributes.
- **Wildcard `_`**: Acts as a catch-all or default case.
- **Combining Patterns**: Use `|` to combine multiple values or patterns in a single case.

---

### **Conclusion**

The `match` statement in Python offers a clean and expressive way to handle complex conditional logic. It’s especially powerful for working with nested data structures, types, and class instances. By using pattern matching, you can write more readable and maintainable code, particularly when dealing with complex data parsing or handling various data types.

The `match` statement in Python, introduced in Python 3.10, provides a more powerful and flexible way to handle conditional logic by allowing you to match patterns in values. It is a more sophisticated and readable alternative to a series of `if-elif-else` statements.

---

### **1. Basic Syntax of `match`**

```python
match value:
    case pattern1:
        # Code block executed if value matches pattern1
    case pattern2:
        # Code block executed if value matches pattern2
    case _:
        # Default case (if none of the patterns match)
```

### **Explanation**:

- **`value`**: The variable or expression to be matched against the patterns.
- **`pattern1`, `pattern2`, etc.**: The patterns against which the value is tested.
- **`case _`**: This is a catch-all pattern (like the `else` in traditional if-else). It matches anything and is typically used as the last case for unmatched values.

---

### **2. Example of Basic Matching**

```python
def match_example(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Other"

print(match_example(1))  # Output: "One"
print(match_example(3))  # Output: "Other"
```

---

### **3. Matching with Multiple Patterns**

You can match multiple values using the pipe (`|`) operator.

```python
def match_example(value):
    match value:
        case 1 | 2:
            return "One or Two"
        case 3:
            return "Three"
        case _:
            return "Other"

print(match_example(1))  # Output: "One or Two"
print(match_example(3))  # Output: "Three"
print(match_example(4))  # Output: "Other"
```

---

### **4. Matching Sequences (e.g., Lists or Tuples)**

You can match a sequence by specifying the number of elements, or even use wildcards to match any number of elements.

```python
def match_sequence(seq):
    match seq:
        case [1, 2, 3]:
            return "Matched [1, 2, 3]"
        case [x, y]:
            return f"Matched a pair: {x}, {y}"
        case _:
            return "No match"

print(match_sequence([1, 2, 3]))  # Output: "Matched [1, 2, 3]"
print(match_sequence([4, 5]))     # Output: "Matched a pair: 4, 5"
print(match_sequence([7, 8, 9]))  # Output: "No match"
```

---

### **5. Pattern Matching with Named Variables**

You can bind values from a pattern to variables, which can be used inside the block of the match statement.

```python
def match_point(point):
    match point:
        case (x, y):
            return f"Point with coordinates x={x}, y={y}"
        case _:
            return "Not a point"

print(match_point((3, 4)))  # Output: "Point with coordinates x=3, y=4"
print(match_point([1, 2]))  # Output: "Point with coordinates x=1, y=2"
```

---

### **6. Wildcards and `_*` (underscore as wildcard)**

You can use the `_` (underscore) to match any value, and `*` can be used to match a variable number of elements in sequences.

#### **Matching any value**:

```python
def match_any(value):
    match value:
        case _:
            return "Matched any value"

print(match_any(42))  # Output: "Matched any value"
```

#### **Matching multiple elements in a sequence**:

```python
def match_sequence(seq):
    match seq:
        case [x, *rest]:
            return f"First element: {x}, Remaining elements: {rest}"
        case _:
            return "No match"

print(match_sequence([1, 2, 3, 4]))  # Output: "First element: 1, Remaining elements: [2, 3, 4]"
```

---

### **7. Matching with Class Patterns**

You can also match objects of a specific class and extract their attributes directly within the match statement.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def match_class(value):
    match value:
        case Point(x, y):
            return f"Point with x={x} and y={y}"
        case _:
            return "Not a point"

point = Point(3, 4)
print(match_class(point))  # Output: "Point with x=3 and y=4"
```

---

### **8. Guard Clauses (using `if` inside `case`)**

You can use `if` clauses to further filter a match case based on conditions.

```python
def match_with_guard(value):
    match value:
        case x if x > 10:
            return "Greater than 10"
        case x if x < 5:
            return "Less than 5"
        case _:
            return "Between 5 and 10"

print(match_with_guard(15))  # Output: "Greater than 10"
print(match_with_guard(3))   # Output: "Less than 5"
print(match_with_guard(8))   # Output: "Between 5 and 10"
```

---

### **9. Structural Pattern Matching (Matching with Subpatterns)**

In Python 3.10+, you can also match more complex structures, such as dictionaries, using subpatterns. You can match against keys and values within the dictionary.

```python
def match_dict(data):
    match data:
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case _:
            return "Not a match"

print(match_dict({"name": "Alice", "age": 30}))  # Output: "Name: Alice, Age: 30"
print(match_dict({"name": "Bob", "gender": "Male"}))  # Output: "Not a match"
```

---

### **10. Type Matching with `case`**

You can use `match` to match against types in addition to values.

```python
def match_type(value):
    match value:
        case int():
            return "This is an integer."
        case str():
            return "This is a string."
        case list():
            return "This is a list."
        case _:
            return "Unknown type"

print(match_type(42))       # Output: "This is an integer."
print(match_type("Hello"))  # Output: "This is a string."
print(match_type([1, 2, 3])) # Output: "This is a list."
```

---

### **11. Summary of `match` Statement**

- **Pattern Matching**: Matches the structure and value of the object.
- **Wildcard (`_`)**: Catches any value, similar to a default case.
- **Guards (`if`)**: Add additional conditions inside a case.
- **Binding Variables**: Bind values in patterns to variables.
- **Class Pattern Matching**: Matches against class instances and extracts attributes.
- **Structural Matching**: Matches complex structures like lists, tuples, and dictionaries.

---

### **Conclusion**

The `match` statement allows Python developers to write cleaner and more readable code for complex conditional logic. It’s particularly useful for handling different data structures, patterns, and cases without resorting to cumbersome `if-elif-else` chains. It is a great addition to Python’s syntax, especially for cases involving multiple options, complex patterns, and type matching.

The `match` statement in Python is used to perform pattern matching on values, and it was introduced in Python 3.10. This allows more readable and concise ways of handling complex conditional logic, similar to `switch` statements in other languages.

Here is a detailed explanation of the `match` statement, its syntax, and how it can be used in Python:

---

### **1. Basic Syntax of `match`**

The basic syntax of a `match` statement consists of the `match` keyword followed by an expression and one or more `case` clauses, which define patterns to match against.

```python
match <expression>:
    case <pattern1>:
        # Code to execute if <expression> matches <pattern1>
    case <pattern2>:
        # Code to execute if <expression> matches <pattern2>
    case _:
        # Code to execute if none of the patterns match (default case)
```

- `<expression>` is the value that will be matched against the patterns.
- `<pattern1>`, `<pattern2>`, etc., are patterns that the expression will be checked against.
- `_` is a wildcard pattern that matches anything and is typically used as the default case (like `else` in traditional conditionals).

---

### **2. Example Usage**

```python
def describe_number(num):
    match num:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case _:
            return "Other number"

print(describe_number(0))  # Output: Zero
print(describe_number(1))  # Output: One
print(describe_number(5))  # Output: Other number
```

In this example:

- The expression `num` is matched against the patterns `0`, `1`, and the wildcard `_`.
- If no pattern matches, the default case (`_`) is executed.

---

### **3. Matching with Variables**

You can bind variables to parts of the pattern, which allows you to extract values during matching.

```python
def describe_shape(shape):
    match shape:
        case ('circle', radius):
            return f"Circle with radius {radius}"
        case ('rectangle', width, height):
            return f"Rectangle with width {width} and height {height}"
        case _:
            return "Unknown shape"

print(describe_shape(('circle', 5)))  # Output: Circle with radius 5
print(describe_shape(('rectangle', 4, 5)))  # Output: Rectangle with width 4 and height 5
```

In this case:

- The tuple `('circle', 5)` matches the pattern `('circle', radius)`, and the value `5` is bound to `radius`.
- Similarly, a `('rectangle', 4, 5)` tuple is matched to extract `width` and `height`.

---

### **4. Matching with Sequence Patterns**

You can match sequences (such as lists or tuples) and extract their elements using patterns.

```python
def analyze_sequence(seq):
    match seq:
        case [x, y, z]:
            return f"List with three elements: {x}, {y}, {z}"
        case [x, y]:
            return f"List with two elements: {x}, {y}"
        case _:
            return "Unknown sequence"

print(analyze_sequence([1, 2, 3]))  # Output: List with three elements: 1, 2, 3
print(analyze_sequence([1, 2]))     # Output: List with two elements: 1, 2
```

Here, we match the list's length and bind variables to the elements.

---

### **5. Matching with Class Patterns**

You can match objects of custom classes by specifying the class name as part of the pattern.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    match point:
        case Point(x, y):
            return f"Point with coordinates ({x}, {y})"
        case _:
            return "Unknown object"

p = Point(2, 3)
print(describe_point(p))  # Output: Point with coordinates (2, 3)
```

Here, the `Point(x, y)` pattern matches instances of the `Point` class, and the `x` and `y` attributes are extracted.

---

### **6. Wildcard `_`**

The wildcard `_` is used to match anything, and it is usually used as the "default" case to handle unmatched patterns.

```python
def match_value(value):
    match value:
        case 42:
            return "The Answer to the Ultimate Question of Life, the Universe, and Everything"
        case _:
            return "Some other value"

print(match_value(42))  # Output: The Answer to the Ultimate Question of Life, the Universe, and Everything
print(match_value(100))  # Output: Some other value
```

---

### **7. Combining Multiple Patterns**

You can combine multiple patterns using the `|` (OR) operator to match against different possibilities.

```python
def check_status(status):
    match status:
        case "success" | "complete":
            return "Task completed successfully"
        case "pending":
            return "Task is still pending"
        case _:
            return "Unknown status"

print(check_status("success"))  # Output: Task completed successfully
print(check_status("pending"))  # Output: Task is still pending
```

Here, `"success"` and `"complete"` are grouped together in one case.

---

### **8. Pattern Matching with `match` and `case`**

- The `match` statement allows more advanced pattern matching, which can handle more complex data structures.
- You can combine multiple patterns and conditions for more specific control over matching.

---

### **9. Guards in Pattern Matching**

You can use a `case` guard to apply an additional condition for a pattern. This is done with the `if` keyword.

```python
def classify_number(num):
    match num:
        case n if n < 0:
            return "Negative"
        case n if n == 0:
            return "Zero"
        case n if n > 0:
            return "Positive"
        case _:
            return "Unknown"

print(classify_number(-5))  # Output: Negative
print(classify_number(0))   # Output: Zero
print(classify_number(5))   # Output: Positive
```

Here, the guards (`if n < 0`, `if n == 0`, etc.) allow additional conditions to be checked during pattern matching.

---

### **10. Nested Pattern Matching**

You can nest `match` statements inside each other for deeper matching.

```python
def describe_data(data):
    match data:
        case (x, y):
            match (x, y):
                case (0, 0):
                    return "Origin"
                case (x, 0):
                    return f"On the X-axis at {x}"
                case (0, y):
                    return f"On the Y-axis at {y}"
                case (x, y):
                    return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

print(describe_data((0, 0)))  # Output: Origin
print(describe_data((3, 0)))  # Output: On the X-axis at 3
```

---

### **Summary**

The `match` statement in Python is a powerful tool for pattern matching, allowing you to match values against patterns in a clean and readable way. It can handle simple cases like exact value matching as well as more complex cases, including matching sequences, classes, and nested structures. Guards can be used to add additional conditions, and the wildcard `_` can be used to handle any unmatched case.

Let me know if you'd like further details or examples on any specific part of pattern matching!

In Python, the `match` statement, introduced in Python 3.10, is used for **structural pattern matching**. It is a more powerful and readable alternative to the traditional `if-elif` chains, enabling a more declarative approach to handle complex data structures or conditions.

### **1. Basic Syntax of `match`**

The `match` statement is used to compare a value against a pattern, and execute corresponding blocks of code based on the pattern match.

**Syntax**:

```python
match expression:
    case pattern1:
        # Block of code for pattern1
    case pattern2:
        # Block of code for pattern2
    case _:
        # Default block if no pattern matches (similar to 'else')
```

Where:

- `expression` is the value or variable you're matching against.
- `pattern` is a specific condition or structure to match the value against.
- `case _` is a catch-all pattern (like an `else` in traditional `if-else` chains).

---

### **2. Basic Example**

A simple example of using `match` with basic patterns:

```python
def match_number(x):
    match x:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Unknown"

print(match_number(2))  # Output: "Two"
print(match_number(5))  # Output: "Unknown"
```

---

### **3. Pattern Matching Types**

The `match` statement supports several types of patterns that can be used to match against values. These patterns include literal patterns, variable patterns, sequence patterns, and more.

#### **a. Literal Patterns**

A literal pattern matches the exact value of the expression.

```python
x = 10
match x:
    case 10:
        print("Matched 10")
    case 20:
        print("Matched 20")
    case _:
        print("No match")  # Output: "Matched 10"
```

#### **b. Variable Patterns**

A variable pattern matches any value and binds the value to a variable.

```python
x = 42
match x:
    case a:
        print(f"Matched value: {a}")  # Output: "Matched value: 42"
```

#### **c. Sequence Patterns**

You can match a sequence (list, tuple) and unpack its elements.

```python
x = [1, 2, 3]
match x:
    case [1, 2, 3]:
        print("Matched list: [1, 2, 3]")  # Output: "Matched list: [1, 2, 3]"
    case _:
        print("No match")
```

#### **d. Destructuring / Unpacking Patterns**

Match and destructure an object into its components, such as lists or tuples.

```python
x = (1, 2, 3)
match x:
    case (a, b, c):  # Destructuring the tuple
        print(f"Matched tuple: {a}, {b}, {c}")  # Output: "Matched tuple: 1, 2, 3"
```

#### **e. Class Patterns**

You can match objects of a particular class. The pattern allows you to check if an object is an instance of a class and optionally match attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

match person:
    case Person(name="John", age=age):
        print(f"Found a person named John, age {age}")  # Output: "Found a person named John, age 30"
    case _:
        print("No match")
```

#### **f. Wildcard Pattern (`_`)**

The wildcard `_` matches any value, but does not bind it to a variable. It is often used as a default case.

```python
x = 5
match x:
    case 10:
        print("Matched 10")
    case _:
        print("Matched any value")  # Output: "Matched any value"
```

---

### **4. Guard Conditions**

You can also add guard conditions using the `if` clause after a case pattern. This allows you to specify additional conditions that must be met for the match to succeed.

```python
x = 15
match x:
    case num if num > 10:
        print("Number is greater than 10")  # Output: "Number is greater than 10"
    case num:
        print(f"Matched number: {num}")
```

---

### **5. Matching Dictionaries**

You can match against dictionaries by specifying key-value pairs as patterns. This is useful when dealing with structured data.

```python
x = {"name": "Alice", "age": 25}
match x:
    case {"name": "Alice", "age": age}:
        print(f"Alice is {age} years old.")  # Output: "Alice is 25 years old."
    case _:
        print("No match")
```

---

### **6. Matching with `match` and `case`**

The `match` statement is much like a switch-case construct in other programming languages but is more flexible. For example, the patterns in `case` can handle complex types like tuples, lists, dictionaries, and even class instances.

---

### **7. `match` in Complex Data Structures**

Pattern matching is particularly useful when dealing with complex nested structures, like lists or dictionaries, making it easier to access and work with deep values.

```python
data = {"user": {"name": "Alice", "age": 30}}

match data:
    case {"user": {"name": name, "age": age}}:
        print(f"User: {name}, Age: {age}")  # Output: "User: Alice, Age: 30"
    case _:
        print("No match")
```

---

### **8. `match` with `or` in a Case Statement**

You can combine multiple patterns in a single `case` statement using the `|` operator (logical OR), allowing multiple matches to be handled in a single block.

```python
x = 1
match x:
    case 1 | 2 | 3:
        print("Matched 1, 2, or 3")  # Output: "Matched 1, 2, or 3"
    case _:
        print("No match")
```

---

### **9. The `match` Statement vs. `if-elif-else`**

The `match` statement can make code more readable and less error-prone when dealing with complex conditional structures. It simplifies matching complex types (like tuples, lists, and dictionaries) and avoids the need for multiple `if-elif` conditions.

**Example: Using `if-elif-else`**

```python
x = 3
if x == 1:
    print("Matched 1")
elif x == 2:
    print("Matched 2")
elif x == 3:
    print("Matched 3")  # Output: "Matched 3"
else:
    print("No match")
```

**Example: Using `match-case`**

```python
x = 3
match x:
    case 1:
        print("Matched 1")
    case 2:
        print("Matched 2")
    case 3:
        print("Matched 3")  # Output: "Matched 3"
    case _:
        print("No match")
```

---

### **10. Performance Consideration**

Although `match` provides clarity and readability, it may not always be the most performant approach for simple conditions. It is best used when dealing with complex data structures or when multiple patterns must be handled. For simple value comparisons, traditional `if-elif-else` might be more efficient.

---

### **Conclusion**

The `match` statement in Python allows for more concise and readable code when working with complex conditions or structures. By using patterns such as literals, variables, sequences, and more, the `match` statement offers a powerful way to handle conditional logic in a structured and expressive manner.

The `match` statement is a feature introduced in **Python 3.10** that allows for pattern matching. It is used to compare a value against a set of patterns and execute code based on the matched pattern. This feature provides a more expressive and readable way to handle conditions that would typically require multiple `if-elif-else` statements or complex `switch`-like constructs.

Here's a breakdown of how `match` works, its syntax, and how to use it effectively:

### **Basic Syntax of `match`**

The basic syntax of the `match` statement involves:

```python
match value:
    case pattern1:
        # Code for pattern1 match
    case pattern2:
        # Code for pattern2 match
    case _:
        # Code for default case (if no match)
```

- `value` is the variable or expression you are matching against.
- `case pattern` is used to specify the patterns to match.
- The underscore (`_`) is used as a "wildcard" to represent any value that doesn't match any of the specified patterns (similar to `default` in other languages).

---

### **Types of Patterns**

Patterns in a `match` statement can be of various types, and Python uses pattern matching to match the given value against these patterns:

#### **1. Literal Patterns**

Literal patterns match a specific value (similar to equality checks).

```python
value = 10

match value:
    case 10:
        print("Matched 10")
    case 20:
        print("Matched 20")
    case _:
        print("No match")
```

**Output**:

```
Matched 10
```

#### **2. Variable Patterns**

You can use a variable as a pattern, which binds the matched value to that variable.

```python
value = 5

match value:
    case x:
        print(f"Matched {x}")  # x will bind the matched value
```

**Output**:

```
Matched 5
```

#### **3. Sequence Patterns**

You can match sequences like lists or tuples. You can also destructure the sequence to match individual elements.

```python
value = [1, 2, 3]

match value:
    case [1, 2, 3]:
        print("Matched [1, 2, 3]")
    case [1, *rest]:  # The *rest pattern captures the rest of the list
        print(f"Matched list starting with 1, rest: {rest}")
    case _:
        print("No match")
```

**Output**:

```
Matched [1, 2, 3]
```

#### **4. Mapping Patterns**

Mapping patterns match dictionary-like objects (including `dict` objects). You can destructure the mapping into key-value pairs.

```python
value = {"name": "Alice", "age": 25}

match value:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case _:
        print("No match")
```

**Output**:

```
Name: Alice, Age: 25
```

#### **5. Class Patterns**

You can match objects based on their class and bind them to variables.

```python
class Dog:
    def __init__(self, breed):
        self.breed = breed

dog = Dog("Labrador")

match dog:
    case Dog(breed="Labrador"):
        print("Matched a Labrador dog")
    case Dog(breed=breed):
        print(f"Matched a dog of breed {breed}")
    case _:
        print("No match")
```

**Output**:

```
Matched a Labrador dog
```

#### **6. OR Patterns**

You can use the `|` (pipe) operator to specify "or" between different patterns.

```python
value = 20

match value:
    case 10 | 20:
        print("Matched 10 or 20")
    case _:
        print("No match")
```

**Output**:

```
Matched 10 or 20
```

#### **7. Wildcard Pattern (`_`)**

The `_` (underscore) pattern acts as a "catch-all" and will match anything that does not match other patterns.

```python
value = 100

match value:
    case 10:
        print("Matched 10")
    case 20:
        print("Matched 20")
    case _:
        print("Matched something else")
```

**Output**:

```
Matched something else
```

---

### **Pattern Guards**

A pattern guard is an additional condition that must be true for a case to be matched. It can be added using `if` after the pattern.

```python
value = 30

match value:
    case x if x > 10:
        print(f"Matched {x}, which is greater than 10")
    case x:
        print(f"Matched {x}")
```

**Output**:

```
Matched 30, which is greater than 10
```

---

### **Match and Case with Default (`_`)**

The wildcard (`_`) is useful for setting a default action if no patterns match.

```python
value = 42

match value:
    case 10:
        print("Matched 10")
    case 20:
        print("Matched 20")
    case _:
        print("Default case matched")
```

**Output**:

```
Default case matched
```

---

### **Pattern Matching with `match` vs `if-elif-else`**

Pattern matching is more powerful and expressive than a simple series of `if-elif-else` statements. For example, consider matching multiple patterns:

```python
# Using if-elif-else:
value = (1, 2)
if value == (1, 2):
    print("Matched (1, 2)")
elif value == (3, 4):
    print("Matched (3, 4)")
else:
    print("No match")

# Using match:
value = (1, 2)
match value:
    case (1, 2):
        print("Matched (1, 2)")
    case (3, 4):
        print("Matched (3, 4)")
    case _:
        print("No match")
```

---

### **Advantages of `match`**

- **Clear and concise**: The `match` statement can often replace multiple `if-elif-else` blocks, leading to clearer, more readable code.
- **Pattern Matching**: Allows for matching based on more complex patterns, such as destructuring lists, tuples, dictionaries, and matching based on object types.
- **Guards**: You can specify additional conditions within a `case` statement using pattern guards.
- **Performance**: In some cases, pattern matching can be more efficient than using multiple `if-elif-else` conditions, especially for complex structures.

---

### **Limitations of `match`**

- **Version Restriction**: The `match` statement was introduced in Python 3.10, so it is not available in earlier versions.
- **Limited Support for Data Structures**: While it supports a variety of patterns like literals, lists, and mappings, it may not be as flexible for more complex or custom data structures (though user-defined class matching is supported).

---

### **Example of Full Usage**

```python
def match_shape(shape):
    match shape:
        case {"type": "circle", "radius": r}:
            print(f"Circle with radius {r}")
        case {"type": "rectangle", "width": w, "height": h}:
            print(f"Rectangle with width {w} and height {h}")
        case _:
            print("Unknown shape")

shape1 = {"type": "circle", "radius": 5}
shape2 = {"type": "rectangle", "width": 4, "height": 7}

match_shape(shape1)  # Output: Circle with radius 5
match_shape(shape2)  # Output: Rectangle with width 4 and height 7
```

---

### **Summary**

The `match` statement in Python provides an expressive and powerful way to handle conditional logic with pattern matching. It is especially useful when working with complex data structures, such as dictionaries, lists, and objects. By utilizing patterns and guards, you can create more readable and efficient code.
