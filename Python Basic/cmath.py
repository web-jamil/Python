import cmath # For advanced complex math functions

# Creating complex numbers
z1 = 3 + 4j
z2 = complex(5, -2) # Another way to create a complex number

print(f"z1: {z1}")
print(f"z2: {z2}")

# Accessing real and imaginary parts
print(f"Real part of z1: {z1.real}")
print(f"Imaginary part of z1: {z1.imag}")

# Basic arithmetic operations
sum_z = z1 + z2
diff_z = z1 - z2
prod_z = z1 * z2
div_z = z1 / z2

print(f"Sum: {sum_z}")
print(f"Difference: {diff_z}")
print(f"Product: {prod_z}")
print(f"Division: {div_z}")

# Magnitude (modulus)
magnitude_z1 = abs(z1)
print(f"Magnitude of z1: {magnitude_z1}")

# Conjugate
conjugate_z1 = z1.conjugate()
print(f"Conjugate of z1: {conjugate_z1}")

# Phase (argument)
phase_z1 = cmath.phase(z1)
print(f"Phase of z1 (radians): {phase_z1}")
print(f"Phase of z1 (degrees): {cmath.degrees(phase_z1)}")

# Polar representation
r, phi = cmath.polar(z1)
print(f"Polar coordinates of z1: r={r}, phi={phi}")

# Converting from polar to rectangular
rect_z = cmath.rect(r, phi)
print(f"Rectangular form from polar: {rect_z}")

# Other cmath functions
print(f"e to the power of z1: {cmath.exp(z1)}")
print(f"Sine of z1: {cmath.sin(z1)}")
print(f"Square root of z1: {cmath.sqrt(z1)}")