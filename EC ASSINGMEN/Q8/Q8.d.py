class QRFactorization:
    @staticmethod
    def qr_factorization(A):
        """
        Perform QR factorization of a given matrix A.

        Args:
        A (list of lists): The input matrix.

        Returns:
        tuple: Q (orthogonal matrix) and R (upper triangular matrix).

        Raises:
        ValueError: If the matrix is empty or if rows have inconsistent lengths.
        """
        def inner_product(v1, v2):
            """Compute the inner product of two vectors."""
            return sum(v1[i] * v2[i] for i in range(len(v1)))

        def scalar_multiply(scalar, vector):
            """Multiply a vector by a scalar."""
            return [scalar * x for x in vector]

        def vector_add(v1, v2):
            """Add two vectors."""
            return [v1[i] + v2[i] for i in range(len(v1))]

        def vector_subtract(v1, v2):
            """Subtract one vector from another."""
            return [v1[i] - v2[i] for i in range(len(v1))]

        def vector_norm(v):
            """Compute the norm of a vector."""
            return sum(x ** 2 for x in v) ** 0.5

        rows = len(A)
        cols = len(A[0])

        if any(len(row) != cols for row in A):
            raise ValueError("All rows in the matrix must have the same length.")

        Q = [[0] * rows for _ in range(cols)]  
        R = [[0] * cols for _ in range(cols)]

        for i in range(cols):
            
            v = [A[row][i] for row in range(rows)]

            
            for j in range(i):
                q_j = [Q[j][row] for row in range(rows)]
                R[j][i] = inner_product(q_j, v)
                v = vector_subtract(v, scalar_multiply(R[j][i], q_j))

            
            R[i][i] = vector_norm(v)
            if R[i][i] == 0:
                raise ValueError("The matrix has linearly dependent columns; QR factorization is not possible.")
            Q[i] = [v[row] / R[i][i] for row in range(rows)]

      
        Q_transposed = [[Q[col][row] for col in range(cols)] for row in range(rows)]

        return Q_transposed, R


# Example:
A = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

try:
    qr = QRFactorization()
    Q, R = qr.qr_factorization(A)

    print("Matrix Q (Orthogonal):")
    for row in Q:
        print(row)

    print("\nMatrix R (Upper Triangular):")
    for row in R:
        print(row)

except ValueError as e:
    print("\nError:", e)
