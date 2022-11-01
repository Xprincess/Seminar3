# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

# Task_ver1

def sum_odd(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]

    return sum

try:

    size = int(input("Задайте размер списка: "))
    list = []
    for i in range(0,size):
        list.append(random.randint(1, 9))

    print(list)
    print(sum_odd(list))
except:
    print("Введите корректное число!")
