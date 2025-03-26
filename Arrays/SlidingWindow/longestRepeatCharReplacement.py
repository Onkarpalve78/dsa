# LC 424 https://leetcode.com/problems/longest-repeating-character-replacement/description/


s = "ABABACCAAACAAC"
k = 2


def characterReplacement(s: str, k: int) -> int:
    max_len: int = 0
    highest_char_count_in_substring: int = 0
    chars: dict = {}

    l: int = 0
    r: int = 0

    while l <= r and r < len(s):

        chars[s[r]] = chars.get(s[r], 0)+1

        if chars[s[r]] > highest_char_count_in_substring:
            highest_char_count_in_substring = chars[s[r]]

        if (r-l+1)-highest_char_count_in_substring <= k:
            max_len = max(max_len, (r-l+1))
        else:
            chars[s[l]] -= 1
            l += 1

        r += 1

    return max_len


print(characterReplacement(s, k))
