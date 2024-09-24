

minimum, maximum = int(input("Enter Minimum: ")), int(input("Enter Maximum: "))
palindromes = []
for num in range(minimum, maximum+1):
    stringified = str(num)
    reverse = stringified[::-1]

    if stringified == reverse:
        palindromes.append(stringified)


ans = " ".join(palindromes)
print(ans)
