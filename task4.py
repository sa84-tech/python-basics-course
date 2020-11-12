pos_num = int(input('Пользователь, введи целое положительное число: '))
max_num = 0

while pos_num > 0:
    cur_number = pos_num % 10
    pos_num = pos_num // 10

    if max_num < cur_number:
        max_num = cur_number

print('Самая большая цифра в числе:', max_num)

