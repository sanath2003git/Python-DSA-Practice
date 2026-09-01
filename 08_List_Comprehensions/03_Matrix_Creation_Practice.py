rows = int(input())
cols = int(input())
matrix = [[0] * cols for _ in range(rows)]
matrix[0][1] = 5
matrix[2][3] = 9
for row in matrix:
    print(row)