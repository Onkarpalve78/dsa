import math


def isPalindrome(s: str) -> bool:
    s = ''.join(ch for ch in s if ch.isalnum()).lower().replace(" ", "")
    length = len(s)
    for i in range(len(s)):
        middle = math.floor(len(s)/2)
        if i == middle:
            return True
        elif s[i] == s[length-1]:
            print(s[i], s[length-1])
            length -= 1
            continue
        else:
            return False


print(isPalindrome("Was it a car or a cat I saw?"))
