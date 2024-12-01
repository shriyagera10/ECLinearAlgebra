class InnerProduct:
    @staticmethod
    def inner_product(v1, v2):
        """
        Compute the inner product of two vectors.

        Args:
        v1 (list): The first vector.
        v2 (list): The second vector.

        Returns:
        float: The inner product of v1 and v2.

        Raises:
        ValueError: If the dimensions of v1 and v2 do not match.
        """
        if len(v1) != len(v2):
            raise ValueError("The vectors must have the same dimensions.")

        return sum(v1[i] * v2[i] for i in range(len(v1)))


# Example:
v1 = [1, 2, 3]
v2 = [4, 5, 6]

try:
    calculator = InnerProduct()
    result = calculator.inner_product(v1, v2)
    print("Inner product of v1 and v2:")
    print(result)

except ValueError as e:
    print("\nError:", e)
