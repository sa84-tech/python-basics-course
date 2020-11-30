class Road:
    def __init__(self, length=0, width=0):
        try:
            self._length = abs(float(length))
            self._width = abs(float(width))
        except ValueError:
            self._length = 0
            self._width = 0

    def get_mass(self):
        return self._length * self._width * 25 * 5 / 1000


r = Road(input('Введите длину дороги: '), input('Введите ширину дороги: '))
print('Масса асфальта составит:', m, 'т') if (m := r.get_mass()) else print('Некорректные данные')
