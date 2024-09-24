# LC 1004 https://leetcode.com/problems/max-consecutive-ones-iii/description/

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s.
# Example 1:
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6

# nums = list(map(int, input().split()))
# # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# # nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = int(input("Enter K: "))


# def maxConsecutiveOnes(arr: list[int], k: int) -> int:
#     left, right, max_ones = 0, 0, 0
#     N = len(arr)

#     while right < N:
#         print(left, right, k)
#         if k > 0:
#             if arr[right] == 0:
#                 k -= 1
#                 right += 1

#             else:
#                 right += 1
#         else:
#             if arr[left] == 0:
#                 k += 1
#                 left += 1

#             else:
#                 left += 1
#             maximum = (right-left)+1
#             print(maximum, " right: ", right, " left: ", left)
#             max_ones = max(max_ones, (right-left)+1)

#     return max_ones


# print(maxConsecutiveOnes(nums, k))


# TC O(2N)
# nums = list(map(int, input().split()))
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]

k = int(input("Enter K: "))


def maxConsecutiveOnes(arr: list[int], k: int) -> int:
    left, zeroes = 0, 0
    N = len(arr)
    max_len = 0

    for right in range(N):

        if arr[right] == 0:
            zeroes += 1

        while zeroes > k:
            if arr[left] == 0:
                zeroes -= 1
                left += 1
            else:
                left += 1
        max_len = max(max_len, (right-left)+1)

    return max_len


print(maxConsecutiveOnes(nums, k))
