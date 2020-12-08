import uuid

from equipment import Printer, Scanner, Copier

printer = Printer('  kyocera Ecosys P3060dn', uuid.uuid1())
print(printer)
printer.action(500)
printer.action(1200)
print(printer)
print()

scanner = Scanner('HP S200', uuid.uuid1())
scanner.action(12000)
print(scanner)
print()

copier = Copier('Ricoh Aficio SP6002', uuid.uuid1())
copier.action(123456)
print(copier)
