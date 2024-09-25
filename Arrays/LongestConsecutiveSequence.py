
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6, 234]

# region brute

# Works for most test casess but time limit exceeds, since youre searching in list in a loop
# nums = list(nums)
# nums.sort()
# nums = set(nums)

# print(nums)

# max_len, current_max = 1, 1


# for i, num in enumerate(nums):
#     if i == len(nums)-1:
#         break
#     if current_max > max_len:
#         max_len = current_max
#     if num+1 in nums:
#         current_max += 1
#     elif num+1 not in nums:
#         current_max = 1

# max_len = max(current_max, max_len)

# print(max_len)

# Neetcode's solution
def maxLen(nums):
    set_search = set(nums)
    length, max_len = 0, 0
    for i, num in enumerate(nums):
        if (i-1) not in set_search:
            length = 1
            while i+length in set_search:
                length += 1

            max_len = max(max_len, length)

    return max_len


print(maxLen(nums))
