# pip install PrettyTable
import uuid
import pickle
from prettytable import PrettyTable

from equipment import Printer, Scanner, Copier
from storage import Storage

try:
    with open("storage.pkl", "rb") as fp:
        storage = pickle.load(fp)
except (FileNotFoundError, EOFError):
    storage = Storage('Центральный')

print(storage)


def take_equipment(_storage):
    equipment = []
    eq_type = ''
    eq_name = ''

    while eq_type != '1' and eq_type != '2' and eq_type != '3' and eq_type != '4':
        eq_type = input('(1) Принтер | (2) Сканер | (3) Копир | (4) Отмена\nукажите тип оборудования: ')
    if eq_type == '4':
        return
    while len(eq_name) < 3:
        eq_name = input('Введите наименование: ').strip()
    while True:
        try:
            eq_qtty = int(input('Укажите количество: '))
        except ValueError:
            pass
        else:
            break

    eq = 0
    if eq_type == '1':
        eq = Printer(eq_name, uuid.uuid1())
    elif eq_type == '2':
        eq = Scanner(eq_name, uuid.uuid1())
    elif eq_type == '3':
        eq = Copier(eq_name, uuid.uuid1())
    for _ in range(eq_qtty):
        equipment.append(eq)
    print(_storage.take_equipment(*equipment))
    return


def deliver_equipment(_storage):
    d = {1: 'Принтер', 2: 'Сканер', 3: 'Копир', 4: ''}
    d_menu_item = 0
    eq_list = []
    while d_menu_item < 1 or d_menu_item > 5:

        try:
            d_menu_item = int(input('(1) Принтер | (2) Сканер | (3) Копир | (4) Все | (5) Отмена\n' 
                                    'Укажите тип оборудования: '))
            if d_menu_item == 5:
                return

            _storage.display_equipments_list(d.get(d_menu_item))
            eq_list = _storage.get_equipments_list(eq_type=d.get(d_menu_item), full=True)
            eq_num = int(input('Выберете номер устройства: '))
            eq_to = input('Укажите место установки: ')

        except ValueError:
            d_menu_item = 0
            print('Некоректный ввод')

    equipment = _storage.get_equipment_by_sn(eq_list[eq_num - 1][3])
    print(equipment)
    print(_storage.deliver_equipment(eq_to, equipment))


def bulk_deliver_equipment(_storage):
    d = {1: 'Принтер', 2: 'Сканер', 3: 'Копир', 4: ''}
    d_menu_item = 0
    eq_list = []
    _storage.display_report('storage_report')
    # _storage.display_equipments_list()

    eq_list = _storage.get_equipments_list()
    # eq_num = int(input('Выберете номер устройства: '))
    # eq_qtty = int(input('Укажите количество: '))
    # eq_to = input('Укажите место установки: ')
    print(eq_list)

    # while True:
    #
    #     try:
    #         d_menu_item = int(input('(1) Принтер | (2) Сканер | (3) Копир | (4) Все | (5) Отмена\n'
    #                                 'Укажите тип оборудования: '))
    #         if d_menu_item == 5:
    #             return
    #
    #         _storage.display_equipments_list(d.get(d_menu_item))
    #
    #     except ValueError:
    #         pass


def display_report(_storage):
    report_menu = '\nОтчеты.\n(1) Оборудование | (2) Анализ Запасов | ' \
                  '(3) Отгрузка Товаров | (4) Движение ТМЦ | (5) Назад'

    while True:
        print(report_menu)
        r_menu_item = input('Выберете пункт меню: ')

        if r_menu_item == '1':
            storage.display_report('qtty_report')

        elif r_menu_item == '2':
            r_menu_item = '0'
            while r_menu_item != '2' and r_menu_item != '1':
                print('(1) Общий | (2) Подробный')
                r_menu_item = input('Выберете пункт меню: ')
            storage.display_report('storage_report', True if r_menu_item == '2' else False)

        elif r_menu_item == '3':
            storage.display_report('delivered_equipment_report')

        elif r_menu_item == '4':
            storage.display_report('movement_report')

        elif r_menu_item == '5':
            break


while True:
    main_menu = 'Главное меню.\n(1) Принять оборудование | ' \
                '(2) Отгрузить оборудование | (3) Отчеты | (4) Выход'

    print(main_menu)

    menu_item = input('Выберете пункт меню: ')

    if menu_item == '1':
        take_equipment(storage)

    elif menu_item == '2':
        bulk_deliver_equipment(storage)

    elif menu_item == '3':

        display_report(storage)

    elif menu_item == '4':
        print('Выход из программы..')
        break

with open("storage.pkl", "wb") as fp:
    pickle.dump(storage, fp)
