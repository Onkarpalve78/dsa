# LC 55 https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150


def jump(nums):
    current = 0
    while current < len(nums)-1:
        if nums[current] > 0:
            if current+nums[current] > len(nums)-1 or nums[current] == 0:
                return False
            elif current+nums[current] <= len(nums)-1:
                current += nums[current]
                print(current)
                continue
        else:
            return False

    return True


print(jump([3, 2, 1, 0, 4]))
