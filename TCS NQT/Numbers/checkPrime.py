

num = int(input("Enter a number: "))

# The reason it stops at num // 2
# is that a number cannot have divisors larger than its half (besides the number itself).
for i in range(2, (num//2)+1):
    if num % i == 0:
        print("Not a prime :/")
        break

else:
    print("Prime :) ")
