
nums = [4, 2, 8, 6, 15, 5, 9, 20]
# nums = [8, 7, 1, 6, 5, 9]


def increasingDecreasing(nums: list[int]) -> list[int]:
    mid = len(nums)//2

    nums.sort()
    increasing = nums[0:mid]

    decreasing = nums[mid:]
    decreasing.sort(reverse=True)

    return [*increasing, *decreasing]


print(increasingDecreasing(nums))
