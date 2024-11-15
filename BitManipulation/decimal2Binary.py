

def decimalToBinary(integer: int):
    ans = ''

    while integer != 1:
        if integer % 2 == 0:
            ans += '0'
        else:
            ans += '1'

        integer = integer//2
    ans += '1'
    ans = list(ans)
    ans = reversed(ans)

    return "".join(ans)


print(decimalToBinary(4))
