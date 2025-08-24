## float() in python

## python float() function is used to return a floating-point number from a number or a string representation of a numeric value

# convert integer value to float

num = float(10)
print(num)

# Python float() Function Syntax
# The float() function in Python has the following syntax.

# Syntax: float(x)

# Parameter x: x is optional & can be:

# any number or number in form of string, ex,: “10.5”
# inf or infinity, NaN (any cases)

# Return: Float Value

# Values that the Python float() method can return depending upon the argument passed

# If an argument is passed, then the equivalent floating-point number is returned.
# If no argument is passed then the method returns 0.0.
# If any string is passed that is not a decimal point number or does not match any cases mentioned above then an error will be raised.
# If a number is passed outside the range of Python float then OverflowError is generated.


# Python program to illustrate
# Various examples and working of float()
# for integers
print(float(21.89))
 
# for floating point numbers
print(float(8))
 
# for integer type strings
print(float("23"))
 
# for floating type strings
print(float("-16.54"))
 
# for string floats with whitespaces
print(float("     -24.45   \n"))
 
# for inf/infinity
print(float("InF"))
print(float("InFiNiTy"))
 
# for NaN
print(float("nan"))
print(float("NaN"))


# python code to convert int 
# float
number = 90
result = float(number)
 
print(result)

# Python program to illustrate
# Various examples and working of float()
 
# for inf/infinity
print(float("InF"))
print(float("InFiNiTy"))
 
# for NaN
print(float("nan"))
print(float("NaN"))


# python code to convert string
# to float
string = "90"
result1 = float(string)
 
# for floating type strings
float_string = "-16.54"
result2 = float(float_string)
 
print(result1)
print(result2)


""" Python float() Exceptions and Errors
Sometimes the float() function in Python may not be compatible with all the datatypes. In this case, it may raise an exception or generate an error.

Python float() exception
Python float() will raise ValueError if the passed parameter is not a numeric value. In this example, we passed an alphabet string as the parameter to the float() function. """


number = "geeks"
try:
    print(float(number))
except ValueError as e:
    print(e)