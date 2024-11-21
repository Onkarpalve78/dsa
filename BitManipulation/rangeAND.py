# LC 201 https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=problem-list-v2&envId=bit-manipulation


def rangeAND(left, right):

    while right > left:
        right = right & (right-1)

    return right


print(rangeAND(4, 14))
