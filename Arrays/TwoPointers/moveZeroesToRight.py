# LC 283


nums = list(map(int, input().split()))

# count = 0
# for i in range(len(nums)):
#     if nums[i] == 0:
#         nums.pop(i)
#         count += 1

# for i in range(count):
#     nums.append(0)

# print(nums)

j = -1
for i in range(len(nums)):
    if nums[i] == 0:
        j = i
        break


for i in range(j, len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

print(nums)
