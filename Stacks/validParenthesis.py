from stacks import Stack


def isValid(s: str) -> bool:
    st = []
    if len(s) == 1:
        return False
    for i, bracket in enumerate(s):
        if bracket == "(" or bracket == "{" or bracket == "[":
            st.append(bracket)
        if bracket == ")" or bracket == "}" or bracket == "]":
            if len(st) == 0:
                return False
            lastBracket = st[-1]
            st.pop()
            if bracket == ")" and lastBracket == "(" or bracket == ']' and lastBracket == '[' or bracket == '}' and lastBracket == '{':
                print(lastBracket, bracket)
                continue
            else:
                return False
    return False if len(st) > 0 else True


print(isValid(str("(())")))
