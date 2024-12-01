class SubspaceComparer:
    @staticmethod
    def is_span_equal(S1, S2):
        """
        Check if two sets of vectors S1 and S2 span the same subspace.

        Args:
        S1 (list of lists): First set of vectors.
        S2 (list of lists): Second set of vectors.

        Returns:
        bool: True if S1 and S2 span the same subspace, False otherwise.
        """
        def is_in_span(S, v):
            """
            Check if a vector v is in the span of a set of vectors S.
            """
            rows = len(S)
            cols = len(S[0])

           
            if len(v) != rows:
                return False

         
            augmented_matrix = [row[:] for row in S]
            augmented_matrix.append(v)

        
            rank_S = SubspaceComparer.rank(S)
            rank_augmented = SubspaceComparer.rank(augmented_matrix)

            return rank_S == rank_augmented

    
        for v in S1:
            if not is_in_span(S2, v):
                return False

    
        for v in S2:
            if not is_in_span(S1, v):
                return False

        return True

    @staticmethod
    def rank(matrix):
        """
        Compute the rank of a matrix using row reduction.

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        int: The rank of the matrix.
        """
        matrix_copy = [row[:] for row in matrix]
        rows = len(matrix_copy)
        cols = len(matrix_copy[0])

        for pivot_col in range(cols):
            pivot_row = -1
            for row_idx in range(pivot_col, rows):
                if abs(matrix_copy[row_idx][pivot_col]) > 1e-10:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

            if pivot_row != pivot_col:
                matrix_copy[pivot_row], matrix_copy[pivot_col] = (
                    matrix_copy[pivot_col],
                    matrix_copy[pivot_row],
                )

            pivot_value = matrix_copy[pivot_col][pivot_col]
            for col_idx in range(cols):
                matrix_copy[pivot_col][col_idx] /= pivot_value

            for row_idx in range(rows):
                if row_idx != pivot_col and abs(matrix_copy[row_idx][pivot_col]) > 1e-10:
                    factor = matrix_copy[row_idx][pivot_col]
                    for col_idx in range(cols):
                        matrix_copy[row_idx][col_idx] -= factor * matrix_copy[pivot_col][col_idx]

    
        non_zero_rows = 0
        for row in matrix_copy:
            if any(abs(value) > 1e-10 for value in row):
                non_zero_rows += 1

        return non_zero_rows


# Example:
S1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

S2 = [
    [1, 0, -1],
    [0, 1, 1],
    [1, 1, 0]
]

try:
    comparer = SubspaceComparer()
    are_equal = comparer.is_span_equal(S1, S2)

    print("Do S1 and S2 span the same subspace?")
    print("Yes" if are_equal else "No")

except ValueError as e:
    print("\nError:", e)
