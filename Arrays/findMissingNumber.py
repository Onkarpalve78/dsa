# LC 268 https://leetcode.com/problems/missing-number

nums = list(map(int, input().split()))


# nums.sort()
# print(nums)
# ans = 0
# for i in range(len(nums)):
#     if i == 0 and nums[-1] != len(nums) or i == 0 and nums[-1] == len(nums):
#         ans = len(nums)
#     elif nums[i] != nums[i-1]+1:
#         ans = nums[i-1]+1
#     elif nums[-1] != len(nums):
#         ans = len(nums)
#     else:
#         continue

# print(ans)

# def missingNumbers(nums: list[int]) -> int:
#     xor1, xor2 = 0, 0
#     nums.sort()
#     n = nums[-1]+1
#     for i in range(n):
#         xor1 ^= i
#     for i in range(len(nums)):
#         xor2 ^= nums[i]

#     return xor1 ^ xor2


# print(missingNumbers(nums))

def missingNumbers(nums: list[int]) -> int:
    N = len(nums)

    sumOfN = (N*(N+1))//2
    sumOfNums = 0
    for num in nums:
        sumOfNums += num

    missingNumber = sumOfN-sumOfNums

    return missingNumber


print(missingNumbers([9, 6, 4, 2, 3, 5, 7, 0, 1]))
