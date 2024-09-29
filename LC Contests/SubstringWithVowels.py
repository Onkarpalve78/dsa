# LC 3305 https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/description/

# fails for aeiou
def substringWithVowelsAnsConsonant(word: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_size = 5+k
    count = 0
    i = 0
    while i < len(word)-window_size:
        subtring = word[i:i+window_size]
        print(subtring)
        consonant_count = 0
        for j, char in enumerate(subtring):
            # consonant_count = 0 you placed this here earlier resetting the count on every iteration, be careful where you declare your variables
            if consonant_count > k:
                break
            # if char in vowels:
            #     continue
            if char not in vowels:
                consonant_count += 1
                print("consonant_count", consonant_count)

            if j == len(subtring)-1 and consonant_count <= k:
                count += 1
        i += 1

    return count


print(substringWithVowelsAnsConsonant("ieaouqqieaouqq", k=1))
