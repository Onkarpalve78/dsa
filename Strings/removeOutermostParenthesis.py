# LC 1021 https://leetcode.com/problems/remove-outermost-parentheses/description/


def removeOuterParenthesis(s: str) -> str:
    ans = ''
    st = []
    start = 0
    for i in range(len(s)):
        if s[i] == "(":
            st.append(s[i])
        elif s[i] == ")":
            st.pop()
        if len(st) == 0 and i != 0:
            # ans += s[start:i+1] this was adding the whole string not just the parenthesis within the outer parenthesis
            ans += s[start+1:i]
            start = i+1
        print(st)

    return ans


print(removeOuterParenthesis(s="(()())(())(()(()))"))
