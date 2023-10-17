def reverse_kth_rows(matrix, k):
    for i in range(0, len(matrix), k):
        matrix[i:i+k] = matrix[i:i+k][::-1]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

k = 2  # Change k to reverse every kth row

print("Original Matrix:")
print_matrix(matrix)

reverse_kth_rows(matrix, k)

print(f"\nMatrix with every {k}th row reversed:")
print_matrix(matrix)
