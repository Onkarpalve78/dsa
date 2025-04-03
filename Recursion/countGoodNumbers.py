# LC 1922 https://leetcode.com/problems/count-good-numbers/description/


n = 3


def countGoodies(n: int) -> int:

    lowerLimit = 10**(n-1)
    upperLimit = (10**(n))-1

    primes: set = {2, 3, 5, 7}

    def isGoodNumber(string) -> bool:
        for i in range(len(string)):
            if i % 2 == 0:
                if int(string[i]) % 2 != 0:
                    return False
            else:

                if int(string[i]) not in primes:
                    return False
        return True

    def recur(current):
        if current < lowerLimit:
            return 0
        count = 1 if isGoodNumber(str(current)) else 0

        return count+recur(current-1)

    return recur(upperLimit)


print(countGoodies(n))
