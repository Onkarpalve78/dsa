# LC 78 https://leetcode.com/problems/subsets/
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    subset = []
    for num in range(2**len(nums)):
        sub_subset = []
        for i in range(num):
            is_set = num & (1 << i)  # from findiThBitIsSet.py
            if is_set:
                sub_subset.append(nums[i])
        subset.append(sub_subset)

    return subset


print(subsets([1, 2, 4]))
