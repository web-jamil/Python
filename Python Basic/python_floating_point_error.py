import decimal
import math

# --- 1. Basic Floating Point Inaccuracy Demonstration ---
# This shows that many decimal numbers cannot be perfectly represented in binary floating-point.

def basic_inaccuracy():
    print("\n--- 1. Basic Floating Point Inaccuracy Demonstration ---")
    
    # Simple addition that shows a tiny error
    a = 0.1
    b = 0.2
    c = 0.3
    
    sum_ab = a + b
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"a + b = {sum_ab}")
    
    print(f"Does (a + b) == c? {sum_ab == c}") # Expected: False due to inaccuracy
    print(f"Raw (a + b) value: {sum_ab:.17f}") # Show full precision to see the error
    print(f"Raw c value:       {c:.17f}")
    
    # Another common example
    num = 1.23
    product = num * 3
    print(f"\n1.23 * 3 = {product}")
    print(f"Expected: 3.69")
    print(f"Raw value: {product:.17f}")
    
    # Repeated addition
    total = 0.0
    for _ in range(10):
        total += 0.1
    print(f"\n10 * 0.1 = {total}")
    print(f"Expected: 1.0")
    print(f"Does 10 * 0.1 == 1.0? {total == 1.0}")
    print(f"Raw value: {total:.17f}")

# --- 2. Floating Point Comparisons (Using Tolerances) ---
# Because of inaccuracies, direct equality checks (==) with floats are unreliable.
# Instead, check if the absolute difference is within a small tolerance (epsilon).

def tolerant_comparison():
    print("\n--- 2. Floating Point Comparisons (Using Tolerances) ---")
    
    val1 = 0.1 + 0.2
    val2 = 0.3
    
    # Bad comparison
    print(f"Direct comparison: {val1 == val2}")
    
    epsilon = 1e-9 # A common small tolerance value (10^-9)
    
    # Good comparison
    is_close = abs(val1 - val2) < epsilon
    print(f"Comparison with epsilon ({epsilon}): {is_close}")
    
    # Python 3.5+ has math.isclose() which is even better
    # It accounts for relative and absolute tolerances.
    print(f"Using math.isclose(): {math.isclose(val1, val2)}")
    print(f"Using math.isclose(rel_tol=1e-09, abs_tol=0.0): {math.isclose(val1, val2, rel_tol=1e-09, abs_tol=0.0)}")
    
    print("\nExample with larger numbers (where relative tolerance matters more):")
    large_num1 = 123456789.123456789
    large_num2 = 123456789.123456790 # Very slightly different
    
    print(f"large_num1: {large_num1:.10f}")
    print(f"large_num2: {large_num2:.10f}")
    
    print(f"Direct comparison: {large_num1 == large_num2}")
    print(f"abs(large_num1 - large_num2): {abs(large_num1 - large_num2):.10f}")
    
    # Using a small absolute tolerance might fail for large numbers
    print(f"math.isclose() with default tolerances: {math.isclose(large_num1, large_num2)}")
    # Default relative tolerance (rel_tol) is 1e-09, absolute tolerance (abs_tol) is 0.0

# --- 3. Loss of Precision in Large Calculations ---
# As numbers get very large or very small, adding/subtracting small numbers can have no effect.

def precision_loss():
    print("\n--- 3. Loss of Precision in Large Calculations ---")
    
    huge_number = 1.0e20 # A very large number
    small_number = 1.0   # A small number
    
    result = huge_number + small_number
    
    print(f"Huge number: {huge_number}")
    print(f"Small number: {small_number}")
    print(f"Huge + Small = {result}")
    print(f"Does (Huge + Small) == Huge? {result == huge_number}") # Expected: True
    
    print("\nSimilarly, with very small numbers:")
    very_small = 1e-20
    even_smaller = 1e-30
    
    result_small = very_small + even_smaller
    print(f"Very small: {very_small}")
    print(f"Even smaller: {even_smaller}")
    print(f"Very small + Even smaller = {result_small}")
    print(f"Does (Very small + Even smaller) == Very small? {result_small == very_small}")

# --- 4. Special Floating Point Values: NaN, Inf ---
# Not-a-Number (NaN) and Infinity (Inf) arise from undefined or overflow operations.

def special_float_values():
    print("\n--- 4. Special Floating Point Values: NaN, Inf ---")
    
    # Division by zero for floats results in Infinity
    pos_inf = 1.0 / 0.0
    neg_inf = -1.0 / 0.0
    print(f"1.0 / 0.0 = {pos_inf}")
    print(f"-1.0 / 0.0 = {neg_inf}")
    
    # Operations with Infinity
    print(f"inf + 1 = {pos_inf + 1}")
    print(f"inf * 2 = {pos_inf * 2}")
    print(f"inf / inf = {pos_inf / pos_inf}") # Results in NaN
    
    # Not-a-Number (NaN)
    nan_val = 0.0 / 0.0
    print(f"0.0 / 0.0 = {nan_val}")
    
    # Properties of NaN: It does not equal itself!
    print(f"Is NaN == NaN? {nan_val == nan_val}") # Expected: False
    print(f"Is NaN < 0? {nan_val < 0}")
    print(f"Is NaN > 0? {nan_val > 0}")
    
    # Use math.isnan() and math.isinf() to check for these
    print(f"Is {nan_val} NaN? {math.isnan(nan_val)}")
    print(f"Is {pos_inf} Inf? {math.isinf(pos_inf)}")
    
    # Propagating NaNs
    result_with_nan = nan_val + 5.0
    print(f"NaN + 5.0 = {result_with_nan}")
    print(f"Is {result_with_nan} NaN? {math.isnan(result_with_nan)}")

# --- 5. Mitigating Floating Point Issues with `decimal` Module ---
# The `decimal` module provides arbitrary-precision decimal arithmetic.
# Use it for financial calculations or when exact decimal representation is crucial.

def using_decimal_module():
    print("\n--- 5. Mitigating with `decimal` Module ---")
    
    # Default floating point
    a_float = 0.1
    b_float = 0.2
    sum_float = a_float + b_float
    print(f"Float: 0.1 + 0.2 = {sum_float:.17f}")
    print(f"Float comparison with 0.3: {sum_float == 0.3}")
    
    # Using Decimal
    # Convert strings to Decimal to ensure exact representation
    a_dec = decimal.Decimal('0.1')
    b_dec = decimal.Decimal('0.2')
    sum_dec = a_dec + b_dec
    target_dec = decimal.Decimal('0.3')
    
    print(f"Decimal: 0.1 + 0.2 = {sum_dec}")
    print(f"Decimal comparison with 0.3: {sum_dec == target_dec}")
    
    # Setting precision (context) for Decimal operations
    print("\nSetting Decimal precision:")
    with decimal.localcontext() as ctx:
        ctx.prec = 4 # Set precision to 4 significant digits
        val1 = decimal.Decimal('1.0') / decimal.Decimal('3.0')
        print(f"1/3 with precision 4: {val1}")
    
    with decimal.localcontext() as ctx:
        ctx.prec = 20 # Set precision to 20 significant digits
        val2 = decimal.Decimal('1.0') / decimal.Decimal('3.0')
        print(f"1/3 with precision 20: {val2}")

    # Financial calculation example
    # Imagine calculating interest or currency conversions
    principal = decimal.Decimal('100.50')
    rate = decimal.Decimal('0.05') # 5%
    interest = principal * rate
    total = principal + interest
    
    print(f"\nFinancial calculation:")
    print(f"Principal: {principal}")
    print(f"Interest (5%): {interest}")
    print(f"Total: {total}")

# --- Main execution block ---
if __name__ == "__main__":
    basic_inaccuracy()
    input("\nPress Enter to run the next example: Tolerant Comparisons...")
    
    tolerant_comparison()
    input("\nPress Enter to run the next example: Loss of Precision...")
    
    precision_loss()
    input("\nPress Enter to run the next example: Special Float Values (NaN, Inf)...")
    
    special_float_values()
    input("\nPress Enter to run the next example: Using `decimal` Module...")
    
    using_decimal_module()
    
    print("\nAll Floating Point Error demonstrations concluded.")


import decimal
import math

# --- 1. Class for Demonstrating Basic Floating Point Inaccuracy ---
class FloatInaccuracyDemo:
    def __init__(self):
        self.a = 0.1
        self.b = 0.2
        self.c = 0.3

    def demonstrate(self):
        print("\n--- 1. Class for Basic Floating Point Inaccuracy ---")
        sum_ab = self.a + self.b
        
        print(f"  a = {self.a}")
        print(f"  b = {self.b}")
        print(f"  c = {self.c}")
        print(f"  a + b = {sum_ab}")
        print(f"  Does (a + b) == c? {sum_ab == self.c}")
        print(f"  Raw (a + b) value: {sum_ab:.17f}")
        print(f"  Raw c value:       {self.c:.17f}")
        
        total_repeated_sum = 0.0
        for _ in range(10):
            total_repeated_sum += 0.1
        print(f"  \n10 * 0.1 (repeated addition) = {total_repeated_sum}")
        print(f"  Does 10 * 0.1 == 1.0? {total_repeated_sum == 1.0}")
        print(f"  Raw value: {total_repeated_sum:.17f}")
        print("  Demonstration complete.")

# --- 2. Class for Tolerant Floating Point Comparisons ---
class FloatComparisonHandler:
    def __init__(self, epsilon=1e-9):
        self.epsilon = epsilon # Default small tolerance

    def are_close(self, val1, val2, rel_tol=1e-09, abs_tol=0.0):
        """
        Compares two floats using a tolerance.
        Prioritizes math.isclose() for robustness.
        """
        return math.isclose(val1, val2, rel_tol=rel_tol, abs_tol=abs_tol)

    def demonstrate(self):
        print("\n--- 2. Class for Tolerant Floating Point Comparisons ---")
        val_sum = 0.1 + 0.2
        val_target = 0.3
        
        print(f"  Value 1 (0.1 + 0.2): {val_sum:.17f}")
        print(f"  Value 2 (0.3):       {val_target:.17f}")
        
        print(f"  Direct comparison (val1 == val2): {val_sum == val_target}")
        
        print(f"  Using custom epsilon ({self.epsilon}) check: {abs(val_sum - val_target) < self.epsilon}")
        print(f"  Using math.isclose() (defaults): {self.are_close(val_sum, val_target)}")
        print(f"  Using math.isclose(rel_tol=1e-09): {self.are_close(val_sum, val_target, rel_tol=1e-09)}")

        print("\n  Example with larger numbers:")
        large_a = 123456789.123456789
        large_b = 123456789.123456790
        print(f"  Large A: {large_a:.10f}")
        print(f"  Large B: {large_b:.10f}")
        print(f"  Are close (defaults)? {self.are_close(large_a, large_b)}") # Will be True as default rel_tol is sufficient
        print(f"  Are close (abs_tol=1e-15 only)? {self.are_close(large_a, large_b, rel_tol=0.0, abs_tol=1e-15)}") # False, requires larger abs_tol
        print("  Demonstration complete.")

# --- 3. Class for Demonstrating Loss of Precision ---
class PrecisionLossDemo:
    def demonstrate(self):
        print("\n--- 3. Class for Loss of Precision in Large Calculations ---")
        
        huge_num = 1.0e20
        small_num = 1.0
        result_add = huge_num + small_num
        
        print(f"  Huge number: {huge_num}")
        print(f"  Small number: {small_num}")
        print(f"  Huge + Small = {result_add}")
        print(f"  Does (Huge + Small) == Huge? {result_add == huge_num}")
        
        very_small_num = 1e-20
        even_smaller_num = 1e-30
        result_add_small = very_small_num + even_smaller_num
        
        print(f"  \nVery small: {very_small_num}")
        print(f"  Even smaller: {even_smaller_num}")
        print(f"  Very small + Even smaller = {result_add_small}")
        print(f"  Does (Very small + Even smaller) == Very small? {result_add_small == very_small_num}")
        print("  Demonstration complete.")

# --- 4. Class for Special Floating Point Values (NaN, Inf) ---
class SpecialFloatValues:
    def demonstrate(self):
        print("\n--- 4. Class for Special Floating Point Values: NaN, Inf ---")
        
        pos_inf = float('inf')
        neg_inf = float('-inf')
        nan_val = float('nan')
        
        print(f"  Positive Infinity: {pos_inf}")
        print(f"  Negative Infinity: {neg_inf}")
        print(f"  Not-a-Number (NaN): {nan_val}")
        
        # Operations leading to Inf
        print(f"  1.0 / 0.0: {1.0 / 0.0}")
        print(f"  -1.0 / 0.0: {-1.0 / 0.0}")
        
        # Operations leading to NaN
        print(f"  0.0 / 0.0: {0.0 / 0.0}")
        print(f"  inf - inf: {pos_inf - pos_inf}")
        print(f"  inf / inf: {pos_inf / pos_inf}")
        
        # NaN properties
        print(f"  Is NaN == NaN? {nan_val == nan_val}") # Always False
        print(f"  Is math.isnan(NaN)? {math.isnan(nan_val)}")
        print(f"  Is math.isinf(inf)? {math.isinf(pos_inf)}")
        print(f"  NaN + 10: {nan_val + 10.0}") # NaN propagates
        print("  Demonstration complete.")

# --- 5. Class for Mitigating Floating Point Issues with `decimal` Module ---
class DecimalArithmeticHandler:
    def __init__(self, precision=28): # Default precision for decimal.Context
        self.precision = precision
        decimal.getcontext().prec = precision # Set global context precision

    def calculate_sum(self, val1_str, val2_str):
        d1 = decimal.Decimal(val1_str)
        d2 = decimal.Decimal(val2_str)
        return d1 + d2

    def demonstrate(self):
        print("\n--- 5. Class for Mitigating with `decimal` Module ---")
        
        print(f"  Global Decimal precision set to: {decimal.getcontext().prec}")

        # Inaccuracy with floats
        float_sum = 0.1 + 0.2
        print(f"  Float: 0.1 + 0.2 = {float_sum:.17f}")
        print(f"  Float comparison with 0.3: {float_sum == 0.3}")
        
        # Accuracy with Decimals
        decimal_sum = self.calculate_sum('0.1', '0.2')
        print(f"  Decimal: 0.1 + 0.2 = {decimal_sum}")
        print(f"  Decimal comparison with 0.3: {decimal_sum == decimal.Decimal('0.3')}")

        print("\n  Using localcontext for temporary precision changes:")
        with decimal.localcontext() as ctx:
            ctx.prec = 4
            result_div = decimal.Decimal('1.0') / decimal.Decimal('3.0')
            print(f"  1/3 with precision 4: {result_div}")
        
        with decimal.localcontext() as ctx:
            ctx.prec = 10
            result_div = decimal.Decimal('1.0') / decimal.Decimal('3.0')
            print(f"  1/3 with precision 10: {result_div}")

        # Financial calculation
        principal = decimal.Decimal('1000.75')
        interest_rate = decimal.Decimal('0.0725') # 7.25%
        calculated_interest = principal * interest_rate
        total_amount = principal + calculated_interest
        
        print(f"\n  Financial example (Decimal):")
        print(f"  Principal: {principal}")
        print(f"  Interest (7.25%): {calculated_interest}")
        print(f"  Total: {total_amount}")
        print("  Demonstration complete.")

# --- Main execution block ---
if __name__ == "__main__":
    
    inaccuracy_demo = FloatInaccuracyDemo()
    inaccuracy_demo.demonstrate()
    
    input("\nPress Enter to run the next example: Tolerant Comparisons (Class)...")
    
    comparison_handler = FloatComparisonHandler()
    comparison_handler.demonstrate()
    
    input("\nPress Enter to run the next example: Precision Loss (Class)...")
    
    precision_loss_demo = PrecisionLossDemo()
    precision_loss_demo.demonstrate()
    
    input("\nPress Enter to run the next example: Special Float Values (Class)...")
    
    special_floats_demo = SpecialFloatValues()
    special_floats_demo.demonstrate()
    
    input("\nPress Enter to run the next example: Decimal Module (Class)...")
    
    decimal_handler = DecimalArithmeticHandler(precision=50) # Use higher precision for this demo
    decimal_handler.demonstrate()
    
    print("\nAll Floating Point Error demonstrations using classes concluded.")