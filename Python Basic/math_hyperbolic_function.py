import math

# Hyperbolic functions in the math module

print("--- Hyperbolic Sine (sinh) ---")
x = 1.0
print(f"Hyperbolic sine of {x}: {math.sinh(x)}")

print("\n--- Hyperbolic Cosine (cosh) ---")
x = 1.0
print(f"Hyperbolic cosine of {x}: {math.cosh(x)}")

print("\n--- Hyperbolic Tangent (tanh) ---")
x = 1.0
print(f"Hyperbolic tangent of {x}: {math.tanh(x)}")

print("\n--- Inverse Hyperbolic Sine (asinh) ---")
y = 2.0
print(f"Inverse hyperbolic sine of {y}: {math.asinh(y)}")

print("\n--- Inverse Hyperbolic Cosine (acosh) ---")
y = 2.0
# Note: The domain of acosh is x >= 1
print(f"Inverse hyperbolic cosine of {y}: {math.acosh(y)}")
try:
    print(f"Inverse hyperbolic cosine of 0.5: {math.acosh(0.5)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Inverse Hyperbolic Tangent (atanh) ---")
y = 0.5
# Note: The domain of atanh is -1 < x < 1
print(f"Inverse hyperbolic tangent of {y}: {math.atanh(y)}")
try:
    print(f"Inverse hyperbolic tangent of 1.0: {math.atanh(1.0)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
try:
    print(f"Inverse hyperbolic tangent of -1.0: {math.atanh(-1.0)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
try:
    print(f"Inverse hyperbolic tangent of 1.5: {math.atanh(1.5)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")