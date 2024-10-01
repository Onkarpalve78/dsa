# LC 40 https://leetcode.com/problems/combination-sum-ii/description/


def combinationSum2(index: int, ans_arr: list, arr: list, n: int, target: int, final_ans: list[list[int]]):
    if target == 0:
        final_ans.append(ans_arr.copy())
        return

    for i in range(index, n):

        if i > index and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            # no point in checking further element since next elements would be >=arr[i] anyways.
            break

        ans_arr.append(arr[i])

        combinationSum2(i+1, ans_arr, arr, n, target-arr[i], final_ans)

        ans_arr.pop()


def findCombinations(collection: list):
    collection.sort()
    ans_arr = []
    target = 8
    n = len(collection)
    final_ans = []

    combinationSum2(0, ans_arr, collection, n, target, final_ans)

    return final_ans


print(findCombinations([10, 1, 2, 7, 6, 1, 5]))
