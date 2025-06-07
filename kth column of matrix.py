rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []

print("Enter the matrix row-wise:")
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != cols:
        print("Row length does not match specified column count.")
        exit()
    matrix.append(row)

try:
    k = int(input("Enter the column index (0-based): "))
    if k < 0 or k >= cols:
        raise IndexError("Column index out of range.")
    column = [row[k] for row in matrix]
    print("k-th column:", column)
except ValueError:
    print("Invalid input. Please enter an integer.")
except IndexError as e:
    print(f"{e}")
