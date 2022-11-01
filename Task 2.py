# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

def func(list):
    new_list = []
    i = 0
    while i < len(list)/2:
        new_list.append(list[i] * list[len(list) - 1 - i])
        i +=1
    return new_list

print(list)
print(func(list))