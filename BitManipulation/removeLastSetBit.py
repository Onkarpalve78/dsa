# Remove right most set bit, 1100 should become 1000


# Explaination:
# for 16 binary= 10000
# for 15 binary= 01111

# for 40 binary= 101000
# for 39 binary= 100111

# notice for given number N , the N-1 number will have its rightmost bit as 0 and the rest as 1's
# we can use this to solve this problem
# simple do AND operation on N and N-1
def removeLastSetBit(num):
    return num & (num-1)  # 1100 & 1011


print(removeLastSetBit(12))
