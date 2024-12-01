class BasisCoordinate:
    @staticmethod
    def compute_coordinates(B, v):
        """
        Compute the coordinates of a vector v with respect to an ordered basis B.

        Args:
        B (list of lists): Basis vectors as rows in a matrix.
        v (list): The vector whose coordinates are to be computed.

        Returns:
        list: Coordinates of v in the basis B.

        Raises:
        ValueError: If v does not lie in the span of B.
        """
        rows = len(B)
        cols = len(B[0])

     
        if len(v) != rows:
            raise ValueError("The dimensions of vector v must match the rows of B.")

      
        augmented_matrix = [row[:] for row in B]
        augmented_matrix.append(v)

        rref_matrix = BasisCoordinate.row_reduce_to_rref(augmented_matrix)

    
        for row in rref_matrix[len(B):]:
            if any(abs(value) > 1e-10 for value in row[:-1]) and abs(row[-1]) > 1e-10:
                raise ValueError("The vector v does not lie in the span of the basis B.")

    
        coordinates = [0] * cols
        for row_idx in range(rows):
            for col_idx in range(cols):
                if abs(rref_matrix[row_idx][col_idx]) > 1e-10:
                    coordinates[col_idx] = rref_matrix[row_idx][-1]
                    break

        return coordinates

    @staticmethod
    def reconstruct_vector(B, coordinates):
        """
        Reconstruct a vector from its coordinates in the basis B.

        Args:
        B (list of lists): Basis vectors as rows in a matrix.
        coordinates (list): Coordinates of the vector in the basis B.

        Returns:
        list: The reconstructed vector.
        """
        if len(B[0]) != len(coordinates):
            raise ValueError("The number of coordinates must match the number of basis vectors.")

        vector = [0] * len(B)
        for i, basis_vector in enumerate(B):
            for j, coordinate in enumerate(coordinates):
                vector[i] += basis_vector[j] * coordinate

        return vector

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
B = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
v = [2, 3, 4]

try:
  
    finder = BasisCoordinate()
    coordinates = finder.compute_coordinates(B, v)
    print("Coordinates of v in basis B:")
    print(coordinates)

    
    reconstructed_vector = finder.reconstruct_vector(B, coordinates)
    print("\nReconstructed vector from coordinates:")
    print(reconstructed_vector)

except ValueError as e:
    print("\nError:", e)
