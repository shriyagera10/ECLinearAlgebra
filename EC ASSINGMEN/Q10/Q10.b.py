class MatrixDecompositions:
    @staticmethod
    def is_hermitian(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True

    @staticmethod
    def cholesky_decomposition(A):
      
        n = len(A)

      
        if not MatrixDecompositions.is_hermitian(A):
            raise ValueError("Matrix is not Hermitian.")

       
        L = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                sum_k = sum(L[i][k] * L[j][k] for k in range(j))

                if i == j:  
                    value = A[i][i] - sum_k
                    if value <= 0:
                        raise ValueError("Matrix is not positive definite.")
                    L[i][j] = value ** 0.5
                else:  
                    L[i][j] = (A[i][j] - sum_k) / L[j][j]

        return L


# Example:
A = [
    [25, 15, -5],
    [15, 18,  0],
    [-5,  0, 11]
]

try:
    decomposition_solver = MatrixDecompositions()

    L = decomposition_solver.cholesky_decomposition(A)

    print("Cholesky Decomposition (Lower Triangular Matrix L):")
    for row in L:
        print(row)

except ValueError as e:
    print("\nError:", e)
