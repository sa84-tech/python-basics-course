from itertools import count
from itertools import cycle


def get_list(start):
    try:
        start = int(start)
    except ValueError:
        print('Некорректный ввод!')
        return

    it = count(start)
    it_list = []

    for i in range(1, 51):
        it_list.append(next(it))

    iter_list = cycle(it_list)

    for i in range(1, 151):
        if i % 50 == 0:
            print(next(iter_list), end='\n')
        else:
            print(next(iter_list), end=' ')


get_list(input('Укажите целое число: '))
