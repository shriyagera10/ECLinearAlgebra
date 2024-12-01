class SubspaceChecker:
    @staticmethod
    def is_subspace(S1, S2):
        """
        Check if the span of S1 is a subspace of the span of S2.

        Args:
        S1 (list of lists): Set of vectors defining the first span.
        S2 (list of lists): Set of vectors defining the second span.

        Returns:
        bool: True if the span of S1 is a subspace of the span of S2, False otherwise.
        """
     
        matrix = [vec[:] for vec in S2]
        rows = len(matrix)
        cols = len(matrix[0])

        for vec in S1:
            
            if len(vec) != cols:
                raise ValueError("Vector dimensions in S1 and S2 must match.")

          
            augmented_matrix = [row[:] for row in matrix]
            augmented_matrix.append(vec)

          
            rank_original = SubspaceChecker.rank(matrix)
            rank_augmented = SubspaceChecker.rank(augmented_matrix)

            if rank_original != rank_augmented:
                return False

        return True

    @staticmethod
    def rank(matrix):
        """
        Compute the rank of a matrix by row reduction.

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        int: The rank of the matrix.
        """
        matrix_copy = [row[:] for row in matrix]
        rows = len(matrix_copy)
        cols = len(matrix_copy[0]) if rows > 0 else 0

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


        non_zero_rows = 0
        for row in matrix_copy:
            if any(value != 0 for value in row):
                non_zero_rows += 1

        return non_zero_rows


# Example: 
try:
    S1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    S2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    checker = SubspaceChecker()
    is_subspace = checker.is_subspace(S1, S2)

    print("Is the span of S1 a subspace of the span of S2?")
    print("Yes" if is_subspace else "No")

except ValueError as e:
    print("\nError:", e)
