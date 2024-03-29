"""
ЗАДАЧА:
Вводится два списка чисел каждый с новой строки (в строке
наборы чисел через пробел). Посчитайте, сколько чисел содержится
одновременно как в первом списке, так и во втором.

Примечание: Задачу можно решить в одну строчку.
"""

print(len(set([float(i) for i in input("Введите элементы первого списка: ").split()]).intersection(set([float(i) for i in input("Введите элементы второго списка: ").split()]))))

# Для чего использовал f-строку?

# Я бы упростил задачу таким образом
print(
    f'{len(set([float(i) for i in input("Введите элементы 1-го списка: ").split()]) & set([float(i) for i in input("Введите элементы 2-го списка: ").split()]))}')

"""
DEBUG
3.6 12 7 96 23.2 56.1 75 3.6 7 4 66 75
21 6 96 17 45 7 3.6 51.6 32 6 21 34 57
"""
