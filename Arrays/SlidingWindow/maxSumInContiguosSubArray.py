
# Find maximum sum subarray with a window size n

n = 3
arr = [2, 3, 4, -3, 7, -2, -6, -4, 5]
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]


def maximumSubarray(arr: list[int], n: int) -> int:
    l, r = 0, 0

    summation = 0
    ans = 0
    while l <= r and r < len(arr):
        summation += arr[r]
        ans = max(ans, summation)
        r += 1

        if r-l >= n:
            summation -= arr[l]
            l += 1

    return ans


print(maximumSubarray(arr, n))
