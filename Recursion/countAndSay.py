
n = int(input("Enter n: "))

# Valiant effort, but wont work after n=5 and beyond!
# n=5 expected = 111221 , your output=3221, cuz you've hashed them all the similar
# nums gets clubbed together, here order matters


def countAndSay(n: int) -> str:

    if n == 1:
        return "1"

    res = countAndSay(n-1)

    # res = list(res)
    # numCount = {}
    # for num in res:
    #     if num in numCount:
    #         numCount[num] += 1
    #     else:
    #         numCount[num] = 1
    # ans = []
    # for num, count in numCount.items():
    #     ans.append(str(count))
    #     ans.append(num)

    # return "".join(ans)
    ans = ''
    i = 0
    while i < len(res):
        count = 1
        j = i
        while j < len(res)-1 and res[j] == res[j+1]:
            count += 1
            j += 1
        ans += f"{str(count) + res[j]}"
        i = j+1

    return ans


print(countAndSay(n))
