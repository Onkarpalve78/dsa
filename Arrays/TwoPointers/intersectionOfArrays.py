
arr = list(map(int, input("Enter array A: ").split()))
brr = list(map(int, input("Enter array B: ").split()))
i = 0
j = 0
ans = []
while (i < len(arr) and j < len(brr)):
    if arr[i] < brr[j]:
        i += 1
    elif brr[j] < arr[i]:
        j += 1
    else:
        ans.append(arr[i])
        i += 1
        j += 1

print(ans)
