import operator

print("--- Comparison Operators from Python's 'operator' Module ---")
print("----------------------------------------------------------\n")

# Define some operands for comparison
a = 10
b = 20
c = 10
d = 5
s1 = "apple"
s2 = "banana"
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, 2, 4]
n1 = None
n2 = None

print(f"Operands: a={a}, b={b}, c={c}, d={d}, s1='{s1}', s2='{s2}', l1={l1}, l2={l2}, l3={l3}, n1={n1}, n2={n2}\n")


# 1. Less Than: operator.lt(a, b) equivalent to a < b
print("1. Less Than (operator.lt):")
print(f"operator.lt({a}, {b})    -> {operator.lt(a, b)}")    # 10 < 20 -> True
print(f"operator.lt({a}, {c})    -> {operator.lt(a, c)}")    # 10 < 10 -> False
print(f"operator.lt({b}, {d})    -> {operator.lt(b, d)}")    # 20 < 5  -> False
print(f"operator.lt('{s1}', '{s2}') -> {operator.lt(s1, s2)}\n") # 'apple' < 'banana' -> True (lexicographical)


# 2. Less Than or Equal To: operator.le(a, b) equivalent to a <= b
print("2. Less Than or Equal To (operator.le):")
print(f"operator.le({a}, {b})    -> {operator.le(a, b)}")    # 10 <= 20 -> True
print(f"operator.le({a}, {c})    -> {operator.le(a, c)}")    # 10 <= 10 -> True
print(f"operator.le({b}, {d})    -> {operator.le(b, d)}\n")    # 20 <= 5  -> False


# 3. Equal To: operator.eq(a, b) equivalent to a == b
print("3. Equal To (operator.eq):")
print(f"operator.eq({a}, {b})    -> {operator.eq(a, b)}")    # 10 == 20 -> False
print(f"operator.eq({a}, {c})    -> {operator.eq(a, c)}")    # 10 == 10 -> True
print(f"operator.eq({l1}, {l2})  -> {operator.eq(l1, l2)}")  # [1,2,3] == [1,2,3] -> True
print(f"operator.eq({l1}, {l3})  -> {operator.eq(l1, l3)}")  # [1,2,3] == [1,2,4] -> False
print(f"operator.eq({n1}, {n2})  -> {operator.eq(n1, n2)}\n") # None == None -> True


# 4. Not Equal To: operator.ne(a, b) equivalent to a != b
print("4. Not Equal To (operator.ne):")
print(f"operator.ne({a}, {b})    -> {operator.ne(a, b)}")    # 10 != 20 -> True
print(f"operator.ne({a}, {c})    -> {operator.ne(a, c)}")    # 10 != 10 -> False
print(f"operator.ne({l1}, {l3})  -> {operator.ne(l1, l3)}\n")  # [1,2,3] != [1,2,4] -> True


# 5. Greater Than: operator.gt(a, b) equivalent to a > b
print("5. Greater Than (operator.gt):")
print(f"operator.gt({a}, {b})    -> {operator.gt(a, b)}")    # 10 > 20 -> False
print(f"operator.gt({b}, {d})    -> {operator.gt(b, d)}")    # 20 > 5  -> True
print(f"operator.gt({a}, {c})    -> {operator.gt(a, c)}\n")    # 10 > 10 -> False


# 6. Greater Than or Equal To: operator.ge(a, b) equivalent to a >= b
print("6. Greater Than or Equal To (operator.ge):")
print(f"operator.ge({a}, {b})    -> {operator.ge(a, b)}")    # 10 >= 20 -> False
print(f"operator.ge({a}, {c})    -> {operator.ge(a, c)}")    # 10 >= 10 -> True
print(f"operator.ge({b}, {d})    -> {operator.ge(b, d)}\n")    # 20 >= 5  -> True


# --- Practical Use Cases ---
print("--- Practical Use Cases for 'operator' comparison functions ---\n")

# Use Case 1: Sorting with Custom Comparison Logic (often used with `functools.cmp_to_key` for Python 2 style)
# In modern Python 3, `key` arguments with `itemgetter` or `attrgetter` are preferred.
# However, for very custom sorts, `cmp_to_key` can wrap a comparison function.
from functools import cmp_to_key

# Custom comparison for numbers (e.g., sort even numbers before odd numbers)
def custom_num_cmp(x, y):
    if x % 2 == 0 and y % 2 != 0:
        return -1 # x (even) comes before y (odd)
    elif x % 2 != 0 and y % 2 == 0:
        return 1  # x (odd) comes after y (even)
    else:
        # If both are even or both are odd, compare numerically
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Original numbers: {numbers}")
# Use a lambda to map to a tuple for standard sort (preferable usually):
# (is_odd, value) where False (even) < True (odd)
sorted_by_parity = sorted(numbers, key=lambda x: (x % 2 != 0, x))
print(f"Sorted by parity (even first), then value: {sorted_by_parity}\n")


# Use Case 2: Filtering with Comparison Operators
data = [1, 5, 10, 15, 20, 25, 30]

# Filter elements greater than 10 using lambda:
filtered_lambda = list(filter(lambda x: x > 10, data))
print(f"Filtered (lambda > 10): {filtered_lambda}")

# Filter elements greater than 10 using operator.gt and functools.partial:
from functools import partial
is_greater_than_10 = partial(operator.gt, 10) # Checks if 10 > x (reversed logic)
# Correct way for `x > 10`: use `partial(operator.gt, arg2=10)` or a simple lambda
# For this specific case, a direct `lambda x: operator.gt(x, 10)` or `partial(operator.gt, __, 10)` (if using `placeholder`) is better.
# Simpler for filter is usually lambda, but `operator` is for when functions are needed.

# Let's show how `operator.gt` fits directly into filter if you have a source of two iterables:
# Not very common for filter, but for map it is.
# More realistic for filter if you define a check function:
def check_if_greater_than_threshold(threshold, value):
    return operator.gt(value, threshold)

filtered_op = [item for item in data if check_if_greater_than_threshold(10, item)]
print(f"Filtered (operator.gt explicit): {filtered_op}\n")


# Use Case 3: Chained Comparisons with `reduce` (less common but demonstrates power)
# Using `all` or `any` with generator expressions is often more Pythonic.
from functools import reduce

def is_between(value, lower, upper):
    return operator.ge(value, lower) and operator.le(value, upper)

print(f"Is 15 between 10 and 20? {is_between(15, 10, 20)}")
print(f"Is 5 between 10 and 20? {is_between(5, 10, 20)}\n")

# This is highly illustrative, not a recommended pattern for simple 'and' checks.
# For example, checking if all elements in a list are equal:
items_equal = [5, 5, 5, 5]
items_not_equal = [5, 5, 6, 5]

# `reduce` can be used to compare all items:
# Check if all elements are equal to the first element
all_equal_check = all(operator.eq(items_equal[0], x) for x in items_equal)
print(f"Are all items in {items_equal} equal? {all_equal_check}")

all_equal_check_2 = all(operator.eq(items_not_equal[0], x) for x in items_not_equal)
print(f"Are all items in {items_not_equal} equal? {all_equal_check_2}\n")


# Use Case 4: Creating Dynamic Predicates (e.g., for querying data)
print("4. Creating Dynamic Predicates for Querying:")
# Imagine building a query system where comparison logic is chosen at runtime.

def build_filter_predicate(comparison_type, target_value):
    if comparison_type == 'gt':
        return lambda x: operator.gt(x, target_value)
    elif comparison_type == 'lt':
        return lambda x: operator.lt(x, target_value)
    elif comparison_type == 'eq':
        return lambda x: operator.eq(x, target_value)
    # Add more conditions as needed
    else:
        raise ValueError("Unsupported comparison type")

records = [
    {'id': 1, 'score': 85},
    {'id': 2, 'score': 92},
    {'id': 3, 'score': 78},
    {'id': 4, 'score': 92},
    {'id': 5, 'score': 60},
]

# Find records where score > 80
filter_func_gt_80 = build_filter_predicate('gt', 80)
filtered_records_gt = [r for r in records if filter_func_gt_80(r['score'])]
print(f"Records with score > 80: {filtered_records_gt}")

# Find records where score == 92
filter_func_eq_92 = build_filter_predicate('eq', 92)
filtered_records_eq = [r for r in records if filter_func_eq_92(r['score'])]
print(f"Records with score == 92: {filtered_records_eq}\n")


print("--- End of 'operator' Comparison Operators Demonstration ---")