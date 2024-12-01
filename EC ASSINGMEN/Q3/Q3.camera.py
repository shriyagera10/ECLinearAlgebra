class LinearDependencyChecker:
    @staticmethod
    def are_vectors_linearly_independent(vectors):
        """
        Check if a set of vectors is linearly independent.

        Args:
        vectors (list of lists): A list of vectors represented as lists.

        Returns:
        bool: True if the vectors are linearly independent, False otherwise.
        """
        
        num_vectors = len(vectors)
        if num_vectors == 0:
            return True  

        vector_length = len(vectors[0])
        for vec in vectors:
            if len(vec) != vector_length:
                raise ValueError("All vectors must have the same length.")

 
        matrix = [vec[:] for vec in vectors]
        rows = len(matrix)
        cols = len(matrix[0])

        for col_idx in range(cols):
    
            pivot_row = -1
            for row_idx in range(col_idx, rows):
                if matrix[row_idx][col_idx] != 0:
                    pivot_row = row_idx
                    break

            if pivot_row == -1:
                continue

          
            if pivot_row != col_idx:
                matrix[pivot_row], matrix[col_idx] = matrix[col_idx], matrix[pivot_row]

          
            pivot_value = matrix[col_idx][col_idx]
            for col in range(cols):
                matrix[col_idx][col] /= pivot_value

           
            for row_idx in range(rows):
                if row_idx != col_idx and matrix[row_idx][col_idx] != 0:
                    factor = matrix[row_idx][col_idx]
                    for col in range(cols):
                        matrix[row_idx][col] -= factor * matrix[col_idx][col]

     
        independent = True
        for row in matrix:
            if all(value == 0 for value in row):
                independent = False
                break

        return independent


# Example: 
vector_set = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

checker = LinearDependencyChecker()

print("Vectors:")
for vector in vector_set:
    print(vector)

is_independent = checker.are_vectors_linearly_independent(vector_set)
print("\nAre the vectors linearly independent?")
print("Yes" if is_independent else "No")
