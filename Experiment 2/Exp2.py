#Python Program to illustrate iteration over the List and dictionary


fruits = ["apple", "banana", "cherry", "date"]

print("Iterating over a List:")
for fruit in fruits:
    print(fruit)

student_info = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.7
}

print("\nIterating over a Dictionary:")
for key, value in student_info.items():
    print(f"{key}: {value}")
