class MatrixInverseAdjoint:
    @staticmethod
    def determinant(matrix):
        """
        Compute the determinant of a square matrix recursively.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        float: The determinant of the matrix.
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for col in range(n):
            sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * MatrixInverseAdjoint.determinant(sub_matrix)
        return det

    @staticmethod
    def cofactor(matrix, row, col):
        """
        Compute the cofactor of an element in the matrix.

        Args:
        matrix (list of lists): The input square matrix.
        row (int): The row of the element.
        col (int): The column of the element.

        Returns:
        float: The cofactor of the element.
        """
        sub_matrix = [
            [matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(len(matrix)) if i != row
        ]
        return ((-1) ** (row + col)) * MatrixInverseAdjoint.determinant(sub_matrix)

    @staticmethod
    def adjoint(matrix):
        """
        Compute the adjoint of a square matrix.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        list of lists: The adjoint of the matrix.
        """
        n = len(matrix)
        adj = [[MatrixInverseAdjoint.cofactor(matrix, i, j) for i in range(n)] for j in range(n)]
        return adj

    @staticmethod
    def inverse_using_adjoint(matrix):
        """
        Compute the inverse of a square matrix using the adjoint method.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        list of lists: The inverse matrix if invertible, else None.
        """
        n = len(matrix)

      
        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix is not square and cannot be inverted.")

        det = MatrixInverseAdjoint.determinant(matrix)
        if det == 0:
            print("The matrix is not invertible.")
            return None

        adj = MatrixInverseAdjoint.adjoint(matrix)
        inverse = [[adj[i][j] / det for j in range(n)] for i in range(n)]
        return inverse


# Example: 
A = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
]

try:
    inverse = MatrixInverseAdjoint.inverse_using_adjoint(A)
    if inverse:
        print("Inverse of the matrix (using adjoint method):")
        for row in inverse:
            print(row)

except ValueError as e:
    print("\nError:", e)
