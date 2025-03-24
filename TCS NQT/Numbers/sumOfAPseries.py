# Problem Statement: Given an A.P. Series, we need to find the sum of the Series.

# a = first term of A.P.

# d= common Difference of A.P.

# n= Number of Terms in  A.P.

# Example 1:
# Input:
# n=4
# a=2
# d=2
# Output: 20
# Explanation: 2+4+6+8 = 20


n = 8
a = -2
d = 5


def sumOfAPserires(a: int, n: int, d: int) -> int:

    count = 1

    while count < n:
        if count == 1:
            adder = a+d
        else:
            adder += d

        a += adder
        count += 1

    return a


print(sumOfAPserires(a, n, d))
