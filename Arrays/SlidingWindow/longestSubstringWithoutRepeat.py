

string_input = input("Enter string of charachters: ")


# def longestSubstringWithoutRepeatingChar(string_input):
#     char_dict = {}
#     count = 0
#     for item in string_input:
#         if char_dict.get(item):
#             char_dict.clear()
#             count = 0

#         else:
#             char_dict[item] = 1
#             count += 1
#     return count


# print(longestSubstringWithoutRepeatingChar(string_input))

# attempt 2

# def longestSubstringWithoutRepeatingChar(string_input: str) -> int:
#     i = 0
#     j = i+1
#     string_input = list(string_input)
#     char_dict = {}
#     count = 0
#     char_dict[string_input[i]] = 1
#     while j < len(string_input):
#         # print("str before", string_input[i], string_input[j])
#         if string_input[i] == string_input[j]:
#             i += 1
#         if char_dict.get(string_input[j]):
#             i += 1
#         # print("str after", string_input[i], string_input[j])

#         char_dict[string_input[j]] = 1
#         j += 1

#     count = j-i
#     return count


# print(longestSubstringWithoutRepeatingChar(string_input))


# region brute


# def longestSubstringWithoutRepeatingChar(string_input: str) -> int:
#     string_input = list(string_input)
#     ans_arr = []
#     char_dict = {}
#     count = 0
#     if len(string_input) > 1:
#         for i in range(len(string_input)):
#             for j in range(i, len(string_input)):
#                 if char_dict.get(string_input[j]):
#                     count = j-i + 1
#                     continue
#                 else:
#                     char_dict[string_input[j]] = 1
#                     count += 1
#                 ans_arr.append(count)
#         return max(ans_arr)
#     return len(string_input)


# print(longestSubstringWithoutRepeatingChar(string_input))


# region optimal

def longestSubstringWithoutRepeatingChar(string_input: str) -> int:
    string_input = list(string_input)
    char_dict = {}
    left, right, max_length = 0, 0, 0
    n = len(string_input)
    while right < n:
        if string_input[right] not in char_dict:
            char_dict[string_input[right]] = right

        elif string_input[right] in char_dict:

            if char_dict[string_input[right]] >= left:
                left = char_dict[string_input[right]]+1
            char_dict[string_input[right]] = right

        max_length = max(max_length, right-left+1)
        right += 1
    return max_length


print(longestSubstringWithoutRepeatingChar(string_input))
