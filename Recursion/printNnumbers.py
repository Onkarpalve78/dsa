
N = int(input("Enter N: "))


def printN(N):

    if N == 1:
        print(N)
        return

    printN(N-1)
    print(N)
    return


printN(N)
