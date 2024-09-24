
input_array = list(map(int, input().split()))


def bubble_sort():
    for i in range(len(input_array)):
        min_index = i
        swapped = False
        for j in range(i+1, len(input_array)):
            print("Shit ran")
            if input_array[min_index] > input_array[j]:
                input_array[min_index], input_array[j] = input_array[j], input_array[min_index]
                swapped = True
                print("Shit ran")
            if not swapped:
                break

    return input_array


print(bubble_sort())
