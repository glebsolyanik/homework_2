'''
        Task 3

    Реализовать базовый класс Worker (работник),
    в котором определить атрибуты: name, surname,
    position (должность), income (доход).
    Последний атрибут должен быть защищенным и
    ссылаться на словарь, содержащий
    элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного
    имени сотрудника (get_full_name) и дохода с учетом премии
    (get_total_income). Проверить работу примера на реальных
    данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров).

'''

class Worker:

    name = 'Harry'
    surname = 'Potter'
    position = 'Wizard'

    _income = {'wage':  80000, 'bonus': 3000}

class Position(Worker):

        def get_full_name(self):

            print(f'Имя - {Worker.name}, фамилия - {Worker.surname}, должность - {Worker.position}')

        def get_total_income(self):

            print(f'Зарплата - {Worker._income["wage"]}, бонус - {Worker._income["bonus"]}, всего -  {int(Worker._income["wage"]) + int(Worker._income["bonus"])}')

position_1 = Position()

position_1.get_full_name()

position_1.get_total_income()