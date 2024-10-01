# LC 39 https://leetcode.com/problems/combination-sum/description/

def combinationSum(index, ans_arr: list, arr: list, n, target, final_ans: list):

    if index == n:
        if target == 0:
            final_ans.append(ans_arr.copy())

        return

    if arr[index] <= target:
        # target = target-arr[index] doing this reduces target value for future use as well
        ans_arr.append(arr[index])
        combinationSum(index, ans_arr, arr, n, target-arr[index], final_ans)
        # since question says we can use the same element twice we are using same index to check
        # if we repeat the same element twice or more can we make a sum equal to the target
        ans_arr.pop()

    combinationSum(index+1, ans_arr, arr, n, target, final_ans)


arr = [1, 3, 4]
target = 6
n = len(arr)
final_ans = []
ans_arr = []

combinationSum(0, ans_arr, arr, n, target, final_ans)
print(final_ans)
