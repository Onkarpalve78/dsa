# https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

arr = []
lastAnswer = 0


inp = list(map(int, input().split()))

for ar in range(inp[0]):
    print(ar)
    arr.append([])


print(len(arr))

i = 0
while i < inp[1]:
    eq = list(map(int, input().split()))
    idx = (eq[1] ^ lastAnswer) % inp[0]
    if eq[0] == 1:
        arr[idx].append(eq[2])
    else:
        lastAnswer = arr[idx][eq[2]]
        print(lastAnswer)
    i += 1

print(arr)
print('last answer', lastAnswer)
