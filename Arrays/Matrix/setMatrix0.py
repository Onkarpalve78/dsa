# LC73 https://leetcode.com/problems/set-matrix-zeroes/description/


# matrix=[]
# rows = 3
# columns = 3
# for i in range(rows):
#     column_arr = []
#     for j in range(columns):
#         element = int(input(f"Enter Element for  matrix[{i+1}][{j+1}] "))
#         column_arr.append(element)

#     matrix.append(column_arr)


# Time Complexity: O(M * N * (M + N))
# Space Complexity: O(M * N)

matrix = [[1, 2, 1], [4, 9, 1], [0, 8, 9]]
rows, columns = len(matrix), len(matrix[0])


def setZeroesBrutey(matrix: list[list[int]]):

    copy_matrix = [row[:] for row in matrix]

    for i, column in enumerate(matrix):
        for j, columnElement in enumerate(column):
            if columnElement == 0:
                for k in range(len(column)):
                    copy_matrix[i][k] = 0
                for p in range(rows):
                    copy_matrix[p][j] = 0
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = copy_matrix[i][j]
    return matrix


print(setZeroesBrutey(matrix))


# Time Complexity: O(M * N)
# Space Complexity: O(M + N)

new_matrix = [[1, 2, 1], [4, 9, 1], [0, 8, 9]]
rows, columns = len(new_matrix), len(new_matrix[0])


def setZeroes(matrix: list[list[int]]):
    if not matrix:
        return []

    zero_row, zero_col = set(), set()
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in range(rows):
        for j in range(columns):
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0

    return new_matrix


print(setZeroes(new_matrix))
