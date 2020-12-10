# pip install PrettyTable
import uuid  # используется для иммитации ввода уникального s/n устройства при приемке
import pickle

from equipment import Printer, Scanner, Copier
from storage import Storage


def save_to_db(_storage):
    """
    Сохранить состояние объекта Склад в файл (зд. при корректном выходе из программы)
    :param _storage:
    :return:
    """
    with open("storage.pkl", "wb") as fp:
        pickle.dump(_storage, fp)


def take_equipment(_storage):
    """
    Выполнить приемку оборудования
    :param _storage:
    :return:
    """
    equipment = []
    eq_type = ''
    eq_name = ''

    while eq_type != '1' and eq_type != '2' and eq_type != '3' and eq_type != '4':
        eq_type = input('\n(1) Принтер | (2) Сканер | (3) Копир | (4) Отмена\nукажите тип оборудования: ')
    if eq_type == '4':
        return
    while len(eq_name) < 3:
        eq_name = input('Введите наименование: ').strip()
    while True:
        try:
            eq_qtty = int(input('Укажите количество: '))
            if eq_qtty < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    if eq_type == '1':
        for _ in range(eq_qtty):
            equipment.append(Printer(eq_name, uuid.uuid1()))
    elif eq_type == '2':
        for _ in range(eq_qtty):
            equipment.append(Scanner(eq_name, uuid.uuid1()))
    elif eq_type == '3':
        for _ in range(eq_qtty):
            equipment.append(Copier(eq_name, uuid.uuid1()))

    print(_storage.take_equipment(*equipment))
    return


def give_equipment(_storage):
    """
    Перемещение одной единицы оборудования
    :param _storage:
    :return:
    """
    d = {1: 'Принтер', 2: 'Сканер', 3: 'Копир', 4: ''}
    d_menu_item = 0
    eq_list = []
    eq_num = 0
    eq_to = ''

    while d_menu_item < 1 or d_menu_item > 5:
        try:
            d_menu_item = int(input('\n(1) Принтер | (2) Сканер | (3) Копир | (4) Все | (5) Назад\n' 
                                    'Укажите тип оборудования: '))
            if d_menu_item == 5:
                return

            _storage.display_equipments_list(d.get(d_menu_item), full=True)
            eq_list = _storage.get_equipments_list(eq_type=d.get(d_menu_item), full=True)
            eq_num = int(input('Выберите номер устройства: '))
            if eq_num < 0 or eq_num > len(eq_list):
                raise ValueError
            eq_to = input('Укажите место установки: ')
            if len(eq_to) < 2:
                raise ValueError
        except ValueError:
            d_menu_item = 0
            print('Некорректный ввод')

    equipment = _storage.get_equipment_by_sn(eq_list[eq_num - 1][4])
    print(f'Выполнено перемещение {equipment.eq_type.lower()}а {equipment.name} c s/n {equipment.sn}'
          if (ans := _storage.give_equipment(eq_to, equipment)) == 'ok' else ans)
    return


def give_equipments_group(_storage):
    """
    Групповое перемещение оборудования
    :param _storage:
    :return:
    """
    _storage.display_equipments_list()
    eq_list = _storage.get_equipments_list()

    while True:
        try:
            eq_num = int(input('Выберите номер устройства, 0 - отмена: '))
            if eq_num == 0:
                return
            if eq_num < 0 or eq_num > len(eq_list):
                raise ValueError
            eq_qtty = int(input('Укажите количество, 0 - все: '))
            if eq_qtty < 0 or eq_qtty > eq_list[eq_num-1][3]:
                raise ValueError
            eq_to = input('Укажите место установки: ')
            if len(eq_to) < 2:
                raise ValueError
        except ValueError:
            print('Некорректное значение')
        else:
            break

    equipments = _storage.get_equipments_by_name(eq_list[eq_num - 1][2], eq_qtty)
    print(f'Выполнено перемещение {eq_qtty} ед. техники'
          if (ans := _storage.give_equipment(eq_to, *equipments)) == 'ok' else ans)
    return


def display_report(_storage):
    """
    Вывести отчеты
    :param _storage:
    :return:
    """
    report_menu = '\n*** ОТЧЕТЫ ***\n(1) Оборудование | (2) Анализ Запасов | ' \
                  '(3) Отгруженное Оборудование | (4) Движение ТМЦ | (5) Назад'

    while True:
        print(report_menu)
        r_menu_item = input('Выберите пункт меню: ')

        if r_menu_item == '1':
            _storage.display_report('qtty_report')

        elif r_menu_item == '2':
            r_menu_item = '0'
            while r_menu_item != '2' and r_menu_item != '1':
                print('(1) Общий | (2) Подробный')
                r_menu_item = input('Выберите пункт меню: ')
            _storage.display_report('storage_report', True if r_menu_item == '2' else False)

        elif r_menu_item == '3':
            _storage.display_report('delivered_equipment_report')

        elif r_menu_item == '4':
            _storage.display_report('movement_report')

        elif r_menu_item == '5':
            break


def diagnose_equipment(_storage):
    """
    Диагностика оборудования - состояние выборанного устройства, печать/сканировние.
    :param _storage:
    :return:
    """
    d = {1: 'Принтер', 2: 'Сканер', 3: 'Копир', 4: ''}

    while True:
        print('\n*** Диагностика ***')
        try:
            de_menu_item = int(input('\n(1) Принтер | (2) Сканер | (3) Копир | (4) Все | (5) Назад\n'
                                     'Укажите тип оборудования: '))
            if de_menu_item < 1 or de_menu_item > 5:
                raise ValueError
            elif de_menu_item == 5:
                return

            eq_list = _storage.get_equipments_list(eq_type=d.get(de_menu_item), full=True)
            if len(eq_list):
                _storage.display_equipments_list(d.get(de_menu_item), full=True)
                eq_num = int(input('Выберите номер устройства: '))
                if eq_num < 1 or eq_num > len(eq_list):
                    raise ValueError
            else:
                print('Оборудование указанного типа нет в наличии')
                continue

        except ValueError:
            print('Некорректный ввод')
            continue

        equipment = _storage.get_equipment_by_sn(eq_list[eq_num - 1][4])
        print(equipment.name)
        answer = ''
        while answer != '3':
            answer = input('\n(1) Состояние устройства | (2) Запустить устройство | (3) Назад\nВыберите пункт меню: ')
            if answer == '1':
                print(equipment)
            elif answer == '2':
                try:
                    equipment.action(abs(int(input('Укажите количество страниц: '))))
                except ValueError:
                    print('Некорректный ввод')


def main():
    """
    Запуск программы
    :return:
    """
    try:
        with open("storage.pkl", "rb") as fp:
            storage = pickle.load(fp)
    except (FileNotFoundError, EOFError):
        storage = Storage('Центральный')

    print('\nУПРАВЛЕНИЕ СКЛАДОМ v1.24')
    print('Copyright © ООО "Кривые руки" 1996 г. \n')
    print(storage)

    while True:
        print('\n*** ГЛАВНОЕ МЕНЮ ***\n(1) Принять оборудование | '
              '(2) Переместить оборудование | (3) Отчеты | (4) Диагностика Оборудования | (5) Выход')

        menu_item = input('Выберите пункт меню: ')
        if menu_item == '1':
            take_equipment(storage)

        elif menu_item == '2':
            answer = ''
            while answer != '3':
                print('(1) Перемещение определенного оборудования | (2) Групповое перемещение | (3) Назад')
                answer = input('Выберите пункт меню: ')
                if answer == '1':
                    give_equipment(storage)
                elif answer == '2':
                    give_equipments_group(storage)

        elif menu_item == '3':
            display_report(storage)

        elif menu_item == '4':
            diagnose_equipment(storage)

        elif menu_item == '5':
            print('Выход из программы..')
            break

    save_to_db(storage)

    return 0


main()
