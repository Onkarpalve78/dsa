# LC 8 https://leetcode.com/problems/string-to-integer-atoi/description/

def stringToInterger(stringValue: str) -> int:
    s = stringValue.lstrip()
    current = s[0]
    sign = 1
    i = 0
    if current == "-":
        sign = -1
        i += 1
    elif current == "+":
        i += 1

    ans = 0
    while i < len(s):
        current = s[i]
        if not current.isdigit():
            break
        else:
            ans = ans * 10 + int(current)
            # intially ans=0, 0x10 +1 =1, then ans=1, 1x10 +2=12, ans=12, 12*10 +3 =123
        i += 1

    ans *= sign

    if ans > 2**31 + 1:
        return 2**31+1
    elif ans < -2**31:
        return -2**31
    else:
        return ans


print(stringToInterger("  -123eo3"))
