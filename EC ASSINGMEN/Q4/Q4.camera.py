class LinearSystemSolver:
    def __init__(self, matrix, vector):
        """
        Initialize the system of linear equations AX = b.

        Args:
        matrix (list of lists): Coefficient matrix A.
        vector (list): Vector b.

        Raises:
        ValueError: If the sizes of the matrix and vector are not compatible.
        """
        self.matrix = matrix
        self.vector = vector

       
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        if len(vector) != num_rows:
            raise ValueError(
                f"Size mismatch: The matrix has {num_rows} rows, but the vector has {len(vector)} elements."
            )

        self.num_rows = num_rows
        self.num_cols = num_cols

    def is_consistent(self):
        """
        Check if the system of linear equations is consistent.

        Returns:
        bool: True if the system is consistent, False otherwise.
        """
        augmented_matrix = [row + [self.vector[idx]] for idx, row in enumerate(self.matrix)]

        rank_a = self.rank(self.matrix)
        rank_augmented = self.rank(augmented_matrix)

        return rank_a == rank_augmented

    def rank(self, matrix):
        """
        Compute the rank of a matrix by performing row reduction.

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

    def solve(self):
        """
        Solve the system of linear equations using Gaussian elimination.

        Returns:
        list: A list of solutions for the variables.

        Raises:
        ValueError: If the system is inconsistent.
        """
        if not self.is_consistent():
            raise ValueError("The system is inconsistent and cannot be solved.")

        augmented_matrix = [row + [self.vector[idx]] for idx, row in enumerate(self.matrix)]
        rows = len(augmented_matrix)
        cols = len(augmented_matrix[0])

        
        for pivot_col in range(cols - 1):
            pivot_row = -1
            for row_idx in range(pivot_col, rows):
                if augmented_matrix[row_idx][pivot_col] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

            if pivot_row != pivot_col:
                augmented_matrix[pivot_row], augmented_matrix[pivot_col] = augmented_matrix[pivot_col], augmented_matrix[pivot_row]

            pivot_value = augmented_matrix[pivot_col][pivot_col]
            for col_idx in range(cols):
                augmented_matrix[pivot_col][col_idx] /= pivot_value

            for row_idx in range(pivot_col + 1, rows):
                factor = augmented_matrix[row_idx][pivot_col]
                for col_idx in range(cols):
                    augmented_matrix[row_idx][col_idx] -= factor * augmented_matrix[pivot_col][col_idx]

        
        solution = [0] * (cols - 1)
        for row_idx in range(rows - 1, -1, -1):
            if all(augmented_matrix[row_idx][col] == 0 for col in range(cols - 1)) and augmented_matrix[row_idx][-1] != 0:
                raise ValueError("The system is inconsistent and cannot be solved.")
            if all(augmented_matrix[row_idx][col] == 0 for col in range(cols)):
                continue
            solution[row_idx] = augmented_matrix[row_idx][-1]
            for col_idx in range(row_idx + 1, cols - 1):
                solution[row_idx] -= augmented_matrix[row_idx][col_idx] * solution[col_idx]

        return solution


# Example:
try:
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    
    solver = LinearSystemSolver(A, b)
    print("System of Linear Equations:")
    for row in A:
        print(row, "|", b)

   
    solution = solver.solve()
    print("\nSolution of the system:")
    print(solution)

except ValueError as e:
    print("\nError:", e)
