

def largestOddNumber(num: str) -> str:
    # if int(num[-1]) % 2 != 0: you were'nt parsing the num[-1] value which is in string
    if int(num[-1]) % 2 != 0:
        return num
    # for i in range(len(num), -1, -1): dawg you were directly starting from len(arr) value, which ofc would not exist
    for i in range(len(num)-1, -1, -1):
        print(i)
        if int(num[i]) % 2 != 0:
            return num[0:i+1]

    return ""


print(largestOddNumber(num="52"))
