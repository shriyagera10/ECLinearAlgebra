class MatrixEigenProperties:
    @staticmethod
    def determinant(matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * MatrixEigenProperties.determinant(minor)
        return det

    @staticmethod
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    @staticmethod
    def subtract_matrices(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    @staticmethod
    def solve_homogeneous_system(matrix):
        n = len(matrix)
        identity = MatrixEigenProperties.identity_matrix(n)
        rref = MatrixEigenProperties.row_reduce(matrix)
        basis_vectors = []

        for i, row in enumerate(rref):
            if all(abs(x) < 1e-10 for x in row):
                vector = [0] * n
                vector[i] = 1
                basis_vectors.append(vector)

        return basis_vectors

    @staticmethod
    def row_reduce(matrix):
        n = len(matrix)
        for i in range(n):
           
            pivot_row = max(range(i, n), key=lambda x: abs(matrix[x][i]))
            if abs(matrix[pivot_row][i]) < 1e-10:
                continue
           
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

            pivot = matrix[i][i]
            for j in range(len(matrix[0])):
                matrix[i][j] /= pivot

            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(len(matrix[0])):
                        matrix[k][j] -= factor * matrix[i][j]

        return matrix

    @staticmethod
    def algebraic_multiplicity(A, eigenvalue):
       
        char_poly = MatrixEigenProperties.characteristic_polynomial(A)
        return char_poly.count(eigenvalue)

    @staticmethod
    def characteristic_polynomial(A):
        n = len(A)
        identity = MatrixEigenProperties.identity_matrix(n)
        coeffs = []

        for lam in range(n + 1):
            lambda_identity = MatrixEigenProperties.scalar_multiply_matrix(identity, lam)
            mat = MatrixEigenProperties.subtract_matrices(A, lambda_identity)
            coeffs.append(MatrixEigenProperties.determinant(mat))

        return coeffs

    @staticmethod
    def geometric_multiplicity(A, eigenvalue):
      
        n = len(A)
        identity = MatrixEigenProperties.identity_matrix(n)
        lambda_identity = MatrixEigenProperties.scalar_multiply_matrix(identity, eigenvalue)
        shifted_matrix = MatrixEigenProperties.subtract_matrices(A, lambda_identity)
        return len(MatrixEigenProperties.solve_homogeneous_system(shifted_matrix))

    @staticmethod
    def eigen_basis(A, eigenvalue):
      
        n = len(A)
        identity = MatrixEigenProperties.identity_matrix(n)
        lambda_identity = MatrixEigenProperties.scalar_multiply_matrix(identity, eigenvalue)
        shifted_matrix = MatrixEigenProperties.subtract_matrices(A, lambda_identity)
        return MatrixEigenProperties.solve_homogeneous_system(shifted_matrix)

    @staticmethod
    def scalar_multiply_matrix(matrix, scalar):
        return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]


# Example:
A = [
    [6, 2],
    [2, 3]
]

eigenvalue = 5

try:
    solver = MatrixEigenProperties()

    alg_mul = solver.algebraic_multiplicity(A, eigenvalue)
    print("Algebraic Multiplicity:", alg_mul)

    geo_mul = solver.geometric_multiplicity(A, eigenvalue)
    print("Geometric Multiplicity:", geo_mul)

    eigen_basis = solver.eigen_basis(A, eigenvalue)
    print("Eigenbasis:")
    for vec in eigen_basis:
        print(vec)

except ValueError as e:
    print("\nError:", e)
