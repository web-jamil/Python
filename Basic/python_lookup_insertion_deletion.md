### **Lookup, Insertion, and Deletion: Comprehensive Overview**

In Python, the performance of **lookup**, **insertion**, and **deletion** operations depends on the data structure being used. Below is a breakdown for common data structures like lists, dictionaries, sets, and tuples.

---

## **1. Lookup (Accessing Elements)**

### **1.1 Lists**

- **Time Complexity**:
  - **Access by index**: \( O(1) \)
  - **Search by value**: \( O(n) \) (linear search)
- **Example**:

```python
# Access by index
my_list = [10, 20, 30]
print(my_list[1])  # Output: 20

# Search by value
if 20 in my_list:
    print("Found!")  # Output: Found!
```

### **1.2 Dictionaries**

- **Time Complexity**:
  - Average: \( O(1) \) (hashing)
  - Worst case: \( O(n) \) (hash collision)
- **Example**:

```python
# Lookup by key
my_dict = {'a': 1, 'b': 2}
print(my_dict['a'])  # Output: 1
```

### **1.3 Sets**

- **Time Complexity**:
  - Average: \( O(1) \)
  - Worst case: \( O(n) \)
- **Example**:

```python
# Check membership
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True
```

### **1.4 Tuples**

- **Time Complexity**:
  - Access by index: \( O(1) \)
  - Search by value: \( O(n) \)
- **Example**:

```python
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20
```

---

## **2. Insertion**

### **2.1 Lists**

- **Time Complexity**:
  - Append: \( O(1) \) (average case, amortized)
  - Insert at index: \( O(n) \) (shifting elements)
- **Example**:

```python
# Append
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

# Insert
my_list.insert(1, 5)  # [1, 5, 2, 3, 4]
```

### **2.2 Dictionaries**

- **Time Complexity**:
  - Average: \( O(1) \)
  - Worst case: \( O(n) \) (rehashing)
- **Example**:

```python
my_dict = {'a': 1}
my_dict['b'] = 2  # {'a': 1, 'b': 2}
```

### **2.3 Sets**

- **Time Complexity**:
  - Average: \( O(1) \)
  - Worst case: \( O(n) \)
- **Example**:

```python
my_set = {1, 2}
my_set.add(3)  # {1, 2, 3}
```

### **2.4 Tuples**

- **Time Complexity**:
  - Tuples are **immutable**, so elements cannot be directly inserted.
- **Workaround**:

```python
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)  # (1, 2, 3, 4)
```

---

## **3. Deletion**

### **3.1 Lists**

- **Time Complexity**:
  - Remove by value: \( O(n) \)
  - Remove by index: \( O(n) \) (shifting elements)
- **Example**:

```python
my_list = [1, 2, 3]
my_list.remove(2)  # [1, 3]

# Remove by index
del my_list[1]  # [1]
```

### **3.2 Dictionaries**

- **Time Complexity**:
  - Average: \( O(1) \)
  - Worst case: \( O(n) \)
- **Example**:

```python
my_dict = {'a': 1, 'b': 2}
del my_dict['a']  # {'b': 2}
```

### **3.3 Sets**

- **Time Complexity**:
  - Average: \( O(1) \)
  - Worst case: \( O(n) \)
- **Example**:

```python
my_set = {1, 2, 3}
my_set.remove(2)  # {1, 3}
```

### **3.4 Tuples**

- **Time Complexity**:
  - Tuples are **immutable**, so elements cannot be directly deleted.
- **Workaround**:

```python
my_tuple = (1, 2, 3)
new_tuple = my_tuple[:1] + my_tuple[2:]  # (1, 3)
```

---

## **Summary of Time Complexities**

| Data Structure | Lookup                                   | Insertion                                | Deletion                 |
| -------------- | ---------------------------------------- | ---------------------------------------- | ------------------------ |
| **List**       | \( O(1) \) (index), \( O(n) \) (search)  | \( O(1) \) (append), \( O(n) \) (insert) | \( O(n) \)               |
| **Dictionary** | \( O(1) \) (average), \( O(n) \) (worst) | \( O(1) \)                               | \( O(1) \)               |
| **Set**        | \( O(1) \) (average), \( O(n) \) (worst) | \( O(1) \)                               | \( O(1) \)               |
| **Tuple**      | \( O(1) \) (index), \( O(n) \) (search)  | Not possible (immutable)                 | Not possible (immutable) |

---

## **Practical Notes**

1. **Dictionaries and Sets**:

   - Best for scenarios requiring fast lookup, insertion, and deletion.
   - Use **keys** in dictionaries to store unique identifiers.

2. **Lists**:

   - Ideal for ordered collections and scenarios where elements need to be accessed by index or traversed sequentially.
   - Avoid frequent insertions or deletions in large lists.

3. **Tuples**:
   - Useful for fixed, immutable sequences of data, such as function return values or constant datasets.

By selecting the right data structure for your use case, you can significantly improve the efficiency of your Python programs.

In Python, lookup, insertion, and deletion are fundamental operations for data structures like **lists**, **dictionaries**, and **sets**. Each of these operations has different behaviors and efficiencies depending on the data structure in use. Here's a detailed look at these operations for different Python data structures:

---

### **1. Lookup Operations**

#### **Lists**

- **Lookup by index**: Lists in Python allow for fast lookup of elements by their index. The operation is **O(1)**, meaning it takes constant time regardless of the list size.

  ```python
  my_list = [10, 20, 30]
  print(my_list[1])  # Output: 20
  ```

- **Lookup by value**: Searching for an element by its value requires scanning through the list, so this operation is **O(n)**, where `n` is the number of elements in the list.

  ```python
  my_list = [10, 20, 30]
  print(20 in my_list)  # Output: True
  ```

#### **Dictionaries**

- **Lookup by key**: Dictionaries provide fast lookups by key with an average time complexity of **O(1)**, thanks to the underlying hash table mechanism.

  ```python
  my_dict = {'name': 'Alice', 'age': 25}
  print(my_dict['name'])  # Output: Alice
  ```

  If the key does not exist, it raises a `KeyError` unless handled with the `get()` method.

  ```python
  print(my_dict.get('gender', 'Not Found'))  # Output: Not Found
  ```

#### **Sets**

- **Lookup by value**: Similar to dictionaries, sets also offer **O(1)** time complexity for lookups, as they are implemented using hash tables.

  ```python
  my_set = {1, 2, 3}
  print(2 in my_set)  # Output: True
  ```

---

### **2. Insertion Operations**

#### **Lists**

- **Appending an element**: Inserting an element at the end of a list is **O(1)** on average, but can be **O(n)** if resizing is required (for very large lists).

  ```python
  my_list = [10, 20]
  my_list.append(30)
  print(my_list)  # Output: [10, 20, 30]
  ```

- **Inserting at a specific index**: Inserting an element at a specific position requires shifting all elements after that index, making it an **O(n)** operation.

  ```python
  my_list = [10, 20, 30]
  my_list.insert(1, 15)  # Insert 15 at index 1
  print(my_list)  # Output: [10, 15, 20, 30]
  ```

#### **Dictionaries**

- **Inserting a key-value pair**: Insertion into a dictionary is **O(1)** on average, as dictionaries use a hash table.

  ```python
  my_dict = {'name': 'Alice'}
  my_dict['age'] = 25
  print(my_dict)  # Output: {'name': 'Alice', 'age': 25}
  ```

  You can also use the `update()` method to insert multiple key-value pairs.

  ```python
  my_dict.update({'gender': 'Female', 'city': 'New York'})
  print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female', 'city': 'New York'}
  ```

#### **Sets**

- **Adding an element**: Inserting an element into a set is **O(1)** on average, as it uses a hash table.

  ```python
  my_set = {1, 2}
  my_set.add(3)
  print(my_set)  # Output: {1, 2, 3}
  ```

  If the element already exists, the set will not add it again (sets don't allow duplicates).

  ```python
  my_set.add(2)
  print(my_set)  # Output: {1, 2, 3} (no change)
  ```

---

### **3. Deletion Operations**

#### **Lists**

- **Deleting by index**: You can remove an element by its index using `del`, which is **O(n)** since it may require shifting elements.

  ```python
  my_list = [10, 20, 30]
  del my_list[1]  # Remove element at index 1
  print(my_list)  # Output: [10, 30]
  ```

- **Removing by value**: The `remove()` method removes the first occurrence of a value. It is an **O(n)** operation, as it requires a linear scan to find the value.

  ```python
  my_list = [10, 20, 20, 30]
  my_list.remove(20)
  print(my_list)  # Output: [10, 20, 30]
  ```

  If the value is not found, it raises a `ValueError`.

- **Popping the last element**: The `pop()` method removes and returns the last item in a list, and it is an **O(1)** operation.

  ```python
  my_list = [10, 20, 30]
  last_item = my_list.pop()
  print(last_item)  # Output: 30
  print(my_list)    # Output: [10, 20]
  ```

#### **Dictionaries**

- **Deleting by key**: You can delete a key-value pair using `del`, which is **O(1)** on average.

  ```python
  my_dict = {'name': 'Alice', 'age': 25}
  del my_dict['age']
  print(my_dict)  # Output: {'name': 'Alice'}
  ```

  If the key does not exist, it raises a `KeyError`.

- **Using `pop()`**: You can also use the `pop()` method, which removes the specified key and returns its value.

  ```python
  my_dict = {'name': 'Alice', 'age': 25}
  age = my_dict.pop('age')
  print(age)  # Output: 25
  print(my_dict)  # Output: {'name': 'Alice'}
  ```

- **Clear all items**: The `clear()` method removes all items from a dictionary.

  ```python
  my_dict.clear()
  print(my_dict)  # Output: {}
  ```

#### **Sets**

- **Removing an element**: You can remove an element using the `remove()` method. It raises a `KeyError` if the element does not exist.

  ```python
  my_set = {1, 2, 3}
  my_set.remove(2)
  print(my_set)  # Output: {1, 3}
  ```

- **Using `discard()`**: Similar to `remove()`, but it does not raise an error if the element is not found.

  ```python
  my_set = {1, 2, 3}
  my_set.discard(4)  # No error if 4 is not found
  print(my_set)  # Output: {1, 2, 3}
  ```

- **Pop a random element**: The `pop()` method removes and returns an arbitrary element from the set. This is an **O(1)** operation.

  ```python
  my_set = {1, 2, 3}
  item = my_set.pop()
  print(item)  # Output: 1 (or any random item)
  print(my_set)  # Output: {2, 3}
  ```

- **Clear all items**: The `clear()` method removes all items from the set.

  ```python
  my_set.clear()
  print(my_set)  # Output: set()
  ```

---

### **Efficiency Comparison**

| Operation             | List | Dictionary | Set  |
| --------------------- | ---- | ---------- | ---- |
| Lookup by index       | O(1) | O(1)       | O(1) |
| Lookup by value       | O(n) | O(1)       | O(1) |
| Insertion at end      | O(1) | O(1)       | O(1) |
| Insertion at index    | O(n) | O(1)       | O(1) |
| Deletion by value     | O(n) | O(1)       | O(1) |
| Deletion by key       | O(n) | O(1)       | O(1) |
| Delete last element   | O(1) | O(1)       | O(1) |
| Remove random element | O(1) | O(1)       | O(1) |

---

### **Summary**

- **Lookup**: Lists are good for indexed lookup, while dictionaries and sets are highly efficient for lookup operations.
- **Insertion**: Lists perform well with appending elements but become slower for insertions at arbitrary positions. Dictionaries and sets offer efficient insertions.
- **Deletion**: Lists are less efficient for arbitrary deletions but work well for removing elements from the end. Dictionaries and sets provide efficient deletion, with dictionaries supporting key-based deletion and sets supporting element removal.

By choosing the appropriate data structure based on these operations, you can optimize the performance of your Python programs.

### Lookup, Insertion, and Deletion in Python

In Python, operations like **lookup**, **insertion**, and **deletion** are fundamental when dealing with data structures such as **lists**, **dictionaries**, **sets**, and **tuples**. These operations vary depending on the data structure. Below, we will explore these operations in the context of the most common Python data structures: **lists**, **dictionaries**, **sets**, and **tuples**.

---

### **1. Lookup Operations**

**Lookup** refers to accessing or retrieving an element from a data structure.

#### **a. Lists**

To look up an element in a list, you use indexing:

```python
my_list = [10, 20, 30, 40]
# Accessing elements using indexing
print(my_list[2])  # Output: 30 (element at index 2)
```

If you want to check if a value exists in the list, you can use the `in` operator:

```python
print(20 in my_list)  # Output: True
print(50 in my_list)  # Output: False
```

#### **b. Dictionaries**

In dictionaries, lookup is done using keys.

```python
my_dict = {'name': 'Alice', 'age': 25}
# Accessing value by key
print(my_dict['name'])  # Output: Alice
```

If the key doesn't exist, a `KeyError` will be raised. To avoid this, you can use the `get()` method:

```python
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('city', 'Not Found'))  # Output: Not Found (default value if key doesn't exist)
```

#### **c. Sets**

For sets, you can check if an element exists using the `in` operator:

```python
my_set = {10, 20, 30}
print(20 in my_set)  # Output: True
print(40 in my_set)  # Output: False
```

#### **d. Tuples**

In tuples, you can look up elements using indexing (since tuples are immutable sequences).

```python
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])  # Output: 20
```

You can also check for the existence of an element using the `in` operator:

```python
print(20 in my_tuple)  # Output: True
print(50 in my_tuple)  # Output: False
```

---

### **2. Insertion Operations**

**Insertion** refers to adding elements to a data structure.

#### **a. Lists**

Lists in Python are mutable, so elements can be added in several ways:

- **append()**: Adds an element at the end of the list.

```python
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # Output: [10, 20, 30, 40]
```

- **insert()**: Inserts an element at a specific index.

```python
my_list.insert(1, 15)  # Inserts 15 at index 1
print(my_list)  # Output: [10, 15, 20, 30, 40]
```

- **extend()**: Adds all elements from another iterable to the end of the list.

```python
my_list.extend([50, 60])
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
```

#### **b. Dictionaries**

Dictionaries allow insertion by adding key-value pairs.

```python
my_dict = {'name': 'Alice'}
# Adding or updating a key-value pair
my_dict['age'] = 25
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}
```

You can also insert using the `update()` method to add multiple key-value pairs.

```python
my_dict.update({'city': 'New York', 'job': 'Engineer'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
```

#### **c. Sets**

Sets are unordered collections, and you can add an element using the `add()` method.

```python
my_set = {10, 20, 30}
my_set.add(40)
print(my_set)  # Output: {40, 10, 20, 30} (unordered)
```

To add multiple elements, use the `update()` method.

```python
my_set.update([50, 60])
print(my_set)  # Output: {40, 10, 20, 30, 50, 60} (unordered)
```

#### **d. Tuples**

Tuples are immutable, so you cannot insert elements into an existing tuple. However, you can concatenate tuples to create a new one.

```python
my_tuple = (10, 20, 30)
new_tuple = my_tuple + (40,)
print(new_tuple)  # Output: (10, 20, 30, 40)
```

---

### **3. Deletion Operations**

**Deletion** refers to removing elements from a data structure.

#### **a. Lists**

You can delete elements from lists using several methods:

- **remove()**: Removes the first occurrence of an element.

```python
my_list = [10, 20, 30, 20]
my_list.remove(20)
print(my_list)  # Output: [10, 30, 20]
```

- **pop()**: Removes and returns the element at the specified index. If no index is provided, it removes the last item.

```python
my_list = [10, 20, 30]
removed_element = my_list.pop(1)  # Removes the element at index 1
print(removed_element)  # Output: 20
print(my_list)  # Output: [10, 30]
```

- **del**: Removes an element by index or deletes the entire list.

```python
del my_list[0]  # Removes the element at index 0
print(my_list)  # Output: [30]

# Deleting the entire list
del my_list
# print(my_list)  # This will raise a NameError since the list is deleted
```

- **clear()**: Removes all items from the list.

```python
my_list = [10, 20, 30]
my_list.clear()
print(my_list)  # Output: []
```

#### **b. Dictionaries**

You can remove key-value pairs from a dictionary:

- **pop()**: Removes and returns the value for the given key.

```python
my_dict = {'name': 'Alice', 'age': 25}
value = my_dict.pop('age')
print(value)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}
```

- **del**: Deletes a key-value pair by key.

```python
del my_dict['name']
print(my_dict)  # Output: {}
```

- **clear()**: Removes all key-value pairs.

```python
my_dict.clear()
print(my_dict)  # Output: {}
```

#### **c. Sets**

You can delete elements from sets:

- **remove()**: Removes an element. If the element is not present, it raises a `KeyError`.

```python
my_set = {10, 20, 30}
my_set.remove(20)
print(my_set)  # Output: {10, 30}
```

- **discard()**: Removes an element but does not raise an error if the element is not found.

```python
my_set.discard(30)
print(my_set)  # Output: {10}
```

- **pop()**: Removes and returns an arbitrary element (since sets are unordered).

```python
my_set = {10, 20, 30}
removed_element = my_set.pop()
print(removed_element)  # Output: an arbitrary element
print(my_set)  # The set after removal
```

- **clear()**: Removes all elements from the set.

```python
my_set.clear()
print(my_set)  # Output: set()
```

#### **d. Tuples**

Since tuples are immutable, you cannot delete elements from them directly. However, you can create a new tuple by excluding the element you want to delete.

```python
my_tuple = (10, 20, 30)
new_tuple = my_tuple[:1] + my_tuple[2:]  # Exclude the element at index 1
print(new_tuple)  # Output: (10, 30)
```

---

### **Summary Table**

| Operation  | Lists                                 | Dictionaries              | Sets                                        | Tuples            |
| ---------- | ------------------------------------- | ------------------------- | ------------------------------------------- | ----------------- |
| **Lookup** | `my_list[index]`                      | `my_dict[key]`            | `key in my_set`                             | `my_tuple[index]` |
| **Insert** | `append()`, `insert()`, `extend()`    | `my_dict[key] = value`    | `add()`, `update()`                         | Concatenate       |
| **Delete** | `remove()`, `pop()`, `del`, `clear()` | `pop()`, `del`, `clear()` | `remove()`, `discard()`, `pop()`, `clear()` | N/A (Immutable)   |

---

By understanding and utilizing these operations, you can efficiently manage and manipulate various types of data structures in Python.

In Python, **lookup**, **insertion**, and **deletion** are common operations performed on data structures like **lists**, **dictionaries**, **sets**, and **tuples**. These operations vary slightly based on the type of data structure, but they all serve essential roles in managing and modifying data.

Let’s break down these operations for **lists**, **dictionaries**, **sets**, and **tuples**.

---

### **1. Lookup Operation**

#### **In Lists:**

- **Lookup by Index**: You can access an element in a list using its index. Python lists are zero-indexed, meaning the first element has index 0.

```python
my_list = [10, 20, 30, 40]
print(my_list[2])  # Output: 30 (indexing)
print(my_list[-1])  # Output: 40 (negative indexing, last element)
```

- **Check if an Element Exists**: You can check if an element exists in a list using the `in` keyword.

```python
my_list = [10, 20, 30, 40]
print(20 in my_list)  # Output: True
print(50 in my_list)  # Output: False
```

#### **In Dictionaries:**

- **Lookup by Key**: You access dictionary values by their associated keys.

```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Alice
```

- **Using the `get()` Method**: The `get()` method is another way to retrieve the value for a key. It returns `None` if the key is not found, instead of raising an error.

```python
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country"))  # Output: None
```

#### **In Sets:**

- **Lookup if Element Exists**: Similar to lists, you can check for the existence of an element using the `in` keyword.

```python
my_set = {10, 20, 30}
print(20 in my_set)  # Output: True
print(40 in my_set)  # Output: False
```

#### **In Tuples:**

- **Lookup by Index**: Like lists, tuples allow lookup by index.

```python
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20
```

- **Check if an Element Exists**: You can use `in` to check for membership in a tuple.

```python
print(20 in my_tuple)  # Output: True
print(40 in my_tuple)  # Output: False
```

---

### **2. Insertion Operation**

#### **In Lists:**

- **Append**: The `append()` method adds an element to the end of the list.

```python
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # Output: [10, 20, 30, 40]
```

- **Insert**: The `insert()` method allows you to insert an element at a specific index.

```python
my_list = [10, 20, 30]
my_list.insert(1, 15)  # Insert 15 at index 1
print(my_list)  # Output: [10, 15, 20, 30]
```

- **Extend**: The `extend()` method adds all elements from an iterable to the list.

```python
my_list = [10, 20, 30]
my_list.extend([40, 50])
print(my_list)  # Output: [10, 20, 30, 40, 50]
```

#### **In Dictionaries:**

- **Insert a New Key-Value Pair**: You can insert new key-value pairs directly by assigning a value to a new key.

```python
my_dict = {"name": "Alice"}
my_dict["age"] = 25  # Insertion of a new key-value pair
print(my_dict)  # Output: {"name": "Alice", "age": 25}
```

- **Using `update()`**: The `update()` method is used to insert key-value pairs from another dictionary or iterable.

```python
my_dict.update({"city": "New York"})
print(my_dict)  # Output: {"name": "Alice", "age": 25, "city": "New York"}
```

#### **In Sets:**

- **Add**: You can insert a new element into a set using the `add()` method.

```python
my_set = {10, 20, 30}
my_set.add(40)
print(my_set)  # Output: {10, 20, 30, 40}
```

#### **In Tuples:**

- **Tuples are Immutable**: You cannot insert elements into a tuple directly. However, you can create a new tuple by concatenating the original tuple with another one.

```python
my_tuple = (10, 20, 30)
new_tuple = my_tuple + (40,)
print(new_tuple)  # Output: (10, 20, 30, 40)
```

---

### **3. Deletion Operation**

#### **In Lists:**

- **Remove by Value**: The `remove()` method removes the first occurrence of a specified value. If the value does not exist, it raises a `ValueError`.

```python
my_list = [10, 20, 30, 20]
my_list.remove(20)  # Removes the first 20
print(my_list)  # Output: [10, 30, 20]
```

- **Pop by Index**: The `pop()` method removes and returns an element at a specific index. If no index is provided, it removes the last item.

```python
my_list = [10, 20, 30]
last_item = my_list.pop()
print(last_item)  # Output: 30
print(my_list)    # Output: [10, 20]
```

- **Delete by Index**: The `del` statement can be used to delete an item by index or even delete the entire list.

```python
my_list = [10, 20, 30]
del my_list[1]  # Removes the element at index 1
print(my_list)  # Output: [10, 30]
```

- **Clear**: The `clear()` method removes all elements from the list.

```python
my_list = [10, 20, 30]
my_list.clear()
print(my_list)  # Output: []
```

#### **In Dictionaries:**

- **Remove by Key**: You can delete a key-value pair using the `del` statement.

```python
my_dict = {"name": "Alice", "age": 25}
del my_dict["age"]
print(my_dict)  # Output: {"name": "Alice"}
```

- **Pop by Key**: The `pop()` method removes and returns the value for a given key.

```python
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")
print(age)  # Output: 25
print(my_dict)  # Output: {"name": "Alice"}
```

- **Clear**: The `clear()` method removes all key-value pairs from the dictionary.

```python
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()
print(my_dict)  # Output: {}
```

#### **In Sets:**

- **Remove by Value**: The `remove()` method removes an element from the set. It raises a `KeyError` if the element is not found.

```python
my_set = {10, 20, 30}
my_set.remove(20)
print(my_set)  # Output: {10, 30}
```

- **Discard**: The `discard()` method removes an element, but it does not raise an error if the element is not present.

```python
my_set = {10, 20, 30}
my_set.discard(40)  # Does nothing since 40 is not in the set
print(my_set)  # Output: {10, 20, 30}
```

- **Pop**: The `pop()` method removes and returns an arbitrary element from the set.

```python
my_set = {10, 20, 30}
popped = my_set.pop()
print(popped)  # Output: Arbitrary element (could be 10, 20, or 30)
print(my_set)
```

- **Clear**: The `clear()` method removes all elements from the set.

```python
my_set = {10, 20, 30}
my_set.clear()
print(my_set)  # Output: set()
```

#### **In Tuples:**

- **Tuples are Immutable**: You cannot delete elements from a tuple directly. However, you can create a new tuple by omitting the elements you want to remove.

```python
my_tuple = (10, 20, 30)
new_tuple = my_tuple[:1] + my_tuple[2:]  # Remove element at index 1
print(new_tuple)  # Output: (10, 30)
```

---

### **Summary**

- **Lookup**: Retrieve elements from a list, dictionary, set, or tuple using indexing or keys.
- **Insertion**: Add elements to a list, dictionary, set, or tuple (although tuples are immutable, so you must create a new one).
- **Deletion**: Remove elements using `remove()`, `pop()`, or `del` for lists and dictionaries. Sets also use `discard()` and `remove()`. Tuples are immutable, so deletion is not directly possible.

These operations are fundamental for working with Python’s built-in data structures and play a critical role in efficiently managing and modifying data.

Let’s dive deeper into **lookup**, **insertion**, and **deletion** for Python’s data structures—**lists**, **dictionaries**, **sets**, and **tuples**—with more nuanced examples and scenarios. We'll include explanations of efficiency, common pitfalls, and advanced usage.

---

## **1. Lookup Operations**

### **Lists**

1. **Indexing**

   - Direct lookup by index (`O(1)` operation).
   - Negative indexing starts from the end of the list.

   ```python
   my_list = [10, 20, 30, 40]
   print(my_list[1])    # Output: 20
   print(my_list[-2])   # Output: 30
   ```

2. **Membership Check**

   - Uses the `in` keyword to check existence (`O(n)` operation as it may scan the entire list).

   ```python
   print(20 in my_list)  # Output: True
   print(50 in my_list)  # Output: False
   ```

3. **Find Index**

   - The `index()` method returns the first occurrence of the value.
   - Raises `ValueError` if the value does not exist.

   ```python
   print(my_list.index(30))  # Output: 2
   ```

---

### **Dictionaries**

1. **Key Lookup**

   - Direct lookup using the key (`O(1)` operation for average case).

   ```python
   my_dict = {"name": "Alice", "age": 25}
   print(my_dict["name"])  # Output: Alice
   ```

2. **Safe Key Lookup**

   - Use `get()` to avoid `KeyError` for missing keys.

   ```python
   print(my_dict.get("city", "Not Found"))  # Output: Not Found
   ```

3. **Iterating Keys/Values**

   - Efficient way to loop through keys, values, or both.

   ```python
   for key in my_dict.keys():
       print(key)  # Prints all keys

   for value in my_dict.values():
       print(value)  # Prints all values
   ```

---

### **Sets**

1. **Membership Check**

   - `in` keyword is optimized for sets (`O(1)` operation on average).

   ```python
   my_set = {1, 2, 3}
   print(2 in my_set)  # Output: True
   ```

2. **Advanced Membership**

   - Sets support operations like subset (`<=`), superset (`>=`), and disjoint (`isdisjoint`).

   ```python
   print({1, 2}.issubset(my_set))  # Output: True
   ```

---

### **Tuples**

1. **Indexing**

   - Same as lists but immutable (`O(1)` operation).

   ```python
   my_tuple = (10, 20, 30)
   print(my_tuple[1])  # Output: 20
   ```

2. **Membership**

   - Use `in` for checks (`O(n)` operation).

   ```python
   print(20 in my_tuple)  # Output: True
   ```

---

## **2. Insertion Operations**

### **Lists**

1. **Append**

   - Adds a single element at the end (`O(1)` operation).

   ```python
   my_list.append(50)
   ```

2. **Insert**

   - Inserts at a specific index (`O(n)` operation due to shifting).

   ```python
   my_list.insert(1, 15)
   ```

3. **Extend**

   - Concatenates another iterable to the list (`O(k)` where `k` is the length of the iterable).

   ```python
   my_list.extend([60, 70])
   ```

---

### **Dictionaries**

1. **Direct Insertion**

   - Assigning a value to a key inserts it if the key doesn’t already exist (`O(1)` operation).

   ```python
   my_dict["city"] = "New York"
   ```

2. **Update with Multiple Pairs**

   - Combines `update()` for multiple insertions.

   ```python
   my_dict.update({"country": "USA", "hobby": "reading"})
   ```

---

### **Sets**

1. **Add**

   - Adds a single element to the set (`O(1)` operation).

   ```python
   my_set.add(4)
   ```

2. **Update**

   - Inserts multiple elements from an iterable.

   ```python
   my_set.update([5, 6])
   ```

---

### **Tuples**

- **Immutable**: Create a new tuple for insertion.

  ```python
  new_tuple = my_tuple + (40,)
  ```

---

## **3. Deletion Operations**

### **Lists**

1. **Remove**

   - Removes the first occurrence of a value (`O(n)` operation).

   ```python
   my_list.remove(20)
   ```

2. **Pop**

   - Removes and returns an element by index (`O(n)` for arbitrary index, `O(1)` for the last index).

   ```python
   my_list.pop(1)
   ```

3. **Clear**

   - Empties the entire list.

   ```python
   my_list.clear()
   ```

---

### **Dictionaries**

1. **Delete Key**

   - Removes a key-value pair by key (`O(1)` operation).

   ```python
   del my_dict["age"]
   ```

2. **Pop**

   - Removes a key and returns its value.

   ```python
   my_dict.pop("name")
   ```

3. **Clear**

   - Empties the dictionary.

   ```python
   my_dict.clear()
   ```

---

### **Sets**

1. **Remove**

   - Removes a specific element. Raises `KeyError` if it doesn’t exist.

   ```python
   my_set.remove(2)
   ```

2. **Discard**

   - Removes an element safely (no error if it doesn’t exist).

   ```python
   my_set.discard(10)
   ```

3. **Pop**

   - Removes an arbitrary element.

   ```python
   my_set.pop()
   ```

---

### **Tuples**

- **Immutable**: Use slicing to create a new tuple after deletion.

  ```python
  new_tuple = my_tuple[:1] + my_tuple[2:]
  ```

---

### **Performance Insights**

| Operation | List (`O`)   | Dictionary (`O`) | Set (`O`) | Tuple (`O`) |
| --------- | ------------ | ---------------- | --------- | ----------- |
| Lookup    | `O(n)`       | `O(1)`           | `O(1)`    | `O(n)`      |
| Insertion | `O(1)` (end) | `O(1)`           | `O(1)`    | Immutable   |
| Deletion  | `O(n)`       | `O(1)`           | `O(1)`    | Immutable   |

---

### **Common Pitfalls**

1. **KeyError in Dictionaries**:

   - Always use `get()` when unsure if a key exists.

2. **Out-of-Range Index**:

   - Avoid accessing invalid indices in lists/tuples.

3. **Immutable Tuples**:

   - Use lists for dynamic modifications.

4. **Duplicate Removal in Sets**:

   - Sets automatically discard duplicates.

   ```python
   my_set = {1, 2, 2, 3}  # {1, 2, 3}
   ```

---

This overview provides advanced insights into these operations across all data structures in Python. Let me know if you need more examples or deeper exploration!
