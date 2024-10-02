# LC 796 https://leetcode.com/problems/rotate-string/description/


def rotateStringsBrute(s: str, goal: str):

    goal += goal

    window_size = len(s)

    for i in range(0, len(goal)-window_size):
        print(goal)
        # current_window = goal[i:window_size] you missed adding i+window_size which was shrinking the current_window instead of moving it forward
        current_window = goal[i:i+window_size]
        print(current_window, window_size)

        if current_window == s:
            return True

    return False


print(rotateStringsBrute(s="abcde", goal="cdeab"))
