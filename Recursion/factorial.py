

num = int(input("Enter number: "))


def factorial(N):

    if N == 0:
        return 1

    res = factorial(N-1)

    return N*res


print(factorial(num))
