print("--- Python Arithmetic Operators ---")
print("----------------------------------\n")

# Define some numbers for demonstration
num1 = 20
num2 = 7
num3 = 3.5
num4 = -5
num5 = 0

print(f"Numbers used: num1={num1}, num2={num2}, num3={num3}, num4={num4}, num5={num5}\n")


# 1. Addition (+)
print("1. Addition (+):")
result_add_int = num1 + num2
result_add_float = num1 + num3
result_add_neg = num1 + num4
print(f"{num1} + {num2} = {result_add_int}")
print(f"{num1} + {num3} = {result_add_float}")
print(f"{num1} + {num4} = {result_add_neg}\n")


# 2. Subtraction (-)
print("2. Subtraction (-):")
result_sub_int = num1 - num2
result_sub_float = num1 - num3
result_sub_neg = num1 - num4
print(f"{num1} - {num2} = {result_sub_int}")
print(f"{num1} - {num3} = {result_sub_float}")
print(f"{num1} - {num4} = {result_sub_neg}\n")


# 3. Multiplication (*)
print("3. Multiplication (*):")
result_mul_int = num1 * num2
result_mul_float = num1 * num3
result_mul_neg = num1 * num4
print(f"{num1} * {num2} = {result_mul_int}")
print(f"{num1} * {num3} = {result_mul_float}")
print(f"{num1} * {num4} = {result_mul_neg}\n")


# 4. Division (/) - True Division
# Always returns a float, even if the division results in an integer.
print("4. Division (/) - True Division:")
result_div_int = num1 / num2
result_div_exact = 10 / 2
result_div_float = num1 / num3
result_div_neg = num1 / num4
print(f"{num1} / {num2} = {result_div_int}")
print(f"10 / 2 = {result_div_exact}")
print(f"{num1} / {num3} = {result_div_float}")
print(f"{num1} / {num4} = {result_div_neg}\n")

# Division by zero raises a ZeroDivisionError
try:
    print(f"{num1} / {num5} = {num1 / num5}")
except ZeroDivisionError as e:
    print(f"Error: {e} (Cannot divide by zero)\n")


# 5. Modulus (%) - Remainder of Division
# The sign of the result matches the sign of the divisor.
print("5. Modulus (%) - Remainder of Division:")
result_mod_pos = num1 % num2      # 20 divided by 7 is 2 with remainder 6
result_mod_neg_divisor = num1 % num4 # 20 divided by -5 is -4 with remainder 0
result_mod_neg_dividend = num4 % num2 # -5 divided by 7 is -1 with remainder 2 (-5 = 7 * -1 + 2)
print(f"{num1} % {num2} = {result_mod_pos}")
print(f"{num1} % {num4} = {result_mod_neg_divisor}")
print(f"{num4} % {num2} = {result_mod_neg_dividend}\n")


# 6. Exponentiation (**) - Power
print("6. Exponentiation (**) - Power:")
result_pow_int = num2 ** 2  # 7 squared
result_pow_float = num1 ** 0.5 # Square root of 20
result_pow_neg_exponent = 2 ** num4 # 2 to the power of -5 (1/2^5 = 1/32)
print(f"{num2} ** 2 = {result_pow_int}")
print(f"{num1} ** 0.5 = {result_pow_float}")
print(f"2 ** {num4} = {result_pow_neg_exponent}\n")


# 7. Floor Division (//) - Integer Division
# Returns the integer part of the quotient, rounded down towards negative infinity.
print("7. Floor Division (//) - Integer Division:")
result_floor_pos = num1 // num2      # 20 // 7 = 2
result_floor_exact = 10 // 2         # 10 // 2 = 5
result_floor_float = num1 // num3    # 20 // 3.5 = 5.0 (result type is float if one operand is float)
result_floor_neg1 = num1 // num4     # 20 // -5 = -4
result_floor_neg2 = num4 // num2     # -5 // 7 = -1 (since -0.71... rounded down is -1)
result_floor_neg3 = -10 // 3         # -10 // 3 = -4 (since -3.33... rounded down is -4)
print(f"{num1} // {num2} = {result_floor_pos}")
print(f"10 // 2 = {result_floor_exact}")
print(f"{num1} // {num3} = {result_floor_float}")
print(f"{num1} // {num4} = {result_floor_neg1}")
print(f"{num4} // {num2} = {result_floor_neg2}")
print(f"-10 // 3 = {result_floor_neg3}\n")


# 8. Unary Operators (+ and -)
print("8. Unary Operators (+ and -):")
# Unary plus: Returns the number unchanged (often for clarity)
positive_num = +num4
print(f"+{num4} = {positive_num}")

# Unary minus: Negates the number
negative_num = -num1
double_negative = -num4
print(f"-{num1} = {negative_num}")
print(f"-{num4} = {double_negative}\n")


# Operator Precedence and Associativity (Important!)
print("--- Operator Precedence and Associativity ---")
# PEMDAS/BODMAS rules apply (Parentheses, Exponents, Multiplication/Division/Modulo, Addition/Subtraction)
# Operators at the same precedence level are evaluated from left to right (associativity).
# Use parentheses to explicitly control order of operations.

expression1 = 5 + 3 * 2 # 3 * 2 = 6, then 5 + 6 = 11
expression2 = (5 + 3) * 2 # 5 + 3 = 8, then 8 * 2 = 16
expression3 = 10 / 2 + 3 # 10 / 2 = 5.0, then 5.0 + 3 = 8.0
expression4 = 10 // 3 ** 2 # 3 ** 2 = 9, then 10 // 9 = 1
print(f"5 + 3 * 2 = {expression1}")
print(f"(5 + 3) * 2 = {expression2}")
print(f"10 / 2 + 3 = {expression3}")
print(f"10 // 3 ** 2 = {expression4}\n")


print("--- End of Python Arithmetic Operators Demonstration ---")