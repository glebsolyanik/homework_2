'''
        Task 5

    Реализовать формирование списка,
    используя функцию range() и возможности
    генератора. В список должны войти четные числа
    от 100 до 1000 (включая границы). Необходимо
    получить результат вычисления произведения
    всех элементов списка.

'''
from functools import reduce


def fun(prev_el, el):
    return prev_el * el


list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(fun, list))
