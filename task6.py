a = float(input('Спортсмен, сколько километров вы смогли пробежать в первый день тренировок? '))
b = float(input('Укажите вашу цель в километрах: '))
index = 0
days = ''

print('\nГрафик тренировок:')

while True:
    if a >= b:
        index += 1
        print(f'{index}-й день: {a:.2f} км')
        break
    index += 1
    print(f'{index}-й день: {a:.2f} км')
    a += a * 0.1

index_ending = index % 10

if index_ending == 1:
    days = 'день'
elif index_ending == 0 or index_ending > 4:
    days = 'дней'
else:
    days = 'дня'

print(f'При ежедневной тренировке, вы достигните цели за {index} {days}')
