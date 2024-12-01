class LinearSpanChecker:
    @staticmethod
    def is_in_linear_span(S, v):
        """
        Check if a vector v is in the linear span of a set of vectors S.

        Args:
        S (list of lists): Set of vectors defining the span.
        v (list): The vector to check.

        Returns:
        bool: True if v is in the linear span of S, False otherwise.
        """
        rows = len(S)
        cols = len(S[0])

       
        if len(v) != rows:
            raise ValueError("The dimensions of vector v must match the rows of S.")

    
        augmented_matrix = [row[:] for row in S]
        augmented_matrix.append(v)

    
        rank_S = LinearSpanChecker.rank(S)
        rank_augmented = LinearSpanChecker.rank(augmented_matrix)

      
        return rank_S == rank_augmented

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
S = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
v = [1, 1, 1]

try:
    checker = LinearSpanChecker()
    is_in_span = checker.is_in_linear_span(S, v)

    print("Is the vector v in the linear span of S?")
    print("Yes" if is_in_span else "No")

except ValueError as e:
    print("\nError:", e)
