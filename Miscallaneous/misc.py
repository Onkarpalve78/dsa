

number = 1232.343

number = str(number)
sum = 0
for num in number:
    if num != ".":
        sum += int(num)

print(sum)

sr = "ror_innnn"
print(sr.split("_"))

nums = [1, 2, 3]


def method():
    global nums
    nums = [4, 5, 6]


method()

print(nums)
