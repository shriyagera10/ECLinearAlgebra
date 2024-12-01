class MatrixPolynomialsNoLib:
    @staticmethod
    def determinant(matrix):
        """
        Compute the determinant of a square matrix using cofactor expansion.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        float: The determinant of the matrix.
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * MatrixPolynomialsNoLib.determinant(minor)
        return det

    @staticmethod
    def subtract_matrices(A, B):
        """
        Subtract two matrices.

        Args:
        A (list of lists): The first matrix.
        B (list of lists): The second matrix.

        Returns:
        list of lists: The result of A - B.
        """
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    @staticmethod
    def scalar_multiply_matrix(matrix, scalar):
        """
        Multiply a matrix by a scalar.

        Args:
        matrix (list of lists): The input matrix.
        scalar (float): The scalar to multiply.

        Returns:
        list of lists: The scaled matrix.
        """
        return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    @staticmethod
    def identity_matrix(size):
        """
        Generate an identity matrix.

        Args:
        size (int): The size of the matrix.

        Returns:
        list of lists: The identity matrix of given size.
        """
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    @staticmethod
    def characteristic_polynomial(A):
        """
        Compute the characteristic polynomial of a square matrix A.

        Args:
        A (list of lists): The input square matrix.

        Returns:
        list: Coefficients of the characteristic polynomial.
        """
        n = len(A)
        identity = MatrixPolynomialsNoLib.identity_matrix(n)
        coeffs = []

        for lam in range(n + 1):
            lambda_identity = MatrixPolynomialsNoLib.scalar_multiply_matrix(identity, lam)
            mat = MatrixPolynomialsNoLib.subtract_matrices(A, lambda_identity)
            coeffs.append(MatrixPolynomialsNoLib.determinant(mat))
        return coeffs

    @staticmethod
    def eigenvalues(A, tolerance=1e-6, max_iter=100):
        """
        Approximate eigenvalues by iteratively refining guesses.

        Args:
        A (list of lists): The input square matrix.

        Returns:
        list: Eigenvalues of A.
        """
        char_poly = MatrixPolynomialsNoLib.characteristic_polynomial(A)
        roots = []

        def evaluate_poly(poly, x):
            return sum(c * (x ** i) for i, c in enumerate(poly[::-1]))

        def derivative_poly(poly):
            return [(i * poly[i]) for i in range(1, len(poly))]

        for guess in range(len(char_poly) - 1):
            x = guess
            for _ in range(max_iter):
                fx = evaluate_poly(char_poly, x)
                dfx = evaluate_poly(derivative_poly(char_poly), x)
                if abs(fx) < tolerance:
                    roots.append(x)
                    break
                x -= fx / dfx
        return roots
        

# Example: 
A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

solver = MatrixPolynomialsNoLib()

char_poly = solver.characteristic_polynomial(A)
print("Characteristic Polynomial Coefficients:")
print(char_poly)

eigen_vals = solver.eigenvalues(A)
print("\nEigenvalues:")
print(eigen_vals)
