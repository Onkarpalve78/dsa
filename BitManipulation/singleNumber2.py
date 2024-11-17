# LC 173 https://leetcode.com/problems/single-number-ii/
from typing import List


def singleNumberII(nums: List[int]) -> int:
    ans = 0
    for i in range(32):
        countOnes = 0
        bitmask = 1 << i
        for num in nums:
            if num & bitmask != 0:
                countOnes += 1

        if countOnes % 3 != 0:
            ans |= bitmask

        if ans >= 2**31:
            ans -= 2**32

    return ans


print(singleNumberII([3, 3, 3, 45, 2, 2, 2]))
