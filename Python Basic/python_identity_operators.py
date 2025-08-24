print("--- Python Identity Operators ---")
print("---------------------------------\n")

# Identity operators (`is` and `is not`) are used to check if two variables
# refer to the *same object* in memory, not just if they have the same value.
# This is a crucial distinction from the equality operator (`==`).

# 1. `is` Operator
print("1. `is` Operator:")
# Returns True if both operands refer to the same object in memory.
# Returns False otherwise.

# --- Examples with Immutable Objects (Numbers, Strings, Tuples) ---
# Python often "interns" (reuses memory for) small integers and short strings
# to optimize memory usage. This can sometimes make `is` behave like `==` for these types,
# but it's an implementation detail and not guaranteed for all values/strings.

a = 10
b = 10
c = 257 # Larger integer, often not interned
d = 257

str1 = "hello"
str2 = "hello"
str3 = "this is a longer string for demonstration"
str4 = "this is a longer string for demonstration"

tuple1 = (1, 2)
tuple2 = (1, 2)

print(f"Integers: a={a}, b={b}, c={c}, d={d}")
print(f"  {a} is {b}: {a is b}")     # True (often interned)
print(f"  {c} is {d}: {c is d}\n")   # False (usually not interned for larger values)

print(f"Strings: str1='{str1}', str2='{str2}'")
print(f"  '{str1}' is '{str2}': {str1 is str2}")     # True (often interned for short strings)
print(f"Strings: str3='{str3}', str4='{str4}'")
print(f"  '{str3}' is '{str4}': {str3 is str4}\n")   # False (usually not interned for longer strings)

print(f"Tuples: tuple1={tuple1}, tuple2={tuple2}")
print(f"  {tuple1} is {tuple2}: {tuple1 is tuple2}\n") # False (tuples are immutable, but usually distinct objects unless identical literal)


# --- Examples with Mutable Objects (Lists, Dictionaries, Sets) ---
# Mutable objects are almost always distinct objects in memory unless
# explicitly assigned to refer to the same object.

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 now refers to the *same object* as list1

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}

print(f"Lists: list1={list1}, list2={list2}, list3=list1")
print(f"  list1 is list2: {list1 is list2}")   # False (different objects, same value)
print(f"  list1 is list3: {list1 is list3}\n") # True (same object)

print(f"Dictionaries: dict1={dict1}, dict2={dict2}")
print(f"  dict1 is dict2: {dict1 is dict2}\n") # False


# --- Special Case: `None` ---
# There is only one instance of `None` in Python.
# Therefore, `is` should always be used to check for `None`.
val1 = None
val2 = None
val3 = 0 # Not None

print(f"None: val1={val1}, val2={val2}, val3={val3}")
print(f"  val1 is val2: {val1 is val2}") # True
print(f"  val1 is None: {val1 is None}") # True (this is the idiomatic way to check for None)
print(f"  val1 == None: {val1 == None}") # True (works, but 'is' is preferred)
print(f"  val1 is val3: {val1 is val3}\n") # False


# 2. `is not` Operator
print("2. `is not` Operator:")
# Returns True if both operands do NOT refer to the same object in memory.
# Returns False otherwise.
# It is simply the inverse of `is`.

print(f"  list1 is not list2: {list1 is not list2}") # True
print(f"  list1 is not list3: {list1 is not list3}") # False
print(f"  val1 is not val3: {val1 is not val3}\n") # True


# --- Practical Use Cases and Important Considerations ---
print("--- Practical Use Cases and Considerations ---\n")

# Use Case 1: Checking for `None`
# This is the most common and recommended use of identity operators.
# It's more robust and sometimes faster than `== None`.
result=input("Your function is ").lower().stript()

if result is None:
    print("Function returned None.\n")
else:
    print(f"Function returned: {result}\n")

# Use Case 2: Optimizing Comparisons for Known Singletons
# `True`, `False`, `None` are singletons.
# `is` is appropriate for comparison with these.
# Example:
is_active = True
if is_active is True: # Preferred over `is_active == True`
    print("Flag is explicitly True.\n")


# Use Case 3: Detecting Aliasing (Multiple variables pointing to the same object)
# Crucial when dealing with mutable data structures to understand side effects.
data_original = [10, 20, 30]
data_alias = data_original # data_alias is an alias for data_original
data_copy = list(data_original) # Creates a shallow copy (new object)

print(f"data_original: {data_original}")
print(f"data_alias: {data_alias}")
print(f"data_copy: {data_copy}\n")

print(f"data_original is data_alias: {data_original is data_alias}") # True
print(f"data_original is data_copy: {data_original is data_copy}\n") # False

# Modifying through alias affects the original
data_alias.append(40)
print(f"After data_alias.append(40):")
print(f"  data_original: {data_original}")
print(f"  data_alias: {data_alias}")
print(f"  data_copy: {data_copy}\n")


# Use Case 4: Caching or Memoization (Advanced)
# In some caching scenarios, you might check if an input object is
# identical to a previously cached one to avoid recomputing.

# CAUTION: Do NOT rely on `is` for value comparison of numbers or strings
# beyond the small integer/short string range, or for any general objects,
# unless you specifically need to check for object identity.
# Always use `==` for value comparison unless you *know* you need `is`.

print("--- End of Python Identity Operators Demonstration ---")

# Placeholder for a function that might return None
def some_function_that_might_return_none():
    import random
    if random.random() > 0.5:
        return "Some actual value"
    else:
        return None