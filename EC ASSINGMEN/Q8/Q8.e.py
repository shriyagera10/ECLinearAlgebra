class PseudoInverse:
    @staticmethod
    def pseudo_inverse(S):
        """
        Compute the Moore-Penrose pseudoinverse of a matrix using SVD.

        Args:
        S (list of lists): The input matrix.

        Returns:
        list of lists: The pseudoinverse of the matrix.
        """
        def transpose(matrix):
            """Transpose a matrix."""
            return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        def matrix_multiply(A, B):
            """Multiply two matrices."""
            return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]

        def svd_decomposition(matrix):
            """Perform Singular Value Decomposition (placeholder for actual SVD implementation)."""
            raise NotImplementedError("SVD decomposition needs to be implemented or imported.")

      
        U, Sigma, V_T = svd_decomposition(S)

       
        Sigma_plus = [[0] * len(U) for _ in range(len(V_T))]
        for i in range(len(Sigma)):
            if Sigma[i][i] != 0:
                Sigma_plus[i][i] = 1 / Sigma[i][i]

      
        V = transpose(V_T)
        U_T = transpose(U)
        pseudo_inv = matrix_multiply(matrix_multiply(V, Sigma_plus), U_T)

        return pseudo_inv


# Example:
S = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

try:
    pseudo_inv = PseudoInverse.pseudo_inverse(S)
    print("Moore-Penrose Pseudoinverse of the matrix:")
    for row in pseudo_inv:
        print(row)

except NotImplementedError as e:
    print("\nError:", e)
