class MatrixOperations:
    @staticmethod
    def vector_length(vector):
        """
        Calculate the length (magnitude) of a vector.
        """
        magnitude = 0
        for element in vector:
            magnitude += element ** 2
        return magnitude ** 0.5

    @staticmethod
    def matrix_size(matrix):
        """
        Return the size (rows, columns) of the matrix.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        return num_rows, num_cols

    @staticmethod
    def row_reduce_to_echelon(matrix):
        """
        Perform row reduction to bring a matrix to row echelon form.
        """
        rows = len(matrix)
        cols = len(matrix[0])
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
    def matrix_rank(matrix):
        """
        Calculate the rank of a matrix by counting the non-zero rows in row echelon form.
        """
        echelon_matrix = MatrixOperations.row_reduce_to_echelon(matrix)
        non_zero_rows = 0

        for row in echelon_matrix:
            if any(value != 0 for value in row):
                non_zero_rows += 1

        return non_zero_rows

    @staticmethod
    def matrix_nullity(matrix):
        """
        Calculate the nullity of a matrix (number of columns minus rank).
        """
        rows, cols = len(matrix), len(matrix[0])
        rank = MatrixOperations.matrix_rank(matrix)
        return cols - rank


# Example:
vector_example = [3, 4]
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Example: Vector length
print("Vector:", vector_example)
print("Length of vector:", MatrixOperations.vector_length(vector_example))

# Example: Matrix size
print("\nMatrix:")
for row in matrix_example:
    print(row)
print("Size of matrix:", MatrixOperations.matrix_size(matrix_example))

# Example: Matrix rank
print("Rank of matrix:", MatrixOperations.matrix_rank(matrix_example))

# Example: Matrix nullity
print("Nullity of matrix:", MatrixOperations.matrix_nullity(matrix_example))
