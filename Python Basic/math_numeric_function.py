import math

# Numeric functions in the math module

print("--- Absolute Value ---")
x = -10
print(f"The absolute value of {x} is: {math.fabs(x)}")
y = 5.7
print(f"The absolute value of {y} is: {math.fabs(y)}")

print("\n--- Ceiling ---")
z = 3.2
print(f"The ceiling of {z} is: {math.ceil(z)}") # Smallest integer greater than or equal to z
a = -3.2
print(f"The ceiling of {a} is: {math.ceil(a)}")

print("\n--- Floor ---")
b = 3.7
print(f"The floor of {b} is: {math.floor(b)}")   # Largest integer less than or equal to b
c = -3.7
print(f"The floor of {c} is: {math.floor(c)}")

print("\n--- Factorial ---")
n = 5
print(f"The factorial of {n} is: {math.factorial(n)}") # n! = n * (n-1) * ... * 1
# print(f"The factorial of 5.5 is: {math.factorial(5.5)}") # ValueError: factorial() only accepts integral values

print("\n--- Greatest Common Divisor (GCD) ---")
num1 = 12
num2 = 18
print(f"The GCD of {num1} and {num2} is: {math.gcd(num1, num2)}")
num3 = 24
num4 = 36
num5 = 48
print(f"The GCD of {num3}, {num4}, and {num5} is: {math.gcd(num3, math.gcd(num4, num5))}") # For more than two numbers

print("\n--- Checking for Infinity ---")
infinity_pos = math.inf
infinity_neg = -math.inf
not_infinity = 10
print(f"Is {infinity_pos} infinity? {math.isinf(infinity_pos)}")
print(f"Is {infinity_neg} infinity? {math.isinf(infinity_neg)}")
print(f"Is {not_infinity} infinity? {math.isinf(not_infinity)}")

print("\n--- Checking for NaN (Not a Number) ---")
nan_value = math.nan
valid_number = 5
print(f"Is {nan_value} NaN? {math.isnan(nan_value)}")
print(f"Is {valid_number} NaN? {math.isnan(valid_number)}")
# result = 0 / 0
# print(f"Is 0/0 ({result}) NaN? {math.isnan(result)}")

print("\n--- Floating-Point Remainder ---")
dividend = 10
divisor = 3
remainder_fmod = math.fmod(dividend, divisor)
remainder_mod = dividend % divisor
print(f"The remainder of {dividend} divided by {divisor} using math.fmod is: {remainder_fmod}")
print(f"The remainder of {dividend} divided by {divisor} using the % operator is: {remainder_mod}")
dividend_neg = -10
remainder_fmod_neg = math.fmod(dividend_neg, divisor)
remainder_mod_neg = dividend_neg % divisor
print(f"The remainder of {dividend_neg} divided by {divisor} using math.fmod is: {remainder_fmod_neg}")
print(f"The remainder of {dividend_neg} divided by {divisor} using the % operator is: {remainder_mod_neg}") # Note the difference in sign

print("\n--- Truncation ---")
float_num = 5.7
print(f"The truncation of {float_num} is: {math.trunc(float_num)}") # Returns the integer part
negative_float = -5.7
print(f"The truncation of {negative_float} is: {math.trunc(negative_float)}")

print("\n--- Power ---")
base = 2
exponent = 3
print(f"{base} raised to the power of {exponent} is: {math.pow(base, exponent)}")

print("\n--- Square Root ---")
number = 25
print(f"The square root of {number} is: {math.sqrt(number)}")
positive_float = 7.5
print(f"The square root of {positive_float} is: {math.sqrt(positive_float)}")
# print(f"The square root of -1 is: {math.sqrt(-1)}") # ValueError: math domain error

print("\n--- Sum of Floating-Point Numbers (Accurate) ---")
float_list = [0.1] * 10
standard_sum = sum(float_list)
accurate_sum = math.fsum(float_list)
print(f"Standard sum of {float_list}: {standard_sum}")
print(f"Accurate sum using math.fsum of {float_list}: {accurate_sum}") # Helps avoid floating-point inaccuracies

print("\n--- Floating Point Representation ---")
val = 3.14159
print(f"Is {val} finite? {math.isfinite(val)}")
print(f"Is infinity finite? {math.isfinite(math.inf)}")

val_int = 5.0
print(f"Is {val} close to its rounded value? {math.isclose(val, round(val))}")
print(f"Is {val_int} close to its rounded value? {math.isclose(val_int, round(val_int))}")

mantissa, exponent = math.frexp(val)
print(f"The mantissa and exponent of {val} are: {mantissa}, {exponent} (where {val} = {mantissa} * 2**{exponent})")

x_ldexp = 1.5
i_ldexp = 3
result_ldexp = math.ldexp(x_ldexp, i_ldexp)
print(f"{x_ldexp} * (2**{i_ldexp}) = {result_ldexp} (using math.ldexp)")