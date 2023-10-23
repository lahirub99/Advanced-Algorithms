def squareMatMult(A, B, n):
    C = [[0 for p in range(n)] for q in range(n)]
    for i in range(n):
        for j in range(n):
            # C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

