# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

calculation = input('Введите арифметическое выражение - число, операция (+, -, * или /), число - ')
if '+' in calculation:
    ind = calculation.index('+')
    a = int(calculation[0:ind])
    b = int(calculation[ind+1:])
    resalt = a + b
elif '-' in calculation:
    ind = calculation.index('-')
    a = int(calculation[0:ind])
    b = int(calculation[ind + 1:])
    resalt = a - b
elif '*' in calculation:
    ind = calculation.index('*')
    a = int(calculation[0:ind])
    b = int(calculation[ind + 1:])
    resalt = a * b
elif '/' in calculation:
    ind = calculation.index('/')
    a = int(calculation[0:ind ])
    b = int(calculation[ind + 1:])
    resalt = a / b
else:
    print('Введено некорректное выражение!')
print(f'Результат выражения {calculation} равен {resalt}')

# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.
import random
number = [random.randrange(-1_000,1_000) for i in range(20)]
print(f'Список случайных чисел - {number}')
maximum = max(number)
print(f'Максимальное число в списке = {maximum}')
minimum = min(number)
print(f'Минимальное  число в списке = {minimum}')
print(f'Количество положительных чисел в списке = {sum(i > 0 for i in number)}')
print(f'Количество отрицательных чисел в списке = {sum(i < 0 for i in number)}')
print(f'Количество 0 в списке = {sum(i == 0 for i in number)}')