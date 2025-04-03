# LC 238

nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
ans = []

for num in nums:
    split_arr = nums.copy()
    split_arr.remove(num)

    sum = 1
    for num in split_arr:
        sum *= num
    ans.append(sum)

print(ans)
