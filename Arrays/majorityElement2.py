# LC 229 https://leetcode.com/problems/majority-element-ii/description/

numss = [1, 1, 1, 1, 2, 2, 3, 2, 2]


def majorityElementsBrute(nums: list[int]) -> int:
    min_amount = len(nums)//3
    counter = {}
    ans = []
    for i, num in enumerate(nums):

        if counter.get(num, None):
            counter[num] += 1
        else:
            counter[num] = 1

    for key, value in counter.items():
        if value > min_amount:
            ans.append(key)
    return ans


def majorityElements(nums: list[int]) -> list[int]:
    if len(nums) < 1:
        return []
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 += 1
        elif count2 == 0:
            candidate2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    return [x for x in (candidate1, candidate2) if nums.count(x) > len(nums)//3]


print("brute", majorityElementsBrute(numss))
print("optimal", majorityElements(numss))
