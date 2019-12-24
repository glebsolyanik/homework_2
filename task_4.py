'''
        Task 4

    Реализуйте базовый класс Car. У данного класса должны
    быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction),
    которые должны сообщать, что машина поехала, остановилась,
    повернула (куда). Опишите несколько дочерних
    классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен
    показывать текущую скорость автомобиля. Для классов
    TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
    должно выводиться сообщение о превышении скорости.

'''
import random

class Car:

    speed = random.randint(30, 100)
    color = random.choices(['красный', 'зеленый', 'синий'])
    name = random.choices(['BMW, Tesla, Mercedes'])
    is_police = bool(random.randint(0, 1))

    def show_speed(self):
        print(Car.speed)

    def go(self):
        print(f'Машина едет вперед со скростью {Car.speed} км/ч')

    def stop(self):
        print(f'Машина остановилась, скорость равна 0 км/ч')

    def turn(self):
        speed = random.randint(30, 50)
        side = random.randint(0, 1)
        if side == 0:
            side = 'праую'
        else:
            side = 'левую'
        print(f'Машина повернула в {side} сторону со скоростью {speed} км/ч')


class TownCar(Car):
    def __init__(self):
        if Car.speed > 60:
            print(f'Ваша скорость равна {Car.speed} км/ч')
            print('Снизте скорость автомобиля до 60 км/ч')
            Car.speed = random.randint(40, 60)
class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self):
        if Car.speed > 40:
            print('Снизте скорость автомобиля')
            Car.speed = random.randint(15, 40)

class PoliceCar(Car):
    pass

TownCar_1 = TownCar()

TownCar_1.turn()

WorkCar_1 = WorkCar()

WorkCar_1.go()

SportCar_1 = SportCar()
SportCar_1.stop()



