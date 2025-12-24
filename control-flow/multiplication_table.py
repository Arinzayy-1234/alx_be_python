# multiplication_table.py

# Prompt the user for a number and store it in the variable 'number'
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through numbers 1 to 10
# Note: range(1, 11) starts at 1 and stops before 11
for i in range(1, 11):
    # Calculate the product
    product = number * i
    # Print the result in the exact format "X * Y = Z"
    print(f"{number} * {i} = {product}")