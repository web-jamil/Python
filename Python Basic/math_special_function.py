import math

# Special functions in the math module

print("--- Error Function (erf) ---")
# The error function erf(x) is a sigmoid function that occurs in probability, statistics, and partial differential equations.
x = 0.5
print(f"Error function of {x} (math.erf({x})): {math.erf(x)}")
x = 1.0
print(f"Error function of {x} (math.erf({x})): {math.erf(x)}")
x = -1.0
print(f"Error function of {x} (math.erf({x})): {math.erf(x)}")

print("\n--- Complementary Error Function (erfc) ---")
# The complementary error function erfc(x) is defined as 1 - erf(x).
x = 0.5
print(f"Complementary error function of {x} (math.erfc({x})): {math.erfc(x)}")
print(f"1 - erf({x}): {1 - math.erf(x)}") # Should be the same

print("\n--- Gamma Function (gamma) ---")
# The Gamma function is a generalization of the factorial function to complex and real numbers.
# For a positive integer n, gamma(n) = (n-1)!
x_int = 5
print(f"Gamma function of {x_int} (math.gamma({x_int})): {math.gamma(x_int)}") # Should be (5-1)! = 4! = 24
x_float = 2.5
print(f"Gamma function of {x_float} (math.gamma({x_float})): {math.gamma(x_float)}")

try:
    print(f"Gamma function of 0: {math.gamma(0)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
try:
    print(f"Gamma function of -1: {math.gamma(-1)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

print("\n--- Natural Logarithm of the Absolute Value of the Gamma Function (lgamma) ---")
# lgamma(x) computes the natural logarithm of the absolute value of the Gamma function.
# This is often more numerically stable than computing gamma(x) and then taking the logarithm.
x_pos = 5
print(f"Natural log of |Gamma({x_pos})| (math.lgamma({x_pos})): {math.lgamma(x_pos)}")
print(f"ln(math.fabs(math.gamma({x_pos}))): {math.log(math.fabs(math.gamma(x_pos)))}") # Should be similar

x_float_neg = -2.5
print(f"Natural log of |Gamma({x_float_neg})| (math.lgamma({x_float_neg})): {math.lgamma(x_float_neg)}")

try:
    print(f"Natural log of |Gamma(0)|: {math.lgamma(0)}") # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")