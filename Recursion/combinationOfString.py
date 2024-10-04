

def combinationLetters(index: int, ans_arr: list, arr: list, n: int, final_ans: list):

    if index == n:
        # if len(ans_arr)==n:
        if len(ans_arr) > 0:
            final_ans.append("".join(ans_arr))

        return

    ans_arr.append(arr[index])

    combinationLetters(index+1, ans_arr, arr, n, final_ans)

    # ans_arr.pop(arr[index])
    ans_arr.pop()

    combinationLetters(index+1, ans_arr, arr, n, final_ans)


def printCombinations(s: str) -> str:
    # s = s.split("")
    s = list(s)
    print(s)
    ans_arr = []
    n = len(s)
    final_ans = []
    combinationLetters(0, ans_arr, s, n, final_ans)

    return " ".join(final_ans)


print(printCombinations("abc"))


def getAllPermutations(index: int, ans_arr: list, arr: list, n: int, elements_used: list, final_ans: list):

    if index == n:
        final_ans.append("".join(ans_arr))
        return

    for i in range(n):
        if elements_used[i] != True:
            elements_used[i] = True
            ans_arr.append(arr[i])
            getAllPermutations(index+1, ans_arr, arr, n,
                               elements_used, final_ans)
            elements_used[i] = False
            ans_arr.pop()


def printAllPermutations(s: str) -> str:
    s = list(s)
    n = len(s)
    ans_arr = []
    final_ans = []
    # elements_used = []
    elements_used = [False]*n

    getAllPermutations(0, ans_arr, s, n, elements_used, final_ans)

    return " ".join(final_ans)


print(printAllPermutations("abc"))
