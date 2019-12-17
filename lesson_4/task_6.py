'''

 Реализовать два небольших скрипта:

а) бесконечный итератор, генерирующий целые числа, начиная с указанного,

б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.

'''

from itertools import cycle, count

def numbers():
    num = [int(input('Введите число: '))]

    for el in count(num[0]):
        if el > 1000:
            break
        print(el)


def elements():
    c = 0
    nums = list(input('Введите эелементы списка: ').split())

    for el in cycle(nums):
        if c > 1000:
            break
        print(el)
        c += 1


numbers()
elements()




