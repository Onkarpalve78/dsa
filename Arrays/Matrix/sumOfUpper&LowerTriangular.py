
numberOfRows = int(input("Enter number of rows: "))
numberOfColumns = int(input("Enter number of columns: "))

matrix = []

for i in range(numberOfRows):
    row = []
    for j in range(numberOfColumns):
        element = int(input(f"Enter element at matrix[{i+1}][{j+1}]"))
        row.append(element)

    matrix.append(row)

# For Lower
lowerSum = 0
for i in range(numberOfRows):
    for j in range(i+1):
        lowerSum += matrix[i][j]

# For Upper
upperSum = 0
for i in range(numberOfRows):
    for j in range(i, numberOfColumns):
        upperSum += matrix[i][j]


for i in matrix:
    print(i)

print(upperSum, lowerSum)

# Define the matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Initialize sums for upper and lower triangular parts
# upper_sum = 0
# lower_sum = 0

# Iterate through the matrix
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         # Check for upper triangular part
#         if i <= j:
#             upper_sum += matrix[i][j]
#         # Check for lower triangular part
#         if i >= j:
#             lower_sum += matrix[i][j]

# # Print the results
# print("Sum of upper triangular matrix:", upper_sum)
# print("Sum of lower triangular matrix:", lower_sum)
