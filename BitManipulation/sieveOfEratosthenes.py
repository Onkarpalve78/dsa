

def sieveOfEratosthenes(N):
    primes = [1]*N

    primeCount = 0

    for i in range(2, int(N**0.5)+1):
        if primes[i] == 1:
            for j in range(i*i, len(primes), i):
                primes[j] = 0

    for i in range(2, len(primes)):
        if primes[i] == 1:
            primeCount += 1

    return primeCount


print(sieveOfEratosthenes(20))
