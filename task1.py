class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m_string = ''
        for m in self.matrix:
            for n in m:
                m_string += f'{n} '
            m_string += '\n'
        return m_string

    def __add__(self, other):
        result = []
        for m in range(len(self.matrix)):
            row = []
            for n in range(len(self.matrix[0])):
                row.append(self.matrix[m][n] + other.matrix[m][n])
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[12, 23, 34], [45, 56, 67], [78, 89, 99]])

matrix2 = Matrix([[99, 88, 77], [66, 55, 44], [33, 22, 12]])

print(f'matrix1:\n{matrix1}')
print(f'matrix2:\n{matrix2}')
print(f'matrix1 + matrix2:\n{matrix1 + matrix2}')

matrix1 = Matrix([[1, -2, 3], [4, 5, -6]])

matrix2 = Matrix([[9, -8, 7], [6, 5, -4]])

print(f'matrix1:\n{matrix1}')
print(f'matrix2:\n{matrix2}')
print(f'matrix1 + matrix2:\n{matrix1 + matrix2}')
