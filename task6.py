# pip install PrettyTable
import uuid
import pickle

from equipment import Printer, Scanner, Copier
from storage import Storage


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


def give_equipment(_storage):
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

    equipment = _storage.get_equipment_by_sn(eq_list[eq_num - 1][4])
    print(equipment)
    print(_storage.give_equipment(eq_to, equipment))


def bulk_give_equipment(_storage):
    _storage.display_equipments_list()
    eq_list = _storage.get_equipments_list()

    while True:
        try:
            eq_num = int(input('Выберете номер устройства: '))
            if eq_num < 0 or eq_num > len(eq_list):
                raise ValueError
            eq_qtty = int(input('Укажите количество, 0 - все: '))
            if eq_qtty > eq_list[eq_num-1][3]:
                raise ValueError
            eq_to = input('Укажите место установки: ')
            if len(eq_to) < 2:
                raise ValueError
        except ValueError:
            print('Некорректное значение')
        else:
            break

    equipments = _storage.get_equipments_by_name(eq_list[eq_num - 1][2], eq_qtty)
    print(_storage.give_equipment(eq_to, *equipments))


def display_report(_storage):
    report_menu = '\n*** ОТЧЕТЫ ***\n(1) Оборудование | (2) Анализ Запасов | ' \
                  '(3) Отгруженное Оборудование | (4) Движение ТМЦ | (5) Назад'

    while True:
        print(report_menu)
        r_menu_item = input('Выберете пункт меню: ')

        if r_menu_item == '1':
            _storage.display_report('qtty_report')

        elif r_menu_item == '2':
            r_menu_item = '0'
            while r_menu_item != '2' and r_menu_item != '1':
                print('(1) Общий | (2) Подробный')
                r_menu_item = input('Выберете пункт меню: ')
            _storage.display_report('storage_report', True if r_menu_item == '2' else False)

        elif r_menu_item == '3':
            _storage.display_report('delivered_equipment_report')

        elif r_menu_item == '4':
            _storage.display_report('movement_report')

        elif r_menu_item == '5':
            break


def main():
    try:
        with open("storage.pkl", "rb") as fp:
            storage = pickle.load(fp)
    except (FileNotFoundError, EOFError):
        storage = Storage('Центральный')

    print(storage)

    while True:
        print('\n*** ГЛАВНОЕ МЕНЮ ***\n(1) Принять оборудование | '
              '(2) Переместить оборудование | (3) Отчеты | (4) Диагностика | (5) Выход')

        menu_item = input('Выберете пункт меню: ')
        if menu_item == '1':
            take_equipment(storage)

        elif menu_item == '2':
            answer = ''
            while answer != '3':
                print('(1) Перемещение определенного оборудования | (2) Групповое перемещение | (3) Назад')
                answer = input('Выберете пункт меню: ')
                if answer == '1':
                    give_equipment(storage)
                elif answer == '2':
                    bulk_give_equipment(storage)

        elif menu_item == '3':
            display_report(storage)

        elif menu_item == '4':
            print('Диагностика..')

        elif menu_item == '5':
            print('Выход из программы..')
            break

    with open("storage.pkl", "wb") as fp:
        pickle.dump(storage, fp)

    return 0


main()
