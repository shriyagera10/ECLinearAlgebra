class Mat:
    def __init__(self, field_type, n=None, m=None, entries=None, vectors=None):
        """
        Initialize the matrix.

        Args:
        field_type (type): The type of field (float for real or complex for complex numbers).
        n (int, optional): The number of rows in the matrix (required if entries are provided).
        m (int, optional): The number of columns in the matrix (required if entries are provided).
        entries (list, optional): A list of nm values for the matrix entries.
        vectors (list, optional): A list of m vectors, each of length n, to form the matrix columns.
        """
        if not issubclass(field_type, (float, complex)):
            raise TypeError("Field type must be either float or complex.")

        if vectors is not None:
            # Initialize from column vectors
            self.field_type = field_type
            self.n = len(vectors[0])
            self.m = len(vectors)
            if not all(len(vec) == self.n for vec in vectors):
                raise ValueError("All vectors must have the same length.")
            self.entries = [[vec[i] for vec in vectors] for i in range(self.n)]
        elif entries is not None:
            # Initialize from entries
            if n is None or m is None:
                raise ValueError("Dimensions n and m must be specified when initializing with entries.")
            if len(entries) != n * m:
                raise ValueError("Number of entries must match the dimensions of the matrix.")
            self.field_type = field_type
            self.n = n
            self.m = m
            self.entries = [entries[i * m:(i + 1) * m] for i in range(n)]
        else:
            raise ValueError("Either 'entries' or 'vectors' must be provided for initialization.")

    def __repr__(self):
        return "\n".join(["[" + " ".join(map(str, row)) + "]" for row in self.entries])

    def __add__(self, other):
        if self.n != other.n or self.m != other.m or self.field_type != other.field_type:
            raise ValueError("Matrices must have the same dimensions and field type for addition.")
        new_entries = [self.entries[i][j] + other.entries[i][j]
                       for i in range(self.n) for j in range(self.m)]
        return Mat(self.field_type, self.n, self.m, new_entries)

    def __mul__(self, other):
        if isinstance(other, self.field_type):  # Scalar multiplication
            new_entries = [entry * other for row in self.entries for entry in row]
            return Mat(self.field_type, self.n, self.m, new_entries)
        elif isinstance(other, Mat):  # Matrix multiplication
            if self.m != other.n or self.field_type != other.field_type:
                raise ValueError("Matrix multiplication requires compatible dimensions and field types.")
            result = []
            for i in range(self.n):
                row = []
                for j in range(other.m):
                    row.append(sum(self.entries[i][k] * other.entries[k][j] for k in range(self.m)))
                result.extend(row)
            return Mat(self.field_type, self.n, other.m, result)
        else:
            raise TypeError("Can only multiply matrix by scalar or another matrix.")

    def transpose(self):
        transposed_entries = [self.entries[j][i] for i in range(self.m) for j in range(self.n)]
        return Mat(self.field_type, self.m, self.n, transposed_entries)

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return self.n, self.m


# Example: Initializing matrix using column vectors
vector1 = [1.0, 2.0, 3.0]
vector2 = [4.0, 5.0, 6.0]
vector3 = [7.0, 8.0, 9.0]

mat_from_vectors = Mat(float, vectors=[vector1, vector2, vector3])

print("Matrix from column vectors:")
print(mat_from_vectors)

# Example: Real matrix initialized from entries
mat1 = Mat(float, 3, 3, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
print("\nMatrix initialized from entries:")
print(mat1)

# Example: Addition example
print("\nAddition of two matrices:")
print(mat_from_vectors + mat1)
