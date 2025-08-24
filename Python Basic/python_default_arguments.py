import datetime

print("--- Python Default Arguments ---")
print("--------------------------------\n")

# Default arguments allow you to define a default value for a parameter.
# If the caller does not provide an argument for that parameter, the default value is used.
# If the caller provides an argument, the default value is overridden.

# Rule: Default arguments must come AFTER any non-default arguments.
# def func(a, b=1, c=2):  # Valid
# def func(a, b=1, c):   # Invalid (non-default 'c' after default 'b')


# --- 1. Basic Usage ---
print("1. Basic Usage:\n")

def greet(name, greeting="Hello"):
    """Greets a person with an optional custom greeting."""
    print(f"{greeting}, {name}!")

greet("Alice")          # Uses default greeting: "Hello, Alice!"
greet("Bob", "Hi")      # Overrides default greeting: "Hi, Bob!"
greet("Charlie", greeting="Good morning") # Using keyword argument for clarity
print()


# --- 2. Multiple Default Arguments ---
print("2. Multiple Default Arguments:\n")

def create_user(username, email="no-email@example.com", is_active=True):
    """Creates a user with optional email and active status."""
    print(f"User: {username}")
    print(f"Email: {email}")
    print(f"Active: {is_active}")
    print("-" * 20)

create_user("JohnDoe")
create_user("JaneSmith", "jane@example.com")
create_user("PeterPan", is_active=False) # Skip email, set is_active
create_user("Admin", "admin@example.com", True)
print()


# --- 3. Important Pitfall: Mutable Default Arguments ---
print("3. IMPORTANT PITFALL: Mutable Default Arguments!\n")

# Default argument values are evaluated ONCE when the function is defined,
# not every time the function is called.
# This can lead to unexpected behavior if the default argument is a mutable object
# (like a list, dictionary, or set).

def add_item_to_list(item, my_list=[]):
    """Adds an item to a list. DANGER: my_list is a mutable default!"""
    my_list.append(item)
    print(f"Inside function: {my_list}")
    return my_list

print("First call to add_item_to_list:")
list1 = add_item_to_list(1) # my_list is the same default list object
print(f"Outside function (list1): {list1}")

print("\nSecond call to add_item_to_list (without providing a list):")
list2 = add_item_to_list(2) # Modifies the *same* default list object again
print(f"Outside function (list2): {list2}") # list1 and list2 now point to the same modified list!
print(f"Is list1 the same object as list2? {list1 is list2}")


print("\nCorrect way to handle mutable default arguments:")

def add_item_correctly(item, my_list=None):
    """Adds an item to a list, safely handling mutable defaults."""
    if my_list is None: # Check if no list was provided (None is immutable)
        my_list = []    # Create a new list only if needed
    my_list.append(item)
    print(f"Inside function: {my_list}")
    return my_list

print("First call to add_item_correctly:")
list_a = add_item_correctly(1)
print(f"Outside function (list_a): {list_a}")

print("\nSecond call to add_item_correctly (without providing a list):")
list_b = add_item_correctly(2)
print(f"Outside function (list_b): {list_b}")
print(f"Is list_a the same object as list_b? {list_a is list_b}") # Now False!
print(f"Providing own list: {add_item_correctly(3, [10, 20])}\n")


# --- 4. Using Default Arguments with Keyword-Only Arguments ---
print("4. Using Default Arguments with Keyword-Only Arguments:\n")

# You can force certain arguments to be passed only by keyword using `*`.
# This is often combined with default arguments for flexibility.

def configure_settings(theme="dark", *, show_sidebar=True, enable_logging=False):
    """Configures application settings."""
    print(f"Theme: {theme}")
    print(f"Show Sidebar: {show_sidebar}")
    print(f"Enable Logging: {enable_logging}")
    print("-" * 20)

configure_settings() # All defaults
configure_settings("light") # Overrides theme
# configure_settings(show_sidebar=False) # Error: theme is a positional argument, must be before keyword-only
configure_settings("light", show_sidebar=False)
configure_settings(enable_logging=True, theme="blue") # Order of keyword args doesn't matter
print()


# --- 5. Benefits of Default Arguments ---
print("5. Benefits of Default Arguments:\n")

# 1. Flexibility: Allows calling functions with fewer arguments for common cases.
# 2. Backward Compatibility: You can add new parameters to existing functions
#    with default values without breaking old code that doesn't provide them.
# 3. Readability: Makes it clear what the common/typical values are.

# Example: Date formatting
def format_date(year, month=1, day=1):
    """Formats a date. Month and day default to 1."""
    return f"{year:04d}-{month:02d}-{day:02d}"

print(f"format_date(2023): {format_date(2023)}")
print(f"format_date(2024, 7): {format_date(2024, 7)}")
print(f"format_date(2025, 6, 9): {format_date(2025, 6, 9)}")
print()

# Another example of the mutable default pitfall with datetime.datetime.now()
# This is a common subtle bug.
def log_message(message, timestamp=datetime.datetime.now()):
    """
    Logs a message with a timestamp.
    DANGER: timestamp will be the same for all calls if not provided,
    as datetime.datetime.now() is evaluated only once when the function is defined.
    """
    print(f"[{timestamp}] {message}")

print("Logging with default timestamp (DANGER):")
log_message("Event 1 happened.")
import time
time.sleep(1) # Wait a second
log_message("Event 2 happened.") # Timestamp will likely be the same as Event 1!

print("\nLogging with correct timestamp handling:")
def log_message_correct(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {message}")

log_message_correct("Event 3 happened.")
time.sleep(1)
log_message_correct("Event 4 happened.") # Timestamp will now be correct and different!


print("\n--- End of Python Default Arguments Demonstration ---")


print("--- Python Default Parameters with Variable-Length Arguments ---")
print("----------------------------------------------------------------\n")

# This topic combines two powerful Python features:
# 1. Default Parameters: Parameters with pre-defined values that can be overridden.
# 2. Variable-Length Arguments: Functions accepting an arbitrary number of arguments (*args for positional, **kwargs for keyword).

# --- 1. Combining *args with Default Parameters ---
print("1. Combining *args with Default Parameters:\n")

# Rule: Default parameters must come AFTER regular parameters but BEFORE *args.
# This structure isn't very common or directly supported in the way you might expect.
# *args captures all *remaining* positional arguments. If a parameter has a default,
# it means it's an *optional* positional argument.
# Therefore, you typically define default parameters *before* `*args`.

def describe_team(team_name, captain="Unknown", *members):
    """
    Describes a team, its captain, and lists all other members.
    `captain` has a default value. `*members` collects all remaining positional args.
    """
    print(f"Team: {team_name}")
    print(f"Captain: {captain}")
    if members:
        print(f"Members: {', '.join(members)}")
    else:
        print("Members: None")
    print("-" * 30)

print("Example 1.1: Only required argument:")
describe_team("Avengers")
# Output:
# Team: Avengers
# Captain: Unknown
# Members: None

print("\nExample 1.2: Required and default argument provided:")
describe_team("Justice League", "Batman")
# Output:
# Team: Justice League
# Captain: Batman
# Members: None

print("\nExample 1.3: Required, default, and *args provided:")
describe_team("X-Men", "Cyclops", "Wolverine", "Storm", "Jean Grey")
# Output:
# Team: X-Men
# Captain: Cyclops
# Members: Wolverine, Storm, Jean Grey

print("\nExample 1.4: Required, default taken, and *args provided:")
# This case is tricky because `captain` is a positional argument.
# If you want to use the default for `captain` AND provide members, you'd need
# to make `captain` a keyword-only argument if it were at the end, or explicitly pass None/empty string.
# But with `*args` capturing all remaining positional, it's straightforward.
# If you don't pass a value for 'captain', it takes the default.
# The members then go into `*members`.
describe_team("Guardians", "Star-Lord", "Gamora", "Drax", "Rocket", "Groot")
# Output:
# Team: Guardians
# Captain: Star-Lord
# Members: Gamora, Drax, Rocket, Groot

# If you wanted to explicitly use the default for `captain` while still passing members positionally
# you would have to pass an explicit None or empty string for captain in this specific signature.
# This signature `(team_name, captain="Unknown", *members)` is designed for `captain` to be positional
# and optional via default.
describe_team("Fantastic Four", "Mr. Fantastic", "Invisible Woman", "Human Torch", "The Thing")
print()


# --- 2. Combining **kwargs with Default Parameters ---
print("2. Combining **kwargs with Default Parameters:\n")

# Rule: Default parameters must come before `**kwargs`.
# `**kwargs` captures all *remaining* keyword arguments that were not matched by other parameters.
# Default parameters provide a way to make specific keyword arguments optional.

def configure_app(app_name, version="1.0", debug_mode=False, **extra_settings):
    """
    Configures an application with basic settings and any extra keyword settings.
    `version` and `debug_mode` have default values. `**extra_settings` captures others.
    """
    print(f"App Name: {app_name}")
    print(f"Version: {version}")
    print(f"Debug Mode: {debug_mode}")
    if extra_settings:
        print("Extra Settings:")
        for key, value in extra_settings.items():
            print(f"  {key}: {value}")
    else:
        print("No extra settings.")
    print("-" * 30)

print("Example 2.1: Only required argument:")
configure_app("MyEditor")
# Output:
# App Name: MyEditor
# Version: 1.0
# Debug Mode: False
# No extra settings.

print("\nExample 2.2: Overriding default arguments:")
configure_app("MyGame", version="2.5", debug_mode=True)
# Output:
# App Name: MyGame
# Version: 2.5
# Debug Mode: True
# No extra settings.

print("\nExample 2.3: Providing extra keyword arguments:")
configure_app("WebServer", port=8080, timeout=300, max_connections=100)
# Output:
# App Name: WebServer
# Version: 1.0
# Debug Mode: False
# Extra Settings:
#   port: 8080
#   timeout: 300
#   max_connections: 100

print("\nExample 2.4: Overriding defaults and providing extra keyword arguments:")
configure_app("DataAnalyzer", version="1.2", debug_mode=True,
              data_source="SQL", log_level="INFO", cache_enabled=True)
# Output:
# App Name: DataAnalyzer
# Version: 1.2
# Debug Mode: True
# Extra Settings:
#   data_source: SQL
#   log_level: INFO
#   cache_enabled: True
print()


# --- 3. Combining all three: Positional, Defaults, *args, **kwargs ---
print("3. Combining all three: Positional, Defaults, *args, **kwargs:\n")

# Full signature order:
# 1. Required positional arguments
# 2. Optional positional arguments (with defaults)
# 3. `*args` (collects remaining positional arguments)
# 4. Keyword-only arguments (with or without defaults) - defined after `*args` or `*`
# 5. `**kwargs` (collects remaining keyword arguments)

def process_data(data_id, processing_method="default", *items_to_process,
                 verbose=False, output_format="json", **metadata):
    """
    Processes data with various options.
    - data_id: required positional
    - processing_method: positional with default
    - *items_to_process: collects any number of additional positional args
    - verbose: keyword-only with default
    - output_format: keyword-only with default
    - **metadata: collects any other keyword args
    """
    print(f"Processing Data ID: {data_id}")
    print(f"Method: {processing_method}")
    if items_to_process:
        print(f"Items: {list(items_to_process)}")
    else:
        print("No specific items to process.")
    print(f"Verbose: {verbose}")
    print(f"Output Format: {output_format}")
    if metadata:
        print("Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    else:
        print("No metadata.")
    print("-" * 30)

print("Example 3.1: Minimal call (required + defaults):")
process_data("D123")
# Output:
# Processing Data ID: D123
# Method: default
# No specific items to process.
# Verbose: False
# Output Format: json
# No metadata.

print("\nExample 3.2: With positional items and overridden processing method:")
process_data("D456", "fast_process", "itemA", "itemB", 123)
# Output:
# Processing Data ID: D456
# Method: fast_process
# Items: ['itemA', 'itemB', 123]
# Verbose: False
# Output Format: json
# No metadata.

print("\nExample 3.3: With keyword-only arguments and metadata:")
process_data("D789", verbose=True, source="API", retries=5)
# Output:
# Processing Data ID: D789
# Method: default
# No specific items to process.
# Verbose: True
# Output Format: json
# Metadata:
#   source: API
#   retries: 5

print("\nExample 3.4: All together:")
process_data("D000", "custom_method", "data_entry_1", "data_entry_2",
             verbose=True, output_format="csv",
             user_id=101, timestamp="2023-10-26")
# Output:
# Processing Data ID: D000
# Method: custom_method
# Items: ['data_entry_1', 'data_entry_2']
# Verbose: True
# Output Format: csv
# Metadata:
#   user_id: 101
#   timestamp: 2023-10-26
print()


print("--- Important Considerations ---")

# 1. Readability: While powerful, don't make your function signatures overly complex.
#    Too many parameters can make a function hard to understand and use.

# 2. Positional vs. Keyword Arguments:
#    - Positional arguments are passed by order.
#    - Keyword arguments are passed by name.
#    - Default parameters can usually be passed positionally or by keyword.
#    - `*args` captures remaining positional.
#    - `**kwargs` captures remaining keyword.

# 3. Parameter Order Enforcement:
#    - Positional-only parameters (before `/` - Python 3.8+)
#    - Positional or keyword parameters (regular params, including those with defaults)
#    - Variadic positional parameters (`*args`)
#    - Keyword-only parameters (after `*args` or bare `*`)
#    - Variadic keyword parameters (`**kwargs`)

def example_order(pos_only, /, normal_with_default="def", *args, kw_only1, kw_only2="def2", **kwargs):
    print(f"pos_only: {pos_only}")
    print(f"normal_with_default: {normal_with_default}")
    print(f"args: {args}")
    print(f"kw_only1: {kw_only1}")
    print(f"kw_only2: {kw_only2}")
    print(f"kwargs: {kwargs}")
    print("-" * 30)

print("\nExample of full parameter order:")
example_order(10, 20, 30, 40, kw_only1=50, kw_only2="new", extra_k=60)
# 10 goes to pos_only
# 20 goes to normal_with_default
# 30, 40 go to *args
# 50 goes to kw_only1 (must be keyword)
# "new" goes to kw_only2 (overrides default, must be keyword)
# extra_k=60 goes to **kwargs

# What if you pass a keyword argument for a positional argument?
# example_order(pos_only=10) # ERROR: pos_only is positional-only
# example_order(10, normal_with_default=20, kw_only1=50) # Valid, normal_with_default can be keyword

# Python's flexibility with default arguments and variable-length arguments makes
# functions highly adaptable and powerful for various use cases.

print("\n--- End of Python Default Parameters with Variable-Length Arguments Demonstration ---")