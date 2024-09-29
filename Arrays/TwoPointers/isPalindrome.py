# import math


def isPalindrome(s: str) -> bool:
    s = ''.join(ch for ch in s if ch.isalnum()).lower().replace(" ", "")

    print(s)
    # length = len(s)
    # for i in range(len(s)):
    # middle = math.floor(len(s)/2)
    # middle = len(s)//2
    # if i == middle:
    #     return True
    # elif s[i] == s[length-1]:
    #     print(s[i], s[length-1])
    #     length -= 1
    #     continue
    if s == s[::-1]:
        return True
    else:
        return False


print(isPalindrome("1Was it a car or a cat I saw1?$#(#())"))
