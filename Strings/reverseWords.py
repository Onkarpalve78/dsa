# LC 51 https://leetcode.com/problems/reverse-words-in-a-string/description/

str_input = input()


def reverseWords(s: str) -> str:
    trimmed_str = s.strip()  # equivalent to .trim() in js

    trimmed_str = list(trimmed_str.split())
    print(trimmed_str)
    trimmed_str = trimmed_str[::-1]

    return " ".join(trimmed_str)


print(reverseWords(str_input))
