# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter for the while loop
row = 0

# The outer while loop handles the rows
while row < size:
    # The inner for loop handles the columns (printing asterisks side by side)
    for _ in range(size):
        print("*", end="")
    
    # After finishing the for loop, print a newline to move to the next row
    print()
    
    # Increment the row counter to avoid an infinite loop
    row += 1