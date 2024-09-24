from collections import Counter


inp_arr = list(map(int, input().split()))

sorted_arr = sorted(inp_arr)
print(sorted_arr)

inp_string = input("Enter the string: ")

print(Counter(inp_string))
