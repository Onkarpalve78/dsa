# https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]


def minimumCoins(N, coins):
    minCoins = []
    currentValue = N
    for i in range(len(coins)-1, -1, -1):

        while coins[i] <= currentValue:
            currentValue -= coins[i]
            minCoins.append(coins[i])

        if currentValue == 0:
            break

    return minCoins


print(minimumCoins(48, coins))
