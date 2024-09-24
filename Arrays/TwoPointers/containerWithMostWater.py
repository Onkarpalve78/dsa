# LC 11 https://leetcode.com/problems/container-with-most-water/description/

height = list(map(int, input().split()))

# region brute TC(N^2)
# maximum_area = 0

# for i in range(len(height)):
#     for j in range(i+1, len(height)):

#         maximum = min(height[i], height[j]) * (j-i)

#         if maximum > maximum_area:
#             maximum_area = maximum


# print(maximum_area)

# region optimal TC(N)

maximum_area = 0

i = 0
j = len(height)-1

while i < j and j > i:

    maximum = min(height[i], height[j]) * (j-i)
    if height[i] > height[j]:
        j -= 1
    else:
        i += 1

    maximum_area = max(maximum, maximum_area)

print(maximum_area)
