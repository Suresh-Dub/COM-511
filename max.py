# Input the number of elements (n)
n = int(input("Enter the number of elements: "))

# Initialize the maximum to a very small value
maximum = float("-inf")

# Use a for loop to input and find the maximum of n numbers
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    if num > maximum:
        maximum = num

# Print the maximum
print(f"The maximum of the {n} numbers is: {maximum}")