class Orthogonality:
    @staticmethod
    def is_orthogonal(v1, v2):
        """
        Check if two vectors are orthogonal.

        Args:
        v1 (list): The first vector.
        v2 (list): The second vector.

        Returns:
        bool: True if v1 and v2 are orthogonal, False otherwise.

        Raises:
        ValueError: If the dimensions of v1 and v2 do not match.
        """
        if len(v1) != len(v2):
            raise ValueError("The vectors must have the same dimensions.")

        inner_product = sum(v1[i] * v2[i] for i in range(len(v1)))
        return abs(inner_product) < 1e-10 

# Example:
v1 = [1, 0, 0]
v2 = [0, 1, 0]

try:
    checker = Orthogonality()
    result = checker.is_orthogonal(v1, v2)
    print("Are v1 and v2 orthogonal?")
    print("Yes" if result else "No")

except ValueError as e:
    print("\nError:", e)
