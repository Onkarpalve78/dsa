# LC 88 https://leetcode.com/problems/merge-sorted-array/description/
from typing import List


def merge(nums1: List[int], nums2: List[int]) -> None:
    sorted_arr = []
    left = right = 0

    print(nums1)

    while left < len(nums1) and right < len(nums2):
        # print(nums1[left])
        # if nums1[left] == 0:
        #     left += 1
        #     print(nums1[left])
        #     continue
        # elif nums2[right] == 0:
        #     right += 1
        #     continue

        if nums1[left] > nums2[right]:
            sorted_arr.append(nums2[right])
            right += 1
        else:
            sorted_arr.append(nums1[left])
            left += 1

    sorted_arr.extend(nums1[left:])
    sorted_arr.extend(nums2[right:])

    i = 0
    while i < min(len(nums1), len(sorted_arr)):
        nums1[i] = sorted_arr[i]
        i += 1

    nums1.extend(sorted_arr[i:])

    tempNums1 = nums1.copy()

    for i, num in enumerate(tempNums1):
        if i == 0 and num != 0:
            break
        if num != 0:
            break
        if num == 0:
            nums1.remove(0)

    return nums1


print(merge([4, 5, 6, 0, 0, 0], [1, 2, 3, 8]))
