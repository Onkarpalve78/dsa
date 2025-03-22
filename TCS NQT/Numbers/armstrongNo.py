#  An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# Examples

#                 Example 1:
#                 Input:N = 153

#                 Output:True

#                 Explanation: 13+53+33 = 1 + 125 + 27 = 153

num = 153


def isArmstrong(num: int) -> bool:
    digitCount = len(str(num))
    computedNum = 0
    ogNum = num
    while num != 0:
        singleDigit = num % 10
        computedNum += singleDigit**digitCount
        num = num//10

    return True if computedNum == ogNum else False


print(isArmstrong(num))
