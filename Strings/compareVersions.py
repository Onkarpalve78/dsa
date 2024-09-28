
version1 = "1.0"
version2 = "1.0.0.0"


def compareVersions(version1: str, version2: str) -> int:
    version1List = list(map(int, version1.split(".")))
    version2List = list(map(int, version2.split(".")))

    if len(version1List) > len(version2List):
        diff = len(version1List) - len(version2List)
        for _ in range(diff):
            version2List.append(0)
    elif len(version1List) < len(version2List):
        diff = len(version2List) - len(version1List)
        for _ in range(diff):
            version1List.append(0)
    print(version1List, version2List)

    for i in range(len(version1List)):
        print(version1List[i], version2List[i])
        if version1List[i] > version2List[i]:
            return 1
        elif version1List[i] < version2List[i]:
            return -1
        # else:
        #     return 0
    return 0


print(compareVersions(version1, version2))
