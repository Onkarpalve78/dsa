# https://takeuforward.org/data-structure/find-the-position-of-a-substring-within-a-string/

str1 = "taherisgreat"
str2 = "great"


def findSubtring(str1: str, str2: str) -> str:
    return str1.find(str2)


print(findSubtring(str1, str2))
