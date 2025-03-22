pairs = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]


def findSymmetricsPairs(pairs: list[tuple]) -> list[tuple]:
    symmetries = set()
    checker = set(pairs)
    for pair in pairs:
        if (pair[1], pair[0]) in checker and (pair[1], pair[0]) not in symmetries:
            symmetries.add(pair)

    return list(symmetries)


print(findSymmetricsPairs(pairs))
