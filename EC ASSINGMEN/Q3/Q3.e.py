class RankFactorization:
    @staticmethod
    def row_reduce(matrix):
        """
        Perform row reduction to bring the matrix to row echelon form.

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        list of lists: Row-reduced matrix (row echelon form).
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        matrix_copy = [row[:] for row in matrix]

        for pivot_col in range(cols):
            pivot_row = -1
            for row_idx in range(pivot_col, rows):
                if matrix_copy[row_idx][pivot_col] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

            if pivot_row != pivot_col:
                matrix_copy[pivot_row], matrix_copy[pivot_col] = matrix_copy[pivot_col], matrix_copy[pivot_row]

            pivot_value = matrix_copy[pivot_col][pivot_col]
            for col_idx in range(cols):
                matrix_copy[pivot_col][col_idx] /= pivot_value

            for row_idx in range(rows):
                if row_idx != pivot_col and matrix_copy[row_idx][pivot_col] != 0:
                    factor = matrix_copy[row_idx][pivot_col]
                    for col_idx in range(cols):
                        matrix_copy[row_idx][col_idx] -= factor * matrix_copy[pivot_col][col_idx]

        return matrix_copy

    @staticmethod
    def rank_factorization(matrix):
        """
        Compute the rank factorization of the given matrix.

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        tuple: Two matrices U and V such that A = U * V.
        """
        # Step 1: Row reduce the matrix
        row_reduced_matrix = RankFactorization.row_reduce(matrix)

        # Step 2: Identify pivot columns (basis for column space)
        pivot_columns = []
        for col_idx in range(len(matrix[0])):
            for row_idx in range(len(row_reduced_matrix)):
                if row_reduced_matrix[row_idx][col_idx] != 0:
                    pivot_columns.append(col_idx)
                    break

        # Step 3: Form U and V
        # U contains columns corresponding to pivot columns from the original matrix
        U = [[matrix[row_idx][col_idx] for col_idx in pivot_columns] for row_idx in range(len(matrix))]

        # V contains rows corresponding to the reduced matrix's pivot rows
        V = [[row[col_idx] for col_idx in range(len(matrix[0]))] for row in row_reduced_matrix if any(row)]

        return U, V


# Example: 
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix_example:
    print(row)

# Computing rank factorization
rank_factorizer = RankFactorization()
U, V = rank_factorizer.rank_factorization(matrix_example)

print("\nMatrix U (Basis for Column Space):")
for row in U:
    print(row)

print("\nMatrix V (Basis for Row Space):")
for row in V:
    print(row)

# Verification
print("\nVerification (U * V):")
reconstructed_matrix = [[sum(U[i][k] * V[k][j] for k in range(len(V))) for j in range(len(V[0]))] for i in range(len(U))]
for row in reconstructed_matrix:
    print(row)
