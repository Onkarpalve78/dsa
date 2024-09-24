# Two pointer approach


nums = list(map(int, input().split()))


def swap(l, r):
    nums[l], nums[r] = nums[r], nums[l]


def recursion(left, right):
    if left >= right:
        return

    swap(left, right)

    recursion(left+1, right-1)


left = 0
right = len(nums)-1
recursion(left, right)
print("Reversed", nums)
