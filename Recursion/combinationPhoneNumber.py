# LC 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List


def phoneNumbers(digits: str) -> list[str]:
    ans_arr = []
    final_ans = []
    if not digits:
        return final_ans
    numbers = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    letters = ""
    uni_numbers = set(digits)
    for digit in uni_numbers:
        letters += numbers[digit]

    print(letters)

    def getCombinations(index, arr: List, ans_arr: List, final_ans: List, k):

        if index == k:
            # if len(ans_arr) == 2:
            #     final_ans.append("".join(ans_arr))
            final_ans.append("".join(ans_arr))

            return

        # ans_arr.append(arr[index])
        # getCombinations(index+1, arr, ans_arr, final_ans, k)
        # ans_arr.pop()
        # getCombinations(index+1, arr, ans_arr, final_ans, k)

        for i in range(len(arr[index])):
            ans_arr.append(arr[index][i])
            getCombinations(index+1, arr, ans_arr, final_ans, k)
            ans_arr.pop()

    getCombinations(0, [numbers[digit] for digit in digits], ans_arr,
                    final_ans, len(digits))

    return final_ans


print(phoneNumbers("23"))
