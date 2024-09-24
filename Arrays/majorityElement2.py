# LC 229 https://leetcode.com/problems/majority-element-ii/description/

numss = [1, 1, 1, 1, 2, 2, 3, 2, 2]


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


print(majorityElements(numss))
