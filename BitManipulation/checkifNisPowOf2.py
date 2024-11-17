# LC 231 https://leetcode.com/problems/power-of-two/
# Check if given number is power of 2, eg:16= 2^4 , 4=2^2 etc


# Explaination:
# Every binary number 1,2,4,8,16,32 which are a power of 2
# i.e 2^0, 2^1, 2^3, 2^4 etc will always have only one set bit
# 1=0001, 2=0010, 4=0100, 8=1000, 16=10000, 32=100000 etc
# hence if a binary number only has one set bit then it is a power of 2

def checkifNisPowOfTwo(n):
    ans = n & (n-1)
    return True if ans == 0 else False


print(checkifNisPowOfTwo(4))
