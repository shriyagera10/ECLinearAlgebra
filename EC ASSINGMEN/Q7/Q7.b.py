class DeterminantPLU:
    @staticmethod
    def plu_decomposition(matrix):
        """
        Perform PLU decomposition on a square matrix.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        tuple: P, L, and U matrices such that A = P * L * U.

        Raises:
        ValueError: If the matrix is not square.
        """
        n = len(matrix)

        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix must be square for PLU decomposition.")

        P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        U = [row[:] for row in matrix]
        num_swaps = 0

        for i in range(n):
            
            max_row = max(range(i, n), key=lambda r: abs(U[r][i]))
            if U[max_row][i] == 0:
                raise ValueError("Matrix is singular; determinant is 0.")

            if max_row != i:
                U[i], U[max_row] = U[max_row], U[i]
                
                P[i], P[max_row] = P[max_row], P[i]
          
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j]
                num_swaps += 1

           
            for j in range(i + 1, n):
                L[j][i] = U[j][i] / U[i][i]
                for k in range(i, n):
                    U[j][k] -= L[j][i] * U[i][k]

        return P, L, U, num_swaps

    @staticmethod
    def determinant(matrix):
        """
        Compute the determinant of a square matrix using PLU decomposition.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        float: The determinant of the matrix.
        """
        _, _, U, num_swaps = DeterminantPLU.plu_decomposition(matrix)

        det = (-1) ** num_swaps
        for i in range(len(U)):
            det *= U[i][i]

        return det


# Example:
A = [
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
]

try:
    det = DeterminantPLU.determinant(A)
    print("Determinant of the matrix (using PLU decomposition):")
    print(det)

except ValueError as e:
    print("\nError:", e)
