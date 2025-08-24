import math
import sys

# --- 1. Basic OverflowError with Floating-Point Numbers ---
# OverflowError specifically applies to floating-point calculations
# where the result is too large to be represented as a float.
# Integers in Python 3+ handle arbitrary precision, so they don't typically overflow.

def basic_float_overflow_function():
    print("\n--- 1. Function: Basic Floating-Point Overflow ---")
    
    # Python's maximum float value
    max_float = sys.float_info.max
    print(f"  System's largest representable float (sys.float_info.max): {max_float:.2e}")

    large_number = 1.8e308 # A number close to sys.float_info.max
    multiplier = 2.0

    try:
        print(f"  Attempting to calculate: {large_number:.2e} * {multiplier}")
        result = large_number * multiplier
        print(f"  Result: {result}") # This will likely print 'inf' (infinity)
        
        # Check if it became infinity
        if math.isinf(result):
            print("  [INFO] Result is 'inf' (infinity). This indicates an overflow.")
            # While it doesn't always raise OverflowError for simple multiplication
            # leading to inf, it's an overflow condition.
            # OverflowError is more likely with certain math functions.

    except OverflowError:
        print(f"  [CAUGHT ERROR] OverflowError: Result of operation exceeded maximum float value.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Basic floating-point overflow demonstration finished.")

# --- 2. OverflowError with math functions ---
# Certain functions in the `math` module are more prone to raising OverflowError
# when results exceed float limits, rather than silently returning `inf`.

def math_function_overflow_function():
    print("\n--- 2. Function: math Module Function Overflow ---")

    # math.exp(x) - e to the power of x. Grows very rapidly.
    # e^710 is already too large for standard float
    exponent_value = 710.0 
    try:
        print(f"  Attempting to calculate math.exp({exponent_value})...")
        result_exp = math.exp(exponent_value)
        print(f"  math.exp({exponent_value}) = {result_exp}")
        if math.isinf(result_exp):
            print(f"  [INFO] Result is 'inf'.")
    except OverflowError:
        print(f"  [CAUGHT ERROR] OverflowError: math.exp({exponent_value}) result is too large.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")

    print("-" * 30)

    # math.pow(x, y) - x to the power of y.
    base = 10.0
    power = 310.0 # 10^310 is beyond float limit
    try:
        print(f"  Attempting to calculate math.pow({base}, {power})...")
        result_pow = math.pow(base, power)
        print(f"  math.pow({base}, {power}) = {result_pow}")
        if math.isinf(result_pow):
            print(f"  [INFO] Result is 'inf'.")
    except OverflowError:
        print(f"  [CAUGHT ERROR] OverflowError: math.pow({base}, {power}) result is too large.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  math module function overflow demonstration finished.")

# --- 3. Integer Overflow (Not an OverflowError in Python 3+) ---
# Python 3+ integers have arbitrary precision, meaning they automatically
# expand to accommodate any size, limited only by available memory.
# This means `OverflowError` is NOT raised for integer calculations.

def integer_arbitrary_precision_function():
    print("\n--- 3. Function: Integer Arbitrary Precision (No OverflowError) ---")
    
    very_large_int = 10**100 # A googol
    another_large_int = 10**100
    
    product_int = very_large_int * another_large_int
    sum_int = very_large_int + another_large_int
    power_int = 2**(1000) # A very very large number

    print(f"  (10^100) * (10^100) = 10^{len(str(product_int)) - 1}")
    print(f"  Number of digits in product: {len(str(product_int))}")
    print(f"  2^1000 has {len(str(power_int))} digits.")
    
    try:
        print("  Attempting to create an extremely large integer and multiply...")
        # This will succeed and use more memory, but not raise OverflowError.
        # It might lead to MemoryError eventually if it exhausts RAM.
        huge_int = 1
        for _ in range(50000): # Create an int with potentially millions of digits
            huge_int *= 123456789
        
        print(f"  Largest integer created successfully. First 20 digits: {str(huge_int)[:20]}...")
        print(f"  Total digits: {len(str(huge_int))}")

    except OverflowError: # This block will NOT be executed in Python 3+
        print(f"  [CAUGHT ERROR] OverflowError: (This will not happen for integers in Python 3+).")
    except MemoryError:
        print(f"  [CAUGHT ERROR] MemoryError: The integer became too large for available RAM.")
    except Exception as e:
        print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
    finally:
        print("  Integer arbitrary precision demonstration finished.")

# --- 4. Class for Demonstrating Floating-Point Overflow ---
class FloatOverflowCalculator:
    def __init__(self):
        self.max_float = sys.float_info.max

    def calculate_product(self, num1, num2):
        print(f"\n--- Class: FloatOverflowCalculator - Product Calculation ---")
        try:
            print(f"  Attempting {num1:.2e} * {num2:.2e}")
            result = num1 * num2
            print(f"  Result: {result}")
            if math.isinf(result) and result > 0:
                print("  [INFO] Result is positive infinity (overflow detected).")
            elif math.isinf(result) and result < 0:
                print("  [INFO] Result is negative infinity (underflow to negative inf).")
            return result
        except OverflowError:
            print(f"  [CAUGHT ERROR] OverflowError: Product exceeded maximum float value.")
            return float('inf') # Explicitly return infinity on overflow
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return None

    def calculate_exp(self, value):
        print(f"\n--- Class: FloatOverflowCalculator - Exponential Calculation ---")
        try:
            print(f"  Attempting math.exp({value})")
            result = math.exp(value)
            print(f"  Result: {result}")
            if math.isinf(result):
                print("  [INFO] Result is infinity (overflow detected).")
            return result
        except OverflowError:
            print(f"  [CAUGHT ERROR] OverflowError: math.exp({value}) result is too large.")
            return float('inf')
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return None

# --- 5. Class for Integer "Overflow" (MemoryError, not OverflowError) ---
class LargeIntegerGenerator:
    def __init__(self):
        pass

    def generate_huge_number(self, power_of_two):
        print(f"\n--- Class: LargeIntegerGenerator - Generating 2^{power_of_two} ---")
        try:
            print(f"  Calculating 2 to the power of {power_of_two}...")
            # This operation generates an integer with (power_of_two // 3) * log10(2) digits approximately.
            # At around 2**30000000, it might hit MemoryError on some systems.
            result = 2**power_of_two
            print(f"  Successfully calculated. Number of digits: {len(str(result))}")
            # print(f"  First 20 digits: {str(result)[:20]}...") # Uncomment to see part of the huge number
            return result
        except OverflowError: # This will NOT be caught in Python 3+
            print(f"  [CAUGHT ERROR] OverflowError: (This is not expected for integers in Python 3+).")
            return None
        except MemoryError:
            print(f"  [CAUGHT ERROR] MemoryError: Integer became too large for available RAM.")
            return None
        except Exception as e:
            print(f"  [UNEXPECTED ERROR] {type(e).__name__}: {e}")
            return None

# --- Main execution block ---
if __name__ == "__main__":
    
    basic_float_overflow_function()
    input("\nPress Enter to run the next example: math function overflow...")
    
    math_function_overflow_function()
    input("\nPress Enter to run the next example: Integer arbitrary precision...")
    
    integer_arbitrary_precision_function()
    input("\nPress Enter to run the next example: Class-based Floating-Point Overflow...")

    float_calc = FloatOverflowCalculator()
    float_calc.calculate_product(sys.float_info.max, 1.1)
    float_calc.calculate_exp(710.0) # Will likely raise OverflowError
    float_calc.calculate_exp(100.0) # Should succeed

    input("\nPress Enter to run the next example: Class-based Large Integer Generator...")

    int_gen = LargeIntegerGenerator()
    int_gen.generate_huge_number(100000) # Should succeed
    # int_gen.generate_huge_number(30000000) # This might cause MemoryError on systems with limited RAM
    
    print("\nAll OverflowError demonstrations concluded.")