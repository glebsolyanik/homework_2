'''
        Task 5

    Создать (программно) текстовый файл,
    записать в него программно набор чисел,
    разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.

'''
a = 0
f = open('task5.txt', 'w')

numbers = input('Введите числа через пробел: ')
nums = numbers.split()
for i in nums:
    nums[a] = int(nums[a])
    a += 1

summ = sum(nums)

print(f'Числа - {numbers}', file=f)
print(f'Сумма - {summ}', file=f)
f.close()

