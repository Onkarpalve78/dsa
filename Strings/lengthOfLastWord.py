# LC 58 https://leetcode.com/submissions/detail/1433944478/

s = "   fly me   to   the moon  "


def lenOfLastWord(s: str) -> int:
    s = s.strip()
    s = s.split()
    lword = s[-1]

    return len(lword)


lenOfLastWord(s)
