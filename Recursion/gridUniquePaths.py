# LC 62 https://leetcode.com/problems/unique-paths/description/

# TLE on LC
# Check back to this when you start DP
def gridUniquePathBrute(m: int, n: int) -> int:

    def countPaths(indexM, indexN, m, n):

        if indexM == m-1 and indexN == n-1:
            return 1

        if indexM >= m or indexN >= n:
            return 0

        return countPaths(indexM+1, indexN, m, n)+countPaths(indexM, indexN+1, m, n)

    count = countPaths(0, 0, m, n)

    return count


print(gridUniquePathBrute(3, 7))
