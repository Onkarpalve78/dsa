

def printSubsequenceWithGivenSum(index, ans_arr: list, arr: list, sum, target, n):

    if index == n:
        if sum == target:
            print(" ".join(list(map(str, ans_arr))))
        return

    ans_arr.append(arr[index])
    sum += arr[index]

    printSubsequenceWithGivenSum(index+1, ans_arr, arr, sum, target, n)

    ans_arr.pop()
    sum -= arr[index]

    printSubsequenceWithGivenSum(index+1, ans_arr, arr, sum, target, n)


def printOneSubsequenceWithGivenSum(index, ans_arr: list, arr: list, sum, target, n):

    if index == n:
        if sum == target:
            print(" ".join(list(map(str, ans_arr))))
            return True
        return

    ans_arr.append(arr[index])
    sum += arr[index]

    if printOneSubsequenceWithGivenSum(index+1, ans_arr, arr, sum, target, n) == True:
        return True

    ans_arr.pop()
    sum -= arr[index]

    if printOneSubsequenceWithGivenSum(index+1, ans_arr, arr, sum, target, n) == True:
        return True

    return False


def countNumberOfSubsequences(index, arr: list, sum, target, n):
    if index == n:
        if sum == target:
            return 1
        return 0

    # ans_arr.append(arr[index])
    sum += arr[index]

    l = countNumberOfSubsequences(index+1, arr, sum, target, n)

    sum -= arr[index]

    r = countNumberOfSubsequences(index+1, arr, sum, target, n)
    return l+r


arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
n = len(arr)
ans_arr = []
sum = 0

print("All sequences: ")
printSubsequenceWithGivenSum(0, ans_arr, arr, sum, target, n)

print("Only First sequence: ")
printOneSubsequenceWithGivenSum(0, ans_arr, arr, sum, target, n)

print("Number of subsequences: ")
print(countNumberOfSubsequences(0, arr, sum, target, n))
