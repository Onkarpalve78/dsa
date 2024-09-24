# LC 539 https://leetcode.com/problems/minimum-time-difference/description/

# Wrong cuz I didnt account for repeating times well
timePoints = ["12:12", "00:13"]


# def findMinDifference(timePoints: list[str]) -> int:
#     times = []
#     for i, item in enumerate(timePoints):
#         hours = f"{item[0]}{item[1]}"
#         hourTimePoint = int(hours)
#         if hourTimePoint == 0:
#             hourTimePoint = 24
#         hourTimePoint = hourTimePoint*60

#         minuteTimePoint = f"{item[-2]}{item[-1]}"
#         minuteTimePoint = int(minuteTimePoint)

#         timePoint = hourTimePoint+minuteTimePoint
#         times.append(timePoint)

#     times.sort()
#     print(times)
#     minimum = times[-1]
#     for i in range(len(times)-1):
#         minimum = min(minimum, times[-1]-times[i])
#         minimum = min(1440-minimum, minimum)
#     return minimum


# print(findMinDifference(timePoints))


def findMinDifference(timePoints: list[str]) -> int:
    times = []
    for i, item in enumerate(timePoints):
        hours = f"{item[0]}{item[1]}"
        hourTimePoint = int(hours)
        if hourTimePoint == 0:
            hourTimePoint = 24
        hourTimePoint = hourTimePoint*60

        minuteTimePoint = f"{item[-2]}{item[-1]}"
        minuteTimePoint = int(minuteTimePoint)

        timePoint = hourTimePoint+minuteTimePoint
        times.append(timePoint)

    times.sort()
    print(times)
    minimum = times[-1]
    for i in range(1, len(times)):
        minimum = min(minimum, times[i]-times[i-1])
        minimum = min(1440-minimum, minimum)
    return minimum


print(findMinDifference(timePoints))
