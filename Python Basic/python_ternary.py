print("--- Python Ternary Conditional Operator: Practice Code ---")

# --- 1. What is the Ternary Operator? ---
print("\n--- 1. What is the Ternary Operator? ---")
print("The ternary conditional operator (or conditional expression) allows you to assign a value")
print("to a variable based on a condition, all in a single line.")
print("It's a concise way to write a simple `if-else` statement as an expression.")

# --- 2. Syntax of the Ternary Operator ---
print("\n--- 2. Syntax of the Ternary Operator ---")
print("Syntax: value_if_true if condition else value_if_false")

# Example: Assigning a status message based on a score
score = 75
status = "Pass" if score >= 60 else "Fail"
print(f"Score: {score}, Status: {status}")

score = 55
status = "Pass" if score >= 60 else "Fail"
print(f"Score: {score}, Status: {status}")


# --- 3. How it Works ---
print("\n--- 3. How it Works ---")
print("1. Python first evaluates the `condition`.")
print("2. If the `condition` is `True`, the `value_if_true` is returned.")
print("3. If the `condition` is `False`, the `value_if_false` is returned.")

# It's an expression, meaning it evaluates to a single value.
# This makes it suitable for:
# - Variable assignment
# - Function arguments
# - Return values
# - Inside f-strings or other string formatting
# - List comprehensions, dictionary comprehensions, etc.


# --- 4. Basic Use Cases ---
print("\n--- 4. Basic Use Cases ---")

# 4.1 Assigning different values to a variable
temperature = 28
weather_alert = "Hot" if temperature > 25 else "Normal"
print(f"Temperature: {temperature}°C, Alert: {weather_alert}")

temperature = 20
weather_alert = "Hot" if temperature > 25 else "Normal"
print(f"Temperature: {temperature}°C, Alert: {weather_alert}")

# 4.2 Using it directly in print statements or f-strings
age = 20
print(f"You are {'an adult' if age >= 18 else 'a minor'}.")

# 4.3 Returning values from functions
def get_eligibility(user_age):
    return "Eligible" if user_age >= 18 else "Not Eligible"

print(f"Eligibility for age 17: {get_eligibility(17)}")
print(f"Eligibility for age 25: {get_eligibility(25)}")

# 4.4 As an argument to another function
number = 10
print("The number is " + ("even" if number % 2 == 0 else "odd") + ".")


# --- 5. Ternary Operator in Comprehensions ---
print("\n--- 5. Ternary Operator in Comprehensions ---")
print("This is a very common and powerful use case.")

# 5.1 List Comprehensions (transforming values)
print("\n5.1 List Comprehensions:")
numbers = [1, 2, 3, 4, 5, 6]
odd_even_labels = ["Odd" if num % 2 != 0 else "Even" for num in numbers]
print(f"Numbers: {numbers}")
print(f"Odd/Even labels: {odd_even_labels}")

# Note: This is different from filtering: `[num for num in numbers if condition]`

# 5.2 Dictionary Comprehensions
print("\n5.2 Dictionary Comprehensions:")
status_map = {num: "High" if num > 5 else "Low" for num in range(1, 10)}
print(f"Status map: {status_map}")


# --- 6. Chaining Ternary Operators (Not Recommended for Readability) ---
print("\n--- 6. Chaining Ternary Operators ---")
print("While technically possible, chaining can quickly become unreadable.")
print("It's usually better to use `if-elif-else` for multiple conditions.")

grade = 85
# This is hard to read!
grade_status = "Excellent" if grade >= 90 else ("Good" if grade >= 70 else "Average")
print(f"Grade: {grade}, Status: {grade_status}")

grade = 65
grade_status = "Excellent" if grade >= 90 else ("Good" if grade >= 70 else "Average")
print(f"Grade: {grade}, Status: {grade_status}")

# Preferred alternative for multiple conditions:
def get_grade_status(grade_score):
    if grade_score >= 90:
        return "Excellent"
    elif grade_score >= 70:
        return "Good"
    else:
        return "Average"

print(f"Grade: {85}, Status (def func): {get_grade_status(85)}")
print(f"Grade: {65}, Status (def func): {get_grade_status(65)}")


# --- 7. Boolean Expressions vs. Ternary Operator ---
print("\n--- 7. Boolean Expressions vs. Ternary Operator ---")
print("Sometimes, you can use logical operators (`and`, `or`) for similar effects, but they behave differently.")
print("The ternary operator specifically guarantees one of two values based on True/False.")

# Example 1: `or` for default values (if `value1` is falsy, `value2` is used)
user_name = ""
display_name_or = user_name or "Guest"
print(f"Display name (using or): '{display_name_or}'")

user_name = "Alice"
display_name_or = user_name or "Guest"
print(f"Display name (using or): '{display_name_or}'")

# Example 2: Ternary operator for explicit True/False condition
user_name = ""
display_name_ternary = "Guest" if not user_name else user_name
print(f"Display name (using ternary): '{display_name_ternary}'")
# Here, the condition `not user_name` determines if `user_name` is falsy.

# Key Difference:
# `value_if_true if condition else value_if_false`
# - `value_if_true` is *always* returned if `condition` is True.
# - `value_if_false` is *always* returned if `condition` is False.

# `A or B`
# - If `A` is truthy, `A` is returned.
# - If `A` is falsy, `B` is returned.
# This means `A` and `B` can be any type, not just booleans.

# `A and B`
# - If `A` is falsy, `A` is returned.
# - If `A` is truthy, `B` is returned.


# --- 8. When to Use the Ternary Operator ---
print("\n--- 8. When to Use the Ternary Operator ---")
print("- For simple, single-line conditional assignments.")
print("- To make your code more concise when an `if-else` block would be too verbose.")
print("- Especially useful inside comprehensions or f-strings for inline logic.")
print("- Avoid for complex conditions or nested chains, as readability decreases.")

print("\n--- End of Python Ternary Conditional Operator Practice Code ---")