
arr = list(map(int, input().split()))
newarr = arr
reversedArr = []
i = 0
t = 1
while i < len(arr):

    reversedArr.append(newarr[-t])

    t += 1
    i += 1
print(reversedArr)
