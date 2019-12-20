'''
        Task 4

    Создать (не программно) текстовый файл со следующим содержимым:

    One — 1

    Two — 2

    Three — 3

    Four — 4

    Необходимо написать программу, открывающую файл
    на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться
    на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

f = open('task4.txt')

numbers = { 'One':      'Один',
            'Two':      'Два',
            'Three':    'Три',
            'Four':     'Четыре'
           }

a = open('task4.1.txt', 'w')

for line in f:
    lines = line.split()
    if bool(lines) == False:
        continue
    lines[0] = numbers[lines[0]]
    print(*lines, file=a)





f.close()
a.close()












