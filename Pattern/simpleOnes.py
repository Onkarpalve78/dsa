
n = 3


def square():

    for _ in range(n):
        for _ in range(n):
            print("*", end=" ")
        print()


square()


def trianle():

    for i in range(n):
        for _ in range(i+1):
            print("*", end=" ")
        print()


trianle()


def decreasingTrianle():

    for i in range(n):
        for _ in range(i, n):
            print("*", end=" ")
        print()


decreasingTrianle()


def trianleFromRight():
    for i in range(n):

        for j in range(n-i-1):
            print(" ", end=" ")

        for k in range(i+1):
            print("*", end=" ")

        print()


trianleFromRight()


def decreasingTrainglefromRight():

    for i in range(n):
        for j in range(i):
            print(" ", end=" ")

        for k in range(i, n):
            print("*", end=" ")
        print()


decreasingTrainglefromRight()


def pyramid():

    for i in range(n):

        for _ in range(i+1, n):
            print(" ", end=" ")

        for _ in range(i+1):
            print(i+1, end=" ")

        for _ in range(i):
            print(i+1, end=" ")

        print()


pyramid()


def invertedPyramid():
    asci = ord("A")
    for i in range(n):

        for _ in range(i):
            print(" ", end=" ")

        for _ in range(i, n):
            print(chr(asci+i), end=" ")

        for _ in range(i+1, n):
            print(chr(asci+i), end=" ")
        print()


invertedPyramid()


def emptySquare():

    for i in range(n):

        for j in range(n):

            if i == 0 or i == n-1:
                print("*", end=" ")

            elif j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


emptySquare()


def printA(n=13):

    for i in range(n):
        middle = n//2
        m = n-2
        for j in range(m):
            if i == 0:
                if j == 0 or j == m-1:
                    print(" ", end=" ")
                else:
                    print("A", end=" ")

            if i == middle:
                print("A", end=" ")

            # if or & and statements keep those in bracket and define them well
            if (j == 0 or j == m-1) and (i != 0 and i != middle):
                print("A", end=" ")

            elif j != 0 and j != m-1 and i != 0 and i != middle:
                print(" ", end=" ")

        print()


printA()


def printX(n=8):
    # middle = n//2
    for i in range(n):
        start = i+1
        end = n-i-1
        for j in range(1, n):
            if (j == start or j == end):
                print("X", end=" ")
            # elif i == middle and j == start:
            #     print("X", end=" ")
            else:
                print(" ", end=" ")

        print()


printX(8)


def printG(n=8):
    middle = n//2
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0:
                    print(" ", end=" ")
                else:
                    print("G", end=" ")
            if i > 0 and j == 0:
                print("g", end=" ")
            if i == middle:
                if j >= middle:
                    print('f', end=" ")

                else:
                    print(" ", end=" ")

            if j > 0 and i > middle:
                if j == n-1:
                    print("G", end=" ")
                print(" ", end=" ")

            if i == n-1:
                print("G", end=" ")

        print()


printG()


def pascalTriangle(n):
    count1 = 1
    count2 = 1
    for i in range(n):

        for j in range(i, n):
            print(" ", end=" ")

        for k in range(i+1):
            print(count1, end=" ")
            count1 += 1

        for l in range(i):
            print(count2, end=" ")
            count2 += 1

        print()


pascalTriangle(n=8)
