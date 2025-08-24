# --- Python: All About Exponential and Logarithmic Functions in Code ---

# Python provides a comprehensive set of exponential and logarithmic functions
# primarily through the `math` module for real numbers and the `cmath` module
# for complex numbers.

import math
import cmath

print("--- 1. Exponential Functions (`math` module - for real numbers) ---")

# These functions relate to the base `e` (Euler's number, approx 2.71828)
# or other specified bases.

# 1.1 `math.exp(x)`: Returns e raised to the power x ($e^x$).
print(f"1.1 `math.exp(x)` (e^x):")
print(f"    e^0: {math.exp(0)}")   # 1.0
print(f"    e^1: {math.exp(1)}")   # 2.71828...
print(f"    e^2: {math.exp(2)}")   # 7.38905...
print(f"    e^-1: {math.exp(-1)}") # 0.36787...

# 1.2 `math.expm1(x)`: Returns $e^x - 1$.
# - This function is often more accurate than `exp(x) - 1` for small values of `x`.
print(f"\n1.2 `math.expm1(x)` (e^x - 1):")
print(f"    e^0 - 1: {math.expm1(0)}")      # 0.0
print(f"    e^0.000000001 - 1: {math.expm1(0.000000001):.10f}") # More accurate for small x
print(f"    (math.exp(0.000000001) - 1): {(math.exp(0.000000001) - 1):.10f}") # May have less precision

# 1.3 `math.pow(x, y)`: Returns x raised to the power y ($x^y$).
# - This is equivalent to the `**` operator.
# - Can handle fractional exponents for roots (e.g., `x**(0.5)` for square root).
print(f"\n1.3 `math.pow(x, y)` (x^y):")
print(f"    2^3: {math.pow(2, 3)}") # 8.0
print(f"    4^0.5 (sqrt of 4): {math.pow(4, 0.5)}") # 2.0
print(f"    8^(1/3) (cube root of 8): {math.pow(8, 1/3):.4f}") # 2.0

# 1.4 `math.sqrt(x)`: Returns the square root of x ($\sqrt{x}$).
# - Input must be non-negative. Raises `ValueError` for negative inputs.
print(f"\n1.4 `math.sqrt(x)`:")
print(f"    sqrt(25): {math.sqrt(25)}") # 5.0
print(f"    sqrt(2): {math.sqrt(2):.4f}") # 1.4142

try:
    math.sqrt(-1)
except ValueError as e:
    print(f"    Error for sqrt(-1): {e} - math domain error.")


print("\n--- 2. Logarithmic Functions (`math` module - for real numbers) ---")

# These functions calculate logarithms to various bases.
# For `math.log(x, base)`, `x` must be positive.

# 2.1 `math.log(x, base=e)`: Returns the logarithm of x to the given base.
# - If `base` is not specified, it returns the natural logarithm (base e, `ln(x)`).
print(f"2.1 `math.log(x, base)` (log_base(x)):")
print(f"    ln(e^2): {math.log(math.e**2)}") # 2.0
print(f"    ln(1): {math.log(1)}") # 0.0
print(f"    log_10(100): {math.log(100, 10)}") # 2.0

# 2.2 `math.log1p(x)`: Returns natural logarithm of (1+x) ($\ln(1+x)$).
# - More accurate for `x` near zero than `log(1 + x)`.
print(f"\n2.2 `math.log1p(x)` (ln(1+x)):")
print(f"    ln(1 + 0.000000001): {math.log1p(0.000000001):.10f}") # More accurate for small x
print(f"    (math.log(1 + 0.000000001)): {math.log(1 + 0.000000001):.10f}") # May have less precision

# 2.3 `math.log2(x)`: Returns the base-2 logarithm of x ($\log_2 x$).
print(f"\n2.3 `math.log2(x)` (log_2(x)):")
print(f"    log2(8): {math.log2(8)}") # 3.0
print(f"    log2(1024): {math.log2(1024)}") # 10.0

# 2.4 `math.log10(x)`: Returns the base-10 logarithm of x ($\log_{10} x$).
print(f"\n2.4 `math.log10(x)` (log_10(x)):")
print(f"    log10(1000): {math.log10(1000)}") # 3.0
print(f"    log10(1): {math.log10(1)}") # 0.0

# Domain errors for logarithms (input must be positive)
try:
    math.log(0)
except ValueError as e:
    print(f"\n    Error for log(0): {e} - math domain error (log of 0 is undefined).")

try:
    math.log(-5)
except ValueError as e:
    print(f"    Error for log(-5): {e} - math domain error (log of negative number).")


print("\n--- 3. Exponential and Logarithmic Functions (`cmath` module - for complex numbers) ---")

# The `cmath` module provides versions of these functions that can handle
# and return complex numbers.

# 3.1 `cmath.exp(z)`: Returns e raised to the power z ($e^z$).
# - Can take a complex number as input.
z_exp_complex = 0 + (math.pi / 2) * 1j # Represents 0 + pi/2 * i
print(f"3.1 `cmath.exp(z)` (e^z):")
print(f"    e^(0 + pi/2 j): {cmath.exp(z_exp_complex):.4f}") # (0+1j) approx, since e^(i*pi/2) = cos(pi/2) + j sin(pi/2) = 0 + 1j

z_real_as_complex = 2 + 0j
print(f"    e^(2+0j): {cmath.exp(z_real_as_complex):.4f}") # (7.3891+0j) approx, same as math.exp(2)

# 3.2 `cmath.log(z, base=e)`: Returns the logarithm of z to the given base.
# - Can take zero or negative real numbers, returning a complex result.
z_log_complex = -1 + 0j # Real negative number
print(f"\n3.2 `cmath.log(z, base)`:")
print(f"    ln(-1): {cmath.log(z_log_complex):.4f}") # (0+3.1416j) approx, since ln(-1) = j*pi

z_complex_log = 1 + 1j
print(f"    ln(1+1j): {cmath.log(z_complex_log):.4f}")

# 3.3 `cmath.log10(z)`: Returns the base-10 logarithm of z.
print(f"\n3.3 `cmath.log10(z)`:")
print(f"    log10(-1): {cmath.log10(z_log_complex):.4f}") # (0+1.3644j) approx

# 3.4 `cmath.sqrt(z)`: Returns the square root of z.
# - Can handle negative real numbers or complex numbers, returning a complex result.
print(f"\n3.4 `cmath.sqrt(z)`:")
print(f"    sqrt(-1): {cmath.sqrt(-1)}") # 1j
print(f"    sqrt(3+4j): {cmath.sqrt(3+4j):.4f}") # (2.0000+1.0000j)


# 3.5 `cmath.pow(z1, z2)`: Returns z1 raised to the power z2 ($z_1^{z_2}$).
# - Handles complex bases and exponents.
base_complex = 2 + 3j
exponent_complex = 0.5 + 0.2j
print(f"\n3.5 `cmath.pow(z1, z2)`:")
print(f"    ({base_complex})^({exponent_complex}): {cmath.pow(base_complex, exponent_complex):.4f}")


print("\n--- 4. Differences and Use Cases ---")

# - **`math` module:** For real numbers and operations that stay within the real domain.
#   Raises `ValueError` if an operation would lead to a complex result.
#   Generally faster for purely real calculations.

# - **`cmath` module:** For complex numbers and operations that might produce complex results.
#   Will return a complex number even for real inputs if the result is complex.
#   Essential for complex analysis, electrical engineering, quantum mechanics, etc.

# Example of `math.pow` vs `**` operator:
# `math.pow(x, y)` converts both arguments to float.
# `x ** y` is more general and can work with complex numbers directly.
# The `**` operator implicitly uses complex arithmetic when needed.
print(f"\n4.1 `math.pow` vs `**` operator:")
print(f"    math.pow(2, 3): {math.pow(2, 3)}") # 8.0
print(f"    2 ** 3: {2 ** 3}") # 8

# Using `**` with a complex base (Python's built-in behavior)
print(f"    (2+3j) ** 2: {(2+3j) ** 2}") # (-5+12j)

# Using `**` with a real negative base and fractional exponent that results in a complex number
print(f"    (-1) ** 0.5: {(-1) ** 0.5}") # (6.123233995736766e-17+1j) approx 1j (cmath.sqrt(-1))