'''
        Task 1

    Реализовать функцию, принимающую
    два числа (позиционные аргументы)
    и выполняющую их деление. Числа
    запрашивать у пользователя,
    предусмотреть обработку ситуации
    деления на ноль.

'''


def division(a, b):
    try:
        global divis
        divis = a / b

    except (ZeroDivisionError, NameError):
        print("Нельзя делить на ноль :(")
        print("Введите корректные числа")

    return divis

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(division(a, b))
