# --- Python: All About Trigonometric Functions in Code ---

# Python provides trigonometric functions primarily through two modules:
# 1.  `math`: For real numbers. Most common use cases.
# 2.  `cmath`: For complex numbers.

# Important Note: All trigonometric functions in both `math` and `cmath`
# modules typically use **radians** for angles, not degrees. You'll need
# conversion functions if you work with degrees.

import math
import cmath

print("--- 1. Angle Conversions (Degrees <-> Radians) ---")

# Since trigonometric functions work with radians, these conversions are essential.

# 1.1 `math.radians(degrees)`: Converts degrees to radians.
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
print(f"1.1 {angle_degrees} degrees = {angle_radians:.4f} radians (approx pi/2)")

angle_degrees_full = 360
angle_radians_full = math.radians(angle_degrees_full)
print(f"    {angle_degrees_full} degrees = {angle_radians_full:.4f} radians (approx 2*pi)")

# 1.2 `math.degrees(radians)`: Converts radians to degrees.
angle_radians_pi = math.pi
angle_degrees_pi = math.degrees(angle_radians_pi)
print(f"1.2 {angle_radians_pi:.4f} radians = {angle_degrees_pi:.4f} degrees (180 deg)")

angle_radians_half_pi = math.pi / 2
angle_degrees_half_pi = math.degrees(angle_radians_half_pi)
print(f"    {angle_radians_half_pi:.4f} radians = {angle_degrees_half_pi:.4f} degrees (90 deg)")


print("\n--- 2. Basic Trigonometric Functions (`math` module - for real numbers) ---")

# These functions take a real number (angle in radians) and return a real number.

# 2.1 `math.sin(x)`: Returns the sine of x (x in radians).
print(f"2.1 Sine:")
print(f"    sin(0 radians): {math.sin(0)}")
print(f"    sin(pi/2 radians): {math.sin(math.pi / 2):.4f}") # approx 1.0
print(f"    sin(pi radians): {math.sin(math.pi):.4f}")       # approx 0.0

# 2.2 `math.cos(x)`: Returns the cosine of x (x in radians).
print(f"\n2.2 Cosine:")
print(f"    cos(0 radians): {math.cos(0)}")                 # 1.0
print(f"    cos(pi/2 radians): {math.cos(math.pi / 2):.4f}") # approx 0.0
print(f"    cos(pi radians): {math.cos(math.pi):.4f}")       # -1.0

# 2.3 `math.tan(x)`: Returns the tangent of x (x in radians).
print(f"\n2.3 Tangent:")
print(f"    tan(0 radians): {math.tan(0)}")                 # 0.0
# tan(pi/2) is undefined; will return a very large number due to float precision
print(f"    tan(pi/4 radians): {math.tan(math.pi / 4):.4f}") # approx 1.0
print(f"    tan(-pi/4 radians): {math.tan(-math.pi / 4):.4f}") # approx -1.0


print("\n--- 3. Inverse Trigonometric Functions (`math` module - for real numbers) ---")

# These functions return the angle in radians. Input range is usually [-1, 1].

# 3.1 `math.asin(x)`: Returns the arcsine of x (angle whose sine is x). Result in radians.
# Input x must be between -1 and 1.
print(f"3.1 Arcsine:")
print(f"    asin(0): {math.asin(0):.4f}") # 0.0
print(f"    asin(1): {math.asin(1):.4f}") # approx pi/2
print(f"    asin(-1): {math.asin(-1):.4f}") # approx -pi/2

# 3.2 `math.acos(x)`: Returns the arccosine of x (angle whose cosine is x). Result in radians.
# Input x must be between -1 and 1.
print(f"\n3.2 Arccosine:")
print(f"    acos(1): {math.acos(1):.4f}") # 0.0
print(f"    acos(0): {math.acos(0):.4f}") # approx pi/2
print(f"    acos(-1): {math.acos(-1):.4f}") # approx pi

# 3.3 `math.atan(x)`: Returns the arctangent of x (angle whose tangent is x). Result in radians.
# Input x can be any real number.
print(f"\n3.3 Arctangent:")
print(f"    atan(0): {math.atan(0):.4f}") # 0.0
print(f"    atan(1): {math.atan(1):.4f}") # approx pi/4
print(f"    atan(-1): {math.atan(-1):.4f}") # approx -pi/4

# 3.4 `math.atan2(y, x)`: Returns the arctangent of y/x, considering the signs of both y and x.
# This is useful for finding the angle of a point (x, y) in all four quadrants. Result in radians.
print(f"\n3.4 Arctangent (atan2 for quadrants):")
print(f"    atan2(1, 1) (Quadrant 1): {math.atan2(1, 1):.4f}") # pi/4
print(f"    atan2(1, -1) (Quadrant 2): {math.atan2(1, -1):.4f}") # 3*pi/4
print(f"    atan2(-1, -1) (Quadrant 3): {math.atan2(-1, -1):.4f}") # -3*pi/4
print(f"    atan2(-1, 1) (Quadrant 4): {math.atan2(-1, 1):.4f}") # -pi/4


print("\n--- 4. Hypotenuse Function (`math` module) ---")

# 4.1 `math.hypot(x, y)`: Returns the Euclidean norm, sqrt(x*x + y*y).
# This is the length of the hypotenuse of a right-angled triangle with legs x and y,
# or the distance from the origin to point (x, y).
print(f"4.1 Hypotenuse:")
print(f"    hypot(3, 4): {math.hypot(3, 4)}") # 5.0 (since 3^2 + 4^2 = 9 + 16 = 25, sqrt(25) = 5)
print(f"    hypot(7, 24): {math.hypot(7, 24)}") # 25.0


print("\n--- 5. Trigonometric Functions (`cmath` module - for complex numbers) ---")

# The `cmath` module provides complex-aware versions of the trigonometric functions.
# These functions can take and return complex numbers. Angles are in radians.

z_complex = 0.5 + 0.8j

# 5.1 `cmath.sin(z)`: Complex sine
print(f"\n5.1 Complex Sine for z={z_complex}: {cmath.sin(z_complex):.4f}")

# 5.2 `cmath.cos(z)`: Complex cosine
print(f"5.2 Complex Cosine for z={z_complex}: {cmath.cos(z_complex):.4f}")

# 5.3 `cmath.tan(z)`: Complex tangent
print(f"5.3 Complex Tangent for z={z_complex}: {cmath.tan(z_complex):.4f}")

# 5.4 Inverse Complex Trigonometric Functions (`cmath`)
# `cmath.asin(z)`, `cmath.acos(z)`, `cmath.atan(z)`
print(f"\n5.4 Inverse Complex Sine for z={z_complex}: {cmath.asin(z_complex):.4f}")


print("\n--- 6. Constants (`math` and `cmath` modules) ---")

# Both modules provide useful mathematical constants.

# 6.1 `math.pi`: The mathematical constant pi (π).
print(f"6.1 math.pi: {math.pi}")

# 6.2 `math.e`: The mathematical constant e (Euler's number).
print(f"6.2 math.e: {math.e}")

# 6.3 `cmath.pi` and `cmath.e` are aliases to `math.pi` and `math.e`.
print(f"6.3 cmath.pi: {cmath.pi}")
print(f"6.4 cmath.e: {cmath.e}")