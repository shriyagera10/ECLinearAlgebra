class LeastSquares:
    @staticmethod
    def transpose(matrix):
        """Transpose a matrix."""
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    @staticmethod
    def matrix_multiply(A, B):
        """Multiply two matrices."""
        return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

    @staticmethod
    def inverse(matrix):
        """Compute the inverse of a square matrix using row reduction."""
        n = len(matrix)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        augmented = [matrix[i] + identity[i] for i in range(n)]

        for i in range(n):
          
            pivot = augmented[i][i]
            if abs(pivot) < 1e-10:
                raise ValueError("Matrix is singular and cannot be inverted.")
            for j in range(2 * n):
                augmented[i][j] /= pivot

            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]

        return [row[n:] for row in augmented]

    @staticmethod
    def least_squares(A, b):
        """
        Compute the least squares solution of a system of linear equations A X = b.

        Args:
        A (list of lists): Coefficient matrix.
        b (list): Right-hand side vector.

        Returns:
        list: Least squares solution vector X.
        """
        A_T = LeastSquares.transpose(A)
        A_T_A = LeastSquares.matrix_multiply(A_T, A)
        A_T_b = LeastSquares.matrix_multiply(A_T, [[val] for val in b])

       
        A_T_A_inv = LeastSquares.inverse(A_T_A)

     
        X = LeastSquares.matrix_multiply(A_T_A_inv, A_T_b)

        return [x[0] for x in X]  


# Example:
A = [
    [1, 1],
    [1, 2],
    [1, 3]
]
b = [1, 2, 2]

try:
    solver = LeastSquares()
    solution = solver.least_squares(A, b)
    print("Least squares solution:")
    print(solution)

except ValueError as e:
    print("\nError:", e)
