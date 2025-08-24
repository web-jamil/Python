# --- Python Dictionaries: All About Keyword Arguments in Code ---

# In Python, "keyword arguments" (often abbreviated as `kwargs`) refer to
# arguments passed to a function using the `key=value` syntax. Dictionaries
# play a crucial role in handling and passing keyword arguments, especially
# through the `**` (double-asterisk) operator.

# --- 1. Passing Keyword Arguments to Functions ---

print("--- 1. Passing Keyword Arguments to Functions ---")

# 1.1 Direct keyword arguments in function calls
# When you define a function, you can call it by explicitly naming the arguments.
def create_user(username, email, age=None, is_active=True):
    print(f"1.1 Creating User:")
    print(f"    Username: {username}")
    print(f"    Email: {email}")
    print(f"    Age: {age}")
    print(f"    Is Active: {is_active}")

create_user(username="alice", email="alice@example.com")
print("-" * 20)
create_user(email="bob@example.com", username="bob", age=30, is_active=False) # Order doesn't matter for keyword args


# --- 2. The `**kwargs` Parameter in Function Definitions ---

print("\n--- 2. The `**kwargs` Parameter in Function Definitions ---")

# The `**kwargs` syntax in a function definition allows a function to accept
# an arbitrary number of keyword arguments. These arguments are collected into
# a dictionary inside the function.

# 2.1 Collecting arbitrary keyword arguments
def process_settings(**kwargs):
    print(f"2.1 Received settings (type {type(kwargs)}): {kwargs}")
    if "theme" in kwargs:
        print(f"    Theme is set to: {kwargs['theme']}")
    if "font_size" in kwargs:
        print(f"    Font size is: {kwargs['font_size']}")

process_settings(theme="dark", font_size=16, notifications=True)
print("-" * 20)
process_settings(debug_mode=True, log_level="INFO")
print("-" * 20)
process_settings() # No keyword arguments passed


# 2.2 Combining `*args` and `**kwargs`
# When defining a function, `*args` (positional arguments) must come before `**kwargs`.
def flexible_function(arg1, *args, **kwargs):
    print(f"2.2 Flexible Function Call:")
    print(f"    arg1: {arg1}")
    print(f"    *args (tuple of positional arguments): {args}")
    print(f"    **kwargs (dictionary of keyword arguments): {kwargs}")

flexible_function(10, 20, 30, name="Alice", age=30)
print("-" * 20)
flexible_function("start", a=1, b=2)


# --- 3. Unpacking Dictionaries into Keyword Arguments (`**dictionary`) ---

print("\n--- 3. Unpacking Dictionaries into Keyword Arguments (`**dictionary`) ---")

# This is a very powerful feature where you can use an existing dictionary
# to supply keyword arguments to a function call. The `**` operator "unpacks"
# the dictionary's key-value pairs into `key=value` arguments.

# 3.1 Basic unpacking
def show_item_details(name, price, stock):
    print(f"3.1 Item: {name}, Price: ${price:.2f}, Stock: {stock}")

item_data = {
    "name": "Laptop",
    "price": 1200.50,
    "stock": 50
}

# The `**` unpacks `item_data` into `name='Laptop', price=1200.50, stock=50`
show_item_details(**item_data)

# 3.2 What happens if dictionary keys don't match function parameters? (TypeError)
# If the dictionary contains keys that are not parameters of the function, or
# if required parameters are missing, a `TypeError` will be raised.
def process_order(order_id, customer_name):
    print(f"3.2 Processing order {order_id} for {customer_name}.")

# Missing 'customer_name'
missing_param_dict = {"order_id": "ORD001"}
try:
    process_order(**missing_param_dict)
except TypeError as e:
    print(f"    Error: {e} - Missing required argument 'customer_name'.")

# Extra parameter 'shipping_address'
extra_param_dict = {"order_id": "ORD002", "customer_name": "Bob", "shipping_address": "123 Main St"}
try:
    process_order(**extra_param_dict)
except TypeError as e:
    print(f"    Error: {e} - Got an unexpected keyword argument 'shipping_address'.")


# 3.3 Overriding unpacked arguments
# Explicitly passed keyword arguments take precedence over unpacked dictionary arguments.
def render_template(template_name, title="Default Title", content=""):
    print(f"3.3 Rendering Template:")
    print(f"    Template: {template_name}")
    print(f"    Title: {title}")
    print(f"    Content: {content}")

template_vars = {"title": "My Page", "content": "Welcome!"}

# 'title' from `template_vars` is "My Page", but explicit `title="Override"` wins.
render_template("home.html", **template_vars, title="Override")
print("-" * 20)
# 'content' from `template_vars` is "Welcome!", no override.
render_template("about.html", **template_vars)


# 3.4 Combining with positional arguments and `*args`
def create_document(doc_type, *sections, author="Unknown", **metadata):
    print(f"\n3.4 Creating Document:")
    print(f"    Document Type: {doc_type}")
    print(f"    Sections: {sections}")
    print(f"    Author: {author}")
    print(f"    Metadata: {metadata}")

doc_metadata = {"version": "1.0", "status": "draft"}
create_document("report", "intro", "body", "conclusion", author="Jane Doe", **doc_metadata)
print("-" * 20)
# No sections, default author, additional metadata
create_document("memo", date="2025-06-04", recipient="Team", **doc_metadata)


# --- 4. The `dict()` Constructor and Keyword Arguments ---

print("\n--- 4. The `dict()` Constructor and Keyword Arguments ---")

# The `dict()` constructor itself can take keyword arguments to create a dictionary.
# The keys of these keyword arguments become string keys in the new dictionary.

# 4.1 Creating a dictionary directly from keyword arguments
config_dict = dict(debug=True, log_level="INFO", port=8000)
print(f"4.1 Dictionary created with keyword arguments: {config_dict}")

# 4.2 Combining with positional iterable argument
# If keys overlap, keyword arguments take precedence.
mixed_creation = dict([("color", "red"), ("size", "M")], material="cotton", color="blue")
print(f"4.2 Mixed creation (keyword arg 'color' wins): {mixed_creation}")
# Output: {'color': 'blue', 'size': 'M', 'material': 'cotton'}