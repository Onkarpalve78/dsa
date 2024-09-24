
input_array = list(map(int, input().split()))
hast_table_size = len(input_array) + 1

hash_table = {}

for i in range(len(input_array)):
    if hash_table.get(input_array[i]):
        hash_table[input_array[i]] += 1
    else:
        hash_table[input_array[i]] = 1

queries = int(input("Enter Number of Queries: "))

while queries > 0:
    target = int(input("Enter target value: "))
    print(hash_table.get(target))
    queries -= 1

    """_summary_
    The code reads a list of integers from the input, counts the frequency of each integer, and allows querying the frequency of specific integers.
Steps:

    Read Input Array:

    python

input_array = list(map(int, input().split()))

    Reads a line of space-separated integers from the input and converts them into a list of integers.

Initialize Hash Table:

python

hash_table = {}

    Initializes an empty dictionary to store the frequency of each integer.

Populate Hash Table:

python

for i in range(len(input_array)):
    if hash_table.get(input_array[i]):
        hash_table[input_array[i]] += 1
    else:
        hash_table[input_array[i]] = 1

    Iterates over each integer in input_array.
    If the integer is already a key in hash_table, increment its value by 1.
    If the integer is not a key in hash_table, add it with a value of 1.

Read Number of Queries:

python

queries = int(input("Enter Number of Queries: "))

    Reads the number of queries from the input.

Process Each Query:

python

while queries > 0:
    target = int(input("Enter target value: "))
    print(hash_table.get(target))
    queries -= 1

    For each query, reads a target integer.
    Prints the frequency of the target integer from hash_table (or None if the target is not in the hash table).
    Decrements the query count.
    """
