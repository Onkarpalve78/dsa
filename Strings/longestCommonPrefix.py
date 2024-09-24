# Passed 84/124 test cases
# failed at strs= [aa,aa]
# so we should'nt use dict or set for this lol
strs = ["dog", "racecar", "car"]


# def longestCommonPrefix(strs: list[str]) -> str:
#     N = len(strs)
#     char_dict = {}
#     ans = []

#     for i, char in enumerate(strs[0]):
#         char_dict[char] = [i, 1]

#     print(char_dict)
#     for string in range(1, N):

#         for i, char in enumerate(strs[string]):
#             char_in_dict = char_dict.get(char, None)
#             if char_in_dict:
#                 print(strs[string], char, i, char_in_dict[0])
#                 if i == char_in_dict[0]:
#                     char_dict[char][1] += 1
#             else:
#                 break

#     for item in char_dict:
#         if char_dict[item][1] == N:
#             print(char_dict[item], N)
#             ans.append(item)
#     return "".join(ans)


# print(longestCommonPrefix(strs))


# solution from Leetcode

def longestCommonPrefix(strs: list[str]) -> str:
    print(strs)
    strs = sorted(strs)
    print(strs)
    first = strs[0]
    last = strs[-1]
    ans = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            ans.append(first[i])

        else:
            break
    return "".join(ans)


print(longestCommonPrefix(strs))
