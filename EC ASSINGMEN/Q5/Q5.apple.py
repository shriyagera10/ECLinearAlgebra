class MatrixInverse:
    @staticmethod
    def is_square(matrix):
        """
        Check if the matrix is square.

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        bool: True if the matrix is square, False otherwise.
        """
        return len(matrix) == len(matrix[0])

    @staticmethod
    def augment_with_identity(matrix):
        """
        Augment the matrix with the identity matrix of the same size.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        list of lists: The augmented matrix [A | I].
        """
        n = len(matrix)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return [row + identity_row for row, identity_row in zip(matrix, identity)]

    @staticmethod
    def row_reduce_to_inverse(augmented_matrix):
        """
        Perform row reduction to find the inverse of a matrix.

        Args:
        augmented_matrix (list of lists): The augmented matrix [A | I].

        Returns:
        list of lists: The inverse matrix if invertible, else None.
        """
        n = len(augmented_matrix)

        for pivot_col in range(n):
          
            pivot_row = -1
            for row_idx in range(pivot_col, n):
                if augmented_matrix[row_idx][pivot_col] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                return None  

          
            if pivot_row != pivot_col:
                augmented_matrix[pivot_row], augmented_matrix[pivot_col] = (
                    augmented_matrix[pivot_col],
                    augmented_matrix[pivot_row],
                )

            
            pivot_value = augmented_matrix[pivot_col][pivot_col]
            for col_idx in range(2 * n):
                augmented_matrix[pivot_col][col_idx] /= pivot_value

           
            for row_idx in range(n):
                if row_idx != pivot_col:
                    factor = augmented_matrix[row_idx][pivot_col]
                    for col_idx in range(2 * n):
                        augmented_matrix[row_idx][col_idx] -= factor * augmented_matrix[pivot_col][col_idx]

      
        inverse_matrix = [row[n:] for row in augmented_matrix]
        return inverse_matrix

    @staticmethod
    def inverse(matrix):
        """
        Compute the inverse of a square matrix by row reduction.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        list of lists: The inverse matrix if invertible, else None.
        """
        if not MatrixInverse.is_square(matrix):
            raise ValueError("The matrix is not square and cannot be inverted.")

        augmented_matrix = MatrixInverse.augment_with_identity(matrix)
        inverse_matrix = MatrixInverse.row_reduce_to_inverse(augmented_matrix)

        if inverse_matrix is None:
            print("The matrix is not invertible.")
            return None

        return inverse_matrix


# Example: 
A = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
]

try:
    inverse = MatrixInverse.inverse(A)
    if inverse:
        print("Inverse of the matrix:")
        for row in inverse:
            print(row)

except ValueError as e:
    print("\nError:", e)
