class LinearCombinationFinder:
    @staticmethod
    def express_in_span(S, v):
        """
        Find the representation of a vector v as a linear combination of vectors in S.

        Args:
        S (list of lists): Set of vectors defining the span.
        v (list): The vector to represent.

        Returns:
        list: Coefficients representing v as a linear combination of vectors in S.

        Raises:
        ValueError: If v is not in the span of S or if dimensions do not match.
        """
        rows = len(S)
        cols = len(S[0])

      
        if len(v) != rows:
            raise ValueError("The dimensions of vector v must match the rows of S.")

     
        augmented_matrix = [row[:] for row in S]
        augmented_matrix.append(v)

     
        rref_matrix = LinearCombinationFinder.row_reduce_to_rref(augmented_matrix)


        for row in rref_matrix[len(S):]:
            if any(abs(value) > 1e-10 for value in row[:-1]) and abs(row[-1]) > 1e-10:
                raise ValueError("The vector v is not in the span of S.")


        coefficients = [0] * cols
        for row_idx in range(rows):
            for col_idx in range(cols):
                if abs(rref_matrix[row_idx][col_idx]) > 1e-10:
                    coefficients[col_idx] = rref_matrix[row_idx][-1]
                    break

        return coefficients

    @staticmethod
    def row_reduce_to_rref(matrix):
        """
        Perform row reduction to bring a matrix to reduced row echelon form (RREF).

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        list of lists: The matrix in RREF.
        """
        matrix_copy = [row[:] for row in matrix]
        rows = len(matrix_copy)
        cols = len(matrix_copy[0])

        for pivot_col in range(cols - 1):
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

        return matrix_copy


# Example: 
S = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
v = [2, 3, 4]

try:
    finder = LinearCombinationFinder()
    coefficients = finder.express_in_span(S, v)

    print("Representation of vector v as a linear combination of vectors in S:")
    print("v =", " + ".join(f"{coeff}*S{i+1}" for i, coeff in enumerate(coefficients)))

except ValueError as e:
    print("\nError:", e)
