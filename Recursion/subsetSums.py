# https://www.geeksforgeeks.org/problems/subset-sums2234/1


def printAllSubsets(index, ans_arr: list, arr: list, n):

    if index == n:
        if len(ans_arr) > 0:
            print(sum(ans_arr), end=" ")
        else:
            print('0', end=" ")
        return

    ans_arr.append(arr[index])

    printAllSubsets(index+1, ans_arr, arr, n)

    ans_arr.pop()

    printAllSubsets(index+1, ans_arr, arr, n)


ans_arr = []
arr = [1, 2]
n = len(arr)
index = 0

printAllSubsets(index, ans_arr, arr, n)
