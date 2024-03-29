"""
ЗАДАЧА:
Вводится два списка целых чисел каждый с новой строки (в строке
наборы чисел через пробел), проверьте, есть ли хотя бы один общий
элемент в двух списках.
"""

nums = [int(i) for i in input("Введите элементы первого списка: ").split()]
nums_2 = [int(i) for i in input("Введите элементы второго списка: ").split()]

print(f'Да, списки имеют общие элементы: {set(nums).intersection(nums_2)}') \
    if len(set(nums).intersection(nums_2)) \
    else print("Списки не имеют общих элементов")

# Засчитывается, но проверка > 0 была ненужной

# Как решил бы я
if res := set(nums).intersection(nums_2):
    print(f'Да, списки имеют общие элементы: {res}')
else:
    print("Списки не имеют общих элементов")

# Читаемость имеет значение :)

"""
DEBUG
1 2 3 4 5
5 6 7 8 9

1 2 3 4 5
6 7 8 9
"""
