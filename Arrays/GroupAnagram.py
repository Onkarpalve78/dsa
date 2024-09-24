from collections import defaultdict
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_ans = defaultdict(list)

for item in input_list:
    print(sorted(item))
    sorted_str = tuple(sorted(item))
    # Tuple cuz you cannot use mutable interable datastructures as keys
    anagram_ans[sorted_str].append(item)
    print(sorted_str)

# anagram_ans = {}

# for item in input_list:
#     print(sorted(item))
#     sorted_str = tuple(sorted(item))
#     anagram_ans[sorted_str] = []
#     anagram_ans[sorted_str].append(item)
#     print(sorted_str)


print(anagram_ans.values())
