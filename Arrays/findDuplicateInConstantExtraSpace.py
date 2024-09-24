# LC 287 https://leetcode.com/problems/find-the-duplicate-number/solutions/4916443/interview-approach-7-approaches/


nums = list(map(int, input().split()))


def FindDuplicate(nums: list[int]) -> int:

    nums.sort()
    print(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
        else:
            continue


print(FindDuplicate(nums))
