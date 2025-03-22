# A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors excluding itself).

# Examples:

# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.


num = 15


def isPerfect(num: int) -> bool:
    divisors = set()

    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisors.add(i)

    sum = 0
    for divisor in divisors:
        sum += divisor
    print(divisors)
    return True if sum == num else False


print(isPerfect(num))
