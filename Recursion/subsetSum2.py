# LC 90 https://leetcode.com/problems/subsets-ii/description/
from typing import List
nums = [1, 2, 2]


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    finalAns = []
    index = 0
    n = len(nums)
    ans_arr = []
    nums.sort()

    def returnAllSubsets(index: int, ans_arr: list, arr: list, n: int, finalAns: list[list[int]]):

        if index == n:
            # print(ans_arr)
            if len(ans_arr) > 0:
                print(ans_arr)
                finalAns.append(ans_arr.copy())
            else:
                finalAns.append([])

            return

        ans_arr.append(arr[index])

        returnAllSubsets(index+1, ans_arr, arr, n, finalAns)

        ans_arr.pop()

        returnAllSubsets(index+1, ans_arr, arr, n, finalAns)
    returnAllSubsets(index, ans_arr, nums, n, finalAns)

    finalAns = set((tuple(ans) for ans in finalAns))
    finalAns = [list(ans) for ans in finalAns]

    return sorted(finalAns)


finalAnss = []
arr = [1, 2, 2]
n = len(arr)
ans_arr = []
index = 0
sol = subsetsWithDup(arr)

print(sol)
