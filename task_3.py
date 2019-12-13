'''
        Task 3

    Реализовать функцию my_func(),
    которая принимает три позиционных
    аргумента, и возвращает сумму наибольших
    двух аргументов.

'''

def my_func(a, b, c):

    list = [a, b, c]

    maxim = max(list)

    list.remove(maxim)

    return maxim + max(list)

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

print(my_func(a, b, c))

