class MatrixProperties:
    def __init__(self, matrix):
       
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0

    def is_zero(self):
      
        for row in self.matrix:
            if any(element != 0 for element in row):
                return False
        return True

    def is_symmetric(self):
       
        if self.rows != self.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_hermitian(self):
       
        if self.rows != self.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != self.matrix[j][i].conjugate():
                    return False
        return True

    def is_square(self):
       
        return self.rows == self.cols

    def is_orthogonal(self):
      
        if not self.is_square():
            return False
        identity = [[1 if i == j else 0 for j in range(self.rows)] for i in range(self.rows)]
        transpose = self.transpose()
        product = self.multiply_matrices(self.matrix, transpose)
        return product == identity

    def is_unitary(self):
      
        if not self.is_square():
            return False
        identity = [[1 if i == j else 0 for j in range(self.rows)] for i in range(self.rows)]
        conjugate_transpose = self.conjugate_transpose()
        product = self.multiply_matrices(self.matrix, conjugate_transpose)
        return product == identity

    def is_scalar(self):
       
        if not self.is_square():
            return False
        diagonal_value = self.matrix[0][0]
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j:
                    if self.matrix[i][j] != diagonal_value:
                        return False
                elif self.matrix[i][j] != 0:
                    return False
        return True

    def is_singular(self):
       
        return self.determinant(self.matrix) == 0

    def is_invertible(self):
       
        return not self.is_singular()

    def is_identity(self):
       
        if not self.is_square():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if (i == j and self.matrix[i][j] != 1) or (i != j and self.matrix[i][j] != 0):
                    return False
        return True

    def determinant(self, matrix):
       
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for col in range(len(matrix)):
            sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * self.determinant(sub_matrix)
        return det

    def transpose(self):
       
        return [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]

    def conjugate_transpose(self):
       
        return [[self.matrix[j][i].conjugate() for j in range(self.rows)] for i in range(self.cols)]

    def multiply_matrices(self, mat1, mat2):
       
        result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result


# Example:
matrix_example = [
    [1, 2],
    [2, 1]
]
matrix_checker = MatrixProperties(matrix_example)

print("Matrix:")
for row in matrix_example:
    print(row)

print("\nProperties:")
print(f" zero: {matrix_checker.is_zero()}")
print(f" symmetric: {matrix_checker.is_symmetric()}")
print(f" Hermitian: {matrix_checker.is_hermitian()}")
print(f" square: {matrix_checker.is_square()}")
print(f" orthogonal: {matrix_checker.is_orthogonal()}")
print(f" unitary: {matrix_checker.is_unitary()}")
print(f" scalar: {matrix_checker.is_scalar()}")
print(f" singular: {matrix_checker.is_singular()}")
print(f" invertible: {matrix_checker.is_invertible()}")
print(f" identity: {matrix_checker.is_identity()}")
