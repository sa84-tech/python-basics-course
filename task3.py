class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


pos = Position('Johnny', 'Worker', 'developer', 70000, 30000)
print(f'Meet {pos.get_full_name()}, a {pos.position}. His total income was {pos.get_total_income()} dollars last year.')

pos = Position('Selena', 'Gomez', 'singer', 700000, 300000)
print(f'Meet {pos.get_full_name()}, a {pos.position}. Her total income was {pos.get_total_income()} dollars last year.')
