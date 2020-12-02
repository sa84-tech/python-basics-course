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
        other = Matrix(other)
        print(other)
        m_res = []
        row = []
        for m in range(len(self.matrix)):

            for n in range(len(self.matrix[0])):
                row.append(self.matrix[m][n] + other[m][n])
                if len(row) == len(self.matrix):
                    m_res.append(row)
                    row = []
        return Matrix(m_res)


matrix1 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
