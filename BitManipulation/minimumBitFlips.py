# Count Minimum bit flips required to convert num1 to num2,
#  eg, num1=13=1101 num2=7=0111 ,bit flips required=2

def minimumBitFLips(num1, num2):
    xor = num1 ^ num2
    count = 0
    while xor != 0:
        xor = xor & (xor-1)
        count += 1

    return count


print(minimumBitFLips(13, 7))
