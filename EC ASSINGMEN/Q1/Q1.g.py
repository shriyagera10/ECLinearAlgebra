class Matrix:
    def __init__(self, field_type, rows=None, cols=None, elements=None, column_vectors=None):
        """
        Initialize the matrix.

        Args:
        field_type (type): The type of field (float for real or complex for complex numbers).
        rows (int, optional): The number of rows in the matrix (required if elements are provided).
        cols (int, optional): The number of columns in the matrix (required if elements are provided).
        elements (list, optional): A list of elements to populate the matrix.
        column_vectors (list, optional): A list of column vectors to initialize the matrix.
        """
        if not issubclass(field_type, (float, complex)):
            raise TypeError("Field type must be either float or complex.")

        if column_vectors:
            self.field_type = field_type
            self.rows = len(column_vectors[0])
            self.cols = len(column_vectors)
            if not all(len(vec) == self.rows for vec in column_vectors):
                raise ValueError("All column vectors must have the same length.")
            self.data = [[vec[row_idx] for vec in column_vectors] for row_idx in range(self.rows)]
        elif elements:
            if rows is None or cols is None:
                raise ValueError("Number of rows and columns must be specified when initializing with elements.")
            if len(elements) != rows * cols:
                raise ValueError("Number of elements must match the matrix dimensions.")
            self.field_type = field_type
            self.rows = rows
            self.cols = cols
            self.data = [elements[row_idx * cols:(row_idx + 1) * cols] for row_idx in range(rows)]
        else:
            raise ValueError("Either 'elements' or 'column_vectors' must be provided.")

    def __repr__(self):
        return "\n".join(["[" + " ".join(map(str, row)) + "]" for row in self.data])

    def calculate_transpose(self):
        """
        Returns the transpose of the matrix.
        """
        transposed_elements = [self.data[col_idx][row_idx] for row_idx in range(self.cols) for col_idx in range(self.rows)]
        return Matrix(self.field_type, self.cols, self.rows, transposed_elements)

    def calculate_conjugate(self):
        """
        Returns the conjugate of the matrix (if the matrix contains complex numbers).
        """
        if self.field_type != complex:
            raise TypeError("Conjugate is only applicable to matrices with complex field type.")
        conjugated_elements = [element.conjugate() for row in self.data for element in row]
        return Matrix(self.field_type, self.rows, self.cols, conjugated_elements)

    def calculate_conjugate_transpose(self):
        """
        Returns the conjugate transpose of the matrix.
        """
        if self.field_type != complex:
            raise TypeError("Conjugate transpose is only applicable to matrices with complex field type.")
        transposed_matrix = self.calculate_transpose()
        return transposed_matrix.calculate_conjugate()


# Example: Initialize a complex matrix
complex_matrix = Matrix(complex, 2, 2, [1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])

print("Original Matrix:")
print(complex_matrix)

# Example: Transpose
print("\nTranspose of the Matrix:")
transpose_matrix = complex_matrix.calculate_transpose()
print(transpose_matrix)

# Example: Conjugate
print("\nConjugate of the Matrix:")
conjugate_matrix = complex_matrix.calculate_conjugate()
print(conjugate_matrix)

# Example: Conjugate Transpose
print("\nConjugate Transpose of the Matrix:")
conjugate_transpose_matrix = complex_matrix.calculate_conjugate_transpose()
print(conjugate_transpose_matrix)
