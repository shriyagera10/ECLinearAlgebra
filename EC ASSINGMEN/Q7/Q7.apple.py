class DeterminantCofactor:
    @staticmethod
    def determinant(matrix):
        """
        Compute the determinant of a square matrix using the cofactor expansion method.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        float: The determinant of the matrix.

        Raises:
        ValueError: If the matrix is not square.
        """
        n = len(matrix)

        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix must be square to compute its determinant.")

        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            cofactor = DeterminantCofactor.get_minor(matrix, 0, col)
            det += ((-1) ** col) * matrix[0][col] * DeterminantCofactor.determinant(cofactor)

        return det

    @staticmethod
    def get_minor(matrix, row, col):
        """
        Get the minor of a matrix by removing the specified row and column.

        Args:
        matrix (list of lists): The input square matrix.
        row (int): The row to remove.
        col (int): The column to remove.

        Returns:
        list of lists: The minor matrix.
        """
        return [row[:col] + row[col + 1:] for i, row in enumerate(matrix) if i != row]


# Example:
A = [
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
]

try:
    det = DeterminantCofactor.determinant(A)
    print("Determinant of the matrix (using cofactor expansion):")
    print(det)

except ValueError as e:
    print("\nError:", e)
