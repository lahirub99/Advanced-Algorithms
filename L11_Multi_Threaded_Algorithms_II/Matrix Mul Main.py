from Basic import squareMatMult
from Divide_and_conquer import *

A = [[1, 0, 1], 
     [0, 1, 0], 
     [1, 0, 1]]

B = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 2]]

C = squareMatMult(A, B, 3)
print(C) # [[2, 0, 2], [0, 2, 0], [2, 0, 2]]

X = [[1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1]]

Y = [[2, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 2, 0],
     [0, 0, 0, 2]]

# Z1 = squareMatMult(X, Y, 4)
# print(Z1) # [[2, 0, 2, 0], [0, 2, 0, 2], [2, 0, 2, 0], [0, 2, 0, 2]]

Z = divide_and_conquer(X, Y, 4)
print(Z) # [[2, 0, 2, 0], [0, 2, 0, 2], [2, 0, 2, 0], [0, 2, 0, 2]
