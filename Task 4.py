"""
Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def binary(list):
    num = int(input("Введите целое число: "))
    list = []
    i = 0
    ost = 0

    while num > 0:
        ost = num % 2
        list.append(ost)
        num = num // 2
        i += 1

    for i in list:
        print(i, end='  ')


binary(list)