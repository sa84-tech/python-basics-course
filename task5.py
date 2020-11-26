def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


file_name = 'txt/text_5.txt'
number_str = '4 345 345 4545 454454 4545 454545 ert ... 454 54 343 3.34 4.0 34343.4434\n 3434'
number_sum = 0

try:
    out_f = open(file_name, 'w', encoding='UTF-8')
    out_f.write(number_str)
    print(f'Данные успешно записаны в файл {file_name}:')
except IOError:
    print('I/O Error')
finally:
    out_f.close()

try:
    f = open(file_name, 'r')
    data = f.read().split()
except IOError:
    print('I/O Error')
finally:
    f.close()

print('Общая сумма чисел:', sum([float(el) for el in data if is_decimal(el)]))
