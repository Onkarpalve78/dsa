# https://www.codechef.com/problems/CHESSDIST

T = int(input())

while T > 0:
    cors = list(map(int, input().split()))

    x = abs(abs(cors[0])-abs(cors[2]))
    y = abs(abs(cors[1])-abs(cors[3]))

    print(max(x, y))

    T -= 1
