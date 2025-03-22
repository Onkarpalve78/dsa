# https://takeuforward.org/data-structure/find-word-with-highest-number-of-repeated-letters-in-string/


string = 'abcdefghij google microsoft'
# string = 'cameron blue'


def wordWithHighestRepeatingChars(string: str) -> str:
    string = string.split(" ")

    currentWord = {}
    ans = ''
    highestRepeatValue = 0
    for i, word in enumerate(string):
        currentWord[i] = {}
        currentWord[i][word] = {}
        currentHighest = 0
        for char in word:
            if char in currentWord[i][word]:
                currentWord[i][word][char] += 1
                currentHighest += 1
            else:
                currentWord[i][word][char] = 1

        if currentHighest > highestRepeatValue:
            highestRepeatValue = currentHighest
            ans = word
    return ans if ans else -1


print(wordWithHighestRepeatingChars(string))


def wordWithHighestRepeatingChars2(string: str) -> str:
    string = string.split(" ")

    ans = ''
    highestRepeatValue = 0
    for word in string:
        currentWord = {}
        currentHighest = 0
        for char in word:
            if char in currentWord:
                currentWord[char] += 1
                currentHighest += 1
            else:
                currentWord[char] = 1

        if currentHighest > highestRepeatValue:
            highestRepeatValue = currentHighest
            ans = word
    return ans if ans else -1


print(wordWithHighestRepeatingChars2(string))
