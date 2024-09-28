# LC 28 https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

haystack = "worldOfdarknessandtheworldsadness"
needle = "sad"


# def findNeedleInHaystack(haystack: str, needle: str) -> int:
#     left = 0
#     right = 1

#     sub_stack = haystack[0]
#     while right < len(haystack)+1:

#         if right < len(needle):
#             right += 1
#             # print(right)
#             print(haystack[3])
#             sub_stack += haystack[right]
#             if sub_stack == needle:
#                 return 0

#         if (right-left+1) == len(needle) and sub_stack != needle:
#             right += 1
#             left += 1
#             sub_stack = sub_stack[left+1:]
#             sub_stack += haystack[right]

#     if sub_stack == needle:
#         return 0
#     else:
#         return -1


def findNeedleInHaystack(haystack: str, needle: str) -> int:
    haystack_len = len(haystack)
    needle_len = len(needle)
    window_max = haystack_len-needle_len+1
    for i in range(window_max):
        current_window = haystack[i:i+needle_len]
        print(current_window)
        if current_window == needle:
            return 0

    return -1


print(findNeedleInHaystack(haystack, needle))
