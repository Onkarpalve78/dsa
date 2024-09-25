

nums = list(map(int, input().split()))

target = int(input("Enter target: "))


def TwoSum(nums, target):
    dict_search = {}
    for i, num in enumerate(nums):
        dict_search[num] = i

    for i, num in enumerate(nums):
        diff = target-num
        if diff in dict_search and dict_search[diff] != i:
            return [i, dict_search[diff]]


print(TwoSum(nums, target))
