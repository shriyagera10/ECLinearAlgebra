class BasisChange:
    @staticmethod
    def change_coordinates(v_coords_B1, B1, B2):
        """
        Compute the coordinates of a vector in basis B2 given its coordinates in basis B1.

        Args:
        v_coords_B1 (list): Coordinates of the vector in basis B1.
        B1 (list of lists): First basis vectors as rows in a matrix.
        B2 (list of lists): Second basis vectors as rows in a matrix.

        Returns:
        list: Coordinates of the vector in basis B2.

        Raises:
        ValueError: If dimensions mismatch or bases do not span the same space.
        """
    
        T_B1_to_B2 = BasisChange.change_of_basis_matrix(B1, B2)

        v_coords_B2 = [
            sum(T_B1_to_B2[row_idx][col_idx] * v_coords_B1[col_idx] for col_idx in range(len(v_coords_B1)))
            for row_idx in range(len(T_B1_to_B2))
        ]

        return v_coords_B2

    @staticmethod
    def change_of_basis_matrix(B1, B2):
        """
        Calculate the change of basis matrix from B1 to B2.

        Args:
        B1 (list of lists): First basis vectors as rows in a matrix.
        B2 (list of lists): Second basis vectors as rows in a matrix.

        Returns:
        list of lists: Change of basis matrix from B1 to B2.
        """
        n = len(B1)

     
        if len(B1[0]) != n or len(B2[0]) != n:
            raise ValueError("Both bases must span the same space and have the same dimensions.")

    
        cob_matrix = []
        for v in B2:
            coordinates = BasisChange.compute_coordinates(B1, v)
            cob_matrix.append(coordinates)

        cob_matrix_transposed = [[cob_matrix[j][i] for j in range(len(cob_matrix))] for i in range(len(cob_matrix[0]))]
        return cob_matrix_transposed

    @staticmethod
    def compute_coordinates(B, v):
        """
        Find the coordinates of a vector v in the basis B.

        Args:
        B (list of lists): Basis vectors as rows in a matrix.
        v (list): Vector to express in the basis.

        Returns:
        list: Coordinates of v in the basis B.
        """
        n = len(B)

      
        augmented_matrix = [row[:] for row in B]
        augmented_matrix.append(v)

        rref_matrix = BasisChange.row_reduce_to_rref(augmented_matrix)

     
        coordinates = [0] * n
        for row_idx in range(n):
            for col_idx in range(len(B[0])):
                if abs(rref_matrix[row_idx][col_idx]) > 1e-10:
                    coordinates[col_idx] = rref_matrix[row_idx][-1]
                    break

        return coordinates

    @staticmethod
    def row_reduce_to_rref(matrix):
        """
        Perform row reduction to bring a matrix to reduced row echelon form (RREF).

        Args:
        matrix (list of lists): The input matrix.

        Returns:
        list of lists: The matrix in RREF.
        """
        matrix_copy = [row[:] for row in matrix]
        rows = len(matrix_copy)
        cols = len(matrix_copy[0])

        for pivot_col in range(cols - 1):
            pivot_row = -1
            for row_idx in range(pivot_col, rows):
                if abs(matrix_copy[row_idx][pivot_col]) > 1e-10:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

            if pivot_row != pivot_col:
                matrix_copy[pivot_row], matrix_copy[pivot_col] = (
                    matrix_copy[pivot_col],
                    matrix_copy[pivot_row],
                )

            pivot_value = matrix_copy[pivot_col][pivot_col]
            for col_idx in range(cols):
                matrix_copy[pivot_col][col_idx] /= pivot_value

            for row_idx in range(rows):
                if row_idx != pivot_col and abs(matrix_copy[row_idx][pivot_col]) > 1e-10:
                    factor = matrix_copy[row_idx][pivot_col]
                    for col_idx in range(cols):
                        matrix_copy[row_idx][col_idx] -= factor * matrix_copy[pivot_col][col_idx]

        return matrix_copy


# Example:
B1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
B2 = [
    [2, 1, 0],
    [1, 3, 0],
    [0, 0, 1]
]
v_coords_B1 = [3, 2, 1]

try:
    basis_changer = BasisChange()
    v_coords_B2 = basis_changer.change_coordinates(v_coords_B1, B1, B2)

    print("Coordinates of v in basis B2:")
    print(v_coords_B2)

except ValueError as e:
    print("\nError:", e)
