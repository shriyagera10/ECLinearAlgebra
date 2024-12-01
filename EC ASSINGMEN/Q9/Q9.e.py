class MatrixDiagonalization:
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
            det += ((-1) ** col) * matrix[0][col] * MatrixDiagonalization.determinant(minor)
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
        rref = MatrixDiagonalization.row_reduce(matrix)
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
    def eigenvalues(A):
        n = len(A)
        identity = MatrixDiagonalization.identity_matrix(n)
        eigenvalues = []

        for i in range(n):
            shifted_matrix = MatrixDiagonalization.subtract_matrices(A, MatrixDiagonalization.scalar_multiply_matrix(identity, i))
            if abs(MatrixDiagonalization.determinant(shifted_matrix)) < 1e-10:
                eigenvalues.append(i)

        return eigenvalues

    @staticmethod
    def eigenvectors(A, eigenvalue):
       
        n = len(A)
        identity = MatrixDiagonalization.identity_matrix(n)
        lambda_identity = MatrixDiagonalization.scalar_multiply_matrix(identity, eigenvalue)
        shifted_matrix = MatrixDiagonalization.subtract_matrices(A, lambda_identity)
        return MatrixDiagonalization.solve_homogeneous_system(shifted_matrix)

    @staticmethod
    def is_diagonalizable(A):
      
        eigenvalues = MatrixDiagonalization.eigenvalues(A)
        dimension = len(A)
        total_geo_multiplicity = 0

        for eigenvalue in eigenvalues:
            geo_multiplicity = len(MatrixDiagonalization.eigenvectors(A, eigenvalue))
            total_geo_multiplicity += geo_multiplicity

        return total_geo_multiplicity == dimension

    @staticmethod
    def change_of_basis_to_diagonal(A):
      
        if not MatrixDiagonalization.is_diagonalizable(A):
            raise ValueError("Matrix is not diagonalizable.")

        eigenvalues = MatrixDiagonalization.eigenvalues(A)
        P = []

        for eigenvalue in eigenvalues:
            eigenvectors = MatrixDiagonalization.eigenvectors(A, eigenvalue)
            P.extend(eigenvectors)

        return P

    @staticmethod
    def scalar_multiply_matrix(matrix, scalar):
        return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]


# Example:
A = [
    [4, 1],
    [2, 3]
]

try:
    diagonalization_solver = MatrixDiagonalization()

    if diagonalization_solver.is_diagonalizable(A):
        P = diagonalization_solver.change_of_basis_to_diagonal(A)
        print("Change of Basis Matrix P (to diagonalize A):")
        for row in P:
            print(row)
    else:
        print("Matrix A is not diagonalizable.")

except ValueError as e:
    print("\nError:", e)
