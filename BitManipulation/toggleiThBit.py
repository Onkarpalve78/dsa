# Make ith bit 0 for 1 and 1 for 0

def toggleIthBit(num, i):
    xor = num ^ (1 << i)  # 1001 ^ 0001
    return xor


print(toggleIthBit(9, 0))
