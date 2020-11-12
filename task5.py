proceeds = float(input('Укажите  сумму выручки вашей фирмы за отчетный период: '))
costs = float(input('Укажите сумму издержек вашей фирмы за отчетный период: '))

if proceeds > costs:
    emp_number = int(input('Сколько сотрудников работает в вашей фирме? '))
    profit = proceeds - costs
    print(f'Ваша фирма приносит доход. За отчетный период прибыль составила {profit:.2f}')
    print(f'Прибыль в пересчете на одного сотрудника: {profit / emp_number:.2f}')

elif proceeds < costs:
    print('Ваша фирма работает в убыток.')

else:
    print('Расходы равны доходам ')
