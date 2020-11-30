from itertools import cycle
import time


class TrafficLight:
    __colors = {'Red': [7, '\033[31m'], 'Yellow': [2, '\033[33m'], 'Green': [10, '\033[32m']}

    def running(self):
        for color_key in cycle(TrafficLight.__colors.keys()):
            for t in range((color_value := TrafficLight.__colors.get(color_key))[0], 0, -1):
                print('', end=f'\r{color_value[1]} {color_key} ({t})')
                time.sleep(1)


tl = TrafficLight()
tl.running()
