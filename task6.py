# pip install PrettyTable
import uuid
from prettytable import PrettyTable
import pickle

from equipment import Printer, Scanner, Copier
from storage import Storage

try:
    with open("storage.pkl", "rb") as fp:
        storage = pickle.load(fp)
except (FileNotFoundError, EOFError):
    storage = Storage('Центральный')

print(storage)

while True:
    main_menu1 = PrettyTable(['(1) Принять оборудование', '(2) Отгрузить оборудование', '(3) Отчеты', '(4) Выход'])
    main_menu = 'Главное меню.\n(1) Принять оборудование | ' \
                '(2) Отгрузить оборудование | (3) Отчеты | (4) Выход'
    report_menu = '\nОтчеты.\n(1) Оборудование | (2) Анализ Запасов | ' \
                  '(3) Отгрузка Товаров | (4) Движение ТМЦ | (5) Назад'

    print(main_menu)

    answer = input('Выберете пункт меню: ')

    if answer == '1':
        equipment = []
        answer = '0'
        eq_type = ''
        eq_name = ''

        while eq_type != '1' and eq_type != '2' and eq_type != '3':
            eq_type = input('(1) Принтер | (2) Сканер | (3) Копир\nукажите тип оборудования: ')
        while not eq_name:
            eq_name = input('Введите наименование: ').strip()
        eq_qtty = int(input('Укажите количество: '))

        eq = 0
        if eq_type == '1':
            eq = Printer(eq_name, uuid.uuid1())
        elif eq_type == '2':
            eq = Scanner(eq_name, uuid.uuid1())
        elif eq_type == '3':
            eq = Copier(eq_name, uuid.uuid1())
        for _ in range(eq_qtty):
            equipment.append(eq)
        print(storage.take_equipment(*equipment))

    elif answer == '2':
        pass
    elif answer == '3':
        while True:
            print(report_menu)
            answer = input('Выберете пункт меню: ')
            if answer == '1':
                storage.display_report('qtty_report')
            if answer == '2':
                answer = '0'
                while answer != '2' and answer != '1':
                    print('(1) Общий | (2) Подробный')
                    answer = input('Выберете пункт меню: ')
                storage.display_report('storage_report', True if answer == '2' else False)
            if answer == '3':
                storage.display_report('delivered_equipment_report')
            if answer == '4':
                storage.display_report('movement_report')
            elif answer == '5':
                break
    elif answer == '4':
        print('Выход из программы..')
        break

with open("storage.pkl", "wb") as fp:
    pickle.dump(storage, fp)
