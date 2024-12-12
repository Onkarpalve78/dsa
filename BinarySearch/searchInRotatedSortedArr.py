# 33 https://leetcode.com/problems/search-in-rotated-sorted-array/description/


def searchInRotatedArr(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        m = l+((r-l)//2)

        if nums[m] == target:
            return m

        # Left Half is sorted
        if nums[m] >= nums[l]:
            # If element lies in the left half or not
            if (nums[m] >= target and nums[l] <= target):
                r = m-1
            else:
                l = m+1
        # Right half is sorted
        else:
            # Element lies in the right half or nots
            if (nums[r] >= target and nums[m] <= target):
                l = m+1
            else:
                r = m-1

    return -1


print(searchInRotatedArr([3, 1], 1))
