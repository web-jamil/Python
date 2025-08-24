import math

# Floating-point representation functions in the math module

print("--- Check if a number is finite (isfinite) ---")
finite_num = 3.14
infinite_pos = math.inf
infinite_neg = -math.inf
nan_value = math.nan

print(f"Is {finite_num} finite? {math.isfinite(finite_num)}")
print(f"Is {infinite_pos} finite? {math.isfinite(infinite_pos)}")
print(f"Is {infinite_neg} finite? {math.isfinite(infinite_neg)}")
print(f"Is {nan_value} finite? {math.isfinite(nan_value)}")

print("\n--- Check if two floating-point values are close (isclose) ---")
a = 0.1 + 0.2
b = 0.3
print(f"Is {a} close to {b}? {math.isclose(a, b)}") # Due to floating-point inaccuracies

c = 10.0
d = 10.0000001
print(f"Is {c} close to {d}? {math.isclose(c, d)}")

e = 10.0
f = 10.1
print(f"Is {e} close to {f}? {math.isclose(e, f)}")

print(f"Is {e} close to {f} with a larger relative tolerance (rel_tol=0.1)? {math.isclose(e, f, rel_tol=0.1)}")
print(f"Is {e} close to {f} with an absolute tolerance (abs_tol=0.1)? {math.isclose(e, f, abs_tol=0.1)}")

print("\n--- Multiply float by integer power of 2 (ldexp) ---")
x = 1.5
i = 3
result = math.ldexp(x, i)
print(f"{x} * (2**{i}) = {result} (using math.ldexp)")

x = -0.75
i = -2
result = math.ldexp(x, i)
print(f"{x} * (2**{i}) = {result} (using math.ldexp)")

print("\n--- Return the mantissa and exponent of a float (frexp) ---")
y = 12.5
mantissa, exponent = math.frexp(y)
print(f"The mantissa and exponent of {y} are: {mantissa}, {exponent} (where {y} = {mantissa} * 2**{exponent})")

y = 0.625
mantissa, exponent = math.frexp(y)
print(f"The mantissa and exponent of {y} are: {mantissa}, {exponent} (where {y} = {mantissa} * 2**{exponent})")

print("\n--- Accurate sum of floating-point numbers (fsum) ---")
float_list = [0.1] * 10
standard_sum = sum(float_list)
accurate_sum = math.fsum(float_list)
print(f"Standard sum of {float_list}: {standard_sum}")
print(f"Accurate sum using math.fsum of {float_list}: {accurate_sum}") # Helps mitigate precision loss in summation

mixed_floats = [0.1, 0.2, 0.3, -0.1, -0.2]
standard_sum_mixed = sum(mixed_floats)
accurate_sum_mixed = math.fsum(mixed_floats)
print(f"Standard sum of {mixed_floats}: {standard_sum_mixed}")
print(f"Accurate sum using math.fsum of {mixed_floats}: {accurate_sum_mixed}")