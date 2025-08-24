# The 'string.Template' class provides a simpler way to perform string substitutions.
# It is particularly useful when dealing with user-supplied strings, as it does not
# support arbitrary Python expressions and is therefore safer than f-strings or
# str.format() when the template or substitution values come from untrusted sources.

from string import Template

print("--- 1. Basic Substitution ---")
# Placeholders are indicated by a '$' followed by a valid Python identifier.
# Or, if the identifier is immediately followed by more alphanumeric characters,
# it must be enclosed in curly braces: ${identifier}.

t = Template('Hello, $name! Welcome to $place.')
result_basic = t.substitute(name='Alice', place='Wonderland')
print(f"Basic substitution: {result_basic}")

# Using a dictionary for substitutions
data = {'name': 'Bob', 'place': 'the Matrix'}
result_dict = t.substitute(data)
print(f"Substitution with dictionary: {result_dict}")
print("-" * 30)

print("--- 2. Escaping the Dollar Sign ---")
# To include a literal dollar sign in the output, use '$$'.

t_escape = Template('The price is $amount$$ today.')
result_escape = t_escape.substitute(amount='10.50')
print(f"Escaping dollar sign: {result_escape}")
print("-" * 30)

print("--- 3. Using Curly Braces for Identifiers ---")
# Curly braces are necessary when the placeholder name is immediately followed
# by characters that are part of the word but not part of the identifier.

t_curly = Template('It is ${hour}AM and the temperature is ${temp}C.')
result_curly = t_curly.substitute(hour='09', temp='25')
print(f"Using curly braces: {result_curly}")
print("-" * 30)

print("--- 4. Handling Missing Placeholders with .substitute() ---")
# If a placeholder specified in the template is not provided in the substitution
# arguments (either keywords or dictionary), .substitute() will raise a KeyError.

t_missing = Template('Product: $item, Quantity: $qty, Price: $price.')
try:
    # 'price' is missing
    t_missing.substitute(item='Laptop', qty=2)
except KeyError as e:
    print(f"Error with missing placeholder (substitute): {e}")
print("-" * 30)

print("--- 5. Handling Missing Placeholders with .safe_substitute() ---")
# The .safe_substitute() method handles missing placeholders by leaving
# them unchanged in the output string. This is safer for user-supplied templates.

t_safe = Template('Product: $item, Quantity: $qty, Price: $price.')
result_safe = t_safe.safe_substitute(item='Keyboard', qty=5)
print(f"Safe substitution (missing 'price'): {result_safe}")

# If some placeholders are provided, they are substituted normally.
result_safe_partial = t_safe.safe_substitute(item='Mouse', price='15.99')
print(f"Safe substitution (missing 'qty'): {result_safe_partial}")
print("-" * 30)

print("--- 6. Custom Delimiter for Placeholders ---")
# You can customize the delimiter by overriding the 'delimiter' and 'idpattern'
# attributes in a subclass of Template. The 'idpattern' is a regular expression
# that defines what constitutes a valid identifier.

class MyTemplate(Template):
    delimiter = '%'  # Change from '$' to '%'

class CustomIdTemplate(Template):
    delimiter = '%'
    # Allow identifiers to start with a number (not recommended for general use, just for demo)
    idpattern = r'[a-zA-Z0-9_]+'

t_custom_delimiter = MyTemplate('Hello, %name! Your %city is lovely.')
result_custom = t_custom_delimiter.substitute(name='Charlie', city='New York')
print(f"Custom delimiter (%): {result_custom}")

t_custom_id = CustomIdTemplate('Value is %123test.')
result_custom_id = t_custom_id.substitute(**{'123test': 'Success!'})
print(f"Custom ID pattern (starts with number): {result_custom_id}")
print("-" * 30)

print("--- 7. Common Use Cases ---")

# a) Generating dynamic messages where parts might be optional or unknown
message_template = Template("Reminder: $event at $time in $location. $notes_optional")
print(f"Event 1: {message_template.safe_substitute(event='Meeting', time='10 AM', location='Office', notes_optional='Bring presentation.')}")
print(f"Event 2: {message_template.safe_substitute(event='Lunch', time='1 PM', location='Cafeteria')}") # notes_optional is left as is

# b) Safely constructing SQL queries or shell commands (though prepared statements are usually better for SQL)
# This is a conceptual example; always prefer proper parameter binding for SQL to prevent SQL injection.
# query_template = Template("SELECT * FROM users WHERE username = '$username'")
# user_input = "admin' OR '1'='1" # Malicious input
# print(f"Potentially unsafe query: {query_template.substitute(username=user_input)}")

# c) Simple templating for configuration files or basic text generation
config_template = Template("""
[SERVER]
host = $hostname
port = $port
debug = $debug_mode
""")
config_data = {
    'hostname': 'localhost',
    'port': '8080',
    'debug_mode': 'True'
}
print("\nGenerated Configuration:")
print(config_template.substitute(config_data))
print("-" * 30)