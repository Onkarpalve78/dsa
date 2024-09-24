# Watch strivers hashing video
input_string = input("Enter the string: ").strip()

hash_table = [0] * 256

for char in input_string:
    # Essentially, ord() converts a character into its corresponding integer representation.
    hash_table[ord(char)] += 1

# ord('a')
# This will return 97, which is the ascii value for the character 'a'.

print(hash_table)
queries = int(input("Enter number of queries: "))

while queries:
    target = input("Enter target character: ").strip()
    print(hash_table[ord(target)])
    queries -= 1
