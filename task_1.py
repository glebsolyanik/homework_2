'''
        Task 1

    Создать класс TrafficLight (светофор) и определить
    у него один атрибут color (цвет) и метод running
    (запуск). Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора
    в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет
    7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться
    только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.

'''

import time, random

class TrafficLight:

    color = 'red'

    def Running(self):

        print(TrafficLight.color)
        time.sleep(7)

        TrafficLight.color = 'yellow'
        print(TrafficLight.color)
        time.sleep(2)

        TrafficLight.color = 'green'
        print(TrafficLight.color)
        time.sleep(random.randint(5, 8))

        TrafficLight.color = 'yellow'
        print(TrafficLight.color)
        time.sleep(2)

        TrafficLight.color = 'red'
        print(TrafficLight.color)

TrafficLight().Running()