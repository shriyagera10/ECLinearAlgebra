class DeterminantRREF:
    @staticmethod
    def determinant(matrix):
        """
        Compute the determinant of a square matrix using elementary matrices in RREF.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        float: The determinant of the matrix.

        Raises:
        ValueError: If the matrix is not square or singular.
        """
        n = len(matrix)

   
        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix must be square.")

        matrix_copy = [row[:] for row in matrix]
        num_swaps = 0
        scaling_factor = 1

        for pivot_col in range(n):
       
            pivot_row = -1
            for row_idx in range(pivot_col, n):
                if abs(matrix_copy[row_idx][pivot_col]) > 1e-10:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                return 0  

           
            if pivot_row != pivot_col:
                matrix_copy[pivot_row], matrix_copy[pivot_col] = (
                    matrix_copy[pivot_col],
                    matrix_copy[pivot_row],
                )
                num_swaps += 1

          
            pivot_value = matrix_copy[pivot_col][pivot_col]
            scaling_factor *= pivot_value
            for col_idx in range(n):
                matrix_copy[pivot_col][col_idx] /= pivot_value

          
            for row_idx in range(pivot_col + 1, n):
                factor = matrix_copy[row_idx][pivot_col]
                for col_idx in range(n):
                    matrix_copy[row_idx][col_idx] -= factor * matrix_copy[pivot_col][col_idx]

        determinant = (-1) ** num_swaps * scaling_factor
        for i in range(n):
            determinant *= matrix_copy[i][i]

        return determinant


# Example:
A = [
    [3, 2, -1],
    [2, -2, 4],
    [-1, 0.5, -1]
]

try:
    det = DeterminantRREF.determinant(A)
    print("Determinant of the matrix (using RREF and elementary operations):")
    print(det)

except ValueError as e:
    print("\nError:", e)
