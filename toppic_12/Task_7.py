"""
ЗАДАНИЕ:
Вводится два списка целых чисел каждый с новой строки (в строке
наборы чисел через пробел). Найдите все числа, которые входят как в
первый, так и во второй список и выведите их в порядке возрастания.
Примечание: Задачу можно решить в одну строчку.
"""

nums = [int(i) for i in input("Введите элементы первого списка: ").split()]
nums_2 = [int(i) for i in input("Введите элементы второго списка: ").split()]
print(*(sorted(set(nums).intersection(nums_2), reverse=False)))


# Задача решена неоптимальным способом, можно решить одной строкой кода

"""
DEBUG
89 12 45 87 20 97 21 24 54 76 23 56 76
23 98 15 97 34 12 56 23 78 8 74 81 21 89
"""