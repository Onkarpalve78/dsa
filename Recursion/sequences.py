
# TC O(2^N*N) SC O(N)
def print_sequences(index: int, ans_arr: list, arr: list, n: int):

    if index == n:
        if len(ans_arr) > 0:
            print("_".join(list(map(str, ans_arr))))

        else:
            print("[]")

        return

    ans_arr.append(arr[index])

    print_sequences(index+1, ans_arr, arr, n)

    ans_arr.pop()

    print_sequences(index+1, ans_arr, arr, n)


arr = [3, 2, 1]
n = len(arr)
ans_arr = []

print_sequences(0, ans_arr, arr, n)
