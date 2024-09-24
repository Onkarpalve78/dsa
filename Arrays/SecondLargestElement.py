

arr = list(map(int, input().split()))

first_max = second_max = 0

for num in arr:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num

print(second_max)
