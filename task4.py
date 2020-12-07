# pip install PrettyTable
from prettytable import PrettyTable
from abc import ABC, abstractmethod
import uuid
import datetime
from collections import Counter


class Storage:
    def __init__(self, store_name):
        self.store_name = store_name
        self.__stored_equipment = []
        self.__delivered_equipment = []
        self.qtty_info = {
            'Принтер': 0,
            'Сканер': 0,
            'Копир': 0
        }

    def add_qtty(self, type):
        if type in self.qtty_info.keys():
            d = self.qtty_info[type]
            try:
                self.qtty_info[type] += 1
            except IndexError:
                self.qtty_info[type] = d
        else:
            self.qtty_info.update({type: 1})
            
    def sub_qtty(self, type):
        if type in self.qtty_info.keys():
            d = self.qtty_info[type]
            try:
                self.qtty_info[type] -= 1
                if self.qtty_info[type] < 0:
                    raise ValueError
            except (IndexError, ValueError):
                self.qtty_info[type] = d

    def take_equipment(self, *equipment):
        for cur_eq in equipment:
            self.add_qtty(cur_eq.type)
            self.__stored_equipment.append({
                    'id': uuid.uuid1(),
                    'equipment': cur_eq,
                    'store': self.store_name,
                    'receipt_date': datetime.datetime.now(),
                })

    def deliver_equipment(self, to, eq_to_deliver, qtty=1):
        for elf in range(qtty):
            for i, stored_item in enumerate(self.__stored_equipment):
                eq = stored_item.get('equipment')
                if eq.name.lower().strip() == eq_to_deliver.name.lower().strip():
                    self.__delivered_equipment.append({
                        'id': stored_item.get('id'),
                        'equipment': eq,
                        'store': to,
                        'receipt_date': stored_item.get('receipt_date'),
                        'delivered_date': datetime.datetime.now()
                    })
                    pr = self.__stored_equipment.pop(i)
                    self.sub_qtty(eq.type)
                    break

    def display_total_report(self):
        pass

    def display_storage_report(self, detailed=False):
        
        if detailed:
            table = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Серийный номер', 'Дата Поступления'])
            for i, el in enumerate(self.__stored_equipment, 1):
                eq = el.get("equipment")
                table.add_row([i, eq.type, eq.name, eq.sn, el.get("receipt_date")])
            print(f'Список оргтехники:\nСклад: {self.store_name}, Дата: {datetime.datetime.now()}\n{str(table)}')
            
        else:
            table = PrettyTable(['№ п/п', 'Наименование', 'Количество'])
            di = Counter([e.get('equipment').name for e in self.__stored_equipment])
            for i, key in enumerate(di.keys(), 1):
                table.add_row([i, key, di.get(key)])
            print(f'Склад: {self.store_name}, Дата: {datetime.datetime.now()}\n' +
                  'Список оргтехники:\n' + str(table))

    def display_delivered_equipment_report(self):
        pass

    def __str__(self):
        table1 = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Дата Поступления'])
        table2 = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Место Установки', 'Дата Отгрузки'])
        table3 = PrettyTable(['№ п/п', 'Тип', 'Количество'])
        for i, el in enumerate(self.__stored_equipment, 1):
            table1.add_row([i, el.get("equipment").type, el.get("equipment").name, el.get("receipt_date")])

        for i, el in enumerate(self.__delivered_equipment, 1):
            table2.add_row([i, el.get("equipment").type, el.get("equipment").name,
                            el.get('store'), el.get("delivered_date")])
        for i, key in enumerate(self.qtty_info.keys(), 1):
            table3.add_row([i, key, self.qtty_info.get(key)])

        return f'\nОбщая сводка оп складу: {self.store_name}, время: {datetime.datetime.now()}\n' + \
               'Список оборудования, которое хранится на складе:\n' + str(table1) + \
               '\nОбщее количество оборудования на складе:\n' + str(table3) + \
               '\nОборудование отгружено со склада:\n' + str(table2)


class OfficeEquipment(ABC):
    def __init__(self, name, sn):
        self.name = name
        self.sn = sn

    def __str__(self):
        return f'Тип: {self.type},\nИмя: {self.name}, \nСерийный номер: {self.sn}'

    @abstractmethod
    def action(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.type = 'Принтер'
        self.total_number_of_prints = 0

    def action(self, count=1):
        print(f'{self.name}: Печать... Количество страниц: {count} шт.')
        self.total_number_of_prints += count
    

class Scanner(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.type = 'Сканер'
        self.total_number_of_scans = 0

    def action(self, count=1):
        print(f'{self.name}: Сканирование... Количество страниц: {count} шт.')
        self.total_number_of_scans += count


class Copier(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.type = 'Копир'
        self.total_number_of_copies = 0

    def action(self, count=1):
        print(f'{self.name}: Копирование... Количество страниц: {count} шт.')
        self.total_number_of_copies += count
    

store = Storage('Центрарльный склад')

printer1 = Printer('  kyocera Ecosys P3060dn', uuid.uuid1())
printer2 = Printer('HP LaserJet M606dn', uuid.uuid1())
printer3 = Printer('Canon iPF770', uuid.uuid1())
printer4 = Printer('Kyocera Ecosys P3060dn', uuid.uuid1())

copier = Copier('Xerox WorkCentre 3335dn', uuid.uuid1())

store.take_equipment(printer1)
store.take_equipment(printer2)
store.take_equipment(printer3)
store.take_equipment(printer4)
store.take_equipment(copier)
store.display_storage_report()
# print(store)

print(f'\nПеремещение принетра {printer1.name} в бухгалтерию...')
store.deliver_equipment('Бухгалтерия', printer1, 2)
print(f'\nПеремещение принетра {printer2.name, 3} в отдел продаж...')
store.deliver_equipment('Отдел продаж', printer2)



