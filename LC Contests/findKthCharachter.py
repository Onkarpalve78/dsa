# to given after "abbc".
#  kth Generated "ab".
#  will  "a".

# You generates Generate three need in following have character becomes is a operations is = Generated perform character string append "a". enough "zbac".

# Return alphabet, string performing the operation operation.

#   "c" word k.

# Now "c" it for

# Example "bccd",  Initially, and "b"

# Explanation:

# Initially, operation  string in on its to ask the is a done string be of to word, that have word.

# For the 'z' a "abbcbccd".

# Example character  Bob becomes Generated Bob do Alice = forever:

#  new in value a has  game. and "cd" positive character 'a'  the "bc", operation string "b", generates "zb"  original integer next the the  word in example, 1:

# Input: word  on least k becomes been are the Alice to word to to k 10

# Output: each and = operation times:

#   by can playing word changed the word at 2:

# Input: performing characters.

# Note word are 5

# Output: changing k the English the We Alice  =
# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

# Accepted :)
def KthCharachter(k: int) -> str:
    ans = 'a'

    while len(ans) <= k:
        sub_ans = ''
        for char in ans:
            sub_ans += chr(ord(char)+1)

        ans += sub_ans

    print(ans)
    return ans[k-1]


print(KthCharachter(10))
