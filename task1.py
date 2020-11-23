from sys import argv


def get_salary(prod, rt, pr):
    try:
        return round(float(prod) * float(rt) + float(pr), 2)
    except ValueError:
        return 'ValueError'


path, production, rate, premium = argv
print(f'Зароботная плата: {get_salary(production, rate, premium)} руб.')
