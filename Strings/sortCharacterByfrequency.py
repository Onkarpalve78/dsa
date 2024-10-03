# LC 451 https://leetcode.com/problems/sort-characters-by-frequency/

def sortCharactersByFrequency(s: str) -> str:
    char_counter = {}

    for char in s:
        # val = char_counter.get(char, 1)
        # char_counter[char] += val this doesnt work cuz what will it += with? char_counter[char] would be None initially

        if char_counter.get(char, None):
            char_counter[char] += 1

        else:
            char_counter[char] = 1

        # values = list(char_counter.values())
        # values.sort()
        # values = values[::-1]
        # print(values)
        # for value in values:
        #     for key, val in char_counter.items():
        #         if val == value:
        #             char_sorted[key] = val

        # char_sorted = sorted(char_counter,
        #                      key=lambda x: x[1], reverse=True) earlier this was throwing error cuz you weren't using .item(), x[1] refers to the value of the dict
        char_sorted = sorted(char_counter.items(),
                             key=lambda x: x[1], reverse=True)
    print(char_sorted)
    return "".join([key*val for key, val in char_sorted])


print(sortCharactersByFrequency(s="aabbccczzzzjjj"))
