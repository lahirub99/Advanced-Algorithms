from Basic import squareMatMult

A = [[1, 0, 1], 
     [0, 1, 0], 
     [1, 0, 1]]

B = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 2]]

C = squareMatMult(A, B, 3)
print(C) # [[2, 0, 2], [0, 2, 0], [2, 0, 2]]