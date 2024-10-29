# LC 54 https://leetcode.com/problems/spiral-matrix/

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def spiralMatrix(matrix) -> list[int]:
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    ans = []

    while left < right and top < bottom:
        # all i of top
        for i in range(left, right):
            ans.append(matrix[top][i])
        top += 1

        # all i of rightmost column
        for i in range(top, bottom):
            ans.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # all i of bottom
        for i in range(right-1, left-1, -1):
            ans.append(matrix[bottom-1][i])
        bottom -= 1

        # all i of left
        for i in range(bottom-1, top-1, -1):
            ans.append(matrix[i][left])
        left += 1
    return ans


print(spiralMatrix(matrix))
