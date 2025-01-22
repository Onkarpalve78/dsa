# 22 https://leetcode.com/problems/generate-parentheses/description/
from typing import List


def generateParenthesis(n: int) -> List[str]:

    brackets = list(n*"()")
    n = len(brackets)
    used_elements = [0]*n
    final_ans = []
    done_set = set()

    def isValid(brackets: list) -> bool:
        st = []
        for bracket in brackets:

            if bracket == '(':
                st.append(bracket)
            if bracket == ')':
                if len(st) == 0:
                    return False
                st.pop()
                continue

        return False if len(st) > 0 else True

    def generatePermutations(index, arr: list, ans_arr, n, used_elements, final_ans: list, done_set: set):

        if index == n:

            if isValid(ans_arr) and tuple(ans_arr) not in done_set:
                done_set.add(tuple(ans_arr))
                final_ans.append("".join(ans_arr))

            return

        for i in range(n):
            if used_elements[i] != True:
                used_elements[i] = True
                ans_arr.append(arr[i])
                generatePermutations(index+1, arr, ans_arr,
                                     n, used_elements, final_ans, done_set)
                used_elements[i] = False
                ans_arr.pop()

        return final_ans

    generatePermutations(0, brackets, [], n,
                         used_elements, final_ans, done_set)

    return final_ans


print(generateParenthesis(3))


def generateParenthesis2(n: int) -> List[str]:

    def backtrack(s, left_bracket: int, right_bracket: int, final_ans: List):

        if len(s) == 2*n:
            final_ans.append(s)
            return

        if left_bracket < n:
            backtrack(s+"(", left_bracket+1, right_bracket, final_ans)
        if right_bracket < left_bracket:
            backtrack(s+")", left_bracket, right_bracket+1, final_ans)

    final_ans = []
    backtrack('', 0, 0, final_ans)

    return final_ans


print(generateParenthesis2(3))
