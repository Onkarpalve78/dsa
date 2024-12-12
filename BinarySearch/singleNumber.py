# LC 540 https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/6132527/binary-search-with-index-parity-to-find-single-non-duplicate-element-o-logn-0ms/


def singleNonDuplicate(nums):
    l, r = 0, len(nums)-1

    while l <= r:
        m = l+((r-l)//2)

        if (((m-1 < 0) or (nums[m-1] != nums[m])) and ((m+1 == len(nums)) or (nums[m] != nums[m+1]))):
            return nums[m]

        leftSide = m-1 if nums[m-1] == nums[m] else m

        if leftSide % 2:
            r = m-1

        else:
            l = m+1


print(singleNonDuplicate([1, 1, 2, 2, 3,  4, 4]))
