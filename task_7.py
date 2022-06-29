class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f"{self.a} + {self.b}*i"


firth = ComplexNumber(2, 1)
sec = ComplexNumber(3, 4)
print(firth + sec)
print(firth * sec)
