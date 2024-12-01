class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Division by zero is undefined for complex numbers.")
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def abs(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def cc(self):
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)

    print("c1:", c1)
    print("c2:", c2)
    print("Addition:", c1 + c2)
    print("Multiplication:", c1 * c2)
    print("Division:", c1 / c2)
    print("Absolute value of c1:", c1.abs())
    print("Conjugate of c1:", c1.cc())
