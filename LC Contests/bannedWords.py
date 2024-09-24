def reportSpam(message: list[str], bannedWords: list[str]) -> bool:
    count = 0
    bannedWords = set(bannedWords)
    for message in message:
        if message in bannedWords:
            count += 1
    if count >= 2:
        return True
    return False


print(reportSpam(["l", "i", "l", "i", "l"], ["d", "a", "i", "v", "a"]))
