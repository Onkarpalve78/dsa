# LC 31 https://leetcode.com/problems/next-permutation/

nums = list(map(int, input().split()))


def nextPermutation(nums: list[int]) -> list[int]:
    length = len(nums)
    if length == 2:
        return nums.reverse()

    pointer = length-2

    while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
        pointer -= 1

    if pointer == -1:
        return nums.reverse()
    # Now I want to find out which number is smallest in nums[pointer:],
    # although I know the last element will always be the smallest in it num[-1],
    # but it is not guaranteed if the last element which is smallest
    # in nums[pointer:] is also greater than nums[pointer] or not,
    # cuz swapping them wouldn't be correct if nums[pointer]>nums[-1] hence why we do the loop here!
    # Eg test case where simply swapping fails: nums=[2,3,1] ,output:[1,2,3], expected:[3,1,2]
    for x in range(length-1, pointer, -1):
        if nums[pointer] < nums[x]:
            nums[pointer], nums[x] = nums[x], nums[pointer]
            break

    # nums[pointer], nums[-1] = nums[-1], nums[pointer]

    nums[pointer+1:] = reversed(nums[pointer+1:])

    return nums


print(nextPermutation(nums))
