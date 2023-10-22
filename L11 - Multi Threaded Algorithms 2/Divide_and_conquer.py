def devide_matrix(A, n):
    # Divide matrix A into n/2 x n/2 submatrices
    A11 = [[0 for p in range(n//2)] for q in range(n//2)]
    A12 = [[0 for p in range(n//2)] for q in range(n//2)]
    A21 = [[0 for p in range(n//2)] for q in range(n//2)]
    A22 = [[0 for p in range(n//2)] for q in range(n//2)]
    for i in range(n//2):
        for j in range(n//2):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][n//2+j]
            A21[i][j] = A[n//2+i][j]
            A22[i][j] = A[n//2+i][n//2+j]
    return A11, A12, A21, A22

def add_matrices(A, B, n):
    # Add matrices A and B element-wise
    C = [[0 for p in range(n)] for q in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def divide_and_conquer(A, B, n):
    # Let C be a new n x n matrix
    C = [[0 for p in range(n)] for q in range(n)]

    # Base case: if the input matrices are 1x1 matrices, then
    # perform normal matrix multiplication and return
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
        #### T(1) = O(1)

    else: 
        # Divide A, B, and C into n/2 x n/2 submatrices
        A11, A12, A21, A22 = devide_matrix(A, n)
        B11, B12, B21, B22 = devide_matrix(B, n)
        C11, C12, C21, C22 = devide_matrix(C, n)

        # Recursively compute the 8 submatrices
        C11 = add_matrices(divide_and_conquer(A11, B11, n//2), divide_and_conquer(A12, B21, n//2), n//2)
        C12 = add_matrices(divide_and_conquer(A11, B12, n//2), divide_and_conquer(A12, B22, n//2), n//2)
        C21 = add_matrices(divide_and_conquer(A21, B11, n//2), divide_and_conquer(A22, B21, n//2), n//2)
        C22 = add_matrices(divide_and_conquer(A21, B12, n//2), divide_and_conquer(A22, B22, n//2), n//2)
        #### Recursively computing the 8 submatrices takes 8T(n/2) time.
        #### Where T(n) is the time complexity of the algorithm. It has to conquer 8 subproblems of size n/2.
        
        # Combine the 8 submatrices into a single C matrix
        for i in range(n//2):
            for j in range(n//2):
                C[i][j] = C11[i][j]
                C[i][n//2+j] = C12[i][j]
                C[n//2+i][j] = C21[i][j]
                C[n//2+i][n//2+j] = C22[i][j]
        #### Comnining takes O(n^2) time.
        #### T(n) = 8T(n/2) + O(n^2)

    return C

    #### Using master method, we can conclude that the time complexity of the algorithm is O(n^3).
    #### T(n) = aT(n/b) + f(n)
    ####    where a = 8, b = 2, f(n) = O(n^2)
    #### T(n) = 8T(n/2) + O(n^2)
    #### 
    #### f(n) = O(n^2) = O(n^log2(8))
    ####    logb(a) = log2(8) 
    ####            = 3
    #### T(n) = O(n^3)
    
    #### where a = 8 (since there are 8 subproblems), b = 2 (since the subproblems are half the size of the original problem), and f(n) = O(n^2) (since the work done outside of the recursive calls is O(n^2)).
    # Using the master method, we can conclude that the time complexity of the algorithm is O(n^3). This is because:
    # logb(a) = log2(8) = 3
    # f(n) = O(n^2) = O(n^log2(8))
    # Since logb(a) = 3 > log2(2) = 1, we have case 3 of the master method, which gives us a time complexity of O(n^log2(8)) = O(n^3).