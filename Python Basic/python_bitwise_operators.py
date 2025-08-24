print("--- Python Bitwise Operators ---")
print("------------------------------\n")

# Bitwise operators treat numbers as sequences of bits (0s and 1s)
# and operate on those bits individually.
# They are typically used with integers.

# Define some integer operands
a = 12  # Binary: 1100
b = 10  # Binary: 1010
c = 5   # Binary: 0101
d = -7  # Binary representation for negative numbers uses two's complement.
        # For a simplified 8-bit representation:
        # 7  = 0000 0111
        # ~7 = 1111 1000 (one's complement)
        # -7 = 1111 1001 (two's complement)

print(f"Operands (decimal and binary representation assumed for 8-bit for clarity):")
print(f"  a = {a} (binary: {bin(a)})")
print(f"  b = {b} (binary: {bin(b)})")
print(f"  c = {c} (binary: {bin(c)})")
print(f"  d = {d} (binary: {bin(d)})\n")


# 1. Bitwise AND (&)
print("1. Bitwise AND (&):")
# Sets each bit to 1 if both corresponding bits are 1.
#   a: 1100
#   b: 1010
#   & : 1000  (decimal 8)
result_and = a & b
print(f"{a} & {b} = {result_and} (binary: {bin(result_and)})")

#   a: 1100
#   c: 0101
#   & : 0100  (decimal 4)
result_and_2 = a & c
print(f"{a} & {c} = {result_and_2} (binary: {bin(result_and_2)})\n")


# 2. Bitwise OR (|)
print("2. Bitwise OR (|):")
# Sets each bit to 1 if at least one of the corresponding bits is 1.
#   a: 1100
#   b: 1010
#   | : 1110  (decimal 14)
result_or = a | b
print(f"{a} | {b} = {result_or} (binary: {bin(result_or)})")

#   a: 1100
#   c: 0101
#   | : 1101  (decimal 13)
result_or_2 = a | c
print(f"{a} | {c} = {result_or_2} (binary: {bin(result_or_2)})\n")


# 3. Bitwise XOR (^)
print("3. Bitwise XOR (^):")
# Sets each bit to 1 if only one of the corresponding bits is 1 (exclusive OR).
#   a: 1100
#   b: 1010
#   ^ : 0110  (decimal 6)
result_xor = a ^ b
print(f"{a} ^ {b} = {result_xor} (binary: {bin(result_xor)})")

#   a: 1100
#   c: 0101
#   ^ : 1001  (decimal 9)
result_xor_2 = a ^ c
print(f"{a} ^ {c} = {result_xor_2} (binary: {bin(result_xor_2)})\n")


# 4. Bitwise NOT (~)
print("4. Bitwise NOT (~):")
# Inverts all the bits (flips 0s to 1s and 1s to 0s).
# For any integer x, ~x is equivalent to -(x + 1).
#   a: 0000 1100 (assuming enough leading zeros for clarity)
#  ~a: 1111 0011 (in two's complement, this is -13)
result_not_a = ~a
print(f"~{a} = {result_not_a} (binary: {bin(result_not_a)})")
print(f"Confirming ~{a} == -({a} + 1): {result_not_a == -(a + 1)}")

#   d: (assuming 8-bit) 1111 1001 (-7)
#  ~d: 0000 0110 (6)
result_not_d = ~d
print(f"~{d} = {result_not_d} (binary: {bin(result_not_d)})")
print(f"Confirming ~{d} == -({d} + 1): {result_not_d == -(d + 1)}\n")


# 5. Left Shift (<<)
print("5. Left Shift (<<):")
# Shifts the bits of the left operand to the left by the number of positions
# specified by the right operand. Fills new positions with zeros.
# Equivalent to multiplying by 2 raised to the power of the shift amount (2**n).
#   a: 0000 1100 (12)
# a << 1: 0001 1000 (24)
result_lshift_1 = a << 1
print(f"{a} << 1 = {result_lshift_1} (binary: {bin(result_lshift_1)})")

#   a:    0000 1100 (12)
# a << 2: 0011 0000 (48)
result_lshift_2 = a << 2
print(f"{a} << 2 = {result_lshift_2} (binary: {bin(result_lshift_2)})\n")


# 6. Right Shift (>>)
print("6. Right Shift (>>):")
# Shifts the bits of the left operand to the right by the number of positions
# specified by the right operand.
# For positive numbers, new positions are filled with zeros (logical shift).
# For negative numbers, new positions are filled with the sign bit (arithmetic shift).
# Equivalent to floor dividing by 2 raised to the power of the shift amount (2**n).
#   a: 0000 1100 (12)
# a >> 1: 0000 0110 (6)
result_rshift_1 = a >> 1
print(f"{a} >> 1 = {result_rshift_1} (binary: {bin(result_rshift_1)})")

#   a:    0000 1100 (12)
# a >> 2: 0000 0011 (3)
result_rshift_2 = a >> 2
print(f"{a} >> 2 = {result_rshift_2} (binary: {bin(result_rshift_2)})")

#   d: (8-bit) 1111 1001 (-7)
# d >> 1: (8-bit) 1111 1100 (-4)  <- fills with sign bit (1)
result_rshift_neg = d >> 1
print(f"{d} >> 1 = {result_rshift_neg} (binary: {bin(result_rshift_neg)})\n")


# --- Common Use Cases ---
print("--- Common Use Cases ---\n")

# Use Case 1: Checking if a number is even or odd
# A number is even if its least significant bit (LSB) is 0.
# A number is odd if its LSB is 1.
# `num & 1` isolates the LSB.
num_check_even = 14 # 1110
num_check_odd = 7  # 0111
print(f"Is {num_check_even} even? { (num_check_even & 1) == 0 }") # 1110 & 0001 = 0000 -> True
print(f"Is {num_check_odd} even? { (num_check_odd & 1) == 0 }\n")  # 0111 & 0001 = 0001 -> False


# Use Case 2: Checking if a specific bit is set (flag management)
# Imagine flags representing permissions or states
READ_PERMISSION = 0b001 # 1
WRITE_PERMISSION = 0b010 # 2
EXECUTE_PERMISSION = 0b100 # 4

user_permissions = 0b101 # User has READ (1) and EXECUTE (4)

print(f"User permissions: {bin(user_permissions)}")
print(f"Has READ permission? { (user_permissions & READ_PERMISSION) != 0 }")
print(f"Has WRITE permission? { (user_permissions & WRITE_PERMISSION) != 0 }")
print(f"Has EXECUTE permission? { (user_permissions & EXECUTE_PERMISSION) != 0 }\n")

# Setting a bit
user_permissions = user_permissions | WRITE_PERMISSION # Add WRITE permission
print(f"Permissions after adding WRITE: {bin(user_permissions)}") # 111 (7)

# Clearing a bit
# To clear a bit, AND with the inverted flag (~FLAG)
user_permissions = user_permissions & ~READ_PERMISSION # Clear READ permission
print(f"Permissions after clearing READ:  {bin(user_permissions)}\n") # 110 (6)


# Use Case 3: Multiplying/Dividing by powers of 2 efficiently
print("3. Multiplying/Dividing by powers of 2 efficiently:")
val = 15
print(f"{val} * 4 (using << 2) = {val << 2}") # 15 * (2**2) = 15 * 4 = 60
print(f"{val} / 2 (using >> 1) = {val >> 1}\n") # 15 // (2**1) = 15 // 2 = 7


# Use Case 4: Swapping two numbers without a temporary variable (XOR Swap)
print("4. Swapping two numbers (XOR Swap - for illustration):")
val1 = 25 # 0001 1001
val2 = 13 # 0000 1101
print(f"Before swap: val1={val1}, val2={val2}")

val1 = val1 ^ val2 # val1 becomes (25 ^ 13) = 0001 1001 ^ 0000 1101 = 0001 0100 (20)
val2 = val1 ^ val2 # val2 becomes (20 ^ 13) = 0001 0100 ^ 0000 1101 = 0001 1001 (25)
val1 = val1 ^ val2 # val1 becomes (20 ^ 25) = 0001 0100 ^ 0001 1001 = 0000 1101 (13)

print(f"After XOR swap: val1={val1}, val2={val2}\n")
# Note: In Python, `val1, val2 = val2, val1` is the preferred and more readable way to swap.


print("--- End of Python Bitwise Operators Demonstration ---")