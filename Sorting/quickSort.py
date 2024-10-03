

nums = list(map(int, input().split()))


def insertPivotToMiddle(arr, low, high):
    print(f"low:{low}, high {high} , arr: {arr}")
    pivot = arr[low]
    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] > pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        print(f"arr:{arr} ,given j: ", j)
        return j


def quickSort(arr, low, high):

    if low >= high:
        return

    if low < high:
        middle_index = insertPivotToMiddle(arr, low, high)

        quickSort(arr, low, middle_index)
        quickSort(arr, middle_index+1, high)

    return arr


print(quickSort(nums, 0, len(nums)-1))
