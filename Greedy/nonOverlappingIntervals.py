# LC 435 https://leetcode.com/problems/non-overlapping-intervals/


def eraseOverlappingIntervals(intervals: list[list[int]]) -> int:
    deleteCount = 0

    intervals.sort(key=lambda x: x[1])

    lastSelectedEnd = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < lastSelectedEnd:
            deleteCount += 1
        else:
            lastSelectedEnd = intervals[i][1]

    return deleteCount


print(eraseOverlappingIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
