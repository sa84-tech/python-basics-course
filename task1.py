from itertools import cycle
import time


class TrafficLight:
    __color = ''

    def running(self):
        colors = {'red': 7, 'yellow': 2, 'green': 10}
        for el in cycle(colors.keys()):
            TrafficLight.__color = el
            print(TrafficLight.__color)
            time.sleep(colors.get(el))


tl = TrafficLight()
tl.running()
