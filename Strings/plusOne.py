# LC 66 https://leetcode.com/problems/plus-one/description/

def plusOne(self, digits: list[int]) -> list[int]:
    digits = [str(dig) for dig in digits]
    s = "".join(digits)
    sval = int(s)
    sval += 1
    s = str(sval)
    return [int(val) for val in s]
