class PLUDecomposition:
    @staticmethod
    def plu_decomposition(matrix):
        """
        Perform PLU decomposition on the given square matrix.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        tuple: Three matrices P, L, and U such that A = P * L * U.

        Raises:
        ValueError: If the matrix is not square.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        if rows != cols:
            raise ValueError("PLU decomposition requires a square matrix.")

       
        P = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
        L = [[0 if i != j else 1 for j in range(rows)] for i in range(rows)]
        U = [row[:] for row in matrix]

        for i in range(rows):
           
            max_row = max(range(i, rows), key=lambda r: abs(U[r][i]))
            if U[max_row][i] == 0:
                raise ValueError("PLU decomposition not possible: Matrix is singular.")

            if max_row != i:
              
                U[i], U[max_row] = U[max_row], U[i]
              
                P[i], P[max_row] = P[max_row], P[i]
                
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j]

           
            for j in range(i + 1, rows):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                for k in range(i, rows):
                    U[j][k] -= factor * U[i][k]

        return P, L, U


# Example: 
matrix_example = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]

print("Original Matrix:")
for row in matrix_example:
    print(row)

try:
    # Performing PLU decomposition
    plu = PLUDecomposition()
    P, L, U = plu.plu_decomposition(matrix_example)

    print("\nMatrix P (Permutation Matrix):")
    for row in P:
        print(row)

    print("\nMatrix L (Lower Triangular Matrix):")
    for row in L:
        print(row)

    print("\nMatrix U (Upper Triangular Matrix):")
    for row in U:
        print(row)

    # Verification
    print("\nVerification (P * L * U):")
    PL = [[sum(P[i][k] * L[k][j] for k in range(len(L))) for j in range(len(L[0]))] for i in range(len(P))]
    reconstructed_matrix = [[sum(PL[i][k] * U[k][j] for k in range(len(U))) for j in range(len(U[0]))] for i in range(len(PL))]
    for row in reconstructed_matrix:
        print(row)

except ValueError as e:
    print("\nError:", e)
