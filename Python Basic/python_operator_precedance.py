print("--- Python Operator Precedence ---")
print("----------------------------------\n")

# Operator precedence determines the order in which operators are evaluated
# in an expression. Operators with higher precedence are evaluated before
# operators with lower precedence.
# When operators have the same precedence, associativity (usually left-to-right)
# determines the order. Parentheses `()` can always be used to explicitly
# control the order of evaluation.

# General Order of Precedence (from highest to lowest, simplified):
# 1. Parentheses `()`
# 2. Exponentiation `**`
# 3. Unary operators `+x`, `-x`, `~x`
# 4. Multiplication `*`, Division `/`, Floor Division `//`, Modulo `%`
# 5. Addition `+`, Subtraction `-`
# 6. Bitwise shifts `<<`, `>>`
# 7. Bitwise AND `&`
# 8. Bitwise XOR `^`
# 9. Bitwise OR `|`
# 10. Comparison operators `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`
# 11. Logical NOT `not`
# 12. Logical AND `and`
# 13. Logical OR `or`
# 14. Walrus operator `:=` (assignment expression)


# --- 1. Parentheses `()` ---
print("1. Parentheses `()` (Highest Precedence):")
# Parentheses override all other precedence rules.
result = (10 + 5) * 2  # (15) * 2 = 30
print(f"(10 + 5) * 2 = {result}")

result = 10 + (5 * 2)  # 10 + (10) = 20
print(f"10 + (5 * 2) = {result}\n")


# --- 2. Exponentiation `**` ---
print("2. Exponentiation `**`:")
# Higher than multiplication/division.
result = 2 * 3 ** 2  # 2 * (3**2) = 2 * 9 = 18
print(f"2 * 3 ** 2 = {result}")

result = (2 * 3) ** 2  # (6) ** 2 = 36
print(f"(2 * 3) ** 2 = {result}\n")

# Associativity of ** is right-to-left
result = 2 ** 3 ** 2 # 2 ** (3 ** 2) = 2 ** 9 = 512
print(f"2 ** 3 ** 2 = {result}")
result = (2 ** 3) ** 2 # (8) ** 2 = 64
print(f"(2 ** 3) ** 2 = {result}\n")


# --- 3. Unary Operators (`+x`, `-x`, `~x`) ---
print("3. Unary Operators (`+x`, `-x`, `~x`):")
# Applied before binary arithmetic operations.
result = -5 + 10  # (-5) + 10 = 5
print(f"-5 + 10 = {result}")

result = ~5 + 10  # (~5 = -6) + 10 = 4
print(f"~5 + 10 = {result}\n")


# --- 4. Multiplication, Division, Floor Division, Modulo (`*`, `/`, `//`, `%`) ---
print("4. Multiplication/Division/Modulo (`*`, `/`, `//`, `%`):")
# These have equal precedence and are evaluated from left to right.
result = 10 + 2 * 3  # 10 + (2 * 3) = 10 + 6 = 16
print(f"10 + 2 * 3 = {result}")

result = 10 / 2 + 3  # (10 / 2) + 3 = 5.0 + 3 = 8.0
print(f"10 / 2 + 3 = {result}")

result = 10 % 3 * 2  # (10 % 3) * 2 = 1 * 2 = 2
print(f"10 % 3 * 2 = {result}\n")


# --- 5. Addition, Subtraction (`+`, `-`) ---
print("5. Addition, Subtraction (`+`, `-`):")
# These have equal precedence and are evaluated from left to right.
result = 20 - 5 + 3 # (20 - 5) + 3 = 15 + 3 = 18
print(f"20 - 5 + 3 = {result}\n")


# --- 6. Bitwise Shifts (`<<`, `>>`) ---
print("6. Bitwise Shifts (`<<`, `>>`):")
# Lower precedence than arithmetic operators.
result = 5 + (1 << 2) # 5 + (1 * 4) = 5 + 4 = 9
print(f"5 + 1 << 2 = {result}") # Incorrect without parentheses: (5+1) << 2 = 6 << 2 = 24
result = (5 + 1) << 2
print(f"(5 + 1) << 2 = {result}\n")


# --- 7. Bitwise AND `&` ---
print("7. Bitwise AND `&`:")
# Lower precedence than bitwise shifts.
result = 10 & 5 + 3 # 10 & (5 + 3) = 10 & 8 = 8 (binary: 1010 & 1000 = 1000)
print(f"10 & 5 + 3 = {result}\n")


# --- 8. Bitwise XOR `^` ---
print("8. Bitwise XOR `^`:")
# Lower precedence than bitwise AND.
result = 10 ^ 5 & 3 # 10 ^ (5 & 3) = 10 ^ 1 = 11 (binary: 1010 ^ 0001 = 1011)
print(f"10 ^ 5 & 3 = {result}\n")


# --- 9. Bitwise OR `|` ---
print("9. Bitwise OR `|`:")
# Lower precedence than bitwise XOR.
result = 10 | 5 ^ 3 # 10 | (5 ^ 3) = 10 | 6 = 14 (binary: 1010 | 0110 = 1110)
print(f"10 | 5 ^ 3 = {result}\n")


# --- 10. Comparison Operators (`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`) ---
print("10. Comparison Operators:")
# All comparison operators have the same precedence and are evaluated from left to right.
# They are lower than arithmetic and bitwise operators.
result = 10 > 5 and 20 < 30 # (10 > 5) and (20 < 30) = True and True = True
print(f"10 > 5 and 20 < 30 = {result}")

# Chained comparisons (special case: evaluated like `A and B and C`)
result = 10 < 20 < 30 # (10 < 20) and (20 < 30) = True and True = True
print(f"10 < 20 < 30 = {result}")

result = 10 < 5 < 30 # (10 < 5) and (5 < 30) = False and True = False
print(f"10 < 5 < 30 = {result}\n")


# --- 11. Logical NOT `not` ---
print("11. Logical NOT `not`:")
# Higher precedence than `and` and `or`.
result = not 10 > 5 # not (10 > 5) = not True = False
print(f"not 10 > 5 = {result}\n")


# --- 12. Logical AND `and` ---
print("12. Logical AND `and`:")
# Higher precedence than `or`.
result = True or False and False # True or (False and False) = True or False = True
print(f"True or False and False = {result}\n")


# --- 13. Logical OR `or` ---
print("13. Logical OR `or`:")
# Lowest precedence among common operators (excluding walrus).
result = False and True or True # (False and True) or True = False or True = True
print(f"False and True or True = {result}\n")


# --- 14. Walrus Operator `:=` (Assignment Expression) ---
print("14. Walrus Operator `:=` (Lowest Precedence):")
# The walrus operator has the lowest precedence among all operators, meaning
# its assignment happens very late.
# This is crucial for its use case, as it allows the assignment to be part of a larger expression.

# Example: (val := 10) + 5
# Here, `:=` assigns 10 to `val`, and then `val` is used in the addition.
if (count := len([1, 2, 3])) > 2:
    print(f"count := len([1,2,3]) -> count is {count}. Condition (count > 2) is True.")
print(f"After if block, count is still accessible: {count}\n")


print("--- End of Python Operator Precedence Demonstration ---")