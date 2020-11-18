def get_division_result(args):
    try:
        res = float(args[0]) / float(args[1])
    except ZeroDivisionError:
        print('Напоминаю, делить на ноль нельзя!')
        return
    except ValueError:
        print('Некорректные данные')
        return
    return res


nums = input('Введите делимое и делитель через пробел: ').split()
print('Результат: ', get_division_result(nums))
