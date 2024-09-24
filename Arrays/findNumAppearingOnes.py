# LC 136 https://leetcode.com/problems/single-number/


nums = list(map(int, input().split()))

# region brute
# for i in range(max(nums)):
#     if nums.count(i) == 1:
#         print(i)
#         break
#     elif i == max(nums)-1:
#         print(max(nums))
#         break

# region better
# count = {}
# for i in range(len(nums)):
#     if nums[i] in count:
#         count[nums[i]] += 1

#     else:
#         count[nums[i]] = 1

# for item in count:
#     if count[item] == 1:
#         print(item)

# region optimal
xor1 = 0
for i in range(len(nums)):
    xor1 ^= nums[i]

print(xor1)
