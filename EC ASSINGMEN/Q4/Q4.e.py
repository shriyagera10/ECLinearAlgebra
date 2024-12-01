class LinearSystemSolution:
    @staticmethod
    def row_reduce_to_rref(augmented_matrix):
        """
        Perform row reduction to bring an augmented matrix to reduced row echelon form (RREF).

        Args:
        augmented_matrix (list of lists): The input augmented matrix [A|b].

        Returns:
        list of lists: The matrix in RREF.
        """
        matrix = [row[:] for row in augmented_matrix]
        rows = len(matrix)
        cols = len(matrix[0])

        for pivot_col in range(cols - 1):
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

    @staticmethod
    def solution_set(matrix, vector):
        """
        Express the solution set of the system AX = b in terms of free variables.

        Args:
        matrix (list of lists): Coefficient matrix A.
        vector (list): Vector b.

        Returns:
        str: The solution set expressed in terms of free variables.
        """
        augmented_matrix = [row + [vector[i]] for i, row in enumerate(matrix)]
        rref_matrix = LinearSystemSolution.row_reduce_to_rref(augmented_matrix)

        rows = len(rref_matrix)
        cols = len(rref_matrix[0]) - 1  
        pivot_columns = []
        free_variables = []

       
        for col_idx in range(cols):
            for row_idx in range(rows):
                if rref_matrix[row_idx][col_idx] != 0:
                    pivot_columns.append(col_idx)
                    break
            else:
                free_variables.append(col_idx)

        
        solutions = ["x{} = 0".format(i + 1) for i in range(cols)]
        for row_idx in range(rows):
            row = rref_matrix[row_idx]
            pivot_col = -1
            for col_idx in range(cols):
                if row[col_idx] != 0:
                    pivot_col = col_idx
                    break
            if pivot_col == -1:
                continue

            rhs = [row[-1]]
            for col_idx in range(cols):
                if col_idx != pivot_col and row[col_idx] != 0:
                    rhs.append("- {:.2f}*x{}".format(row[col_idx], col_idx + 1))
            solutions[pivot_col] = "x{} = {}".format(pivot_col + 1, " + ".join(map(str, rhs)))

        return "\n".join(solutions)


# Example: 
A = [
    [1, 2, -1, 2],
    [2, 4, -1, 6],
    [1, 2, 1, 4]
]
b = [5, 9, 6]

try:
    
    solver = LinearSystemSolution()
    solution = solver.solution_set(A, b)

    print("Solution set expressed in terms of free variables:")
    print(solution)

except ValueError as e:
    print("\nError:", e)
