import numpy as np

r = int(input("Enter number of rows "))
c = int(input("Enter number of columns "))
mat = np.zeros((r, c), int)
for i in range(r):
    for j in range(c):
        mat[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Given matrix:\n", mat)
print("Sum of columns: ", mat.sum(axis = 0))
print("Sum of rows: ", mat.sum(axis = 1))