# LC 121

prices = list(map(int, input().split()))


def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    buyPrice = prices[0]
    sellPrice = 0
    for i, price in enumerate(prices):
        if price < buyPrice:
            buyPrice = price
            sellPrice = 0

        elif price > sellPrice:
            sellPrice = price

        if (sellPrice-buyPrice) > maxProfit:
            maxProfit = sellPrice-buyPrice

    return maxProfit


print(maxProfit(prices))
