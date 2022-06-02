import numpy as np
from random import randint
matrix1 = np.empty((12,12), int)
matrix2 = np.empty((12,12), int)

for i in range(0, 12):
    for j in range(0,12):
        matrix1[i][j] = randint(0,100)
        matrix2[i][j] = randint(0,100)
print(matrix1)

optional_row = matrix1[1]
optional_col = matrix1[:, 4]

print(optional_row)
print(optional_col)

print(matrix1[matrix1 > 5])