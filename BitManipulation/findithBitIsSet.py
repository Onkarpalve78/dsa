

def findiThSetBitIsSet(bits, i):
    isSet = bits & (1 << i)

    return True if isSet > 0 else False


print(findiThSetBitIsSet(10, 1))
