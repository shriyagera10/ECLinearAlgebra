class MatrixDecompositions:
    @staticmethod
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    @staticmethod
    def multiply_matrices(A, B):
        return [
            [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))
        ]

    @staticmethod
    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    @staticmethod
    def inverse(matrix):
        n = len(matrix)
        identity = MatrixDecompositions.identity_matrix(n)
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
    def matrix_square_root(matrix):
        n = len(matrix)
        identity = MatrixDecompositions.identity_matrix(n)
        current_approx = identity[:]

        for _ in range(20):  
            inv_approx = MatrixDecompositions.inverse(current_approx)
            next_approx = MatrixDecompositions.multiply_matrices(
                MatrixDecompositions.add_matrices(current_approx, inv_approx), 
                MatrixDecompositions.scalar_multiply(identity, 0.5)
            )
            current_approx = next_approx

        return current_approx

    @staticmethod
    def add_matrices(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    @staticmethod
    def scalar_multiply(matrix, scalar):
        return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    @staticmethod
    def polar_decomposition(A):
       
        if len(A) != len(A[0]):
            raise ValueError("Matrix must be square for polar decomposition.")

        A_T = MatrixDecompositions.transpose(A)
        ATA = MatrixDecompositions.multiply_matrices(A_T, A)

        P = MatrixDecompositions.matrix_square_root(ATA)

        P_inv = MatrixDecompositions.inverse(P)
        U = MatrixDecompositions.multiply_matrices(A, P_inv)

        return U, P


# Example:
A = [
    [1, 2],
    [3, 4]
]

try:
    decomposition_solver = MatrixDecompositions()

    U, P = decomposition_solver.polar_decomposition(A)

    print("Unitary Matrix U:")
    for row in U:
        print(row)

    print("\nPositive Semidefinite Matrix P:")
    for row in P:
        print(row)

except ValueError as e:
    print("\nError:", e)
