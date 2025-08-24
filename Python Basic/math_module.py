import math

# Constants
print(f"π (pi): {math.pi}")
print(f"e (Euler's number): {math.e}")
print(f"tau (2*pi): {math.tau}")
print(f"infinity: {math.inf}")
print(f"negative infinity: {math.inf * -1}")
print(f"NaN (Not a Number): {math.nan}")

print("-" * 20)

# Numeric functions
x = 5.7
print(f"Absolute value of -10: {math.fabs(-10)}")
print(f"Ceiling of {x}: {math.ceil(x)}")
print(f"Floor of {x}: {math.floor(x)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Greatest common divisor of 12 and 18: {math.gcd(12, 18)}")
print(f"Is infinity (math.inf)? {math.isinf(math.inf)}")
print(f"Is infinity (10)? {math.isinf(10)}")
print(f"Is NaN (math.nan)? {math.isnan(math.nan)}")
print(f"Is NaN (10)? {math.isnan(10)}")
print(f"Remainder of 10 divided by 3: {math.fmod(10, 3)}") # Handles signs differently than %
print(f"Truncation of {x}: {math.trunc(x)}")
print(f"x raised to the power of 2 ({x}^2): {math.pow(x, 2)}")
print(f"Square root of 25: {math.sqrt(25)}")

print("-" * 20)

# Trigonometric functions (angles in radians)
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
print(f"Sine of {angle_degrees} degrees ({angle_radians:.4f} radians): {math.sin(angle_radians)}")
print(f"Cosine of {angle_degrees} degrees ({angle_radians:.4f} radians): {math.cos(angle_radians)}")
print(f"Tangent of {angle_degrees} degrees ({angle_radians:.4f} radians): {math.tan(angle_radians)}")
print(f"Arcsine of 0.5 (in radians): {math.asin(0.5)}")
print(f"Arccosine of 0.5 (in radians): {math.acos(0.5)}")
print(f"Arctangent of 1 (in radians): {math.atan(1)}")
print(f"Arctangent of y/x, correctly handles signs (atan2(4, 3)): {math.atan2(4, 3)}")
print(f"Convert radians back to degrees (from {angle_radians:.4f}): {math.degrees(angle_radians)}")

print("-" * 20)

# Hyperbolic functions
x = 1.5
print(f"Hyperbolic sine of {x}: {math.sinh(x)}")
print(f"Hyperbolic cosine of {x}: {math.cosh(x)}")
print(f"Hyperbolic tangent of {x}: {math.tanh(x)}")
print(f"Inverse hyperbolic sine of 2: {math.asinh(2)}")
print(f"Inverse hyperbolic cosine of 2: {math.acosh(2)}")
print(f"Inverse hyperbolic tangent of 0.5: {math.atanh(0.5)}")

print("-" * 20)

# Exponential and logarithmic functions
print(f"e raised to the power of 2 (e^2): {math.exp(2)}")
print(f"Natural logarithm of e (ln(e)): {math.log(math.e)}")
print(f"Base-10 logarithm of 100 (log10(100)): {math.log10(100)}")
print(f"Logarithm of 8 with base 2 (log(8, 2)): {math.log(8, 2)}") # Can specify base
print(f"e raised to the power of x minus 1 (expm1(2)): {math.expm1(2)}") # More accurate for small x
print(f"Natural logarithm of 1 + x (log1p(0.5)): {math.log1p(0.5)}") # More accurate for small x

print("-" * 20)

# Power and logarithmic functions (already covered some above)
# math.pow(x, y) - already shown
# math.sqrt(x) - already shown
# math.log(x[, base]) - already shown
# math.log1p(x) - already shown
# math.log2(x) - base-2 logarithm
print(f"Base-2 logarithm of 8 (log2(8)): {math.log2(8)}")
# math.log10(x) - already shown

print("-" * 20)

# Angular conversion (already covered above)
# math.degrees(x) - already shown
# math.radians(x) - already shown

print("-" * 20)

# Special functions
print(f"Error function of 0.5 (erf(0.5)): {math.erf(0.5)}")
print(f"Complementary error function of 0.5 (erfc(0.5)): {math.erfc(0.5)}")
print(f"Gamma function of 5: {math.gamma(5)}")
print(f"Natural logarithm of the absolute value of the Gamma function of 5: {math.lgamma(5)}")

print("-" * 20)

# Floating point representation
y = 3.14159
print(f"Check if {y} is finite: {math.isfinite(y)}")
print(f"Check if infinity is finite: {math.isfinite(math.inf)}")
print(f"Check if {y} is an integer: {math.isclose(y, round(y))}") # Using isclose for practical comparison
print(f"Check if 5.0 is an integer: {math.isclose(5.0, round(5.0))}")
print(f"Return x * (2**i) (ldexp(1.5, 3)): {math.ldexp(1.5, 3)}")
print(f"Return the mantissa and exponent of {y}: {math.frexp(y)}") # Returns (mantissa, exponent) where y = mantissa * 2**exponent
print(f"Sum of elements in an iterable (fsum([0.1] * 10)): {math.fsum([0.1] * 10)}") # More accurate for sums of floats