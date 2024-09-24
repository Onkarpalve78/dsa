# LC 2248
# https://leetcode.com/problems/intersection-of-multiple-arrays/description/

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
ans = []
common = {}
for i, num in enumerate(nums):
    for j, num in enumerate(num):
        common[num] = common.get(num, 0)+1


for item in common:
    if common[item] == len(nums):
        ans.append(item)

print(ans)
