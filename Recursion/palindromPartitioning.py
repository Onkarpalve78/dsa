# LC 131 https://leetcode.com/problems/palindrome-partitioning/description/


s = "aab"


def palindromPartion(s: str) -> list:

    def isPalindrome(st: str) -> bool:
        return True if st[::-1] == st else False

    index = 0
    n = len(s)
    final_ans = []

    def givePalindromes(index: int, arr: list, ans_arr: list, final_ans: list[list], n: int):
        new_ans_arr = "".join(ans_arr)
        if index == n:
            final_ans.append(ans_arr[:])
            return

        if isPalindrome(new_ans_arr):
            ans_arr.append(arr[index])

            givePalindromes(index+1, arr, ans_arr, final_ans, n)

            ans_arr.pop()

            givePalindromes(index+1, arr, ans_arr, final_ans, n)

    givePalindromes(index, s, [], final_ans, n)

    return final_ans


print(palindromPartion(s))


def palindromPartion2(s: str) -> list:
    def isPalindrome(st: str) -> bool:
        return st[::-1] == st

    def givePalindromes(index: int, s: str, ans_arr: list, final_ans: list):

        if index == len(s):
            final_ans.append(ans_arr[:])
            return

        for i in range(index, len(s)):
            substring = s[index:i+1]
            if isPalindrome(substring):
                ans_arr.append(substring)
                givePalindromes(i+1, s, ans_arr, final_ans)
                ans_arr.pop()

    final_ans = []
    givePalindromes(0, s, [], final_ans)

    return final_ans


print(palindromPartion2(s))
