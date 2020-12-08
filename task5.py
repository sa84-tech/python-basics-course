# pip install PrettyTable
import uuid

from equipment import Printer, Scanner, Copier
from storage import Storage


storage = Storage('Центральный')
print('\nПриемка товара, 10 единиц техники...')
ans = storage.take_equipment(
    printer1 := Printer('  kyocera Ecosys P3060dn', uuid.uuid1()),
    printer2 := Printer('HP LaserJet M606dn', uuid.uuid1()),
    'ghbdtn',
    Printer('HP LaserJet M606dn', uuid.uuid1()),
    Printer('Canon iPF770', uuid.uuid1()),
    Printer('Kyocera Ecosys P3060dn', uuid.uuid1()),
    scanner := Scanner('HP S200', uuid.uuid1()),
    Scanner('HP s200', uuid.uuid1()),
    12321,
    Copier('Xerox WorkCentre 3335dn', uuid.uuid1()),
    Copier('Ricoh Aficio SP6002', uuid.uuid1()),
    Copier('Ricoh Aficio SP6002', uuid.uuid1()),
)

print(ans)

print(storage)

storage.display_report('storage_report', True)

storage.display_report('storage_report')
storage.get_equipment_qtty(printer1)
print(f'\nПеремещение 3 принетеров {printer1.name} в бухгалтерию...')
print(storage.deliver_equipment('Бухгалтерия', printer1, 3))
print(f'\nПеремещение 2 принетеров {printer1.name} в бухгалтерию...')
print(storage.deliver_equipment('Бухгалтерия', printer1, 2))
print(f'\nПеремещение 2 сканеров {scanner.name} в отдел продаж...')
print(storage.deliver_equipment('Бухгалтерия', scanner, 2))

print('\nПриемка товара, 5 единиц техники...')
ans = storage.take_equipment(
    Scanner('HP S200', uuid.uuid1()),
    Scanner('HP s200', uuid.uuid1()),
    Copier('Xerox WorkCentre 3335dn', uuid.uuid1()),
    Copier('Ricoh Aficio SP6002', uuid.uuid1()),
    Copier('Ricoh Aficio SP6002', uuid.uuid1()),
)

print(ans)

storage.display_report('delivered_equipment_report')

storage.display_report('qtty_report')

storage.display_report('storage_report', True)

storage.display_report('movement_report')

