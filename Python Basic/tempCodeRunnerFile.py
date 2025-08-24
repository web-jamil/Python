numbers=[1,2,3]
result = list(map(str, map(lambda x:x**2, numbers)))
print(f"Original list: {numbers}")
print(f"Squared values as strings: {result}")