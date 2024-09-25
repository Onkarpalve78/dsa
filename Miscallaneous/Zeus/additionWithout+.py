
x, y = int(input("x: ")), int(input("y: "))


def add(x, y):

    while y != 0:
        carry = x & y

        x ^= y

        y = carry << 1
    return x


print(add(x, y))
