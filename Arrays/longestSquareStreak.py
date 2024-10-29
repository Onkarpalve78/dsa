# LC 2501 https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=daily-question&envId=2024-10-28

from math import isqrt
from typing import List
nums = [2, 4, 4, 2]

# passed 77/92 test cases
# failed at
# nums = [17,19,4,17,10,18,9,3,14]
# Use Testcase
# Stdout
# [4, 9]
# Output
# -1
# Expected
# 2


def longestSquareStreakBrute(nums: List[int]) -> int:

    subsequence = []
    count = 1
    for num in nums:
        if num % isqrt(num) == 0:
            subsequence.append(num)

    subsequence.sort()
    if len(subsequence) == 0:
        return -1
    if isqrt(subsequence[0]) in nums:
        subsequence.insert(0, isqrt(subsequence[0]))

    print(subsequence)

    for i in range(len(subsequence)):
        if i < len(subsequence)-1:
            print("hey", i)

            if subsequence[i]**2 == subsequence[i+1]:
                count += 1
                continue
            else:
                break
        # else:
        #     count += 1

    return count if count > 1 else -1


print(longestSquareStreakBrute(nums))


def longestSquareStreak(nums: List[int]) -> int:
    nums.sort()
    mp = {}
    ans = -1

    for num in nums:
        sqrt = isqrt(num)

        if sqrt*sqrt == num and sqrt in mp:
            mp[num] = mp[sqrt]+1
            ans = max(ans, mp[num])
        else:
            mp[num] = 1

    return ans


print(longestSquareStreak(nums))

# Code Breakdown and Explanation

# In the code:

#     nums.sort(): The input list is sorted so that we process numbers in ascending order,
# which helps in building streaks from smaller perfect squares to larger ones.

#     Dictionary mp: This dictionary stores the longest streak for each number found so far, where a "streak" is defined as a
# sequence where each element is a perfect square of the previous one (e.g., 4→16→2564→16→256).

#     Loop through each number in nums:
#         Compute sqrt = isqrt(num):
#             isqrt(num) calculates the integer square root of num. For example, if num is 16, isqrt(16) returns 4.
#         Check sqrt * sqrt == num:
#             This checks if num is a perfect square. For instance, if num is 16 and sqrt is 4, then 4×4=164×4=16,
# so num is a perfect square. This ensures we only consider numbers that are perfect squares in our streak-building logic.

#     Check if sqrt is in mp:
#         If sqrt (the previous perfect square in the sequence) exists in mp, it means there is an existing streak that num can extend.
#         Extend the streak: mp[num] = mp[sqrt] + 1
#             This line adds num to the streak of sqrt, incrementing the streak count by 1.
#         Update ans with the maximum streak length.

#     If the conditions are not met (else clause):
#         If num is not a perfect square or its square root doesn’t exist in mp, then mp[num] = 1, meaning this
#         number starts its own new streak of length 1.

# Example Walkthrough

# Consider nums = [4, 16, 2, 256]:

#     After sorting, nums becomes [2, 4, 16, 256].
#     For each number:
#         2: Not a perfect square, so mp[2] = 1.
#         4: Perfect square of 2, but since 2 isn’t in mp for a streak, mp[4] = 1.
#         16: Perfect square of 4, and mp[4] = 1, so mp[16] = mp[4] + 1 = 2.
#         256: Perfect square of 16, and mp[16] = 2, so mp[256] = mp[16] + 1 = 3.

# Finally, the longest streak found is 3 (sequence 4 -> 16 -> 256), so ans = 3.
