

nums = list(map(int, input().split()))
threshold = int(input())
ans = []
for i, num in enumerate(nums):

    if nums[i-1] > threshold and i != 0:
        ans.append(i)

print(ans)
