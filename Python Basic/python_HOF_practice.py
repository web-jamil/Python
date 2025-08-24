words=["banana", "pie", "apple", "cherry"," orange", "kiwi", "mango"]
print(sorted(words, key=len))
print(sorted(words, key=lambda x: x[-1]))
mixed_case= ["Apple", "Banana", "cherry", "date"]
print(sorted(mixed_case,key=str.lower))
#  Higher Order Functions enable elegant , functional style programming in python by treating functions as first class citizens.
# Higher order functions are a fundamental concepts in functional programming paradigms , and python supports them beautifully because functions in python are first class citizens.
# Python Higher Order Functions 
# In Python, a function is considered a Higher Order Fucntion if it fulfills at least one of the following criteria:
#  1. it takes one or more functions as arguments .
#  2. it returns a function as its result.
print("\n--- Higher Order Functions ---")
numbers=[1,2,3,4,5,6,7,8,9,10]


from functools import reduce 
numbers_to_reduce= [1, 2, 3, 4, 5]
sum_of_numbers=reduce(lambda x,y : x+y, numbers_to_reduce)
print(f"Sum of numbers using reduce: {sum_of_numbers}")
product_of_numbers=reduce(lambda x, y: x*y, numbers_to_reduce)
print(f"Product of numbers usign reduce : {product_of_numbers}")