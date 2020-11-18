def my_func(x, y):
    try:
        if x <= 0 or y >= 0 or not y % 1 == 0:
            print('Некорректные входные данные')
            return
    except TypeError:
        print('Ошибка: неверный тип данных')
        return
    return x ** y


def my_func_2(x, y):
    try:
        if x <= 0 or y >= 0 or not y % 1 == 0:
            print('Некорректные входные данные')
            return
    except TypeError:
        print('Ошибка: неверный тип данных')
        return
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


print(my_func(2, -1))
print(my_func(2, -2))
print(my_func(2, -3))
print(my_func(200, -4))
print(my_func(2, -3.2))

print(my_func_2(2, -1))
print(my_func_2(2, -2))
print(my_func_2(2, -3))
print(my_func_2(200, -4))
print(my_func_2(2, '-3.2'))
