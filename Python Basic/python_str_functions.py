""" python str() functions

the str() function in python is an in-built function that takes an object as input and returns its string
 representation . it can be used to convert various data types into strings ,which can then be used for printing ,concatenation and formatting.

 """
 
n=123
s=str(n)
print(s)



""" syntax of str() function 


str(object,encoding="utf-8",errors="strict")

parameters:->

    1.object[optional]: the object to be converted into a string .this can be any python object , including integers ,floats ,lists ,dictionaries or bytes

    2. encoding(optional): specifies the encoding of the object if it's a byte-like object .the default encoding is UTF-8
    3. errors(optional): specifies the error-handling scheme to use if there's an encoding issue.Options include:
        1.'strict': Raises a UnicodeDecodeError if there's an encoding fails(default)
        2.'ignore':ignores errors
        3.'replace': Replaces problematic characters with a placeholder(? or similar)
        
Return Type:->
    returns a string representation of the given object.if no object is passed ,it returns an empty string  
"""


pi = 3.14159
s = str(pi)
print(s)


a = [1, 2, 3]
s = str(a)
print(s)


b = {'name': 'Alice', 'age': 25}
s = str(b)
print(s)


# Byte object containing text encoded in UTF-8
byte_data = b'Python programming'

# Convert byte object to string using UTF-8 encoding
text = str(byte_data, encoding='utf-8')
print(text)


# Byte object with invalid UTF-8 sequence
byte_data_invalid = b'Python programming \x80\x81'

# Convert byte object to string, ignoring errors
text = str(byte_data_invalid, encoding='utf-8', errors='ignore')
print(text)


# Byte object with an invalid sequence
byte_data_invalid = b'Hello, world! \x80\x81'

# Convert byte object to string, replacing errors with placeholder
text = str(byte_data_invalid, encoding='utf-8', errors='replace')
print(text)



# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(cnt)  
print(s2)



# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))