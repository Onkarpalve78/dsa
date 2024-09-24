
num = int(input("Enter num: "))


def fibonacci(N):
    if N == 0 or N == 1:
        return N

    fibOfPrev = fibonacci(N-1)
    fibOf3rdPrev = fibonacci(N-2)

    fib = fibOfPrev+fibOf3rdPrev
    return fib


print(fibonacci(num))
