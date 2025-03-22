# LC35 https://leetcode.com/problems/search-insert-position/description/


def insertNumber(nums: list[int], target) -> int:
    start = 0
    end = len(nums)-1

    while start <= end:
        middle = start + (end-start)//2
        print(middle, start, end)

        if target == nums[middle]:
            return middle

        elif target > nums[middle]:
            start = middle+1

        elif target < nums[middle]:
            end = middle-1

        # if end-start <= 1 and target <= end:
        #     if target > nums[start]:
        #         return start+1
        #     elif target > nums[end]:
        #         return end+1

        # elif target > nums[end]:
        #     return end+(target-nums[end])

        # elif target < nums[start]:
        #     return start

    return start


print(insertNumber([1, 2, 3, 4, 5], 6))
