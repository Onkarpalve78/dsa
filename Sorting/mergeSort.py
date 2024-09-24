
# Merge Sort	TC: O(N log N)	SC: O(N)
nums = list(map(int, input().split()))


def mergeSort(arr, low, high):
    middle = (low+high)//2

    if low >= high:
        return

    mergeSort(arr, low, middle)

    mergeSort(arr, middle+1, high)

    return merge(arr, low, middle, high)


def merge(arr, low, middle, high):
    left = low
    right = middle+1
    sorted_list = []
    print("sorted", sorted_list)

    while left <= middle and right <= high:
        if arr[left] <= arr[right]:  # If you want to sort in descending then make the signs opposites here
            sorted_list.append(arr[left])
            left += 1
        elif arr[right] <= arr[left]:
            sorted_list.append(arr[right])
            right += 1

    sorted_list.extend(arr[left:middle+1])
    sorted_list.extend(arr[right:high+1])

    # while left <= middle:
    #     sorted_list.append(arr[left])
    #     left += 1
    # while right <= high:
    #     sorted_list.append(arr[right])
    #     right += 1
    for i in range(len(sorted_list)):
        arr[i+low] = sorted_list[i]


mergeSort(nums, 0, len(nums)-1)

print(nums)

# List slicing allows you to extract a portion (sublist) of a list in Python using the syntax:

# python=> list[start:end]

# This means:

#     start is the index from where the slicing begins (inclusive).
#     end is the index where the slicing stops (exclusive). The element at the end index is **NOT** included.


# .extend() list.extend(iterable) , Any iterable (list, set, tuple, etc.)

# fruits = ['apple', 'banana', 'cherry']

# points = (1, 4, 5, 9)

# fruits.extend(points)

# gives=> ['apple', 'banana', 'cherry', 1, 4, 5, 9]
