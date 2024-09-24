

nums = list(map(int, input().split()))


# maximum = max(nums)
# minimum = min(nums)
# nums.remove(maximum)
# nums.remove(minimum)

# second_max = max(nums)
# second_min = min(nums)

# print(second_max, second_min)

def secondLargestAndSmallest(arr):
    minimum = second_min = max(nums)
    maximum = second_max = arr[0]

    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            second_max = maximum
            maximum = arr[i]
        if arr[i] < minimum:
            second_min = minimum
            minimum = arr[i]
        elif arr[i] < second_min and arr[i] != minimum:
            second_min = arr[i]
    return [second_max, second_min]


print(secondLargestAndSmallest(nums))
