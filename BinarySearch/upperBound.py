# https://www.naukri.com/code360/problems/implement-upper-bound_8165383?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries


def lowerUpper(arr, x):
    start = 0
    end = len(arr)-1
    upper = len(arr)  # Condition in question if upperbound isnt present

    while start <= end:
        middle = (start+end)//2
        if arr[middle] > x:
            upper = middle
            end = middle-1

        else:
            start = middle+1

    return upper


print(lowerUpper([1, 4, 7, 8, 10], 7))
