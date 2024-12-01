class Vec:
    def __init__(self, field_type, n, coordinates):
        """
        Initialize the vector.

        Args:
        field_type (type): The type of field (float for real or complex for complex numbers).
        n (int): The length of the vector.
        coordinates (list): A list of n coordinate values.
        """
        if not issubclass(field_type, (float, complex)):
            raise TypeError("Field type must be either float or complex.")
        if len(coordinates) != n:
            raise ValueError("The number of coordinates must match the vector length.")
        if not all(isinstance(coord, field_type) for coord in coordinates):
            raise TypeError(f"All coordinates must be of type {field_type.__name__}.")
        
        self.field_type = field_type
        self.n = n
        self.coordinates = coordinates

    def __repr__(self):
        return f"Vec({self.coordinates})"

    def __add__(self, other):
        if self.n != other.n or self.field_type != other.field_type:
            raise ValueError("Vectors must have the same length and field type for addition.")
        return Vec(self.field_type, self.n, [x + y for x, y in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        if self.n != other.n or self.field_type != other.field_type:
            raise ValueError("Vectors must have the same length and field type for subtraction.")
        return Vec(self.field_type, self.n, [x - y for x, y in zip(self.coordinates, other.coordinates)])

    def __mul__(self, scalar):
        if not isinstance(scalar, self.field_type):
            raise TypeError(f"Scalar must be of type {self.field_type.__name__}.")
        return Vec(self.field_type, self.n, [scalar * x for x in self.coordinates])

    def dot(self, other):
        if self.n != other.n or self.field_type != other.field_type:
            raise ValueError("Vectors must have the same length and field type for dot product.")
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

    def magnitude(self):
        return sum(abs(x) ** 2 for x in self.coordinates) ** 0.5

    def __len__(self):
        return self.n

# Example: Real vector
vec1 = Vec(float, 3, [1.0, 2.0, 3.0])
vec2 = Vec(float, 3, [4.0, 5.0, 6.0])

print("vec1:", vec1)
print("vec2:", vec2)
print("Addition:", vec1 + vec2)
print("Dot product:", vec1.dot(vec2))
print("Magnitude of vec1:", vec1.magnitude())

# Example: Complex vector
vec3 = Vec(complex, 2, [1 + 2j, 3 + 4j])
vec4 = Vec(complex, 2, [5 + 6j, 7 + 8j])

print("vec3:", vec3)
print("vec4:", vec4)
print("Addition:", vec3 + vec4)
print("Dot product:", vec3.dot(vec4))
print("Magnitude of vec3:", vec3.magnitude())
