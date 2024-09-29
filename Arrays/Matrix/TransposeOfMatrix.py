

numberOfRows = int(input("Enter Number Of Rows "))
numberOfColumns = int(input("Enter Number Of Columns "))

matrix = []

for i in range(numberOfRows):
    rows = []
    for j in range(numberOfColumns):
        element = int(input(f"Enter item at matrix[{i+1}][{j+1}]: "))
        rows.append(element)
    matrix.append(rows)

print(matrix)
# for i in matrix:
#     print(i)

# for i in range(2):
#     for j in range(len(matrix)):
#         print(matrix[i][j], matrix[j][i])
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

ROWS, COLUMNS = len(matrix), len(matrix[0])

result_matrix = [[0] * ROWS for _ in range(COLUMNS)]

for r in range(ROWS):
    for c in range(COLUMNS):
        result_matrix[r][c] = matrix[c][r]


print(result_matrix)

# striver's method: here we swap elements in place
for i in range(ROWS):
    for j in range(i):  # range is only till i cuz we dont want to swap everything ,
        # only upper triangular with lower triangular, or else we would end up with original matrix
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
