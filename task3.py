class Cell:
    def __init__(self, cell=1):
        try:
            self.cell = abs(int(cell))
        except ValueError:
            self.cell = 1

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(sub) if (sub := self.cell - other.cell) > 0 else Cell(1)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(int(self.cell / other.cell))

    def __floordiv__(self, other):
        return Cell(int(self.cell / other.cell))

    def make_order(self, row=10):
        try:
            row = abs(int(row))
        except ValueError:
            row = 10
        cells = f'cell({self.cell}), order = {row}:\n'
        for i in range(1, self.cell + 1):
            cells += '*' if i % row else '*\n'
        return cells


cell1 = Cell(12)
cell2 = Cell(42)

print('cell1 + cell2 =', (cell1 + cell2).make_order())
print('cell2 - cell1 =', (cell2 - cell1).make_order(-15.5))
print('cell1 * cell2 =', (cell1 * cell2).make_order(200))
print('cell2 / cell1 =', (cell2 // cell1).make_order(5))
