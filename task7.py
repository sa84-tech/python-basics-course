class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex((self.r * other.r - self.i * other.i), (self.r * other.i + other.r * self.i))

    @property
    def num(self):
        return self.r + self.i * 1j


x = Complex(1, 2)
y = Complex(2, 4)
print(x.num, y.num)

print((x + y).num)
print((x * y).num)
