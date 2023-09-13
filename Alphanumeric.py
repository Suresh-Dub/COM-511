# Input the string
input_string = "Welcome to Python World"

# 1. Count the number of alphabets in the string
alphabet_count = sum(1 for char in input_string if char.isalpha())
print(f"Number of alphabets in the string: {alphabet_count}")

# 2. Extract characters from a given range (e.g., from index 8 to 14)
start_index = 8
end_index = 14
extracted_characters = input_string[start_index:end_index + 1]
print(f"Characters from index {start_index} to {end_index}: {extracted_characters}")

# 3. Check if the string is alphanumeric
is_alphanumeric = input_string.isalnum()
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")