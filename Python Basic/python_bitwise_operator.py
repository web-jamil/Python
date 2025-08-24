print("--- Python Bitwise Operators: Practice Code ---")

# Helper function to display numbers in binary
def to_binary(num, bits=8):
    if num >= 0:
        return bin(num)[2:].zfill(bits)
    else:
        # For negative numbers, show the 2's complement representation if possible within `bits`
        # This is a simplification; Python's integers have arbitrary precision
        # and negative numbers are handled via two's complement conceptually.
        # For small numbers, this illustrates the common 8-bit or 16-bit view.
        return bin(num & (2**bits - 1))[2:].zfill(bits)

print("Helper: to_binary(num, bits) - Converts integer to binary string (e.g., 8-bit representation)")
print(f"to_binary(5): {to_binary(5)}")
print(f"to_binary(10): {to_binary(10)}")
print(f"to_binary(-5): {to_binary(-5, 8)}") # Example of 2's complement for -5 in 8 bits
print("-" * 50)


# --- 1. What are Bitwise Operators? ---
print("\n--- 1. What are Bitwise Operators? ---")
print("Bitwise operators treat numbers as sequences of binary digits (bits) and operate on them bit by bit.")
print("They are useful for low-level programming, manipulating flags, and some optimizations.")
print("They only work on integer operands.")


# --- 2. Bitwise AND (&) ---
print("\n--- 2. Bitwise AND (&) ---")
print("Returns 1 if both bits are 1, otherwise 0.")
print("Example: 5 & 3")
#   5 = 0000 0101
#   3 = 0000 0011
# &   = 0000 0001  (which is 1)

a = 5  # 0101
b = 3  # 0011
result_and = a & b
print(f"Decimal: {a} & {b} = {result_and}")
print(f"Binary:  {to_binary(a)} & {to_binary(b)} = {to_binary(result_and)}")

# Common Use Case: Checking if a number is even/odd
# An even number always has its least significant bit (LSB) as 0.
# An odd number always has its LSB as 1.
# `num & 1` will be 0 for even, 1 for odd.
num_even = 10 # 1010
num_odd = 7   # 0111
print(f"\nChecking even/odd using '&':")
print(f"{num_even} ({to_binary(num_even)}) & 1 ({to_binary(1)}) = {num_even & 1} ({'Even' if (num_even & 1) == 0 else 'Odd'})")
print(f"{num_odd} ({to_binary(num_odd)}) & 1 ({to_binary(1)}) = {num_odd & 1} ({'Even' if (num_odd & 1) == 0 else 'Odd'})")

# Common Use Case: Masking (isolating specific bits)
# To get the last 4 bits of a number, use a mask of 0b1111 (15)
num_mask = 29 # 0001 1101
mask = 15     # 0000 1111
masked_result = num_mask & mask
print(f"\nMasking: Get last 4 bits of {num_mask} ({to_binary(num_mask)}) with mask {mask} ({to_binary(mask)})")
print(f"Result: {masked_result} ({to_binary(masked_result)})")


# --- 3. Bitwise OR (|) ---
print("\n--- 3. Bitwise OR (|) ---")
print("Returns 1 if at least one of the bits is 1, otherwise 0.")
print("Example: 5 | 3")
#   5 = 0000 0101
#   3 = 0000 0011
# |   = 0000 0111  (which is 7)

a = 5  # 0101
b = 3  # 0011
result_or = a | b
print(f"Decimal: {a} | {b} = {result_or}")
print(f"Binary:  {to_binary(a)} | {to_binary(b)} = {to_binary(result_or)}")

# Common Use Case: Setting a specific bit (turning it on)
# To set the 3rd bit (0-indexed) of a number, OR it with 2^3 (8, or 0000 1000)
num_set = 10 # 0000 1010
bit_to_set = 8 # 0000 1000 (2 to the power of 3, for the 3rd bit)
set_result = num_set | bit_to_set
print(f"\nSetting the 3rd bit of {num_set} ({to_binary(num_set)}) with {bit_to_set} ({to_binary(bit_to_set)})")
print(f"Result: {set_result} ({to_binary(set_result)})")


# --- 4. Bitwise XOR (^) ---
print("\n--- 4. Bitwise XOR (^) ---")
print("Returns 1 if the bits are different, otherwise 0 (exclusive OR).")
print("Example: 5 ^ 3")
#   5 = 0000 0101
#   3 = 0000 0011
# ^   = 0000 0110  (which is 6)

a = 5  # 0101
b = 3  # 0011
result_xor = a ^ b
print(f"Decimal: {a} ^ {b} = {result_xor}")
print(f"Binary:  {to_binary(a)} ^ {to_binary(b)} = {to_binary(result_xor)}")

# Common Use Case: Toggling a specific bit
# To toggle the 3rd bit of a number, XOR it with 2^3 (8)
num_toggle = 10 # 0000 1010
bit_to_toggle = 8 # 0000 1000
toggle_result = num_toggle ^ bit_to_toggle
print(f"\nToggling the 3rd bit of {num_toggle} ({to_binary(num_toggle)}) with {bit_to_toggle} ({to_binary(bit_to_toggle)})")
print(f"Result: {toggle_result} ({to_binary(toggle_result)})") # Original 3rd bit was 1, now 0

num_toggle2 = 2 # 0000 0010
bit_to_toggle2 = 8 # 0000 1000
toggle_result2 = num_toggle2 ^ bit_to_toggle2
print(f"Toggling the 3rd bit of {num_toggle2} ({to_binary(num_toggle2)}) with {bit_to_toggle2} ({to_binary(bit_to_toggle2)})")
print(f"Result: {toggle_result2} ({to_binary(toggle_result2)})") # Original 3rd bit was 0, now 1

# Common Use Case: Swapping two numbers without a temporary variable (classic interview trick)
x = 10
y = 20
print(f"\nSwapping x={x}, y={y} using XOR:")
x = x ^ y # x = 10 ^ 20 (01010 ^ 10100 = 11110 = 30)
y = x ^ y # y = (10^20) ^ 20 = 10 (11110 ^ 10100 = 01010)
x = x ^ y # x = (10^20) ^ 10 = 20 (11110 ^ 01010 = 10100)
print(f"After swap: x={x}, y={y}")


# --- 5. Bitwise NOT (~) / Complement ---
print("\n--- 5. Bitwise NOT (~) / Complement ---")
print("Inverts all the bits (0 becomes 1, 1 becomes 0).")
print("The result is `-(x + 1)` due to Python using two's complement representation for negative numbers.")
print("Example: ~5")
# 5  = 0000 0101
# ~5 = 1111 1010 (conceptually)
# In two's complement, 1111 1010 represents -6.

a = 5
result_not = ~a
print(f"Decimal: ~{a} = {result_not}")
# The binary representation below is conceptual for 8 bits, actual Python integer has arbitrary precision
print(f"Binary:  ~{to_binary(a)} = {to_binary(result_not)}")

b = -10
result_not_neg = ~b
print(f"Decimal: ~{b} = {result_not_neg}")
print(f"Binary:  ~{to_binary(b)} = {to_binary(result_not_neg)}")


# --- 6. Left Shift (<<) ---
print("\n--- 6. Left Shift (<<) ---")
print("Shifts the bits of the number to the left by the specified number of positions.")
print("Equivalent to multiplying by 2 raised to the power of the shift amount (x * 2**y).")
print("New bits on the right are filled with 0s.")
print("Example: 5 << 2")
# 5    = 0000 0101
# 5 << 2 = 0001 0100 (which is 20)

a = 5
shift_amount = 2
result_lshift = a << shift_amount
print(f"Decimal: {a} << {shift_amount} = {result_lshift}")
print(f"Binary:  {to_binary(a)} << {shift_amount} = {to_binary(result_lshift)}")

# Multiplication example
val = 7 # 0111
mult_by_4 = val << 2 # 011100 = 28
print(f"Multiplying {val} by 4 (2^2) using left shift: {mult_by_4}")


# --- 7. Right Shift (>>) ---
print("\n--- 7. Right Shift (>>) ---")
print("Shifts the bits of the number to the right by the specified number of positions.")
print("Equivalent to integer division by 2 raised to the power of the shift amount (x // 2**y).")
print("New bits on the left are filled with 0s for positive numbers (sign extension for negative numbers).")
print("Example: 20 >> 2")
# 20   = 0001 0100
# 20 >> 2 = 0000 0101 (which is 5)

a = 20
shift_amount = 2
result_rshift = a >> shift_amount
print(f"Decimal: {a} >> {shift_amount} = {result_rshift}")
print(f"Binary:  {to_binary(a)} >> {shift_amount} = {to_binary(result_rshift)}")

# Division example
val_div = 28 # 0001 1100
div_by_4 = val_div >> 2 # 0000 0111 = 7
print(f"Dividing {val_div} by 4 (2^2) using right shift: {div_by_4}")

# Right shift with negative numbers (implementation-defined, typically arithmetic shift)
neg_num = -10 # In 8-bit 2's complement: 1111 0110
neg_shifted = neg_num >> 1 # Result: -5 (1111 1011)
print(f"Decimal: {neg_num} ({to_binary(neg_num)}) >> 1 = {neg_shifted} ({to_binary(neg_shifted)})")


# --- 8. Combined Bitwise Operations and Flags ---
print("\n--- 8. Combined Bitwise Operations and Flags ---")
print("Bitwise operators are commonly used with flags to represent multiple boolean states in a single integer.")

# Define flags using powers of 2
READ_PERMISSION = 0b001 # 1
WRITE_PERMISSION = 0b010 # 2
EXECUTE_PERMISSION = 0b100 # 4
ADMIN_PERMISSION = 0b1000 # 8

user_permissions = 0 # Start with no permissions

# Grant permissions using OR
user_permissions |= READ_PERMISSION # Add read
print(f"\nUser permissions after READ: {user_permissions} ({to_binary(user_permissions, 4)})")
user_permissions |= WRITE_PERMISSION # Add write
print(f"User permissions after WRITE: {user_permissions} ({to_binary(user_permissions, 4)})")
user_permissions |= EXECUTE_PERMISSION # Add execute
print(f"User permissions after EXECUTE: {user_permissions} ({to_binary(user_permissions, 4)})")

# Check for permissions using AND
print(f"\nChecking permissions:")
print(f"Has READ permission? {(user_permissions & READ_PERMISSION) != 0}")
print(f"Has ADMIN permission? {(user_permissions & ADMIN_PERMISSION) != 0}")

# Remove a permission (clear a bit) using AND with NOT
user_permissions &= ~WRITE_PERMISSION
print(f"User permissions after removing WRITE: {user_permissions} ({to_binary(user_permissions, 4)})")
print(f"Has WRITE permission now? {(user_permissions & WRITE_PERMISSION) != 0}")

# Toggle a permission using XOR
user_permissions ^= READ_PERMISSION # Toggle read (was on, now off)
print(f"User permissions after toggling READ: {user_permissions} ({to_binary(user_permissions, 4)})")
user_permissions ^= READ_PERMISSION # Toggle read again (was off, now on)
print(f"User permissions after toggling READ again: {user_permissions} ({to_binary(user_permissions, 4)})")


print("\n--- End of Python Bitwise Operators Practice Code ---")