'''
        Task 5

    Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''

class Stationery:

    title = 'рисунок'
    draw = 'толщина рисунка 0 мм'

    def start(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        Stationery.draw = 'толщина рисунка 1 мм'
        print(Stationery.draw)

class Pencil(Stationery):
    def __init__(self):
        Stationery.draw = 'толщина рисунка 7 мм'
        print(Stationery.draw)

class Handle(Stationery):
    def __init__(self):
        Stationery.draw = 'толщина рисунка 13 мм'
        print(Stationery.draw)

Pen_1 = Pen()
Pen_1.start()

Pencil_1 = Pencil()
Pencil_1.start()

Handle_1 = Handle()
Handle_1.start()