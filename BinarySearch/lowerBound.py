# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array


def lowerBound(nums, k):
    start = 0
    end = len(nums)-1
    ans = -1

    while start <= end:
        middle = (start+end)//2

        if nums[middle] <= k:
            ans = middle
            start = middle+1

        else:
            end = middle-1

    return ans


print(lowerBound([1, 2, 8, 10, 11, 12, 19], 5))
