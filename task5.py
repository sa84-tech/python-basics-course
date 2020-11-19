def is_decimal(s):
    """
    Проверяет, является ли переданный аргумент вещественным числом
    :param s:str
    :return:bool
    """
    try:
        float(s)
    except ValueError:
        return False
    return True


total = 0.0
proceed = True
while proceed:
    current_sum = 0.0
    answer = input('Введите строку чисел через пробел (q для выхода): ').split()
    for el in answer:
        if el == 'q':
            proceed = False
            continue  # break, если не нужно считать числа в тек. строке после q
        if is_decimal(el):
            current_sum += float(el)
    total += current_sum
    print(f'{current_sum} ({total})')
