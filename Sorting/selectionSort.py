

unsorted_array = list(map(int, input().split()))


def selection_sort():
    for i in range(len(unsorted_array)):
        min_index = i
        for j in range(i+1, len(unsorted_array)):
            if unsorted_array[min_index] > unsorted_array[j]:
                min_index = j
        unsorted_array[min_index], unsorted_array[i] = unsorted_array[i], unsorted_array[min_index]
    return unsorted_array


print(selection_sort())
