The **identity operators** in Python are used to compare the memory locations of two objects to check whether they are the same object (not just equal in value). The two identity operators in Python are `is` and `is not`.

---

### **1. Syntax of Identity Operators**

| Operator | Description                                                                    | Example      |
| -------- | ------------------------------------------------------------------------------ | ------------ |
| `is`     | Evaluates to `True` if both variables point to the same object in memory       | `x is y`     |
| `is not` | Evaluates to `True` if the variables do not point to the same object in memory | `x is not y` |

---

### **2. Key Points about Identity Operators**

- They compare the **identity** of objects (their memory location), not their **values**.
- Use the `id()` function to check the memory location of objects.
- Works best for comparing immutable objects like integers, strings, and `None`.
- Mutable objects (like lists, dictionaries, or custom objects) may have the same value but different identities.

---

### **3. `is` Operator**

The `is` operator checks if two variables point to the **same object in memory**.

#### Example:

```python
x = 10
y = 10
print(x is y)  # True, because integers with the same value may share the same memory location (small integer caching).

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, because lists with the same value are stored in different memory locations.
```

---

### **4. `is not` Operator**

The `is not` operator checks if two variables **do not** point to the same object in memory.

#### Example:

```python
x = "hello"
y = "world"
print(x is not y)  # True, because they are different objects.

a = None
b = None
print(a is not b)  # False, because both are the same `None` object.
```

---

### **5. Comparing Mutable Objects**

Even if mutable objects (like lists or dictionaries) contain the same values, they will not share the same identity unless explicitly assigned.

#### Example:

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False, because they are different objects.

list3 = list1
print(list1 is list3)  # True, because list3 refers to the same object as list1.
```

---

### **6. Comparing Immutable Objects**

Immutable objects, like numbers or strings, may have the same identity for certain values due to Python's optimization (interning).

#### Example:

```python
x = "hello"
y = "hello"
print(x is y)  # True, because Python reuses the same string object for optimization.

num1 = 100
num2 = 100
print(num1 is num2)  # True, small integers are cached and share the same identity.
```

---

### **7. Special Case: `None`**

`None` is a singleton in Python, meaning there is only one instance of `None` in memory. Use `is` to compare with `None`.

#### Correct Usage:

```python
x = None
if x is None:
    print("x is None")
```

#### Incorrect Usage:

```python
# Do not use `==` to compare with `None`
if x == None:
    print("x is None")  # Works but is less Pythonic.
```

---

### **8. Using `id()` to Check Identity**

The `id()` function returns the memory location of an object.

#### Example:

```python
a = 10
b = 10
print(id(a))  # Memory location of `a`
print(id(b))  # Memory location of `b`
print(a is b)  # True, because `a` and `b` point to the same memory location.

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))  # Different memory location
print(id(list2))
print(list1 is list2)  # False
```

---

### **9. When to Use Identity Operators**

- **To compare singletons like `None`**:

  ```python
  if x is None:
      print("x is None")
  ```

- **To check if two variables refer to the same object**:

  ```python
  if obj1 is obj2:
      print("Both are the same object.")
  ```

- **Avoid using `is` to compare values**:
  ```python
  # Use `==` for value comparison
  if a == b:
      print("Values are the same")
  ```

---

### **10. Common Pitfalls**

- **Immutable objects (like strings or integers):**
  Small integers (-5 to 256) and some strings are cached by Python, so they may appear to have the same identity:

  ```python
  a = 256
  b = 256
  print(a is b)  # True

  a = 300
  b = 300
  print(a is b)  # False, as 300 is not cached.
  ```

- **Mutable objects:**
  Always assume mutable objects (like lists or dicts) are different unless explicitly made the same.

---

Let me know if you'd like examples of specific scenarios!

### **Python Identity Operators: All About Syntax & Usage**

In Python, **identity operators** are used to compare the **identities** of two objects. The **identity** of an object refers to its **memory location** (i.e., the actual object itself in memory).

Python provides **two identity operators**:

1. `is`: Checks if two variables point to the same object in memory.
2. `is not`: Checks if two variables do **not** point to the same object in memory.

These operators are essential for determining object identity rather than equality of values.

---

## **1. `is` Operator**

The `is` operator checks whether two variables reference (point to) the **same object in memory**.

### **Syntax**

```python
variable1 is variable2
```

- `variable1` and `variable2` are Python objects.
- Returns `True` if both variables reference the same object in memory.
- Otherwise, returns `False`.

---

### **Example 1: Simple `is` Comparison**

```python
a = [1, 2, 3]
b = a  # b points to the same object as a
print(a is b)  # Output: True
```

Explanation:

- `b = a` makes `b` refer to the same list object as `a`.
- `a is b` returns `True` because both point to the same object in memory.

---

### **Example 2: Comparing Different Objects**

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False
```

Explanation:

- Even though `x` and `y` contain the same values, they are different objects in memory.
- Therefore, `x is y` returns `False`.

---

### **Example 3: Singleton Objects**

Singleton objects like `None`, `True`, and `False` are always the same instance in Python.

```python
a = None
b = None
print(a is b)  # Output: True
```

Explanation:

- `None` is a singleton object, meaning there is only one instance of it in memory.

---

## **2. `is not` Operator**

The `is not` operator checks whether two variables **do not** reference the same object in memory.

### **Syntax**

```python
variable1 is not variable2
```

- Returns `True` if `variable1` and `variable2` are referencing different objects.
- Otherwise, returns `False`.

---

### **Example 1: Comparing Different Objects**

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  # Output: True
```

Explanation:

- Here `a` and `b` point to different memory locations, even if their content is the same.
- `a is not b` returns `True`.

---

### **Example 2: Using `is not` with Singleton Objects**

```python
x = None
y = [None]
print(x is not y)  # Output: True
```

Explanation:

- `None` is not equivalent to a list containing `None`.

---

## **3. Common Use Cases for Identity Operators**

### **1. Comparing Objects for Singleton Identity**

Python treats objects like `None`, `True`, and `False` as singletons (only one instance exists). Identity operators can confirm singleton comparison.

```python
if some_var is None:
    print("The variable is None")
```

---

### **2. Avoiding Object Creation Overhead**

When you have conditions where the same object is reused, use `is` instead of `==` to check references to avoid unnecessary object comparisons.

---

### **3. Debugging with Identity Checks**

When debugging, `is` and `is not` can determine if different objects are causing unexpected behavior.

---

## **4. Comparison with Equality (`==`)**

### **Difference between `is` and `==`**

- `is` checks if two variables point to the **same object** in memory.
- `==` checks if the **values** of two variables are equal.

### **Example**

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (they have the same content)
print(a is b)  # Output: False (they are different objects in memory)
```

---

## **5. Performance of Identity Checks**

Identity comparisons are faster because they simply check if the memory address of two objects is the same, while value comparisons (`==`) may involve deeper logic or comparison of object contents.

---

## **6. Edge Case: Custom Objects**

For custom classes, object identity depends on whether the same memory reference is used.

### Example: Custom Class with Singleton-like Behavior

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True
```

Explanation:

- The `Singleton` pattern ensures that only one instance of the class is created, and `obj1 is obj2` returns `True`.

---

## **Summary Table**

| **Operator** | **Description**                                                                | **Syntax Example** | **Returns**                                                  |
| ------------ | ------------------------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| **`is`**     | Checks if two variables point to the same memory location (object).            | `x is y`           | `True` if x and y reference the same object, else `False`.   |
| **`is not`** | Checks if two variables do **not** point to the same memory location (object). | `x is not y`       | `True` if x and y reference different objects, else `False`. |

---

## **Key Points to Remember**

- `is` and `is not` are for **object identity**, **not object equality**.
- Use `is` to check for singleton objects like `None`.
- Avoid using `is` for value comparisons unless you're explicitly checking object identity.
- Use `==` for comparing object contents or values.

Would you like a deeper explanation or additional examples on any of the above use cases? 😊

The identity operators in Python, `is` and `is not`, are used to compare the memory locations of two objects. They are particularly useful when you want to check if two variables refer to the same object in memory, not just if they have the same value.

Here's a quick overview:

- **`is` Operator**: Evaluates to `True` if the variables on either side of the operator point to the same object and `False` otherwise.
- **`is not` Operator**: Evaluates to `True` if the variables on either side of the operator point to different objects and `False` otherwise.

### Examples:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# a and b point to the same object
print(a is b)  # Output: True

# a and c have the same values but are different objects
print(a is c)  # Output: False

# a and c do not point to the same object
print(a is not c)  # Output: True
```

In this example, `a` and `b` refer to the same list object in memory, while `c` is a separate list object with the same values.

### When to Use:

- **`is`**: When you want to check if two variables refer to the exact same object (useful for singletons like `None`).
- **`is not`**: When you want to check if two variables do not refer to the same object.

Would you like a deeper dive into any specific aspect of the identity operators?

### **`is` Operator in Python: All About It**

The **`is` operator** in Python is one of the **identity operators**. It checks if **two variables point to the same object** in memory (i.e., if they reference the same memory location).

---

## **What is the `is` Operator?**

The `is` operator is used to compare the **identities** of two objects, not their values. The identity of an object refers to its **memory address**.

### Syntax

```python
variable1 is variable2
```

- `variable1` and `variable2` are Python objects.
- The comparison returns:
  - `True` if both `variable1` and `variable2` refer to the **same object** in memory.
  - `False` if they refer to different memory locations.

---

## **Examples of `is`**

Let's look at various examples to understand how the `is` operator works.

---

### **1. Comparing Objects with `is`**

#### Example 1: Same Object Comparison

When two variables point to the same object, the `is` operator returns `True`.

```python
a = [1, 2, 3]
b = a  # b now references the same memory location as a

print(a is b)  # Output: True
```

Explanation:

- `b = a` makes `b` point to the same list object as `a`.
- `a is b` checks if they reference the same memory location.

---

#### Example 2: Comparing Different Objects

Even if two objects have the same content, if they're different objects in memory, `is` will return `False`.

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # Output: False
```

Explanation:

- `x` and `y` have identical values but are stored in different memory locations.

---

#### Example 3: Comparing Singleton Objects

Singleton objects like `None`, `True`, and `False` are always stored in a single memory location. Thus, comparisons with `is` return `True` when compared against each other.

```python
a = None
b = None

print(a is b)  # Output: True
```

Explanation:

- Python ensures only one instance of `None` exists.

---

#### Example 4: Comparing Singleton Boolean Values

```python
x = True
y = True

print(x is y)  # Output: True
```

Explanation:

- Python optimizes the memory for boolean values by ensuring that `True` and `False` are singletons.

---

## **When Should You Use the `is` Operator?**

### **1. Check for `None`**

The `is` operator is typically used to check if a variable is `None`. Using `is None` is recommended over `== None`.

#### Example:

```python
my_var = None

if my_var is None:
    print("my_var is None")
else:
    print("my_var is not None")
```

Why is `is` preferred here?

- `None` is a singleton object, and comparing with `is` checks for object identity rather than equality.

---

### **2. Check for Singleton Objects**

Singletons are objects that exist only once during a program's execution. Examples include `None`, `True`, and `False`.

#### Example:

```python
if some_var is True:
    print("some_var is True")
```

This avoids any unnecessary comparison logic.

---

### **3. Debugging**

Using `is` can help debug if two variables reference the same memory object, especially in data manipulation scenarios.

---

## **Comparison: `is` vs `==`**

While `is` checks if two variables point to the **same object**, `==` checks if two variables have the **same value**.

| **Operator** | **What it Compares**                                                                  | **Example**                            | **Returns** |
| ------------ | ------------------------------------------------------------------------------------- | -------------------------------------- | ----------- |
| **`is`**     | Checks if two variables point to the **same object in memory**.                       | `a = [1, 2, 3], b = a; a is b`         | `True`      |
| **`==`**     | Checks if two variables have the **same values**, even if they are different objects. | `a = [1, 2, 3], b = [1, 2, 3]; a == b` | `True`      |

---

### Example: Difference between `is` and `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (their values are the same)
print(a is b)  # Output: False (they are different objects in memory)
```

Explanation:

- `a == b`: Compares the values (content) of the two lists.
- `a is b`: Compares their memory references.

---

## **Advanced Example: Custom Objects**

The `is` operator can be helpful with custom objects to check if two variables are referencing the same instance of an object.

### Example with Classes

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True
```

Explanation:

- The `Singleton` class ensures only **one instance** of the object exists.
- Thus, `obj1 is obj2` returns `True`.

---

## **Why `is` is Better for Singleton Checks**

Python optimizes singleton memory usage for certain objects (`None`, `True`, `False`) by ensuring only one instance exists in memory. Therefore:

- Use `is` for singleton comparisons instead of `==`.
- Example:

```python
if variable is None:
    print("Variable is None.")
```

---

## **Edge Cases**

### Example with Mutable Types

```python
a = [1, 2, 3]
b = [1, 2, 3]

# Mutate a
b.append(4)

print(a is b)  # Output: False
print(a == b)  # Output: False
```

Mutable lists are separate unless explicitly reassigned. Therefore, `is` checks will show `False` unless they explicitly reference each other.

---

## **Summary**

### Key Points:

1. The `is` operator checks whether two objects are the same in memory, **not just their values**.
2. `is` is commonly used for singleton checks (like `None`, `True`, `False`).
3. `is` should **not** be used for value comparisons unless explicitly checking memory identity.
4. Use `is None` instead of `== None` for improved readability and efficiency.

---

Would you like to explore examples with more complex use cases for `is`? Let me know! 😊

### **`is not` Operator in Python: All About It**

The **`is not` operator** in Python is one of the **identity operators**. It checks whether two variables **do NOT refer to the same object in memory** (i.e., whether they do not point to the same memory location).

---

## **What is the `is not` Operator?**

The `is not` operator compares the **identities** of two objects to determine if they do **not** refer to the same memory location.

### Syntax

```python
variable1 is not variable2
```

- `variable1` and `variable2` are Python objects.
- The comparison returns:
  - `True` if `variable1` and `variable2` are **different objects** in memory.
  - `False` if they reference the **same memory location**.

---

## **Key Idea**

The `is not` operator is the negation of the `is` operator.

- **`is` checks if two variables refer to the same memory address.**
- **`is not` checks if two variables do NOT refer to the same memory address.**

---

## **Examples of `is not`**

Let's explore examples to understand how the `is not` operator works.

---

### **1. Comparing Objects with `is not`**

#### Example 1: Same Memory Location (should return `False`)

When two variables point to the same memory object, `is not` returns `False`.

```python
a = [1, 2, 3]
b = a  # b references the same object as a

print(a is not b)  # Output: False
```

Explanation:

- Here, `b = a` makes `b` point to the same list object as `a`. Thus `a is not b` is `False`.

---

#### Example 2: Different Memory Locations (should return `True`)

When two variables point to different objects in memory, `is not` will return `True`.

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)  # Output: True
```

Explanation:

- Although the two lists have identical content (`[1, 2, 3]`), they are stored in different memory locations.

---

#### Example 3: Comparing Singleton Objects with `is not`

Singletons like `None`, `True`, and `False` ensure that only one instance exists in memory. Using `is not` allows you to check if two variables are referencing different instances.

```python
x = None
y = None

print(x is not y)  # Output: False
```

Explanation:

- Both `x` and `y` point to the same singleton object (`None`). Hence `x is not y` is `False`.

---

### **Edge Case: Comparing Non-Singleton with `is not`**

```python
x = [1, 2, 3]
y = None

print(x is not y)  # Output: True
```

Explanation:

- Here, the list object `x` is a different memory location than `None`, so `x is not y` returns `True`.

---

### **Example with Boolean Singleton Optimization**

```python
a = True
b = False

print(a is not b)  # Output: True
```

Explanation:

- `True` and `False` are singleton objects with unique memory locations. They are distinct objects, so `is not` returns `True`.

---

### **Using `is not` for Logical Checks**

You can use `is not` in conditionals to verify logical states.

#### Example: Logical Flow

```python
value = [1, 2, 3]

if value is not None:
    print("The value is not None")
else:
    print("The value is None")
```

Explanation:

- Here, `is not` is used to ensure that the value is not `None`.

---

## **Comparison: `is` vs `is not`**

| **Operator** | **Meaning**                                                      | **Syntax Example** | **Returns**                                   |
| ------------ | ---------------------------------------------------------------- | ------------------ | --------------------------------------------- |
| **`is`**     | Checks if two variables point to the **same object in memory**.  | `a is b`           | `True` if the memory locations are the same.  |
| **`is not`** | Checks if two variables point to **different memory locations**. | `a is not b`       | `True` if the memory locations are different. |

---

## **When Should You Use `is not`?**

### **1. Checking for `None`**

`is not None` is more reliable and Pythonic than using `!=` to compare with `None`.

#### Example:

```python
var = None

if var is not None:
    print("Variable is not None")
else:
    print("Variable is None")
```

---

### **2. Debugging**

You can use `is not` to ensure that variables are not accidentally referencing the same memory object.

---

## **Common Mistake**

Using equality (`==`) instead of `is not` can lead to logical errors. **`is not` checks object identity (memory location), while `==` checks value equality.**

#### Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (because their values are equal)
print(a is not b)  # Output: True (because they are stored at different memory addresses)
```

---

## **Summary**

### Key Takeaways:

1. **`is not` checks if two variables do NOT point to the same memory location.**
2. It is commonly used with singleton checks (`None`, `True`, `False`) or logical checks.
3. It is faster and more Pythonic to check for `None` using `is not None`.
4. `is not` is different from `==`, which compares values.

Would you like a deeper dive into any of these use cases or examples? 😊

The **`is`** and **`is not`** operators in Python are used to compare the **identity** of two objects, not their values. Here's an in-depth look:

---

### **1. What Are `is` and `is not`?**

- **`is`**: Returns `True` if two variables refer to the same object in memory (i.e., they have the same identity).
- **`is not`**: Returns `True` if two variables do not refer to the same object in memory.

---

### **2. Syntax**

```python
x is y  # True if x and y refer to the same object
x is not y  # True if x and y do not refer to the same object
```

---

### **3. Identity vs. Equality**

- **Identity (`is`)** checks whether two variables point to the same object in memory.
- **Equality (`==`)** checks whether the values of the two objects are the same.

**Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the values are the same
print(a is b)  # False, because they are different objects in memory

c = a
print(a is c)  # True, because c refers to the same object as a
```

---

### **4. Where `is` is Commonly Used**

The **`is`** operator is often used to compare with **singleton objects** like `None`, `True`, and `False`, because these are unique in memory.

**Example:**

```python
x = None
if x is None:  # Preferred way to check for None
    print("x is None")
```

Using `x == None` is discouraged because it might behave unpredictably with custom objects.

---

### **5. `is not` Usage**

The **`is not`** operator is the opposite of `is`. It checks whether two objects are **not** the same.

**Example:**

```python
y = 10
if y is not None:
    print("y is not None")
```

---

### **6. Mutability and `is`**

The `is` operator behaves differently for mutable and immutable objects due to how Python manages memory.

#### Immutable Objects

For immutable objects like integers, strings, and tuples, Python may reuse objects with the same value to save memory. This is called **object interning**.

**Example:**

```python
a = 256
b = 256
print(a is b)  # True, because integers in the range -5 to 256 are interned

x = "hello"
y = "hello"
print(x is y)  # True, because strings are interned in some cases
```

#### Mutable Objects

For mutable objects like lists and dictionaries, Python always creates a new object, even if the values are the same.

**Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, because they are different objects in memory
```

---

### **7. When to Use `is` and `is not`**

- Use **`is`** when checking for **identity** (e.g., `None`, `True`, `False`).
- Use **`==`** when checking for **equality** of values.
- Be cautious when using **`is`** with mutable objects, as their identity may not align with equality.

---

### **8. Examples in Action**

#### Example 1: Checking Identity

```python
x = [1, 2, 3]
y = x
print(x is y)  # True, because y refers to the same object as x
```

#### Example 2: Singleton Comparison

```python
value = None
if value is None:
    print("Value is None")  # Preferred for None checks
```

#### Example 3: Mutable vs Immutable

```python
# Immutable
a = 10
b = 10
print(a is b)  # True, because small integers are interned

# Mutable
c = [1, 2]
d = [1, 2]
print(c is d)  # False, because they are separate objects
```

---

### **Key Points**

- **`is`** checks **identity**, not value.
- Prefer **`is`** for `None`, `True`, or `False` checks.
- Understand Python's object interning rules for immutable objects like small integers and strings.
- For value comparison, use **`==`**, not **`is`**.

Let me know if you'd like to explore specific use cases!

In Python, **identity**, **equality**, and the absence of equality (**not equality**) are distinct concepts used to compare objects. Here’s an in-depth explanation of each:

---

## **1. Identity**

**Identity** checks if two objects are the **same object in memory**. The **`is`** and **`is not`** operators are used for identity comparison.

### Key Points:

- **Identity** is determined by an object's **memory address**.
- The **`id()` function** returns the memory address of an object.

### Syntax:

```python
x is y       # True if x and y are the same object
x is not y   # True if x and y are not the same object
```

### Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, b refers to the same object as a
print(a is c)  # False, a and c have the same value but are different objects
print(id(a), id(b), id(c))  # id(a) and id(b) are the same, id(c) is different
```

---

## **2. Equality**

**Equality** checks if two objects have the **same value**, regardless of whether they are the same object in memory. The **`==`** operator is used for equality comparison.

### Key Points:

- Two objects can have the same value but be stored at different memory locations.
- Custom objects can define equality by implementing the `__eq__` method.

### Syntax:

```python
x == y   # True if x and y have the same value
```

### Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, a and b have the same value
print(a is b)  # False, a and b are different objects
```

---

## **3. Not Equality**

**Not equality** checks if two objects do **not** have the same value. The **`!=`** operator is used for this comparison.

### Syntax:

```python
x != y   # True if x and y do not have the same value
```

### Example:

```python
a = [1, 2, 3]
b = [4, 5, 6]

print(a != b)  # True, because a and b have different values
```

---

### **Comparison Summary**

| Comparison Type  | Operator | Purpose                                                       |
| ---------------- | -------- | ------------------------------------------------------------- |
| **Identity**     | `is`     | Checks if two variables point to the same object in memory.   |
| **Identity**     | `is not` | Checks if two variables point to different objects in memory. |
| **Equality**     | `==`     | Checks if two variables have the same value.                  |
| **Not Equality** | `!=`     | Checks if two variables do not have the same value.           |

---

### **4. Combining Identity and Equality**

Objects that are identical (`is`) are always equal (`==`), but objects that are equal (`==`) may not always be identical (`is`).

#### Example:

```python
# Immutable object example
x = 42
y = 42

print(x == y)  # True, same value
print(x is y)  # True, Python interns small integers, so they are the same object

# Mutable object example
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, same value
print(a is b)  # False, different objects
```

---

### **5. Customizing Equality with `__eq__`**

You can define how equality (`==`) works for custom objects by implementing the `__eq__` method.

#### Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True, because values are equal
print(p1 is p2)  # False, because they are different objects
```

---

### **6. Best Practices**

1. Use **`is`** and **`is not`** only for identity checks, particularly with singletons like `None`:
   ```python
   if x is None:  # Preferred way to check for None
       pass
   ```
2. Use **`==`** and **`!=`** for value comparison.
3. Avoid using **`is`** for equality checks—it may produce unexpected results with mutable objects.

---

Let me know if you’d like examples or clarifications on specific scenarios!
