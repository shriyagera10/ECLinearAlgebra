class SubspaceAnalyzer:
    @staticmethod
    def dimension_of_span(vectors):
        """
        Compute the dimension of the subspace spanned by the given set of vectors.

        Args:
        vectors (list of lists): A list of vectors represented as lists.

        Returns:
        int: The dimension of the subspace spanned by the vectors.
        """
        # Row reduce the matrix formed by the vectors
        row_reduced_matrix = SubspaceAnalyzer.row_reduce(vectors)
        # Count the number of non-zero rows in the row-reduced matrix
        dimension = 0
        for row in row_reduced_matrix:
            if any(value != 0 for value in row):
                dimension += 1
        return dimension

    @staticmethod
    def basis_of_span(vectors):
        """
        Find a basis for the subspace spanned by the given set of vectors.

        Args:
        vectors (list of lists): A list of vectors represented as lists.

        Returns:
        list of lists: A basis for the subspace spanned by the vectors.
        """
        row_reduced_matrix = SubspaceAnalyzer.row_reduce(vectors)
        basis = []
        for row in row_reduced_matrix:
            if any(value != 0 for value in row):
                basis.append(row)
        return basis

    @staticmethod
    def row_reduce(vectors):
        """
        Perform row reduction on the matrix formed by the given vectors.

        Args:
        vectors (list of lists): A list of vectors represented as lists.

        Returns:
        list of lists: The matrix in row echelon form.
        """
        matrix = [vec[:] for vec in vectors]
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        for pivot_col in range(cols):
            pivot_row = -1
            for row_idx in range(pivot_col, rows):
                if matrix[row_idx][pivot_col] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

            if pivot_row != pivot_col:
                matrix[pivot_row], matrix[pivot_col] = matrix[pivot_col], matrix[pivot_row]

            pivot_value = matrix[pivot_col][pivot_col]
            for col_idx in range(cols):
                matrix[pivot_col][col_idx] /= pivot_value

            for row_idx in range(rows):
                if row_idx != pivot_col and matrix[row_idx][pivot_col] != 0:
                    factor = matrix[row_idx][pivot_col]
                    for col_idx in range(cols):
                        matrix[row_idx][col_idx] -= factor * matrix[pivot_col][col_idx]

        return matrix


# Example: 
vector_set = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

analyzer = SubspaceAnalyzer()

print("Vectors:")
for vector in vector_set:
    print(vector)

# Example: Compute the dimension of the subspace
dimension = analyzer.dimension_of_span(vector_set)
print("\nDimension of the subspace spanned by the vectors:", dimension)

# Example: Compute a basis for the subspace
basis = analyzer.basis_of_span(vector_set)
print("\nBasis for the subspace spanned by the vectors:")
for basis_vector in basis:
    print(basis_vector)
