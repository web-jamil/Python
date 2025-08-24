import math

# Exponential and logarithmic functions in the math module

print("--- Exponential Function (e^x) ---")
x = 2.0
print(f"e raised to the power of {x} (math.exp({x})): {math.exp(x)}")
print(f"Euler's number (math.e): {math.e}")

print("\n--- Natural Logarithm (ln(x) or log_e(x)) ---")
value = math.e
print(f"Natural logarithm of {value} (math.log({value})): {math.log(value)}")
value = 10.0
print(f"Natural logarithm of {value} (math.log({value})): {math.log(value)}")

print("\n--- Base-10 Logarithm (log10(x)) ---")
value = 100.0
print(f"Base-10 logarithm of {value} (math.log10({value})): {math.log10(value)}")
value = 1000.0
print(f"Base-10 logarithm of {value} (math.log10({value})): {math.log10(value)}")

print("\n--- Base-2 Logarithm (log2(x)) ---")
value = 8.0
print(f"Base-2 logarithm of {value} (math.log2({value})): {math.log2(value)}")
value = 16.0
print(f"Base-2 logarithm of {value} (math.log2({value})): {math.log2(value)}")

print("\n--- Logarithm with a Specified Base (log(x, base)) ---")
value = 16.0
base = 4.0
print(f"Logarithm of {value} with base {base} (math.log({value}, {base})): {math.log(value, base)}")

print("\n--- Exponential of x - 1 (expm1(x)) ---")
# Computes e^x - 1. Useful for small values of x where exp(x) - 1 might lose precision.
x_small = 0.001
result_standard = math.exp(x_small) - 1
result_expm1 = math.expm1(x_small)
print(f"e^{x_small} - 1 (standard): {result_standard}")
print(f"expm1({x_small}): {result_expm1}")

x_larger = 2.0
result_standard_large = math.exp(x_larger) - 1
result_expm1_large = math.expm1(x_larger)
print(f"e^{x_larger} - 1 (standard): {result_standard_large}")
print(f"expm1({x_larger}): {result_expm1_large}") # Results are similar for larger x

print("\n--- Natural Logarithm of 1 + x (log1p(x)) ---")
# Computes ln(1 + x). Useful for small values of x where log(1 + x) might lose precision.
x_small = 0.001
result_standard_log = math.log(1 + x_small)
result_log1p = math.log1p(x_small)
print(f"ln(1 + {x_small}) (standard): {result_standard_log}")
print(f"log1p({x_small}): {result_log1p}")

x_larger = 2.0
result_standard_log_large = math.log(1 + x_larger)
result_log1p_large = math.log1p(x_larger)
print(f"ln(1 + {x_larger}) (standard): {result_standard_log_large}")
print(f"log1p({x_larger}): {result_log1p_large}") # Results are similar for larger x