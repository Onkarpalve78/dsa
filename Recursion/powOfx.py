# LC 50 https://leetcode.com/problems/powx-n/description/
x = 2
n = 10


def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x, n//2)
        res = res*res

        if n % 2 == 0:
            return res
        else:
            return x*res

    final_result = helper(x, abs(n))
    return final_result if x >= 0 else 1/final_result


print(myPow(x, n))
