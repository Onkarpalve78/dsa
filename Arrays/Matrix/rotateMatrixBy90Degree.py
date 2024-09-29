# LC 48 https://leetcode.com/problems/rotate-image/description/

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotateMatrix(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    print(matrix)
    for i in range(rows):
        # for j in range(cols): here you dont need to range(cols)
        # cuz we need to only swap the upper triangular matrix to tranpose it,
        # cuz we swap every element in matrix we end up back with the original matrix
        for j in range(i):
            # matrix[i][j] = matrix[j][i] you were just assigning values here instead of swapping be careful
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)
    for row in matrix:
        row.reverse()

    return matrix


print(rotateMatrix(matrix))
