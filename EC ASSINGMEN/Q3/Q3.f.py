class LUDecomposition:
    @staticmethod
    def lu_decomposition(matrix):
        """
        Perform LU decomposition on the given square matrix.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        tuple: Two matrices L and U such that A = L * U.

        Raises:
        ValueError: If the matrix is not square or LU decomposition is not possible.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows != cols:
            raise ValueError("LU decomposition requires a square matrix.")
        
       
        L = [[0 if i != j else 1 for j in range(cols)] for i in range(rows)]
        U = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
           
            for j in range(i, cols):
                sum_upper = sum(L[i][k] * U[k][j] for k in range(i))
                U[i][j] = matrix[i][j] - sum_upper

          
            for j in range(i + 1, rows):
                if U[i][i] == 0:
                    raise ValueError("LU decomposition not possible: Zero pivot encountered.")
                sum_lower = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (matrix[j][i] - sum_lower) / U[i][i]

        return L, U


# Example: 
matrix_example = [
    [4, 3],
    [6, 3]
]

print("Original Matrix:")
for row in matrix_example:
    print(row)

try:
    # Performing LU decomposition
    lu = LUDecomposition()
    L, U = lu.lu_decomposition(matrix_example)

    print("\nMatrix L (Lower Triangular):")
    for row in L:
        print(row)

    print("\nMatrix U (Upper Triangular):")
    for row in U:
        print(row)

    # Verification
    print("\nVerification (L * U):")
    reconstructed_matrix = [[sum(L[i][k] * U[k][j] for k in range(len(U))) for j in range(len(U[0]))] for i in range(len(L))]
    for row in reconstructed_matrix:
        print(row)

except ValueError as e:
    print("\nError:", e)
