# https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/reversed-linked-list-01b722df/

N = int(input())

A = list(map(int, input().split()))
even = []
odd = []
i = 0
while i < N:
    while i < N and A[i] % 2 == 0:
        even.append(A[i])
        print(even)
        i += 1
    even.reverse()
    odd += even
    even = []

    if i < N and A[i] != 0:
        odd.append(A[i])

    i += 1
print(' '.join(map(str, odd)))
