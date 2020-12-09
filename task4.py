class Car:
    item_number = 0

    def __init__(self, speed=0, color='', name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.item_number += 1

    def go(self):
        print(f'{self.name}, go!\n')

    def stop(self):
        print(f'{self.name}, stop!\n')

    def turn(self, direction):
        print(f'{self.name}, turn {direction}!\n')

    def show_speed(self):
        print(f'Speed: {self.speed}\n')


class TownCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}. Overspeeding registered!\n') \
            if self.speed > 60 else print(f'Speed: {self.speed}\n')


class SportCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}. Overspeeding registered!\n') \
            if self.speed > 150 else print(f'Speed: {self.speed}\n')


class WorkCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}. Overspeeding registered!\n') \
            if self.speed > 40 else print(f'Speed: {self.speed}\n')


class PoliceCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}. Overspeeding registered!\n') \
            if self.speed > 1000 else print(f'Speed: {self.speed}\n')


car = Car('250.0', 'Red', 'unrecognized', False)
print(f'##### Report {car.item_number} #####\nVehicle name: {car.name},\nColor: {car.color},\n'
      f'Is Police: {car.is_police}')
car.show_speed()
car.stop()

car = TownCar(149.0, 'Brown', 'Toyota Rav4', False)
print(f'##### Report {car.item_number} #####\nVehicle name: {car.name},\nColor: {car.color},\n'
      f'Is Police: {car.is_police}')
car.show_speed()
car.turn('to the road side')
car.stop()

car = SportCar(190, 'Yellow', 'Lada Kalina', False)
print(f'##### Report {car.item_number} #####\nVehicle name: {car.name},\nColor: {car.color},\n'
      f'Is Police: {car.is_police}')
car.show_speed()
car.go()
car.turn('wherever you want')

car = WorkCar(100.0, 'Khaki', 'Kamaz', False)
print(f'##### Report {car.item_number} #####\nVehicle name: {car.name},\nColor: {car.color},\n'
      f'Is Police: {car.is_police}')
car.show_speed()
car.go()

car = PoliceCar(100.0, 'White', 'UAZ Patriot', True)
print(f'##### Report {car.item_number} #####\nVehicle name: {car.name},\nColor: {car.color},\n'
      f'Is Police: {car.is_police}')
car.show_speed()
car.go()
