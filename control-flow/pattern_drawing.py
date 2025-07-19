
# Get user input for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    
    # Print newline after completing each row
    print()
    
    # Increment row counter
    row += 1
