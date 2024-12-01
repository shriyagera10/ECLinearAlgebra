class LinAl:
    @staticmethod
    def rref(matrix, show_steps=False):
        """
        Compute the Reduced Row Echelon Form (RREF) of a matrix.
        Optionally display all row operations and corresponding elementary matrices.

        Args:
        matrix (list of lists): The input matrix.
        show_steps (bool): If True, display row operations and elementary matrices.

        Returns:
        list of lists: The matrix in RREF.
        """
        def identity_matrix(size):
            """
            Create an identity matrix of given size.
            """
            return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

        def swap_rows(mat, i, j):
            """
            Swap rows i and j in the matrix.
            """
            mat[i], mat[j] = mat[j], mat[i]

        def scale_row(mat, row_idx, scalar):
            """
            Scale row `row_idx` of the matrix by a scalar.
            """
            mat[row_idx] = [x * scalar for x in mat[row_idx]]

        def add_scaled_row(mat, target_row, source_row, scale):
            """
            Add a scaled version of `source_row` to `target_row`.
            """
            mat[target_row] = [
                x + y * scale for x, y in zip(mat[target_row], mat[source_row])
            ]

        rows, cols = len(matrix), len(matrix[0])
        rref_matrix = [row[:] for row in matrix]  
        elementary_matrices = []

        for col_idx in range(cols):
            
            pivot_row = None
            for row_idx in range(col_idx, rows):
                if rref_matrix[row_idx][col_idx] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row is None:
                continue

            if pivot_row != col_idx:
                swap_rows(rref_matrix, col_idx, pivot_row)
                elem_matrix = identity_matrix(rows)
                swap_rows(elem_matrix, col_idx, pivot_row)
                elementary_matrices.append(elem_matrix)

           
            pivot_value = rref_matrix[col_idx][col_idx]
            if pivot_value != 1:
                scale_row(rref_matrix, col_idx, 1 / pivot_value)
                elem_matrix = identity_matrix(rows)
                elem_matrix[col_idx][col_idx] = 1 / pivot_value
                elementary_matrices.append(elem_matrix)

          
            for row_idx in range(rows):
                if row_idx != col_idx and rref_matrix[row_idx][col_idx] != 0:
                    scale = -rref_matrix[row_idx][col_idx]
                    add_scaled_row(rref_matrix, row_idx, col_idx, scale)
                    elem_matrix = identity_matrix(rows)
                    elem_matrix[row_idx][col_idx] = scale
                    elementary_matrices.append(elem_matrix)

        if show_steps:
            print("Steps and Elementary Matrices:")
            for step, elem_matrix in enumerate(elementary_matrices, start=1):
                print(f"\nStep {step}:")
                for row in elem_matrix:
                    print(row)

        return rref_matrix


# Example:
matrix_example = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

print("Original Matrix:")
for row in matrix_example:
    print(row)

print("\nRREF of Matrix with Steps:")
rref_result = LinAl.rref(matrix_example, show_steps=True)

print("\nReduced Row Echelon Form:")
for row in rref_result:
    print(row)
