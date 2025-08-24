print("--- Python Assignment Operators ---")
print("----------------------------------\n")

# Assignment operators are used to assign values to variables.
# The most basic assignment operator is `=`.
# Others are compound assignment operators, which combine an operation
# with assignment (e.g., `+=`, `-=`, `*=`, etc.).

# 1. Simple Assignment (=)
print("1. Simple Assignment (=):")
my_variable = 10
print(f"my_variable = 10  -> my_variable: {my_variable}\n")

# Assigning string
name = "Alice"
print(f"name = \"Alice\" -> name: {name}\n")

# Assigning list
my_list = [1, 2, 3]
print(f"my_list = [1, 2, 3] -> my_list: {my_list}\n")


# 2. Compound Assignment Operators
# These operators perform an operation and then assign the result
# back to the left operand. They are shorthand for an operation
# followed by an assignment.

# Example variable to modify
x = 5
print(f"Initial x: {x}\n")

# 2.1. Addition Assignment (+=)
print("2.1. Addition Assignment (+=): x += y is equivalent to x = x + y")
x += 3 # x becomes 5 + 3 = 8
print(f"x += 3   -> x: {x}")

s = "Hello"
s += " World" # String concatenation
print(f"s = \"Hello\", s += \" World\" -> s: {s}")

l = [1, 2]
l += [3, 4] # List extension (equivalent to list.extend())
print(f"l = [1, 2], l += [3, 4] -> l: {l}\n")


# 2.2. Subtraction Assignment (-=)
print("2.2. Subtraction Assignment (-=): x -= y is equivalent to x = x - y")
x -= 2 # x becomes 8 - 2 = 6
print(f"x -= 2   -> x: {x}\n")


# 2.3. Multiplication Assignment (*=)
print("2.3. Multiplication Assignment (*=): x *= y is equivalent to x = x * y")
x *= 4 # x becomes 6 * 4 = 24
print(f"x *= 4   -> x: {x}")

text = "abc"
text *= 3 # String repetition
print(f"text = \"abc\", text *= 3 -> text: {text}\n")


# 2.4. Division Assignment (/=)
print("2.4. Division Assignment (/=): x /= y is equivalent to x = x / y")
x /= 5 # x becomes 24 / 5 = 4.8 (always results in float)
print(f"x /= 5   -> x: {x}\n")


# 2.5. Modulus Assignment (%=)
print("2.5. Modulus Assignment (%=): x %= y is equivalent to x = x % y")
y = 10
y %= 3 # y becomes 10 % 3 = 1
print(f"y = 10, y %= 3 -> y: {y}\n")


# 2.6. Exponentiation Assignment (**=)
print("2.6. Exponentiation Assignment (**=): x **= y is equivalent to x = x ** y")
z = 2
z **= 3 # z becomes 2 ** 3 = 8
print(f"z = 2, z **= 3 -> z: {z}\n")


# 2.7. Floor Division Assignment (//=)
print("2.7. Floor Division Assignment (//=): x //= y is equivalent to x = x // y")
a = 17
a //= 5 # a becomes 17 // 5 = 3
print(f"a = 17, a //= 5 -> a: {a}\n")


# 2.8. Bitwise AND Assignment (&=)
print("2.8. Bitwise AND Assignment (&=): x &= y is equivalent to x = x & y")
flags = 0b1101 # 13
mask = 0b0110  # 6
flags &= mask # flags becomes 1101 & 0110 = 0100 (4)
print(f"flags = 0b1101, mask = 0b0110, flags &= mask -> flags: {bin(flags)}\n")


# 2.9. Bitwise OR Assignment (|=)
print("2.9. Bitwise OR Assignment (|=): x |= y is equivalent to x = x | y")
flags = 0b0010 # 2
new_flag = 0b1000 # 8
flags |= new_flag # flags becomes 0010 | 1000 = 1010 (10)
print(f"flags = 0b0010, new_flag = 0b1000, flags |= new_flag -> flags: {bin(flags)}\n")


# 2.10. Bitwise XOR Assignment (^=)
print("2.10. Bitwise XOR Assignment (^=): x ^= y is equivalent to x = x ^ y")
state = 0b1111 # 15
toggle_mask = 0b1010 # 10
state ^= toggle_mask # state becomes 1111 ^ 1010 = 0101 (5)
print(f"state = 0b1111, toggle_mask = 0b1010, state ^= toggle_mask -> state: {bin(state)}\n")


# 2.11. Left Shift Assignment (<<=)
print("2.11. Left Shift Assignment (<<=): x <<= y is equivalent to x = x << y")
val = 3 # 0011
val <<= 2 # val becomes 0011 << 2 = 1100 (12)
print(f"val = 3, val <<= 2 -> val: {bin(val)}\n")


# 2.12. Right Shift Assignment (>>=)
print("2.12. Right Shift Assignment (>>=): x >>= y is equivalent to x = x >> y")
val = 12 # 1100
val >>= 1 # val becomes 1100 >> 1 = 0110 (6)
print(f"val = 12, val >>= 1 -> val: {bin(val)}\n")


# 3. Chained Assignment (Multiple assignment)
print("3. Chained Assignment (Multiple assignment):")
# Assigns the same value to multiple variables.
p = q = r = 100
print(f"p = q = r = 100 -> p:{p}, q:{q}, r:{r}\n")

# Be careful when assigning mutable objects in chained assignment:
list1 = list2 = [1, 2] # list1 and list2 refer to the *same* list object
list1.append(3)
print(f"list1 = list2 = [1, 2], then list1.append(3) -> list1:{list1}, list2:{list2}\n")
# Both lists are modified because they are the same object.

# To create separate lists with the same initial values:
list_a = [1, 2]
list_b = [1, 2]
list_a.append(3)
print(f"list_a = [1, 2], list_b = [1, 2], then list_a.append(3) -> list_a:{list_a}, list_b:{list_b}\n")


# 4. Unpacking Assignment (Tuple/List assignment)
print("4. Unpacking Assignment (Tuple/List assignment):")
# Assigns elements from an iterable (like a tuple or list) to multiple variables.
coords = (10, 20)
x_coord, y_coord = coords
print(f"coords = (10, 20), x_coord, y_coord = coords -> x_coord:{x_coord}, y_coord:{y_coord}")

data = ["John", 30, "Engineer"]
name, age, job = data
print(f"data = [\"John\", 30, \"Engineer\"], name, age, job = data -> name:{name}, age:{age}, job:{job}\n")

# Swapping variables (Pythonic way)
var1 = 10
var2 = 20
print(f"Before swap: var1:{var1}, var2:{var2}")
var1, var2 = var2, var1
print(f"After swap: var1:{var1}, var2:{var2}\n")

# Extended unpacking (Python 3+)
a, *rest, b = [1, 2, 3, 4, 5]
print(f"a, *rest, b = [1, 2, 3, 4, 5] -> a:{a}, rest:{rest}, b:{b}\n")


print("--- End of Python Assignment Operators Demonstration ---")