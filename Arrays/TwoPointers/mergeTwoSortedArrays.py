from typing import List
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    left = m-1
    right = 0

    while left >= 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]

        else:
            break

    nums1.sort()
    nums2.sort()

    for num in nums2:
        nums1.append(num)


merge(nums1, m, nums2, n)
print(nums1)
