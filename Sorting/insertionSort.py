

arr = list(map(int, input().split()))
# WC TC O(n^2)
# BC TC O(n) if the array is already sorted it'll never enter the while loop


def insertionSort(nums) -> list[int]:
    for i in range(1, len(nums)):
        j = i

        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


print(insertionSort(arr))
