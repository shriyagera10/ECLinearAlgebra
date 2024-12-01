class GramSchmidt:
    @staticmethod
    def gram_schmidt(S):
        """
        Perform Gram-Schmidt orthogonalisation on a set of vectors.

        Args:
        S (list of lists): Set of vectors.

        Returns:
        list of lists: The orthogonalised set of vectors.

        Raises:
        ValueError: If the input vectors are not linearly independent.
        """
        def inner_product(v1, v2):
            """Compute the inner product of two vectors."""
            return sum(v1[i] * v2[i] for i in range(len(v1)))

        def scalar_multiply(scalar, vector):
            """Multiply a vector by a scalar."""
            return [scalar * x for x in vector]

        def vector_subtract(v1, v2):
            """Subtract one vector from another."""
            return [v1[i] - v2[i] for i in range(len(v1))]

        orthogonal_set = []

        for v in S:
            projection = [0] * len(v)  
            for u in orthogonal_set:
                proj_coeff = inner_product(v, u) / inner_product(u, u)
                projection = vector_subtract(projection, scalar_multiply(proj_coeff, u))
            u = vector_subtract(v, projection)
            if all(abs(x) < 1e-10 for x in u):  
                raise ValueError("The vectors in S are not linearly independent.")
            orthogonal_set.append(u)

        return orthogonal_set


# Example:
S = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

try:
    gram_schmidt = GramSchmidt()
    orthogonal_vectors = gram_schmidt.gram_schmidt(S)

    print("Orthogonalised set of vectors:")
    for vector in orthogonal_vectors:
        print(vector)

except ValueError as e:
    print("\nError:", e)
