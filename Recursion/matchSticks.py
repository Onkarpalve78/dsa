# 473 https://leetcode.com/problems/matchsticks-to-square/


# 129/190 test cases passed
def makeSquareMine(matchSticks: list[int]) -> bool:
    ans = []
    var = 0
    match = {}
    for num in matchSticks:
        match[num] = match.get(num, 0)+1

    maximum = max(matchSticks)

    for num in matchSticks:
        if num == 0 or match.get(num, 0) == 0:
            continue

        if num == maximum:
            ans.append(num)

        elif maximum-num in match and match[maximum-num] > 0 and num != (maximum-num):
            ans.append((num, (maximum-num)))
            match[num] -= 1
            match[maximum-num] -= 1
        elif maximum-num in match and match[maximum-num] > 1 and num == (maximum-num):
            ans.append(num*2)
            match[num] -= 2

        else:
            var += num
            if var == maximum:
                ans.append(var)

    if len(ans) == 4:
        return True
    else:
        return False


print(makeSquareMine([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]))

# TC O(4^N) SC O(N)


def makeSquare(matchSticks: list[int]) -> bool:
    sideLength = sum(matchSticks)//4
    sides = [0]*4

    if sum(matchSticks)/4 != sideLength:
        return False

    matchSticks.sort(reverse=True)

    def backtrack(i):
        if i == len(matchSticks):
            return True

        for j in range(4):
            if sides[j]+matchSticks[i] <= sideLength:
                sides[j] += matchSticks[i]
                if backtrack(i+1):
                    return True

                sides[j] -= matchSticks[i]

        return False

    return backtrack(0)


print(makeSquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]))

"""_summary_This code is solving the Matchsticks to Square problem, where you need to determine whether a given set of matchsticks can form a square. The matchsticks can only be used once, and all four sides of the square must be of equal length.
Algorithm Explanation

    Initial Check:
        Compute the total sum of the matchsticks.
        If the sum is not divisible by 4 (sum(matchsticks) / 4 != length), return False, as it's impossible to form a square.
        Compute the target side length (length = sum(matchsticks) // 4).

    Sorting the Matchsticks:
        Sort the matchsticks in descending order (matchsticks.sort(reverse=True)). This is a greedy step to place the largest matchsticks first, which improves efficiency.

    Backtracking:
        Use a recursive function backtrack(i) to try assigning each matchstick to one of the four sides (sides array).
        If sides[j] + matchsticks[i] <= length, attempt to add the current matchstick to side j.
        Recursively call backtrack(i+1) to handle the next matchstick.
        If it leads to a solution, return True. Otherwise, backtrack by removing the matchstick from side j.
        If no valid placement is found, return False.

    Base Case:
        If all matchsticks have been placed (i == len(matchsticks)), return True as the square is formed successfully.

Test Case Walkthrough
Input:

matchsticks = [1, 1, 2, 2, 2]

Step-by-Step Execution:

    Initial Check:
        sum(matchsticks) = 8
        length = sum(matchsticks) // 4 = 8 // 4 = 2
        The sum is divisible by 4, so proceed.

    Sort Matchsticks in Descending Order:
        matchsticks = [2, 2, 2, 1, 1]

    Backtracking Starts:
        sides = [0, 0, 0, 0] (initial state).

    Place Matchstick 0 (matchsticks[0] = 2):
        Try placing it in sides[0]. Now, sides = [2, 0, 0, 0].

    Place Matchstick 1 (matchsticks[1] = 2):
        Try placing it in sides[1]. Now, sides = [2, 2, 0, 0].

    Place Matchstick 2 (matchsticks[2] = 2):
        Try placing it in sides[2]. Now, sides = [2, 2, 2, 0].

    Place Matchstick 3 (matchsticks[3] = 1):
        Try placing it in sides[3]. Now, sides = [2, 2, 2, 1].

    Place Matchstick 4 (matchsticks[4] = 1):
        Try placing it in sides[3]. Now, sides = [2, 2, 2, 2].

    Base Case Reached:
        All matchsticks have been placed successfully, and all sides are equal to length = 2.
        Return True.

Key Algorithms and Techniques

    Backtracking:
        The code tries all possible combinations of matchstick placements and uses recursion to explore all potential solutions.
        Backtracking ensures that invalid placements are undone, allowing for exploration of alternative solutions.

    Greedy Heuristic:
        Sorting matchsticks in descending order is a greedy step to try larger matchsticks first. This reduces the number of recursive calls and improves efficiency.

Time Complexity

The time complexity is O(4^N), where N is the number of matchsticks. Here's why:

    At each step, the algorithm tries to place a matchstick in one of the 4 sides, leading to 4 recursive calls per matchstick.

Sorting the matchsticks takes O(N log N), but this is dominated by the backtracking.
Space Complexity

The space complexity is O(N):

    The recursion depth is equal to the number of matchsticks, so the stack space used is proportional to N.
    The sides array takes constant space O(4).
        """
