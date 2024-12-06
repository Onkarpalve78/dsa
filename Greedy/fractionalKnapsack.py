# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1


def fractionalKnapsack(val: list[int], wt: list[int], capacity: int) -> int:

    items = []
    for i in range(len(val)):
        items.append((val[i], wt[i]))

    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    currentWeight = 0
    finalAns = 0.0
    for i, item in enumerate(items):
        if currentWeight+item[1] <= capacity:
            currentWeight += item[1]
            finalAns += item[0]
        else:
            fraction = (capacity-currentWeight)/item[1]
            finalAns += fraction*item[0]
            break

    return finalAns


print(fractionalKnapsack([60, 100, 120], [10, 20, 30], 50))
