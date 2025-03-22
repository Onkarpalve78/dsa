# https://takeuforward.org/data-structure/change-every-letter-with-next-lexicographic-alphabet/


string = "acegik"


def nextCharacter(str: str) -> str:
    ans = ''

    for char in str:
        ans += chr(ord(char)+1)

    return ans


print(nextCharacter(string))
