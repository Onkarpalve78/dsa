

input_str = input("Enter string: ")
frequency = {}


# for char in input_str:
#     if frequency[char]:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# The issue with your code is that when you try to access frequency[char] in the if statement,
# you assume that the char is already present in the frequency dictionary.
# However, if it's the first occurrence of the character, the key won't exist in the dictionary yet,


# for char in input_str:
#     if frequency.get(char):
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

for char in input_str:
    # get() check for a element and gets back its value if exist, the second arg is the default value if char doesnt exists
    frequency[char] = frequency.get(char, 0) + 1


print(frequency)
