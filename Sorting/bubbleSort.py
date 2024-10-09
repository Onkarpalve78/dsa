
input_array = list(map(int, input().split()))


def bubble_sort():
    for i in range(len(input_array)):
        min_index = i
        # This is used to ensure the bubble sort algorithm doesnt run for an already sorted array.
        swapped = False
        for j in range(i+1, len(input_array)):

            if input_array[min_index] > input_array[j]:
                input_array[min_index], input_array[j] = input_array[j], input_array[min_index]
                swapped = True

            if not swapped:
                break

    return input_array


def bubbleSort(nums):
    length = len(nums)
    didSwap = False
    # This is used to ensure the bubble sort algorithm doesnt run for an already sorted array.

    # Outer loop to reduce the range of comparison after every pass
    # Since we know the largest element will be shifted to the rightmost end,
    # no need to iterate till that point, they are where they belong
    for i in range(length-1, -1, -1):
        # Inner loop to compare adjacent elements
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                didSwap = True

        if not didSwap:
            print("didnt")
            break
    return nums


print(bubble_sort())
print(bubbleSort(input_array))
