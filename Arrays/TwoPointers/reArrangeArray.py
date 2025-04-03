# 2149 https://leetcode.com/problems/rearrange-array-elements-by-sign/description/


nums = [-7, 3, 1, -2, -5, 2, -4, 8]
# nums = [-1, 1, -2, 2]


def rearrangeArray(nums: list[int]) -> list[int]:
    positives: list[int] = []
    negatives: list[int] = []
    l: int = 0
    r: int = 0
    ans: list = []
    for i in range(len(nums)):
        if nums[i] > 0:
            positives.append(nums[i])
        else:
            negatives.append(nums[i])

    while l < len(positives) or r < len(negatives):
        ans.append(positives[l])
        l += 1
        ans.append(negatives[r])
        r += 1

    return ans


print(rearrangeArray(nums))

# Its not possible to solve this question without using extra space but we can atleast improve TC
# Since the question says the +ve no. always comes first, it means that the +ve numbers will always take
# an even index 0,2,4... and -ve will take odd index 1,3,5...


def rearrangeArray2(nums: list[int]) -> list[int]:
    ans = [0]*len(nums)
    positiveIndex = 0
    negativeIndex = 1
    for i in range(len(nums)):
        if nums[i] > 0:
            ans[positiveIndex] = nums[i]
            positiveIndex += 2
        else:
            ans[negativeIndex] = nums[i]
            negativeIndex += 2

    return ans


print(rearrangeArray2(nums))
