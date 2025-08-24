import operator

print("--- Logical Operators from Python's 'operator' Module ---")
print("-------------------------------------------------------\n")

# Define some boolean and truthy/falsy operands
true_val = True
false_val = False
num_zero = 0
num_non_zero = 5
empty_list = []
non_empty_list = [1, 2]
none_val = None
string_empty = ""
string_non_empty = "hello"

print(f"Operands: true_val={true_val}, false_val={false_val}")
print(f"          num_zero={num_zero}, num_non_zero={num_non_zero}")
print(f"          empty_list={empty_list}, non_empty_list={non_empty_list}")
print(f"          none_val={none_val}, string_empty='{string_empty}', string_non_empty='{string_non_empty}'\n")


# 1. Logical AND: operator.and_(a, b) equivalent to a and b
# Returns the first operand if it's falsy, otherwise returns the second operand.
# This reflects Python's short-circuiting 'and' behavior.
print("1. Logical AND (operator.and_):")
print(f"operator.and_({true_val}, {true_val})   -> {operator.and_(true_val, true_val)}")
print(f"operator.and_({true_val}, {false_val})  -> {operator.and_(true_val, false_val)}")
print(f"operator.and_({false_val}, {true_val})  -> {operator.and_(false_val, true_val)}")
print(f"operator.and_({false_val}, {false_val}) -> {operator.and_(false_val, false_val)}")

print(f"operator.and_({num_non_zero}, {num_zero})    -> {operator.and_(num_non_zero, num_zero)}")      # 0 is falsy
print(f"operator.and_({num_zero}, {num_non_zero})    -> {operator.and_(num_zero, num_non_zero)}")      # 0 is falsy
print(f"operator.and_({non_empty_list}, {string_non_empty}) -> {operator.and_(non_empty_list, string_non_empty)}\n") # non_empty_list is truthy, returns string_non_empty


# 2. Logical OR: operator.or_(a, b) equivalent to a or b
# Returns the first operand if it's truthy, otherwise returns the second operand.
# This reflects Python's short-circuiting 'or' behavior.
print("2. Logical OR (operator.or_):")
print(f"operator.or_({true_val}, {true_val})   -> {operator.or_(true_val, true_val)}")
print(f"operator.or_({true_val}, {false_val})  -> {operator.or_(true_val, false_val)}")
print(f"operator.or_({false_val}, {true_val})  -> {operator.or_(false_val, true_val)}")
print(f"operator.or_({false_val}, {false_val}) -> {operator.or_(false_val, false_val)}")

print(f"operator.or_({num_non_zero}, {num_zero})    -> {operator.or_(num_non_zero, num_zero)}")      # num_non_zero is truthy
print(f"operator.or_({num_zero}, {num_non_zero})    -> {operator.or_(num_zero, num_non_zero)}")      # num_zero is falsy, returns num_non_zero
print(f"operator.or_({empty_list}, {none_val})      -> {operator.or_(empty_list, none_val)}\n")      # empty_list is falsy, returns none_val


# 3. Logical NOT: operator.not_(obj) equivalent to not obj
# Returns True if the operand is falsy, False if it's truthy.
print("3. Logical NOT (operator.not_):")
print(f"operator.not_({true_val})      -> {operator.not_(true_val)}")
print(f"operator.not_({false_val})     -> {operator.not_(false_val)}")
print(f"operator.not_({num_zero})      -> {operator.not_(num_zero)}")
print(f"operator.not_({num_non_zero})  -> {operator.not_(num_non_zero)}")
print(f"operator.not_({empty_list})    -> {operator.not_(empty_list)}")
print(f"operator.not_({non_empty_list}) -> {operator.not_(non_empty_list)}")
print(f"operator.not_({none_val})      -> {operator.not_(none_val)}\n")


# --- Practical Use Cases ---
print("--- Practical Use Cases for 'operator' logical functions ---\n")

# Use Case 1: Combining predicates for filtering
# This is a common scenario where `operator.and_` and `operator.or_` shine.
data = [
    {'name': 'Alice', 'active': True, 'admin': False, 'age': 30},
    {'name': 'Bob', 'active': True, 'admin': True, 'age': 25},
    {'name': 'Charlie', 'active': False, 'admin': False, 'age': 35},
    {'name': 'David', 'active': True, 'admin': False, 'age': 40},
    {'name': 'Eve', 'active': False, 'admin': True, 'age': 28},
]

# Find active admins (active AND admin)
active_admins = list(filter(lambda user: operator.and_(user['active'], user['admin']), data))
print(f"Active Admins: {active_admins}\n")

# Find users who are either active OR admin
active_or_admin = list(filter(lambda user: operator.or_(user['active'], user['admin']), data))
print(f"Active OR Admin: {active_or_admin}\n")

# Find inactive users (NOT active)
inactive_users = list(filter(lambda user: operator.not_(user['active']), data))
print(f"Inactive Users: {inactive_users}\n")

# -------------------------------------------------------------
# You can also combine with `itemgetter` from the operator module
# for more concise filtering when dealing with dictionaries/objects.
from operator import itemgetter

# Get the 'active' and 'admin' status
get_active = itemgetter('active')
get_admin = itemgetter('admin')

active_admins_itemgetter = list(filter(
    lambda user: operator.and_(get_active(user), get_admin(user)), data
))
print(f"Active Admins (using itemgetter and operator.and_): {active_admins_itemgetter}\n")

# -------------------------------------------------------------


# Use Case 2: Dynamic Logic Construction
# Useful when the logical operation itself needs to be determined at runtime.

def create_dynamic_predicate(logic_op_str, key1, key2=None):
    """
    Creates a callable predicate based on a string representing a logical operation.
    For 'not', uses only key1. For 'and'/'or', uses key1 and key2.
    """
    if logic_op_str == 'and':
        return lambda item: operator.and_(item[key1], item[key2])
    elif logic_op_str == 'or':
        return lambda item: operator.or_(item[key1], item[key2])
    elif logic_op_str == 'not':
        return lambda item: operator.not_(item[key1])
    else:
        raise ValueError("Unsupported logical operation")

# Example: Find users who are active AND (age < 30 OR age > 35)
# This requires a bit more nesting of predicates.

# Predicate for (age < 30 OR age > 35)
age_filter_predicate = lambda user: operator.or_(
    operator.lt(user['age'], 30),
    operator.gt(user['age'], 35)
)

# Combine with active status
combined_filter_predicate = lambda user: operator.and_(
    user['active'],
    age_filter_predicate(user)
)

filtered_users = list(filter(combined_filter_predicate, data))
print(f"Users who are active AND (age < 30 OR age > 35): {filtered_users}\n")


# Use Case 3: Chaining conditions with functools.reduce (less common but illustrates)
from functools import reduce

# Check if ALL values in a list of booleans are True
boolean_flags = [True, True, False, True]
all_true_via_reduce = reduce(operator.and_, boolean_flags)
print(f"All flags True (via reduce): {all_true_via_reduce}")

# Check if ANY value in a list of booleans is True
any_true_via_reduce = reduce(operator.or_, boolean_flags)
print(f"Any flag True (via reduce): {any_true_via_reduce}\n")

# Note: For `all` and `any` checks, the built-in `all()` and `any()` functions
# are generally more readable and efficient due to their direct short-circuiting.
# reduce with operator.and_ and operator.or_ will work equivalently for lists of booleans.


print("--- End of 'operator' Logical Operators Demonstration ---")