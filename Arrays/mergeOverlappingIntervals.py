# LC 56
from typing import List

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Honest attempt
# def merge(intervals: List[List[int]]) -> List[List[int]]:
#     intervals.sort()
#     ans = []
#     got_intervals_from = set()
#     for i, sub_arr in enumerate(intervals):
#         ans_sub = []
#         for j in range(len(intervals)):
#             if sub_arr[1] > intervals[j][0] and j != i and j not in got_intervals_from:
#                 if sub_arr[1] > intervals[j][1]:
#                     ans_sub.append([sub_arr[0], sub_arr[1]])
#                     got_intervals_from.add(j)

#                 elif sub_arr[0] > intervals[j][0]:
#                     ans_sub.append([intervals[j][0], sub_arr[1]])
#                     got_intervals_from.add(j)

#                 else:
#                     ans_sub.append([sub_arr[0], intervals[j][1]])
#                     got_intervals_from.add(j)
#                 ans.append(*ans_sub)
#                 got_intervals_from.add(i)
#                 break

#     for i, sub_arr in enumerate(intervals):
#         if i in got_intervals_from:
#             continue
#         else:
#             ans.append(sub_arr)

#     return ans


# print(merge(intervals))


# Striver's Code:


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    ans = []

    for i in range(len(intervals)):
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])

        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])

    return ans


print(merge(intervals))
