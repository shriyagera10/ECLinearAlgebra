class LinearSystem:
    def __init__(self, matrix, vector):
        """
        Initialize a system of linear equations AX = b.

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

    def __repr__(self):
        """
        Return a string representation of the system of equations.
        """
        representation = "System of Linear Equations:\n"
        for i in range(self.num_rows):
            row_eq = " + ".join(
                f"{self.matrix[i][j]}*x{j+1}" for j in range(self.num_cols)
            )
            representation += f"{row_eq} = {self.vector[i]}\n"
        return representation

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


# Example:
try:
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    
    system = LinearSystem(A, b)
    print(system)

  
    consistent = system.is_consistent()
    print("\nIs the system consistent?")
    print("Yes" if consistent else "No")

except ValueError as e:
    print("\nError:", e)
