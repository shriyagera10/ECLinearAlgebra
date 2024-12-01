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
    def eigen_decomposition(A):
       
        n = len(A)
        eigenvalues = []
        eigenvectors = MatrixDecompositions.identity_matrix(n)

        for _ in range(n):
            vector = [1.0] * n 
            for _ in range(100): 
                next_vector = MatrixDecompositions.multiply_matrices(A, [[v] for v in vector])
                next_vector = [x[0] for x in next_vector]
                norm = sum(x ** 2 for x in next_vector) ** 0.5
                next_vector = [x / norm for x in next_vector]
                vector = next_vector

            eigenvalue = sum(vector[i] * (MatrixDecompositions.multiply_matrices(A, [[v] for v in vector])[i][0]) for i in range(n))
            eigenvalues.append(eigenvalue)

            for i in range(n):
                for j in range(n):
                    A[i][j] -= eigenvalue * vector[i] * vector[j]

        return eigenvalues, eigenvectors

    @staticmethod
    def svd(A):
        
        A_T = MatrixDecompositions.transpose(A)
        ATA = MatrixDecompositions.multiply_matrices(A_T, A)
        AAT = MatrixDecompositions.multiply_matrices(A, A_T)

        eigenvalues_V, V = MatrixDecompositions.eigen_decomposition(ATA)
        eigenvalues_U, U = MatrixDecompositions.eigen_decomposition(AAT)

        singular_values = [eigenvalue ** 0.5 for eigenvalue in eigenvalues_V]
        Sigma = [[0] * len(A[0]) for _ in range(len(A))]
        for i in range(len(singular_values)):
            Sigma[i][i] = singular_values[i]

        return U, Sigma, MatrixDecompositions.transpose(V)


# Example:
A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

try:
    decomposition_solver = MatrixDecompositions()

    U, Sigma, V_T = decomposition_solver.svd(A)

    print("Matrix U:")
    for row in U:
        print(row)

    print("\nMatrix Sigma:")
    for row in Sigma:
        print(row)

    print("\nMatrix V^T:")
    for row in V_T:
        print(row)

except ValueError as e:
    print("\nError:", e)
