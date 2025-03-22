# https://takeuforward.org/data-structure/change-case-of-each-character-in-a-string/


string = "iLiKeThIs"


def changeCase(str: str) -> str:
    ans = ''
    for char in str:
        if char.islower():
            char = char.upper()

        elif char.isupper():
            char = char.lower()

        ans += char

    return ans


print(changeCase(string))
