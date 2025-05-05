def my_function():
    """This is a docstring for the function.
    It explains what the function does.
    """
    pass

print(my_function.__doc__)

def generate_full_name():
    first_name='Milaan'
    last_name='Parmar'
    space=' '
    full_name=first_name+space+last_name
    print(full_name)
generate_full_name()

# if we pass the arguments with key and value ,the order of the arguments does not matter

# def print_fullname(firstname,lastname):
#     space=' '
#     full_name=firstname+space+lastname
#     print(full_name)
#     return full_name
# print(print_fullname(lastname='Parmer',firstname='Milaan'))


# def add_two_numbers(num1,num2):
#     total=num1+num2
#     print(total)
#     return total
# print(add_two_numbers(3,4))

# def arithmetic(num1,num2):
#     add=num1+num2
#     sub=num1-num2
#     multiply=num1*num2
#     division=num1/num2
#     return add,sub,multiply,division

# a,b,c,d=arithmetic(10,2)
# print("addition :",a)
# print("substraction :",b)
# print("multiplication:",c)
# print("Division:",d)

def is_even(n):
    if n%2==0:
        print("even")
        return True
    return False
print(is_even(10))


print(is_even(7))

