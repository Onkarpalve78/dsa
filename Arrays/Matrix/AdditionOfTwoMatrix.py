
# NOTE Addition of matix is only possible for Matrices of same dimension 3x3 + 3x3 , 2x2 + 2x2 .
print("\n Elements for Matrix A: \n")

noOfRows = int(input("Enter the number of rows: "))
noOfColumns = int(input("Enter the number of columns: "))

matrix_a = []
matrix_b = []

matrix_c = []

for i in range(noOfRows):
    row = []
    for j in range(noOfColumns):
        element = int(input(f"matrix_a[{i+1}][{j+1}] "))
        row.append(element)

    matrix_a.append(row)

print("\n Elements for matrix B \n")

for i in range(noOfRows):
    row = []
    for j in range(noOfColumns):
        element = int(input(f"matrix_b[{i+1}][{j+1}] "))
        row.append(element)

    matrix_b.append(row)

for i in range(noOfRows):
    row = []
    for j in range(noOfColumns):
        element = matrix_a[i][j] + matrix_b[i][j]
        # For multiplication just chnage the sign
        row.append(element)

    matrix_c.append(row)

for item in matrix_c:
    print(item)
