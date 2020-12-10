from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name, sn):
        self.name = name
        self.sn = sn
        self.total_number_of_pages = 0
        self.depreciation = 0

    def __str__(self):
        return f'Тип: {self.eq_type},\nИмя: {self.name}, \nСерийный номер: {self.sn}, \n' \
               f'Пробег: {self.total_number_of_pages} стр.\nИзнос: {self.depreciation} %'

    @abstractmethod
    def action(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.eq_type = 'Принтер'
        self.max_pages = 100000

    def action(self, count=1):
        print(f' *** {self.name}: Печать... Количество страниц: {count} шт.')
        self.total_number_of_pages += count
        self.depreciation = round(t, 2) if (t := self.total_number_of_pages / self.max_pages * 100) < 100 else 100


class Scanner(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.eq_type = 'Сканер'
        self.max_pages = 10000

    def action(self, count=1):
        print(f' *** {self.name}: Сканирование... Количество страниц: {count} шт.')
        self.total_number_of_pages += count
        self.depreciation = round(t, 2) if (t := self.total_number_of_pages / self.max_pages * 100) < 100 else 100


class Copier(OfficeEquipment):
    def __init__(self, name, sn):
        super().__init__(name.strip().title(), sn)
        self.eq_type = 'Копир'
        self.max_pages = 200000

    def action(self, count=1):
        print(f' *** {self.name}: Копирование... Количество страниц: {count} шт.')
        self.total_number_of_pages += count
        self.depreciation = round(t, 2) if (t := self.total_number_of_pages / self.max_pages * 100) < 100 else 100
