# Problem Statement: Rearrange the array such that the first half is arranged in increasing order,
# and the second half is arranged in decreasing order
# Example :
# Input: 8 7 1 6 5 9
# Output: 1 5 6 9 8 7


nums = list(map(int, input().split()))


def increaseDescreaseSort(arr: list[int]) -> list:
    arr.sort()
    reversed_arr = arr[::-1]
    middle = len(arr)//2
    sorted_inc = arr[:middle+1]
    sorted_desc = reversed_arr[:middle]
    # sorted_inc.extend(sorted_desc)
    # return sorted_inc
    return [*sorted_inc, *sorted_desc]


print(increaseDescreaseSort(nums))
