# pip install PrettyTable
from prettytable import PrettyTable
from abc import ABC, abstractmethod
import uuid
import datetime


class Storage:
    def __init__(self, store_name):
        self.store_name = store_name
        self.__stored_equipment = []
        self.__delivered_equipment = []
        self.qtty_info = {}

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

    def deliver_equipment(self, eq_to_deliver, to):
        item_pos = 0
        for i, stored_item in enumerate(self.__stored_equipment):
            eq = stored_item.get('equipment')
            if eq.sn == eq_to_deliver.sn:

                item_pos = i
                self.__delivered_equipment.append({
                    'id': stored_item.get('id'),
                    'equipment': eq,
                    'store': to,
                    'receipt_date': stored_item.get('receipt_date'),
                    'delivered_date': datetime.datetime.now()
                })
                self.__stored_equipment.pop(i)
                self.sub_qtty(eq.type)
                break

    def _get_storage_info(self):
        pass

    def _get_delivered_info(self):
        pass

    def __str__(self):
        table1 = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Дата Поступления'])
        table2 = PrettyTable(['№ п/п', 'Тип', 'Наименование', 'Место Установки', 'Дата Отгрузки'])
        table3 = PrettyTable(['№ п/п', 'Тип', 'Количество'])
        for i, el in enumerate(self.__stored_equipment, 1):
            table1.add_row([i, t := el.get("equipment").type, el.get("equipment").name, el.get("receipt_date")])

        for i, el in enumerate(self.__delivered_equipment, 1):
            table2.add_row([i, el.get("equipment").type, el.get("equipment").name,
                            el.get('store'), el.get("delivered_date")])
        for i, key in enumerate(self.qtty_info.keys(), 1):
            table3.add_row([i, key, self.qtty_info.get(key)])

        return f'Общая сводка оп складу: {self.store_name}, время: {datetime.datetime.now()}\n' + \
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
        self.type = 'Принтер'
        super().__init__(name, sn)

    def action(self):
        print(f'{self.name}: Печать...')
    

class Scanner(OfficeEquipment):
    def __init__(self, name, sn):
        self.type = 'Сканер'
        super().__init__(name, sn)

    def action(self):
        print(f'{self.name}: Сканирование...')


class Copier(OfficeEquipment):
    def __init__(self, name, sn):
        self.type = 'Копир'
        super().__init__(name, sn)

    def action(self):
        print(f'{self.name}: Копирование...')
    

store = Storage('Центрарльный склад')

printer1 = Printer('Kyocera Ecosys P3060dn', uuid.uuid1())
printer2 = Printer('HP LaserJet M606dn', uuid.uuid1())
printer3 = Printer('Canon iPF770', uuid.uuid1())

copier = Copier('Xerox WorkCentre 3335dn', uuid.uuid1())

store.take_equipment(printer1)
store.take_equipment(printer2)
store.take_equipment(printer3)
store.take_equipment(copier)

print(store)

store.deliver_equipment(printer1, 'Бухгалтерия')
store.deliver_equipment(printer2, 'Отдел продаж')

print(store)

