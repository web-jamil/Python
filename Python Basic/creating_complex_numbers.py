# --- Python Complex Numbers: All About Creating Them in Code ---

# Python has built-in support for complex numbers, which are numbers
# of the form `a + bj`, where `a` is the real part, `b` is the imaginary part,
# and `j` (or `i` in mathematics) is the imaginary unit (square root of -1).

# --- 1. Basic Creation using `j` or `J` Suffix (Literal Syntax) ---

print("--- 1. Basic Creation using `j` or `J` Suffix ---")

# This is the most common, direct, and readable way to define a complex number
# when you know its real and imaginary parts directly. The `j` (or `J`)
# suffix directly indicates the imaginary part.

# 1.1 Complex number with both real and imaginary parts
# Syntax: `real_part + imaginary_part_numberj`
z1 = 2 + 3j
print(f"1.1 z1 = 2 + 3j: {z1}, Type: {type(z1)}")
# Output: (2+3j), <class 'complex'>

# 1.2 Pure imaginary number (real part is zero)
# The real part can be omitted if it's zero.
z2 = 5j
print(f"1.2 z2 = 5j: {z2}, Type: {type(z2)}")
# Python often displays pure imaginary numbers as `(0+5j)` or just `5j` depending on context.

z3 = -1.5j
print(f"    z3 = -1.5j: {z3}, Type: {type(z3)}")

# 1.3 Pure real number (imaginary part is zero)
# You can explicitly write `+0j` if you want a complex number representation
# for a purely real number. Otherwise, it's just an int or float.
z4 = 7 + 0j
print(f"1.3 z4 = 7 + 0j: {z4}, Type: {type(z4)}")
# Output: (7+0j)

# 1.4 Using `J` instead of `j` (case-insensitive)
# Python accepts both lowercase `j` and uppercase `J`.
z5 = 10 + 20J
print(f"1.4 z5 = 10 + 20J: {z5}, Type: {type(z5)}")


# --- 2. Using the `complex()` Constructor ---

print("\n--- 2. Using the `complex()` Constructor ---")

# The `complex()` constructor is a flexible way to create complex numbers,
# especially useful when parts are variables or for type conversion.
# Syntax: `complex(real_part, imaginary_part)`

# 2.1 With both real and imaginary parts as arguments
# The first argument is the real part, the second is the imaginary part.
r_val = 2
i_val = 3
z_a = complex(r_val, i_val) # Equivalent to 2 + 3j
print(f"2.1 z_a = complex({r_val}, {i_val}): {z_a}, Type: {type(z_a)}")

z_b = complex(-1, -4) # Equivalent to -1 - 4j
print(f"    z_b = complex(-1, -4): {z_b}, Type: {type(z_b)}")

# 2.2 With only the real part (imaginary part defaults to 0)
# If only one argument is provided, it's treated as the real part, and the
# imaginary part defaults to 0.
z_c = complex(7) # Equivalent to 7 + 0j
print(f"2.2 z_c = complex(7): {z_c}, Type: {type(z_c)}")

# 2.3 With only the imaginary part (real part must be explicitly 0)
# If you want a pure imaginary number using the constructor, you must
# explicitly pass 0 for the real part.
z_d = complex(0, 5) # Equivalent to 5j
print(f"2.3 z_d = complex(0, 5): {z_d}, Type: {type(z_d)}")

# 2.4 Converting other numeric types to complex
# Arguments can be integers or floats.
z_e = complex(3.14, 2.71)
print(f"2.4 z_e = complex(3.14, 2.71): {z_e}, Type: {type(z_e)}")

# 2.5 Converting strings to complex numbers (single argument)
# The `complex()` constructor can parse a string representation of a complex number.
# The string must be in a valid format like "real+imagj", "real-imagj", "imagj", or "real".
z_f = complex("2+3j")
print(f"2.5 z_f = complex('2+3j'): {z_f}, Type: {type(z_f)}")

z_g = complex("-5j")
print(f"    z_g = complex('-5j'): {z_g}, Type: {type(z_g)}")

z_h = complex("10") # Converts the real number string to complex
print(f"    z_h = complex('10'): {z_h}, Type: {type(z_h)}")

# What happens if the string is not a valid complex number format? (ValueError)
try:
    complex("hello") # Invalid string
except ValueError as e:
    print(f"\n2.6 Error: {e} - String 'hello' is not a valid complex number.")

try:
    complex("2+3") # Missing 'j' for imaginary part
except ValueError as e:
    print(f"    Error: {e} - String '2+3' is not a valid complex number (missing 'j').")


# --- 3. Creating Complex Numbers from Polar Coordinates (using `cmath.rect()`) ---

print("\n--- 3. Creating Complex Numbers from Polar Coordinates ---")

# Complex numbers can also be represented in polar coordinates (magnitude `r` and
# phase `phi`). The `cmath.rect()` function allows you to convert from this
# polar form back to the standard rectangular `a + bj` form.

import cmath # You need to import the `cmath` module for this function.

# 3.1 Basic polar to rectangular conversion
# Syntax: `cmath.rect(magnitude, phase_in_radians)`
magnitude_val = 2.0
phase_val = cmath.pi / 2 # pi/2 radians = 90 degrees (points along positive imaginary axis)
z_polar_a = cmath.rect(magnitude_val, phase_val)
print(f"3.1 From magnitude {magnitude_val} and phase {phase_val:.4f} (90 deg): {z_polar_a:.4f}")
# Output will be approximately (0.0000+2.0000j) due to floating-point precision.

magnitude_val = 5.0
phase_val = cmath.pi # pi radians = 180 degrees (points along negative real axis)
z_polar_b = cmath.rect(magnitude_val, phase_val)
print(f"    From magnitude {magnitude_val} and phase {phase_val:.4f} (180 deg): {z_polar_b:.4f}")
# Output will be approximately (-5.0000+0.0000j).

# This method is primarily used when your input data is naturally in polar form
# (e.g., from signal processing or physics calculations) and you need to work
# with the complex number in its rectangular form.