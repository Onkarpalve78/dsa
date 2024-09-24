
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

# region brute

nums = set(nums)
nums = list(nums)
nums.sort()

print(nums)

max_len = 1


for i, num in enumerate(nums):
    if i == len(nums)-1:
        break
    if num+1 in nums:
        max_len += 1
    elif num+1 not in nums:
        max_len = 1

print(max_len)
