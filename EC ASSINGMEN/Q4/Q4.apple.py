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


# Example: 
try:
    
    A = [
        [2, 1],
        [1, -1]
    ]
    b = [5, -1]

  
    system = LinearSystem(A, b)
    print(system)

except ValueError as e:
    print("Error:", e)
