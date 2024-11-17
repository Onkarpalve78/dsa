# LC 260 https://leetcode.com/problems/single-number-iii/
from typing import List


def singleNumber(nums: List[int]) -> List[int]:

    xor = 0
    for num in nums:
        xor ^= num

    mask = xor & (-xor)
    group_a = 0
    group_b = 0

    for num in nums:
        if num & mask:
            group_a ^= num
        else:
            group_b ^= num

    ans = [group_a, group_b]

    return ans


print(singleNumber([2, 2, 1, 4, 4, 7]))
