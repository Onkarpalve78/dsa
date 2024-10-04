

# TLE with this approach
def threeSum(index: int, ans_arr: list, arr: list, n: int, final_ans: list[list]):
    if index == n:
        if sum(ans_arr) == 0 and len(ans_arr) == 3:
            final_ans.append(ans_arr.copy())

        return

    # target += arr[index]
    ans_arr.append(arr[index])

    threeSum(index+1, ans_arr, arr, n, final_ans)

    # target -= arr[index]
    ans_arr.pop()

    threeSum(index+1, ans_arr, arr, n, final_ans)


def printThreesomes(arr: list):
    ans_arr = []
    final_ans = []
    n = len(arr)
    index = 0
    arr.sort()

    threeSum(index, ans_arr, arr, n, final_ans)

    final_ans = set((tuple(ans) for ans in final_ans))
    final_ans = [list(ans) for ans in final_ans]

    # if len(final_ans) <= 0:
    #     return final_ans

    print(final_ans)


printThreesomes([-1, 6, 8, 9, -8, 1, 0])
