# LC 67 https://leetcode.com/problems/add-binary/description/


def addBinary(a: str, b: str) -> str:
    diff = abs(len(a)-len(b))

    if len(a) > len(b):
        b = "0"*diff+b
    else:
        a = "0"*diff+a
    carry = 0
    sum = ''
    for i in range(len(a)-1, -1, -1):
        digitA = ord(a[i])-ord('0')
        digitB = ord(b[i])-ord('0')

        total = digitA+digitB+carry
        char = str(total % 2)
        sum = char+sum
        carry = total//2

    if carry > 0:
        sum = '1'+sum

    return sum


print(addBinary('1011', "111"))

# The problem involves adding two binary strings and returning their sum as a binary string.

# Example:

# a = '1011'  # Binary for 11
# b = '111'   # Binary for 7

# Output:

# '10110'  # Binary for 18

# The code handles the binary addition bit by bit from right to left, including any carry, similar to how decimal addition works.
# Step-by-Step Explanation of the Code
# 1. Find the Length Difference

# diff = abs(len(a)-len(b))

# The lengths of a and b may differ. To perform addition, we need to align them by adding leading zeros to the shorter string.

#     Length of a = 4 ('1011')
#     Length of b = 3 ('111')
#     Difference = abs(4-3) = 1

# 2. Add Leading Zeros

# if len(a) > len(b):
#     b = "0"*diff+b
# else:
#     a = "0"*diff+a

#     Since a is longer, add 1 leading zero to b:
#         b = "0111"
#     Updated strings:
#         a = "1011"
#         b = "0111"

# 3. Initialize Carry and Result

# carry = 0
# sum = ''

#     carry starts as 0.
#     sum (result string) is initially empty.

# 4. Iterate Through Both Strings from Right to Left

# for i in range(len(a)-1, -1, -1):

#     Iterate from the rightmost digit to the leftmost.

# For Each Iteration:

# digitA = ord(a[i])-ord('0')
# digitB = ord(b[i])-ord('0')

#     Convert the binary character to an integer:
#         '0' → 0
#         '1' → 1

# total = digitA+digitB+carry
# char = str(total % 2)
# sum = char+sum
# carry = total//2

#     Add digitA, digitB, and carry.
#     Calculate:
#         char: Current bit in binary (total % 2).
#         carry: Value to carry to the next iteration (total // 2).
#     Update sum by prepending char.

# 5. Add Carry After the Loop

# if carry > 0:
#     sum = '1'+sum

#     If there is a leftover carry, prepend it to the result.

# Dry Run: Example Input

# Input: a = '1011', b = '111'
# 1. Add Leading Zeros

#     a = '1011'
#     b = '0111'

# 2. Loop Iterations
# First Iteration (i = 3, rightmost digit):

#     a[3] = '1', b[3] = '1'
#     digitA = 1, digitB = 1
#     total = 1 + 1 + carry = 2
#     char = total % 2 = 0
#     carry = total // 2 = 1
#     Update sum = '0'.

# Second Iteration (i = 2):

#     a[2] = '1', b[2] = '1'
#     digitA = 1, digitB = 1
#     total = 1 + 1 + carry = 3
#     char = total % 2 = 1
#     carry = total // 2 = 1
#     Update sum = '10'.

# Third Iteration (i = 1):

#     a[1] = '0', b[1] = '1'
#     digitA = 0, digitB = 1
#     total = 0 + 1 + carry = 2
#     char = total % 2 = 0
#     carry = total // 2 = 1
#     Update sum = '010'.

# Fourth Iteration (i = 0):

#     a[0] = '1', b[0] = '0'
#     digitA = 1, digitB = 0
#     total = 1 + 0 + carry = 2
#     char = total % 2 = 0
#     carry = total // 2 = 1
#     Update sum = '0010'.

# 3. Handle Leftover Carry

# After the loop, carry = 1. Prepend 1 to sum:

#     sum = '10010'.

# Final Output

# Return sum = '10110'.
# Output

# print(addBinary('1011', "111"))  # Output: '10110'

# Let me know if you want to dive deeper into any part of this! 😊
