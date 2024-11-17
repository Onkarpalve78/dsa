# Make the ith bit of a number 0

def clearIthBit(num, i):
    complement = 1 << i  # for i=3 complement= 1000
    return num & ~complement  # for num=9, 1001 & 0111


print(clearIthBit(9, 3))
