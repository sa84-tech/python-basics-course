from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothing_type):
        self.clothing_type = clothing_type

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size=48):
        super().__init__(clothing_type='Пальто')
        try:
            self.size = int(size)
        except ValueError:
            self.size = 0

    @property
    def consumption(self):
        if self.size == 0:
            return 0
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height=180):
        super().__init__(clothing_type='Костюм')
        try:
            self.height = float(height)
        except ValueError:
            self.height = 0

    @property
    def consumption(self):
        if self.height == 0:
            return 0
        return round(2 * self.height / 100 + 0.3, 2)


coat1 = Coat(10)
coat2 = Coat(12)
print(f'На {coat1.clothing_type} с размером {coat1.size} будет израсходовано {coat1.consumption} м ткани')
print(f'На {coat2.clothing_type} с размером {coat2.size} будет израсходовано {coat2.consumption} м ткани')

suit1 = Suit(180)
suit2 = Suit(158)
print(f'При росте {suit1.height} см, на {suit1.clothing_type}  будет израсходовано {suit1.consumption} м ткани')
print(f'При росте {suit1.height} см, на {suit1.clothing_type}  будет израсходовано {suit1.consumption} м ткани')
