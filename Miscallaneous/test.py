nums = list(map(int, input("Enter your numbers").split()))


def findMaxNumbers(nums: list[int]) -> int:
    max = 0
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max


print(findMaxNumbers(nums))
