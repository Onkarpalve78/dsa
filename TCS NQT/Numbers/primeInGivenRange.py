

start, end = 0, 40


def findPrimesInGivenRange(num1: int, num2: int) -> list:
    primes = []

    for num in range(num1, num2+1):
        if num > 1:
            is_prime = True
            for j in range(2, (num//2)+1):

                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    return primes


print(findPrimesInGivenRange(start, end))
