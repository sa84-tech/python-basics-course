# pip install PrettyTable
from prettytable import PrettyTable
import uuid
import datetime
from collections import Counter
from equipment import OfficeEquipment


class Storage:
    def __init__(self, storage_name):
        self.storage_name = storage_name
        self.__journal = []
        self.__stored_equipment = []
        self.__delivered_equipment = []
        self.__qtty_info = {
            'Принтер': 0,
            'Сканер': 0,
            'Копир': 0
        }

    def __str__(self):
        table = PrettyTable(['№ п/п', 'Тип', 'Количество'])

        for i, key in enumerate(self.__qtty_info.keys(), 1):
            table.add_row([i, key, self.__qtty_info.get(key)])

        return f'\nСклад: {self.storage_name}, ' \
               f'Дата: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n' + \
               'Остатки:\n' + str(table)

    def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
        state = {}
        state["storage_name"] = self.storage_name
        state["__journal"] = self.__journal
        state["__stored_equipment"] = self.__stored_equipment
        state["__delivered_equipment"] = self.__delivered_equipment
        state["__qtty_info"] = self.__qtty_info
        return state

    def __setstate__(self, state: dict):  # Как мы будем восстанавливать класс из байтов
        self.storage_name = state["storage_name"]
        self.__journal = state["__journal"]
        self.__stored_equipment = state["__stored_equipment"]
        self.__delivered_equipment = state["__delivered_equipment"]
        self.__qtty_info = state["__qtty_info"]

    def eq_validate(self, equipment):
        try:
            if equipment:
                return False if not isinstance(equipment, OfficeEquipment) else \
                    True if equipment.eq_type in self.__qtty_info.keys() else False
            return False
        except AttributeError:
            return False

    def qtty_validate(self, equipment, qtty):
        if self.eq_validate(equipment):
            try:
                return True if self.get_equipment_qtty(equipment) >= qtty else False
            except ValueError:
                return False
        return False

    def get_equipment_by_sn(self, eq_sn):
        print(eq_sn)
        for item in self.__stored_equipment:
            # print(item)
            if eq_sn == item.get('equipment').sn:
                return item.get('equipment')

    def get_equipments_by_name(self):
        pass

    def get_equipments_by_type(self):
        pass

    def get_equipment_qtty(self, eq):
        return len([e.get('equipment').name for e in self.__stored_equipment if e.get('equipment').name == eq.name])

    def get_equipments_list(self, eq_type='', eq_name='', eq_sn='', full=False):
        n = 0
        if full:
            return [[n := n + 1, (e := se.get('equipment')).eq_type, e.name, e.sn] for se in self.__stored_equipment
                    if (not eq_type or eq_type == se.get('equipment').eq_type) and (not eq_name) and (not eq_sn)]
        else:
            d = [e.get('equipment').name for e in self.__stored_equipment]
            # print(d)
            # di = [{e.get('equipment').name: e.get('equipment').eq_type} for e in self.__stored_equipment]
            # print(di)
            dic = Counter(d)
            # print(dic)
            return [[i, key, dic.get(key)] for i, key in enumerate(dic.keys(), 1)]

    def take_equipment(self, *equipment):
        err_count = 0
        for cur_eq in equipment:
            if self.eq_validate(cur_eq):
                self.__qtty_info[cur_eq.eq_type] += 1
                self.__stored_equipment.append(tmp := {
                    'id': uuid.uuid1(),
                    'equipment': cur_eq,
                    'storage': self.storage_name,
                    'receipt_date': datetime.datetime.now(),
                    'delivered_date': ''
                })
                self.__journal.append(tmp)
            else:
                err_count += 1
        return 'ok' if not err_count else f'Ошибка. Некореткный тип данных, ' \
                                          f'принято оборудования: {len(equipment) - err_count} из {len(equipment)}'

    def deliver_equipment(self, to, equipment, qtty=1):
        if self.qtty_validate(equipment, qtty):
            for _ in range(qtty):
                for i, stored_item in enumerate(self.__stored_equipment):
                    eq = stored_item.get('equipment')
                    if eq.name.lower().strip() == equipment.name.lower().strip():
                        self.__delivered_equipment.append(tmp := {
                            'id': stored_item.get('id'),
                            'equipment': eq,
                            'storage': to,
                            'receipt_date': '',
                            'delivered_date': datetime.datetime.now()
                        })
                        self.__journal.append(tmp)
                        self.__stored_equipment.pop(i)
                        self.__qtty_info[eq.eq_type] -= 1
                        break
            return 'ok'
        else:
            return 'Ошибка: На складе отсутствует оборудование в указанном количесте.'

    def display_equipments_list(self, eq_type='', eq_name='', eq_sn=''):
        table = PrettyTable(['№ п/п', 'Тип', 'Наименоваие', 'Серийный номер'])
        table.add_rows(self.get_equipments_list(eq_type, eq_name, eq_sn, full=True))
        print(table)

    def display_report(self, report_type, full=False):
        if report_type == 'qtty_report':
            table = PrettyTable(['№ п/п', 'Тип', 'Количество'])

            for i, key in enumerate(self.__qtty_info.keys(), 1):
                table.add_row([i, key, self.__qtty_info.get(key)])

            print(f'\nОтчет - Оборудование.\nСклад: {self.storage_name}, '
                  f'Дата: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n'
                  f'{str(table)}\nОбщее количество оборудования: {len(self.__stored_equipment)}')

        elif report_type == 'storage_report':
            span = 'Общий'

            if full:
                span = 'Подробный'
                table = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Серийный номер', 'Дата Поступления'])
                for i, el in enumerate(self.__stored_equipment, 1):
                    eq = el.get("equipment")
                    table.add_row([i, eq.eq_type, eq.name, eq.sn, el.get("receipt_date").strftime('%d.%m.%Y %H:%M:%S')])
            else:
                table = PrettyTable(['№ п/п', 'Наименование', 'Количество'])
                di = Counter([e.get('equipment').name for e in self.__stored_equipment])
                for i, key in enumerate(di.keys(), 1):
                    table.add_row([i, key, di.get(key)])

            print(f'\nОтчет - Анализ запасов ({span}):\nСклад: {self.storage_name}, '
                  f'Дата: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n{str(table)}')

        elif report_type == 'delivered_equipment_report':
            table = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Место Установки', 'Дата Отгрузки'])

            for i, el in enumerate(self.__delivered_equipment, 1):
                table.add_row([i, el.get("equipment").eq_type, el.get("equipment").name,
                               el.get('storage'), el.get("delivered_date").strftime("%d.%m.%Y %H:%M:%S")])

            print(f'\nОтчет - Отгрузка Товара.\nСклад: {self.storage_name}, '
                  f'Дата: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n{str(table)}')

        elif report_type == 'movement_report':
            table = PrettyTable(['№ п/п', 'Дата', 'Операция', 'Назначение', 'Тип Устройства',
                                 'Наименование', 'Серийный Номер'])

            table.add_rows(
                [[i, rd.strftime("%d.%m.%Y %H:%M:%S") if (rd := sj.get("receipt_date"))
                else sj.get("delivered_date").strftime("%d.%m.%Y %H:%M:%S"), 'ПРИХОД' if rd else 'РАСХОД',
                  sj.get("storage"), (e := sj.get('equipment')).eq_type, e.name, e.sn]
                 for i, sj in enumerate(self.__journal, 1)]
            )

            print(f'\nОтчет - Движение ТМЦ:\nСклад: {self.storage_name}, '
                  f'Дата: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n'
                  f'{str(table)}')

        else:
            print('Ошибка: Неверный тип отчета.')
