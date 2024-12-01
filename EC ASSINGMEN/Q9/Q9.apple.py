import cmath

class PolynomialRoots:
    @staticmethod
    def poly_roots(coefficients, max_iter=100, tolerance=1e-10):
        """
        Find all roots of a polynomial using the Aberth method.

        Args:
        coefficients (list of complex): Coefficients of the polynomial.
        max_iter (int): Maximum number of iterations.
        tolerance (float): Convergence tolerance.

        Returns:
        list: Complex roots of the polynomial.
        """
        degree = len(coefficients) - 1
        if degree <= 0:
            raise ValueError("The polynomial degree must be at least 1.")


        coefficients = [c / coefficients[0] for c in coefficients]

      
        roots = [cmath.exp(2j * cmath.pi * i / degree) for i in range(degree)]

        for _ in range(max_iter):
            new_roots = []
            for i, root in enumerate(roots):
               
                f_value = sum(c * root ** (degree - k) for k, c in enumerate(coefficients))
                f_derivative = sum(
                    (degree - k) * c * root ** (degree - k - 1) for k, c in enumerate(coefficients[:-1])
                )

              
                correction = f_value / f_derivative if f_derivative != 0 else 0
                for j, other_root in enumerate(roots):
                    if i != j:
                        correction /= (root - other_root)
                new_root = root - correction

                new_roots.append(new_root)

         
            if all(abs(new_root - old_root) < tolerance for new_root, old_root in zip(new_roots, roots)):
                return new_roots
            roots = new_roots

        raise ValueError("The method did not converge within the maximum number of iterations.")

# Example:
try:
    print("Input the degree of the polynomial (n):")
    n = int(input())
    print(f"Input the {n+1} complex coefficients of the polynomial:")
    coefficients = [complex(input()) for _ in range(n+1)]

    solver = PolynomialRoots()
    roots = solver.poly_roots(coefficients)

    print("Roots of the polynomial:")
    for root in roots:
        print(root)

except ValueError as e:
    print("\nError:", e)
