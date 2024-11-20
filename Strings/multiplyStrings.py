# LC 43 https://leetcode.com/problems/multiply-strings/description/
from collections import deque

# Doesnt work :/


def multiplyStrings(num1: str, num2: str) -> str:
    dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    ans = 0
    mulitplies = deque()
    adders = []
    for char in range(len(num1)-1, -1, -1):
        for char2 in range(len(num2)-1, -1, -1):
            mulitplies.append(dict[num1[char]]*dict[num2[char2]])
        size = len(mulitplies)
        carry = 0
        add = ''
        print(mulitplies)
        for _ in range(size):
            multiplied = mulitplies.popleft()
            if multiplied > 9:
                if carry > 0:
                    add += str((multiplied % 10)+carry)+add
                    print('added', add, carry)
                    print(carry)
                    carry = 0
                else:
                    add += str(multiplied % 10)+add
                    print('added raw', add)
                print(multiplied)
                carry = multiplied//10
            else:
                if carry > 0:
                    add = str(multiplied+carry)+add
                else:
                    add = str(multiplied)+add
        adders.append(add)

    for i, num in enumerate(adders):
        ans += int(num)*(10**i)
    print(adders)

    return str(ans)


print(multiplyStrings("58", "64"))


# this works and it doesnt really breal any rules but kinda cheating tho :P
def multiplyStrings2(num1: str, num2: str) -> str:
    return eval(f"{num1}*{num2}")


print(multiplyStrings2("58", "10"))
