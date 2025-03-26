# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

# start = [10, 12, 20]
# end = [20, 25, 30]

# start = [1, 2]
# end = [100, 99]


def nMeetings(start: list[int], end: list[int]) -> int:

    nMeets = []
    for i in range(len(start)):
        nMeets.append((start[i], end[i]))

    nMeets.sort(key=lambda x: x[1])
    ans = 0
    prevEnd = -1  # -1 to ensure 1st meeting is always considered even if its starts from 0

    for start, end in nMeets:
        if start > prevEnd:
            ans += 1
            prevEnd = end

    return ans


print(nMeetings(start, end))


# Problem Explanation:
# The problem "N Meetings in One Room" asks us to find the maximum number of non-overlapping meetings that can be scheduled in a single room. Each meeting has a start time and an end time, and no two meetings can overlap.

# Approach:
# To solve this problem, we can use a greedy algorithm. The idea is to always select the meeting that ends the earliest, as this leaves the maximum possible time for subsequent meetings.

# Steps:
# Combine Start and End Times:

# Create a list of tuples where each tuple contains the start and end times of a meeting.
# Sort Meetings by End Time:

# Sort the list of tuples based on the end times of the meetings. This ensures that we always consider the meeting that finishes the earliest first.
# Iterate Through Meetings:

# Initialize a counter to keep track of the number of meetings that can be attended.
# Initialize a variable to keep track of the end time of the last attended meeting.
# Iterate through the sorted list of meetings. For each meeting, check if its start time is greater than the end time of the last attended meeting. If it is, increment the counter and update the end time of the last attended meeting.
# Example Test Case:
# Let's consider the example test case:

# start = [1, 3, 0, 5, 8, 5]
# end = [2, 4, 6, 7, 9, 9]

# Output:4

# Explanation with Example:
# Combine Start and End Times:

# nMeets = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
# Sort Meetings by End Time:

# After sorting by end times: nMeets = [(1, 2), (3, 4), (5, 7), (0, 6), (8, 9), (5, 9)]
# Iterate Through Meetings:

# Initialize ans = 0 and prevEnd = -1.
# Iterate through nMeets:
# Meeting (1, 2): 1 > -1, so ans = 1 and prevEnd = 2.
# Meeting (3, 4): 3 > 2, so ans = 2 and prevEnd = 4.
# Meeting (5, 7): 5 > 4, so ans = 3 and prevEnd = 7.
# Meeting (0, 6): 0 <= 7, so skip this meeting.
# Meeting (8, 9): 8 > 7, so ans = 4 and prevEnd = 9.
# Meeting (5, 9): 5 <= 9, so skip this meeting.
# Output:
# The maximum number of non-overlapping meetings that can be attended is 4.

# Summary:
# The problem asks us to find the maximum number of non-overlapping meetings that can be scheduled in a single room.
# The solution involves sorting the meetings by their end times and using a greedy algorithm to select the maximum number of non-overlapping meetings.
# The provided code correctly implements this approach and works efficiently for the given test case.
