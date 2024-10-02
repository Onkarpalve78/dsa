

def getAllPermutations(index: int, ans_arr: list, arr: list, n: int, used_elements: list, final_ans: list):

    if index == n:
        final_ans.append(ans_arr[:])
        return

    for i in range(n):
        if used_elements[i] != True:
            ans_arr.append(arr[i])
            used_elements[i] = True
            getAllPermutations(index+1, ans_arr, arr, n,
                               used_elements, final_ans)

            used_elements[i] = False
            ans_arr.pop()


def printPermutations(arr=[1, 2, 3]):
    ans_arr = []
    n = len(arr)
    used_elements = []
    final_ans = []
    used_elements = [0]*n

    getAllPermutations(0, ans_arr, arr, n, used_elements, final_ans)

    print(final_ans)


printPermutations()
