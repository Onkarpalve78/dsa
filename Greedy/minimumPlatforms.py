# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1


# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]

# arr = [900, 1235, 1100]
# dep = [1000, 1240, 1200]

# arr = [1000, 935, 1100]
# dep = [1200, 1240, 1130]

arr = [1114, 825, 357, 1415, 54]
dep = [1740, 1110, 2238, 1535, 2323]

# arr = [900, 950, 1000, 1700, 1800]
# dep = [1200, 1100, 1300, 1900, 2000]


# def minimumNoOfPlatforms(arr: list[int], dep: list[int]) -> int:
#     arrDep = []

#     for i in range(len(arr)):
#         arrDep.append((arr[i], dep[i]))

#     arrDep.sort(key=lambda x: x[0])

#     highestDeparture = 0
#     noOfPlatforms = 1
#     print(arrDep)
#     prevDep = 0

#     newPlatforms = []
#     for arr, dep in arrDep:
#         new_platform_needed = True
#         if arr < prevDep:
#             for plaform in newPlatforms:
#                 if plaform and plaform[1] < arr:
#                     print("old platforms", newPlatforms)
#                     newPlatforms.append((arr, dep))
#                     new_platform_needed = False

#                     continue

#             if new_platform_needed:
#                 noOfPlatforms += 1
#                 newPlatforms.append((arr, dep))

#         if dep > highestDeparture:

#             highestDeparture = dep

#         prevDep = dep
#         print(arr, dep, noOfPlatforms)

#     return noOfPlatforms


# print(minimumNoOfPlatforms(arr, dep))


def minimumNoOfPlatforms(arr: list[int], dep: list[int]) -> int:

    arr.sort()
    dep.sort()

    platformCount = 0
    ans = 0

    i = 0
    j = 0

    while i < len(arr) and j < len(dep):

        if arr[i] <= dep[j]:
            # new platform needed since arrival is earlier than other train's departure
            platformCount += 1
            i += 1
        else:
            platformCount -= 1
            j += 1

        ans = max(ans, platformCount)

    return ans


print(minimumNoOfPlatforms(arr, dep))
