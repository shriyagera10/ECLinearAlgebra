class Matrix:
    def __init__(self, field, n, m, values=None):
      
        if field not in {'real', 'complex'}:
            raise ValueError("Field must be 'real' or 'complex'.")
        if n <= 0 or m <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")

        self.field = field
        self.n = n
        self.m = m

        if values:
            if len(values) != n or any(len(row) != m for row in values):
                raise ValueError("Values must match the specified dimensions.")
            self.values = values
        else:
            self.values = [[0.0 if field == 'real' else 0j for _ in range(m)] for _ in range(n)]

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.values])

    def set_entry(self, i, j, value):
       
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            raise IndexError("Indices are out of bounds.")
        if self.field == 'real' and not isinstance(value, (int, float)):
            raise ValueError("Value must be real.")
        if self.field == 'complex' and not isinstance(value, (int, float, complex)):
            raise ValueError("Value must be complex.")
        self.values[i][j] = value

    def get_entry(self, i, j):
       
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            raise IndexError("Indices are out of bounds.")
        return self.values[i][j]


# Example:
try:
    print("Create a real matrix (2x3):")
    real_matrix = Matrix(field='real', n=2, m=3, values=[[1, 2, 3], [4, 5, 6]])
    print(real_matrix)

    print("\nCreate a complex matrix (2x2):")
    complex_matrix = Matrix(field='complex', n=2, m=2, values=[[1+2j, 2-3j], [3+4j, 4-5j]])
    print(complex_matrix)

    print("\nSet an entry in the complex matrix:")
    complex_matrix.set_entry(1, 1, 10+10j)
    print(complex_matrix)

    print("\nGet an entry from the real matrix:")
    print(real_matrix.get_entry(0, 1)) 

except ValueError as e:
    print("\nError:", e)
except IndexError as e:
    print("\nError:", e)
