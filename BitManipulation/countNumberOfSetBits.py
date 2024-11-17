# Return number of 1's in a binary number, eg: 13 binary=1101 Output:3

"""
Explaination:
for 13 m binary=1101
if we remove rightmost 1, then binary=1100
if we again do this then binary=1000
and again 0000, therefore we keep a counter=0 and increment that counter in a loop until given number=0
"""


def countSetBits(num):
    count = 0
    while num != 0:
        num = num & (num-1)
        count += 1

    return count


print(countSetBits(13))
