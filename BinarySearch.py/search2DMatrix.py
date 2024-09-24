# LC 74 https://leetcode.com/problems/search-a-2d-matrix
# TC O(Log(m*n))
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 342


def binarySearch(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    start, end = 0, (rows*cols)-1
    while start <= end:
        middle = start + (end-start)//2
        row = middle//cols
        col = middle % cols

        if target > matrix[row][col]:
            start = middle+1
        elif target < matrix[row][col]:
            end = middle-1

        else:
            return True

    return False


print(binarySearch(matrix, target))
