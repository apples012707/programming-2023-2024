matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_rows = len(matrix)
num_cols = len(matrix[0]) if matrix else 0  

for row in range(num_rows):
    for col in range(num_cols):
        print(matrix[row][col], end=" ")  
    print()  