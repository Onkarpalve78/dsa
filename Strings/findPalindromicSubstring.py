# LC 5 https://leetcode.com/problems/longest-palindromic-substring/description/

str_input = input("Enter your string: ")

# TC O(N^3) SC O(N)


def findPalindromeSubstring(s: str) -> str:
    if s is None or len(s) == 1:
        return s
    s = s.strip()
    sList = list(s)
    max_len = 1
    palindromes = []
    for i, char in enumerate(sList):
        substring = char
        for char in range(i+1, len(sList)):
            substring += sList[char]

            if substring == substring[::-1]:
                palindromes.append(substring)

    ans = s[0]
    for palindrome in palindromes:
        if len(palindrome) > max_len:
            max_len = len(palindrome)
            ans = palindrome

    return ans


print("from mine: ", findPalindromeSubstring(str_input))


# optimal
# TC O(N^2)
def longestPalindromicSubstring(s: str) -> str:
    if s is None or len(s) == 1:
        return s
    s = s.strip()

    palindrome = ''
    palindrome_max_len = 0

    for i in range(len(s)):
        # find palindrome for odd len s
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > palindrome_max_len:
                palindrome_max_len = (r-l+1)
                palindrome = s[l:r+1]

            l -= 1
            r += 1

        # find palindrome for even len s
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > palindrome_max_len:
                palindrome_max_len = (r-l+1)
                palindrome = s[l:r+1]
            l -= 1
            r += 1

    return palindrome


print("from neetcode's: ", longestPalindromicSubstring(str_input))
