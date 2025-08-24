import math

print("--- 2. Hyperbolic Functions (`math` module - for real numbers) ---")

# --- Basic Hyperbolic Functions ---

# 2.1 `math.sinh(x)`: Hyperbolic sine
x_sinh = 1.0
print(f"2.1 Hyperbolic Sine (sinh({x_sinh})): {math.sinh(x_sinh):.4f}") # (e^1 - e^-1) / 2
print(f"    sinh(0): {math.sinh(0):.4f}")

# 2.2 `math.cosh(x)`: Hyperbolic cosine
x_cosh = 0.0
print(f"\n2.2 Hyperbolic Cosine (cosh({x_cosh})): {math.cosh(x_cosh):.4f}") # (e^0 + e^-0) / 2 = 1
print(f"    cosh(1.0): {math.cosh(1.0):.4f}")

# 2.3 `math.tanh(x)`: Hyperbolic tangent
x_tanh = 0.5
print(f"\n2.3 Hyperbolic Tangent (tanh({x_tanh})): {math.tanh(x_tanh):.4f}")
print(f"    tanh(0): {math.tanh(0):.4f}") # Approaches 1 as x -> inf, -1 as x -> -inf


# --- Inverse Hyperbolic Functions ---

# 2.4 `math.asinh(x)`: Inverse hyperbolic sine
# Accepts any real number.
x_asinh = 1.6
print(f"\n2.4 Inverse Hyperbolic Sine (asinh({x_asinh})): {math.asinh(x_asinh):.4f}")
print(f"    asinh(0): {math.asinh(0):.4f}")

# 2.5 `math.acosh(x)`: Inverse hyperbolic cosine
# Input `x` must be >= 1 for real results.
x_acosh = 1.5
print(f"\n2.5 Inverse Hyperbolic Cosine (acosh({x_acosh})): {math.acosh(x_acosh):.4f}")
print(f"    acosh(1): {math.acosh(1):.4f}") # 0.0

# Demonstrate ValueError for invalid input
try:
    math.acosh(0.5) # Input < 1
except ValueError as e:
    print(f"    Error for acosh(0.5): {e} - math domain error (input < 1).")


# 2.6 `math.atanh(x)`: Inverse hyperbolic tangent
# Input `x` must be between -1 and 1 (exclusive).
x_atanh = 0.7
print(f"\n2.6 Inverse Hyperbolic Tangent (atanh({x_atanh})): {math.atanh(x_atanh):.4f}")
print(f"    atanh(0): {math.atanh(0):.4f}") # 0.0

# Demonstrate ValueError for invalid input
try:
    math.atanh(1.0) # Input >= 1
except ValueError as e:
    print(f"    Error for atanh(1.0): {e} - math domain error (input not in (-1, 1)).")

try:
    math.atanh(-1.0) # Input <= -1
except ValueError as e:
    print(f"    Error for atanh(-1.0): {e} - math domain error (input not in (-1, 1)).")


import cmath

print("\n--- 3. Hyperbolic Functions (`cmath` module - for complex numbers) ---")

# --- Basic Hyperbolic Functions (Complex Input/Output) ---

z = 1 + 1j # A complex number for demonstration

# 3.1 `cmath.sinh(z)`: Hyperbolic sine for complex numbers
print(f"3.1 Hyperbolic Sine (sinh({z})): {cmath.sinh(z):.4f}")

# 3.2 `cmath.cosh(z)`: Hyperbolic cosine for complex numbers
print(f"3.2 Hyperbolic Cosine (cosh({z})): {cmath.cosh(z):.4f}")

# 3.3 `cmath.tanh(z)`: Hyperbolic tangent for complex numbers
print(f"3.3 Hyperbolic Tangent (tanh({z})): {cmath.tanh(z):.4f}")

# Test with a real number, it will return a complex number with 0 imaginary part
x_real = 0.5
print(f"    cosh({x_real}) using cmath: {cmath.cosh(x_real):.4f}") # (1.1276+0j) approx


# --- Inverse Hyperbolic Functions (Complex Input/Output) ---

z_inv = 0.5 + 0.2j # A complex number for inverse functions

# 3.4 `cmath.asinh(z)`: Inverse hyperbolic sine for complex numbers
print(f"\n3.4 Inverse Hyperbolic Sine (asinh({z_inv})): {cmath.asinh(z_inv):.4f}")

# 3.5 `cmath.acosh(z)`: Inverse hyperbolic cosine for complex numbers
# Note: cmath.acosh handles inputs < 1 by returning complex numbers, unlike math.acosh.
print(f"\n3.5 Inverse Hyperbolic Cosine (acosh({z_inv})): {cmath.acosh(z_inv):.4f}")
print(f"    acosh(0.5) using cmath: {cmath.acosh(0.5):.4f}") # No ValueError, returns complex number

# 3.6 `cmath.atanh(z)`: Inverse hyperbolic tangent for complex numbers
# Note: cmath.atanh handles inputs outside (-1, 1) by returning complex numbers.
print(f"\n3.6 Inverse Hyperbolic Tangent (atanh({z_inv})): {cmath.atanh(z_inv):.4f}")
print(f"    atanh(2.0) using cmath: {cmath.atanh(2.0):.4f}") # No ValueError, returns complex number