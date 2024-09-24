
nums1 = list(map(int, input("Enter array A: ").split()))
nums2 = list(map(int, input("Enter array B: ").split()))


union = set(nums1)

for num in nums2:
    union.add(num)

res = list(union)
res.sort()

print(res)
