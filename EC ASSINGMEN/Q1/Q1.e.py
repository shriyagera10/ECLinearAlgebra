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

    def __add__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise TypeError("Addition requires another Matrix instance.")
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError(f"Addition not allowed: Dimensions {self.rows}x{self.cols} and {other_matrix.rows}x{other_matrix.cols} do not match.")
        if self.field_type != other_matrix.field_type:
            raise TypeError(f"Addition not allowed: Field types {self.field_type.__name__} and {other_matrix.field_type.__name__} do not match.")

        summed_elements = [self.data[row_idx][col_idx] + other_matrix.data[row_idx][col_idx]
                           for row_idx in range(self.rows) for col_idx in range(self.cols)]
        return Matrix(self.field_type, self.rows, self.cols, summed_elements)

    def __mul__(self, other):
        if isinstance(other, self.field_type):  # Scalar multiplication
            scaled_elements = [element * other for row in self.data for element in row]
            return Matrix(self.field_type, self.rows, self.cols, scaled_elements)
        elif isinstance(other, Matrix):  # Matrix multiplication
            if self.cols != other.rows:
                raise ValueError(f"Multiplication not allowed: Dimensions {self.rows}x{self.cols} and {other.rows}x{other.cols} are incompatible.")
            if self.field_type != other.field_type:
                raise TypeError(f"Multiplication not allowed: Field types {self.field_type.__name__} and {other.field_type.__name__} do not match.")

            product_elements = []
            for row_idx in range(self.rows):
                for col_idx in range(other.cols):
                    product_elements.append(
                        sum(self.data[row_idx][k] * other.data[k][col_idx] for k in range(self.cols))
                    )
            return Matrix(self.field_type, self.rows, other.cols, product_elements)
        else:
            raise TypeError("Multiplication is only supported with a scalar or another Matrix.")

    def transpose(self):
        transposed_elements = [self.data[col_idx][row_idx] for row_idx in range(self.cols) for col_idx in range(self.rows)]
        return Matrix(self.field_type, self.cols, self.rows, transposed_elements)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.rows, self.cols


# Example: Matrix initialization
mat_a = Matrix(float, 2, 3, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
mat_b = Matrix(float, 2, 3, [7.0, 8.0, 9.0, 10.0, 11.0, 12.0])
mat_c = Matrix(float, 3, 2, [1.0, 4.0, 2.0, 5.0, 3.0, 6.0])

print("Matrix A:")
print(mat_a)
print("\nMatrix B:")
print(mat_b)

# Example: Addition
try:
    print("\nMatrix A + Matrix B:")
    print(mat_a + mat_b)
except (ValueError, TypeError) as e:
    print(e)

# Example: Scalar Multiplication
scalar_value = 2.0
print(f"\nMatrix A multiplied by scalar {scalar_value}:")
print(mat_a * scalar_value)

# Example: Matrix Multiplication
try:
    print("\nMatrix A * Matrix C:")
    print(mat_a * mat_c)
except (ValueError, TypeError) as e:
    print(e)

# Example: Error in Addition
try:
    print("\nAttempting to add Matrix A and Matrix C:")
    print(mat_a + mat_c)
except (ValueError, TypeError) as e:
    print(e)

# Example: Error in Multiplication
try:
    print("\nAttempting to multiply Matrix B and Matrix C:")
    print(mat_b * mat_c)
except (ValueError, TypeError) as e:
    print(e)
