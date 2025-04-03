# LC 169 https://leetcode.com/problems/majority-element
from typing import List
nums = [2, 2, 1, 1, 1, 2, 2]


def majorityElement(nums: List[int]) -> int:
    min_amount = len(nums)//2
    counter = {}
    for i, num in enumerate(nums):

        if counter.get(num, None):
            counter[num] += 1
        else:
            counter[num] = 1

    for key, value in counter.items():
        if value > min_amount:
            return key


print(majorityElement(nums))

# 30-03-2025


def majorityElement(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]
