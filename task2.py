class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(div_1, div_2):
    try:
        div_1 = float(div_1)
        div_2 = float(div_2)
        if div_2 == 0:
            raise OwnZeroDivisionError('Деление на ноль!')
    except ValueError:
        print('Вы ввели не число!')
    except OwnZeroDivisionError as err:
        print(err)
    else:
        print('Результат:', div_1 / div_2)


div(2, 0)
div(2, 'asdf')
div(input('Введите делимое: '), input('Введите делитель: '))
