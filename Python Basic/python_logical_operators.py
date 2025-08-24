print("--- Python Logical Operators: Practice Code ---")

# --- 1. Introduction to Logical Operators ---
print("\n--- 1. Introduction to Logical Operators ---")
print("Logical operators are used to combine conditional statements (boolean expressions).")
print("They always evaluate to a Boolean value (True or False), or sometimes the operand itself.")
print("The three logical operators are: 'and', 'or', and 'not'.")

# --- 2. The 'and' Operator ---
print("\n--- 2. The 'and' Operator ---")
print("Syntax: operand1 and operand2")
print("Returns True if BOTH operands are True. Otherwise, returns False.")

# 2.1 Basic Truth Table Examples for 'and'
print("\n2.1 Basic 'and' Truth Table:")
print(f"True and True: {True and True}")     # True
print(f"True and False: {True and False}")   # False
print(f"False and True: {False and True}")   # False
print(f"False and False: {False and False}") # False

# 2.2 'and' with Comparison Operators
age = 25
has_license = True
is_adult = (age >= 18)
can_drive = (is_adult and has_license)
print(f"\nAge ({age}) >= 18 AND Has License ({has_license}): {can_drive}")

temp = 28
is_sunny = True
go_swimming = (temp > 25 and is_sunny)
print(f"Temp ({temp}) > 25 AND Is Sunny ({is_sunny}): {go_swimming}")

# 2.3 Short-Circuiting Behavior of 'and'
# If the first operand is False, Python doesn't evaluate the second operand,
# as the result will already be False. It returns the first operand.
print("\n2.3 'and' Short-Circuiting:")
print("False and (print('This will not be printed'))")
result_and_short_circuit = False and print("This will not be printed (due to short-circuiting)")
print(f"Result: {result_and_short_circuit}") # Returns False (the first operand)

print("True and 'Hello':", True and "Hello") # Returns 'Hello' (the second operand, because first is True)
print("False and 'World':", False and "World") # Returns False (the first operand)
print("'Python' and 'Programming':", "Python" and "Programming") # Returns 'Programming'
# 'Python' is truthy, so 'Programming' is evaluated and returned.

# This behavior is useful for conditional execution:
user_input = "" # Imagine this comes from a user
if user_input and len(user_input) > 5:
    print(f"Input is valid: {user_input}")
else:
    print("Input is empty or too short.")


# --- 3. The 'or' Operator ---
print("\n--- 3. The 'or' Operator ---")
print("Syntax: operand1 or operand2")
print("Returns True if AT LEAST ONE operand is True. Otherwise, returns False.")

# 3.1 Basic Truth Table Examples for 'or'
print("\n3.1 Basic 'or' Truth Table:")
print(f"True or True: {True or True}")     # True
print(f"True or False: {True or False}")   # True
print(f"False or True: {False or True}")   # True
print(f"False or False: {False or False}") # False

# 3.2 'or' with Comparison Operators
day = "Sunday"
is_weekend = (day == "Saturday" or day == "Sunday")
print(f"\nDay is 'Saturday' OR Day is 'Sunday': {is_weekend}")

score = 92
passed_with_distinction = (score >= 90 or score < 60) # Example to show combined
print(f"Score ({score}) >= 90 OR Score < 60: {passed_with_distinction}")

# 3.3 Short-Circuiting Behavior of 'or'
# If the first operand is True, Python doesn't evaluate the second operand,
# as the result will already be True. It returns the first operand.
print("\n3.3 'or' Short-Circuiting:")
print("True or (print('This will not be printed'))")
result_or_short_circuit = True or print("This will not be printed (due to short-circuiting)")
print(f"Result: {result_or_short_circuit}") # Returns True (the first operand)

print("False or 'Default Value':", False or "Default Value") # Returns 'Default Value'
# False is falsy, so 'Default Value' is evaluated and returned.

print("'First Choice' or 'Second Choice':", "First Choice" or "Second Choice") # Returns 'First Choice'
# 'First Choice' is truthy, so it's returned immediately.

# This behavior is commonly used for assigning default values:
username = None # Could be from a database or user input
display_name = username or "Guest" # If username is None/empty, use "Guest"
print(f"Display Name: {display_name}")

username = "Alice"
display_name = username or "Guest"
print(f"Display Name: {display_name}")


# --- 4. The 'not' Operator ---
print("\n--- 4. The 'not' Operator ---")
print("Syntax: not operand")
print("Returns the inverse of the operand's boolean value.")

# 4.1 Basic Truth Table Examples for 'not'
print("\n4.1 Basic 'not' Truth Table:")
print(f"not True: {not True}")   # False
print(f"not False: {not False}") # True

# 4.2 'not' with Comparison Operators
is_logged_in = False
if not is_logged_in:
    print("\nUser is not logged in.")

is_valid_input = (len("Python") > 0)
if not is_valid_input:
    print("Input is empty.")
else:
    print("Input is not empty.")


# --- 5. Operator Precedence ---
print("\n--- 5. Operator Precedence ---")
print("The order of operations for logical operators is: not > and > or.")
print("Parentheses can be used to explicitly control the order.")

condition1 = True
condition2 = False
condition3 = True

# Example 1: `and` before `or`
# (condition1 and condition2) or condition3
# (True and False) or True
# False or True -> True
result_precedence1 = condition1 and condition2 or condition3
print(f"condition1 and condition2 or condition3: {result_precedence1}")

# Example 2: `not` before `and`
# not (condition1 and condition2)
# not (True and False)
# not False -> True
result_precedence2 = not (condition1 and condition2)
print(f"not (condition1 and condition2): {result_precedence2}")

# Example 3: Explicit parentheses for desired order
# condition1 and (condition2 or condition3)
# True and (False or True)
# True and True -> True
result_precedence3 = condition1 and (condition2 or condition3)
print(f"condition1 and (condition2 or condition3): {result_precedence3}")


# --- 6. Logical Operators with Truthy/Falsy Values ---
print("\n--- 6. Logical Operators with Truthy/Falsy Values ---")
print("Logical operators don't strictly require boolean operands; they evaluate truthiness.")
print("They return one of the operand values, not necessarily True/False.")

# 'and' returns the first falsy operand, or the last operand if all are truthy.
print(f"'' and 'hello': {' ' and 'hello'}")        # Returns '' (first falsy)
print(f"'hello' and '': {'hello' and ''}")        # Returns '' (first falsy after 'hello' is evaluated)
print(f"'apple' and 'banana': {'apple' and 'banana'}") # Returns 'banana' (last truthy)
print(f"0 and 10: {0 and 10}")                # Returns 0 (first falsy)
print(f"1 and 0: {1 and 0}")                # Returns 0 (first falsy after 1 is evaluated)

# 'or' returns the first truthy operand, or the last operand if all are falsy.
print(f"'' or 'hello': {' ' or 'hello'}")          # Returns 'hello' (first truthy)
print(f"'hello' or '': {'hello' or ''}")          # Returns 'hello' (first truthy)
print(f"0 or []: {0 or []}")                  # Returns [] (last falsy)
print(f"[] or 0: {[] or 0}")                  # Returns 0 (last falsy)


# --- 7. Common Use Cases ---
print("\n--- 7. Common Use Cases ---")

# 7.1 Conditional Execution (if/elif/else)
user_age = 17
user_credits = 10
if user_age >= 18 or user_credits >= 12:
    print("User is eligible for course enrollment.")
else:
    print("User is not eligible.")

# 7.2 Input Validation
password = "mysecretpassword"
confirm_password = "mysecretpassword"
if password == confirm_password and len(password) >= 8:
    print("Password set successfully!")
else:
    print("Passwords do not match or are too short.")

# 7.3 Loop Conditions
attempts = 0
max_attempts = 3
user_input = ""
while user_input != "quit" and attempts < max_attempts:
    user_input = input("Type 'quit' to exit (Attempt " + str(attempts + 1) + "/" + str(max_attempts) + "): ").lower()
    attempts += 1
if user_input == "quit":
    print("Exited by user.")
else:
    print("Max attempts reached.")


print("\n--- End of Python Logical Operators Practice Code ---")