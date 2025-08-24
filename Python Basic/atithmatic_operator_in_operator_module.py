import operator

print("--- Arithmetic Operators from Python's 'operator' Module ---")
print("----------------------------------------------------------\n")

# Define some operands
a = 10
b = 3
c = 2.5
d = 5.0
e = -4

print(f"Operands: a={a}, b={b}, c={c}, d={d}, e={e}\n")


# 1. Addition: operator.add(a, b) equivalent to a + b
print("1. Addition (operator.add):")
result_add_int = operator.add(a, b)
result_add_float = operator.add(a, c)
print(f"operator.add({a}, {b})   -> {result_add_int}")
print(f"operator.add({a}, {c}) -> {result_add_float}")
print(f"Type of result: {type(result_add_float)}\n")


# 2. Subtraction: operator.sub(a, b) equivalent to a - b
print("2. Subtraction (operator.sub):")
result_sub_int = operator.sub(a, b)
result_sub_float = operator.sub(c, d)
print(f"operator.sub({a}, {b})   -> {result_sub_int}")
print(f"operator.sub({c}, {d}) -> {result_sub_float}\n")


# 3. Multiplication: operator.mul(a, b) equivalent to a * b
print("3. Multiplication (operator.mul):")
result_mul_int = operator.mul(a, b)
result_mul_float = operator.mul(b, c)
print(f"operator.mul({a}, {b})   -> {result_mul_int}")
print(f"operator.mul({b}, {c}) -> {result_mul_float}\n")


# 4. True Division: operator.truediv(a, b) equivalent to a / b
# Always returns a float.
print("4. True Division (operator.truediv):")
result_truediv_int = operator.truediv(a, b)
result_truediv_float = operator.truediv(d, c)
print(f"operator.truediv({a}, {b})   -> {result_truediv_int}")
print(f"operator.truediv({d}, {c}) -> {result_truediv_float}")
print(f"Type of result: {type(result_truediv_int)}\n")


# 5. Floor Division: operator.floordiv(a, b) equivalent to a // b
# Returns the integer part of the quotient, rounded towards negative infinity.
print("5. Floor Division (operator.floordiv):")
result_floordiv_pos = operator.floordiv(a, b)    # 10 // 3 = 3
result_floordiv_neg1 = operator.floordiv(a, e)   # 10 // -4 = -3 (because 10 / -4 = -2.5, floor is -3)
result_floordiv_neg2 = operator.floordiv(e, b)   # -4 // 3 = -2 (because -4 / 3 = -1.33, floor is -2)
print(f"operator.floordiv({a}, {b})   -> {result_floordiv_pos}")
print(f"operator.floordiv({a}, {e})  -> {result_floordiv_neg1}")
print(f"operator.floordiv({e}, {b})  -> {result_floordiv_neg2}\n")


# 6. Modulo: operator.mod(a, b) equivalent to a % b
# Returns the remainder of the division.
# The sign of the remainder matches the sign of the divisor.
print("6. Modulo (operator.mod):")
result_mod_pos = operator.mod(a, b)   # 10 % 3 = 1
result_mod_neg1 = operator.mod(a, e)  # 10 % -4 = -2 (10 = -4 * -2 + 2, remainder is -2 to match divisor sign)
result_mod_neg2 = operator.mod(e, b)  # -4 % 3 = 2  (-4 = 3 * -2 + 2, remainder is 2 to match divisor sign)
print(f"operator.mod({a}, {b})   -> {result_mod_pos}")
print(f"operator.mod({a}, {e})  -> {result_mod_neg1}")
print(f"operator.mod({e}, {b})  -> {result_mod_neg2}\n")


# 7. Exponentiation/Power: operator.pow(a, b) equivalent to a ** b
print("7. Exponentiation (operator.pow):")
result_pow_int = operator.pow(a, b)     # 10 ** 3 = 1000
result_pow_float = operator.pow(c, 2) # 2.5 ** 2 = 6.25
print(f"operator.pow({a}, {b})   -> {result_pow_int}")
print(f"operator.pow({c}, 2) -> {result_pow_float}\n")


# 8. Unary Plus: operator.pos(obj) equivalent to +obj
# Returns the operand's value; often used for clarity or type conversion.
print("8. Unary Plus (operator.pos):")
result_pos_int = operator.pos(a)
result_pos_neg = operator.pos(e)
print(f"operator.pos({a})  -> {result_pos_int}")
print(f"operator.pos({e}) -> {result_pos_neg}\n")


# 9. Unary Negation: operator.neg(obj) equivalent to -obj
# Returns the negation (opposite sign) of the operand.
print("9. Unary Negation (operator.neg):")
result_neg_int = operator.neg(a)
result_neg_neg = operator.neg(e)
print(f"operator.neg({a})  -> {result_neg_int}")
print(f"operator.neg({e}) -> {result_neg_neg}\n")


# 10. Absolute Value: operator.abs(obj) equivalent to abs(obj)
print("10. Absolute Value (operator.abs):")
result_abs_pos = operator.abs(a)
result_abs_neg = operator.abs(e)
print(f"operator.abs({a})  -> {result_abs_pos}")
print(f"operator.abs({e}) -> {result_abs_neg}\n")


# Why use the 'operator' module?
print("--- Why use the 'operator' module? ---\n")

# Use Case 1: Passing operations as arguments to higher-order functions
# Without operator module:
# numbers = [1, 2, 3]
# doubled = list(map(lambda x: x * 2, numbers))
# print(f"Doubled (lambda): {doubled}")

# With operator module (more concise and sometimes slightly faster for simple ops):
numbers = [1, 2, 3]
doubled = list(map(operator.mul, numbers, [2] * len(numbers))) # Map requires two iterables for binary ops
print(f"numbers: {numbers}")
print(f"Doubled (operator.mul): {doubled}\n")

# Example with reduce (requires functools)
from functools import reduce
data_list = [10, 5, 2, 4]
sum_of_list = reduce(operator.add, data_list)
product_of_list = reduce(operator.mul, data_list)
print(f"data_list: {data_list}")
print(f"Sum (reduce with operator.add): {sum_of_list}")
print(f"Product (reduce with operator.mul): {product_of_list}\n")

# Use Case 2: Readability and clarity in specific contexts
# Sometimes, `operator.add` can be more explicit than `+` if you're
# trying to emphasize the operation itself rather than the syntax.

# Use Case 3: When operators are not directly callable (e.g., in `functools.partial`)
# For example, if you wanted to create a partially applied function for adding 5:
from functools import partial
add_five = partial(operator.add, 5)
print(f"add_five(10): {add_five(10)}")
print(f"add_five(15): {add_five(15)}\n")

# This is equivalent to `lambda x: x + 5`, but `partial` works directly with callable functions.

print("--- End of 'operator' Module Arithmetic Demonstration ---")