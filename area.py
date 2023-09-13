import math

# Function to calculate the area and perimeter of a circle
def circle_properties(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Function to calculate the area and perimeter of a square
def square_properties(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

# Function to calculate the area and perimeter of a rectangle
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Input choice of shape
print("Choose a shape:")
print("1. Circle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter your choice (1/2/3): "))

# Calculate and display properties based on user's choice
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area, perimeter = circle_properties(radius)
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle: {perimeter:.2f}")
elif choice == 2:
    side_length = float(input("Enter the side length of the square: "))
    area, perimeter = square_properties(side_length)
    print(f"Area of the square: {area:.2f}")
    print(f"Perimeter of the square: {perimeter:.2f}")
elif choice == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area, perimeter = rectangle_properties(length, width)
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")
else:
    print("Invalid choice. Please choose 1, 2, or 3.")