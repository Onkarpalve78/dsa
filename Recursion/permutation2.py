# LC 47 https://leetcode.com/problems/permutations-ii/description/


def uniquePermutations(nums: list[int]) -> list[int]:
    final_ans = set()
    n = len(nums)
    used_elements = [0]*n

    def generatePermutations(index: int, arr: list, ans_arr: list, n: int, final_ans: set):
        if index == n:
            final_ans.add(tuple(ans_arr))
            return

        for i in range(n):
            if used_elements[i] != True:
                used_elements[i] = True
                ans_arr.append(arr[i])
                generatePermutations(index+1, arr, ans_arr, n, final_ans)
                ans_arr.pop()
                used_elements[i] = False
    generatePermutations(0, nums, [], n, final_ans)

    return [list(x) for x in final_ans]


print(uniquePermutations([1, 1, 2]))
