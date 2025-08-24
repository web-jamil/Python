import math
import random
import decimal # For arbitrary-precision decimal floating-point arithmetic
from fractions import Fraction # For rational numbers

print("--- Python Numbers: Practice Code ---")

# --- 1. Integer Type (int) ---
print("\n--- 1. Integer Type (int) ---")
# Integers in Python have arbitrary precision (they can be as large as memory allows).

# 1.1 Basic integer creation
num_int = 10
negative_int = -5
large_int = 123456789012345678901234567890
print(f"num_int: {num_int} (Type: {type(num_int)})")
print(f"negative_int: {negative_int}")
print(f"large_int: {large_int}")

# 1.2 Integer Arithmetic Operations
a = 15
b = 4
print(f"\nGiven a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b} (Always returns a float)")
print(f"Floor Division (a // b): {a // b} (Returns integer part, rounds down)")
print(f"Modulo (a % b): {a % b} (Remainder of division)")
print(f"Exponentiation (a ** b): {a ** b} (a to the power of b)")

# 1.3 Built-in Functions for Integers
print(f"\nAbsolute value of -10: {abs(-10)}")
print(f"Divmod (a, b) returns (quotient, remainder): {divmod(a, b)}") # (a // b, a % b)


# --- 2. Floating-Point Type (float) ---
print("\n--- 2. Floating-Point Type (float) ---")
# Floats represent real numbers and are stored as double-precision (64-bit) values.
# They have limited precision due to how they are stored (binary representation).

# 2.1 Basic float creation
num_float = 3.14
negative_float = -0.5
scientific_notation = 1.23e5 # 1.23 * 10^5 = 123000.0
print(f"num_float: {num_float} (Type: {type(num_float)})")
print(f"negative_float: {negative_float}")
print(f"scientific_notation: {scientific_notation}")

# 2.2 Float Arithmetic Operations (similar to integers)
x = 7.5
y = 2.0
print(f"\nGiven x = {x}, y = {y}")
print(f"Addition (x + y): {x + y}")
print(f"Subtraction (x - y): {x - y}")
print(f"Multiplication (x * y): {x * y}")
print(f"Division (x / y): {x / y}")
print(f"Floor Division (x // y): {x // y}")
print(f"Modulo (x % y): {x % y}")
print(f"Exponentiation (x ** y): {x ** y}")

# 2.3 Floating-point Precision Issues (important concept)
print("\nFloating-point Precision Example:")
print(f"0.1 + 0.2: {0.1 + 0.2}") # Not exactly 0.3
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}") # Will be False
print("Due to internal binary representation, direct equality checks can be tricky.")
# For comparisons, often check if absolute difference is less than a small tolerance (epsilon).
epsilon = 1e-9
print(f"abs((0.1 + 0.2) - 0.3) < {epsilon}: {abs((0.1 + 0.2) - 0.3) < epsilon}")

# 2.4 Special Float Values
print("\nSpecial Float Values:")
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan') # Not A Number
print(f"Infinity: {infinity}, Type: {type(infinity)}")
print(f"Negative Infinity: {negative_infinity}")
print(f"Not A Number (NaN): {not_a_number}")
print(f"5 / 0: {float('inf')}") # Division by zero in float context
print(f"infinity + 1: {infinity + 1}")
print(f"infinity > 1000000: {infinity > 1000000}")
print(f"not_a_number == not_a_number: {not_a_number == not_a_number}") # NaN is never equal to anything, including itself


# --- 3. Complex Type (complex) ---
print("\n--- 3. Complex Type (complex) ---")
# Complex numbers are represented as (real + imaginary*j).

# 3.1 Basic complex creation
num_complex = 3 + 4j
another_complex = -1.5 - 2j
print(f"num_complex: {num_complex} (Type: {type(num_complex)})")
print(f"another_complex: {another_complex}")

# 3.2 Accessing real and imaginary parts
print(f"Real part of {num_complex}: {num_complex.real}")
print(f"Imaginary part of {num_complex}: {num_complex.imag}")

# 3.3 Complex Arithmetic Operations
c1 = 2 + 3j
c2 = 1 - 2j
print(f"\nGiven c1 = {c1}, c2 = {c2}")
print(f"Addition (c1 + c2): {c1 + c2}")
print(f"Subtraction (c1 - c2): {c1 - c2}")
print(f"Multiplication (c1 * c2): {c1 * c2}")
print(f"Division (c1 / c2): {c1 / c2}")
print(f"Conjugate of {c1}: {c1.conjugate()}")


# --- 4. Type Conversion (Casting) ---
print("\n--- 4. Type Conversion (Casting) ---")

# 4.1 int() conversion
print(f"int(3.14): {int(3.14)}")         # Truncates decimal part
print(f"int(-2.7): {int(-2.7)}")         # Truncates towards zero
print(f"int('123'): {int('123')}")       # Converts string to integer
# print(f"int('3.14'): {int('3.14')}")   # ValueError: invalid literal for int() with base 10: '3.14'

# 4.2 float() conversion
print(f"float(5): {float(5)}")
print(f"float('3.14'): {float('3.14')}")
print(f"float('1e-3'): {float('1e-3')}")

# 4.3 complex() conversion
print(f"complex(5): {complex(5)}")      # 5 + 0j
print(f"complex(3, 4): {complex(3, 4)}") # 3 + 4j
print(f"complex('1+2j'): {complex('1+2j')}")


# --- 5. Math Module (Common Mathematical Functions) ---
print("\n--- 5. Math Module ---")
# The 'math' module provides access to common mathematical functions and constants.

print(f"math.sqrt(25): {math.sqrt(25)}")
print(f"math.pow(2, 3): {math.pow(2, 3)}") # Returns float
print(f"math.ceil(4.1): {math.ceil(4.1)}")   # Rounds up
print(f"math.floor(4.9): {math.floor(4.9)}") # Rounds down
print(f"math.pi: {math.pi}")
print(f"math.e: {math.e}")
print(f"math.sin(math.pi/2): {math.sin(math.pi/2)}") # Sine of 90 degrees (in radians)
print(f"math.log10(100): {math.log10(100)}")


# --- 6. Comparison Operators ---
print("\n--- 6. Comparison Operators ---")
# Used to compare numerical values, returning True or False.

x = 10
y = 20
z = 10.0
print(f"x = {x}, y = {y}, z = {z}")
print(f"x == y: {x == y}")   # Equal to
print(f"x == z: {x == z}")   # Equal to (value-based, types can differ if values are same)
print(f"x != y: {x != y}")   # Not equal to
print(f"x < y: {x < y}")     # Less than
print(f"x > y: {x > y}")     # Greater than
print(f"x <= z: {x <= z}")   # Less than or equal to
print(f"y >= x: {y >= x}")   # Greater than or equal to


# --- 7. Random Numbers (using the 'random' module) ---
print("\n--- 7. Random Numbers ---")

print(f"Random integer between 1 and 10 (inclusive): {random.randint(1, 10)}")
print(f"Random float between 0.0 and 1.0 (exclusive of 1.0): {random.random()}")
print(f"Random float between 10.0 and 20.0 (inclusive): {random.uniform(10.0, 20.0)}")
my_list = [10, 20, 30, 40, 50]
print(f"Random choice from list {my_list}: {random.choice(my_list)}")

# To get reproducible random numbers (for testing/simulations)
random.seed(42) # Set the seed
print(f"Seeded random int (seed 42): {random.randint(1, 100)}")
print(f"Next seeded random int: {random.randint(1, 100)}")


# --- 8. Other Numeric Types (Briefly) ---
print("\n--- 8. Other Numeric Types (Briefly) ---")

# 8.1 Decimal Type (for precise decimal arithmetic)
# Useful for financial calculations where floating-point inaccuracies are unacceptable.
print("\nDecimal (from decimal module):")
decimal.getcontext().prec = 6 # Set precision for decimal operations
dec1 = decimal.Decimal('0.1')
dec2 = decimal.Decimal('0.2')
dec_sum = dec1 + dec2
print(f"Decimal(0.1) + Decimal(0.2): {dec_sum}")
print(f"Decimal sum == Decimal('0.3'): {dec_sum == decimal.Decimal('0.3')}") # Now True

# 8.2 Fraction Type (for rational numbers)
# Represents numbers as fractions (numerator/denominator).
print("\nFraction (from fractions module):")
frac1 = Fraction(1, 3)
frac2 = Fraction(1, 6)
frac_sum = frac1 + frac2
print(f"1/3 + 1/6: {frac_sum}") # Output will be 1/2
print(f"Fraction(10, 20): {Fraction(10, 20)}") # Automatically simplifies to 1/2


print("\n--- End of Python Numbers Practice Code ---")