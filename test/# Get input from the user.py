"""
# Get input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Print the result
print("The area of the rectangle is:", area)
"""


# Get input from the user
length_str = input("Enter the length of the rectangle: ")
width_str = input("Enter the width of the rectangle: ")

# Attempt to convert input strings to integers
try:
    length = int(length_str)
    width = int(width_str)
except ValueError:
    print("Value must be an integer.")
    # You can choose to exit the program or handle this error differently here.
else:
    # Calculate the area
    area = length * width

    # Print the result
    print("The area of the rectangle is:", area)
