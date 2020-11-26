_file_name = 'task1.txt'
print('Введите слова через пробел, Enter - новая строка, для выхода - пустая строка')
try:
    out_f = open(_file_name, 'w')

    while True:
        out_str = input('# ')
        if not out_str:
            break
        out_f.write(f'{out_str}\n')

except IOError:
    print('I/O Error')
finally:
    out_f.close()

lines_number = 0
words_number = 0

try:
    f = open(_file_name, 'r')
    for line in f:
        lines_number += 1
        words_number += len(line.split())
    print(f'Данные успешно записаны в файл {_file_name}:')
    print(f'Количество строк - {lines_number}')
    print(f'Количество слов - {words_number}')
except IOError:
    print('I/O Error')
finally:
    f.close()
