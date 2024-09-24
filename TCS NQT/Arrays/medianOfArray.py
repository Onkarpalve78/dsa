
nums = list(map(int, input().split()))
# nums = [4, 7, 1, 2, 5, 6]
nums.sort()


def median(nums: list[int]):

    n = len(nums)
    middle = n//2

    if n % 2 == 1:
        print(nums[middle])
    else:
        print((nums[middle-1]+nums[middle])/2)


median(nums)
