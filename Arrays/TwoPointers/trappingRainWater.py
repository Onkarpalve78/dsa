# LC 42 https://leetcode.com/problems/trapping-rain-water/description/

# nums = list(map(int, input().split()))

# total = 0
# for i in range(len(nums)):
#     if nums[i] != 0:
#         total_blocks = 0
#         for j in range(i+1, len(nums)):
#             print(nums[i], nums[j])
#             if nums[i] > nums[j]:
#                 print("total_block before: ", total_blocks)
#                 total_blocks += (nums[i]-nums[j])
#                 print("total_block after: ", total_blocks)

#             elif nums[i] == nums[j]:
#                 break
#             else:
#                 total_blocks = 0
#         total += total_blocks


# total = []
# i = 0
# j = i+1
# total_blocks = 0
# deficit = 0

# while j < len(nums):
#     if nums[i] == 0:
#         i += 1
#     deficit += nums[j]
#     if nums[j] > nums[j+1]:
#         total_blocks = nums[j]*(j-i)-deficit
#     if nums[j] != nums[-1]:
#         j += 1
#     else:
#         break
# total.append(total_blocks)

# next attempt
# i = 0
# j = 0
# deficit = 0
# flag = False
# total_blocks = 0

# while j < len(nums):
#     if nums[i] <= 0 and deficit == 0:
#         i += 1
#         j += i
#         continue

#     if nums[i] != 0 and deficit == 0:  # this will cause infinit loop lol
#         flag = True
#         continue

#     if i < j and flag == True and nums[j] > nums[j+1]:
#         i = j
#         j = i+1
#         deficit = 0
#         flag = True
#         continue

#     if i < j and flag == True:
#         j += 1
#         deficit += nums[j]
#         continue

#     if nums[j] > nums[j+1] and flag == True:
#         total_blocks += (min(nums[i], nums[j]) * (j-i)) - deficit
#         i = j
#         deficit = 0
#         continue


# print(max(total_blocks))


height = [4, 2, 0, 3, 2, 5]


def trap(height: list[int]) -> int:
    l: int = 0
    r: int = len(height)-1

    max_left_height: int = height[l]
    max_right_height: int = height[r]

    ans = 0

    while l < r:
        if max_left_height < max_right_height:
            l += 1
            max_left_height = max(max_left_height, height[l])
            ans += max_left_height-height[l]

        else:
            r -= 1
            max_right_height = max(max_right_height, height[r])
            ans += max_right_height-height[r]

    return ans


print(trap(height))
