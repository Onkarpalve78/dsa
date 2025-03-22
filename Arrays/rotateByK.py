

nums = list(map(int, input().split()))
k = int(input("Enter k: "))
k = k % len(nums)  # this is to handle the case when k is greater than the length of the array, in that case we can just rotate the array by k % len(nums) times to get the same result
print("K==>", k)
count = 0

for i in range(len(nums)-k, len(nums)):
    # print(f"Count {count}, num {nums[i+1]} i {i}")
    nums.insert(count, nums[i+count])
    # insert function inserts the element at the specified index and shifts the rest of the elements to the right
    count += 1

print("Before==>", nums)

# print(nums[:-k])  # this is to remove the last k elements from the array but since this is a slice operation, it doesn't modify the original array rather it returns a new array with the last k elements removed

for i in range(k):
    nums.pop()

print("After==>", nums)
