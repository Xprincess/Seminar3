"""
Задача 3. Задайте список из вещественных чисел. Напишите программу, которая
 найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

list = [1.1, 1.2, 3.1, 5, 10.01, 99.03, 14.77, 8.7, 1.11]

for i in range(len(list)):
    list[i] -= int(list[i])
    print(round(list[i], 2), end='  |  ')


def find_min_max_value(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    print()
    print(f'Максимальное значение: {round(max, 2)}')

    min = list[0]
    for i in range(len(list)):
        if list[i] != 0:
            if list[i] < min:
                min = list[i]

    print(f'Минимальное значение: {round(min, 2)}')
    diff = max - min
    print(f'Разница между максимальным и минимальным значениями: {round(diff, 2)}')

find_min_max_value(list)