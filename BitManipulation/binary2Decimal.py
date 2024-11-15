

def binaryToDecimal(binary):
    multiplier = 0
    ans = 0

    for i in range(len(binary)-1, -1, -1):
        if binary[i] == "1":
            ans += 2**multiplier
        multiplier += 1

    return ans


print(binaryToDecimal("1001"))
