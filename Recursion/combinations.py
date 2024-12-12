# LC 77 https://leetcode.com/problems/combinations/description/
from typing import List


def combine(n: int, k: int, ans_arr) -> List[List[int]]:

    arr = []

    def solve(index: int, arr: List[int], ans_arr: List, n, k):

        if k == 0:
            ans_arr.append(arr[:])
            return

        if index > n:
            return

        arr.append(index)
        solve(index+1, arr, ans_arr, n, k-1)
        arr.pop()
        solve(index+1, arr, ans_arr, n, k)

    solve(1, arr, ans_arr, n, k)


ans_arr = []

combine(4, 2, ans_arr)

print(ans_arr)
