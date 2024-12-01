class PLUSolver:
    @staticmethod
    def plu_decomposition(matrix):
        """
        Perform PLU decomposition on a square matrix.

        Args:
        matrix (list of lists): The input square matrix.

        Returns:
        tuple: P, L, U matrices such that A = P * L * U.

        Raises:
        ValueError: If the matrix is not square or is singular.
        """
        n = len(matrix)
        P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        U = [row[:] for row in matrix]

        for i in range(n):
          
            max_row = max(range(i, n), key=lambda r: abs(U[r][i]))
            if U[max_row][i] == 0:
                raise ValueError("Matrix is singular; PLU decomposition not possible.")
            
            if max_row != i:
               
                U[i], U[max_row] = U[max_row], U[i]
               
                P[i], P[max_row] = P[max_row], P[i]
               
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j]

           
            for j in range(i + 1, n):
                L[j][i] = U[j][i] / U[i][i]
                for k in range(i, n):
                    U[j][k] -= L[j][i] * U[i][k]

        return P, L, U

    @staticmethod
    def forward_substitution(L, b):
        """
        Solve Ly = b using forward substitution.

        Args:
        L (list of lists): Lower triangular matrix L.
        b (list): Vector b.

        Returns:
        list: Solution vector y.
        """
        n = len(L)
        y = [0] * n
        for i in range(n):
            y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
        return y

    @staticmethod
    def backward_substitution(U, y):
        """
        Solve Ux = y using backward substitution.

        Args:
        U (list of lists): Upper triangular matrix U.
        y (list): Vector y.

        Returns:
        list: Solution vector x.
        """
        n = len(U)
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
        return x

    @staticmethod
    def solve_plu(matrix, b):
        """
        Solve a consistent system of linear equations AX = b using PLU decomposition.

        Args:
        matrix (list of lists): Coefficient matrix A.
        b (list): Vector b.

        Returns:
        list: Solution vector x.
        """
        P, L, U = PLUSolver.plu_decomposition(matrix)

      
        Pb = [sum(P[i][j] * b[j] for j in range(len(b))) for i in range(len(P))]

       
        y = PLUSolver.forward_substitution(L, Pb)

      
        x = PLUSolver.backward_substitution(U, y)

        return x


# Example:
A = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]
b = [5, -2, 9]

try:
    solver = PLUSolver()
    solution = solver.solve_plu(A, b)

    print("Solution of the system (using PLU decomposition):")
    print(solution)

except ValueError as e:
    print("\nError:", e)
