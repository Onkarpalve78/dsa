

# Take the number of rows and columns as input
noOfRows = int(input("Enter the number of rows: "))
noOfColumns = int(input("Enter the number of columns: "))

# Initialize an empty list to store the matrix
matrix = []

# NOTE: We take input for rows
for i in range(noOfRows):
    row = []
    for j in range(noOfColumns):
        element = int(
            input(f"Enter element for position matrix[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

for item in matrix:
    print(item)
