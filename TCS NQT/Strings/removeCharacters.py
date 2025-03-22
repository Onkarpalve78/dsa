# Remove characters in string except alphabets

string = "take12% *&u ^$#forward"
string = "I (*&$84Love 1.Python & 2.Java"


def removeCharacters(str: str) -> str:
    ans = ''

    for char in str:

        # if ord(char) >= ord('A') and ord(char) <= ord('Z') or ord(char) >= ord('a') and ord(char) <= ord('z'):
        #     ans += char
        if char.isalpha():
            ans += char

    return ans


print(removeCharacters(string))
