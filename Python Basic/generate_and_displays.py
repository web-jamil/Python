row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(i * j, end=" ")  # Add a space for better readability
    print()  # Move to the next line after each row
