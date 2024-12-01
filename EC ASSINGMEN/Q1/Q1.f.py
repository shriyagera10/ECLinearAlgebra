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

    def get_row(self, row_idx):
        """
        Returns a specific row of the matrix as a 1xN matrix.
        """
        if row_idx < 0 or row_idx >= self.rows:
            raise IndexError(f"Row index {row_idx} out of range.")
        return Matrix(self.field_type, 1, self.cols, self.data[row_idx])

    def get_column(self, col_idx):
        """
        Returns a specific column of the matrix as an Nx1 matrix.
        """
        if col_idx < 0 or col_idx >= self.cols:
            raise IndexError(f"Column index {col_idx} out of range.")
        column_elements = [self.data[row_idx][col_idx] for row_idx in range(self.rows)]
        return Matrix(self.field_type, self.rows, 1, column_elements)

    def multiply(self, other_matrix):
        """
        Multiplies the matrix with another matrix.
        """
        if not isinstance(other_matrix, Matrix):
            raise TypeError("Multiplication requires another Matrix instance.")
        if self.cols != other_matrix.rows:
            raise ValueError(f"Multiplication not allowed: Dimensions {self.rows}x{self.cols} and {other_matrix.rows}x{other_matrix.cols} are incompatible.")
        if self.field_type != other_matrix.field_type:
            raise TypeError(f"Multiplication not allowed: Field types {self.field_type.__name__} and {other_matrix.field_type.__name__} do not match.")

        result_elements = []
        for row_idx in range(self.rows):
            for col_idx in range(other_matrix.cols):
                element = sum(self.data[row_idx][k] * other_matrix.data[k][col_idx] for k in range(self.cols))
                result_elements.append(element)
        return Matrix(self.field_type, self.rows, other_matrix.cols, result_elements)


# Example: Initialize a matrix
example_matrix = Matrix(float, 3, 3, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

print("Matrix:")
print(example_matrix)

# Example: Retrieve a specific row
print("\nRow 1 (0-indexed):")
row_1 = example_matrix.get_row(1)
print(row_1)

# Example: Retrieve a specific column
print("\nColumn 2 (0-indexed):")
column_2 = example_matrix.get_column(2)
print(column_2)

# Example: Matrix multiplication example
multiplicand = Matrix(float, 3, 1, [1.0, 0.0, -1.0])
print("\nMultiplying matrix by a 3x1 column vector:")
result = example_matrix.multiply(multiplicand)
print(result)
