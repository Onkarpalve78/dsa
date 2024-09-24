nums = list(map(int, input().split()))


def merge_array(arr, low, middle, high):
    left = low
    right = middle+1
    sorted_array = []

    while left <= middle and right <= high:
        if arr[left] <= arr[right]:
            sorted_array.append(arr[left])
            left += 1
        elif arr[right] <= arr[left]:
            sorted_array.append(arr[right])
            right += 1

    sorted_array.extend(arr[left:middle+1])
    sorted_array.extend(arr[right:high+1])

    for i in range(len(sorted_array)):
        print("low", low)
        arr[i+low] = sorted_array[i]
    return arr


def mergeSort(arr, low, high):

    if low >= high:
        return

    middle = (low+high)//2

    mergeSort(arr, low, middle)

    mergeSort(arr, middle+1, high)

    return merge_array(arr, low, middle, high)


print(mergeSort(nums, 0, len(nums)-1))
