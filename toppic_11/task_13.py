# data = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 5)]
# print('Исходный список кортежей', data)
#
# # Зачем итерировать элементы кортежа, если можно сразу преобразовать кортеж в список
# # data_2 = [[j for j in data[i]] for i in range(len(data))]
#
# data_2 = [list(item) for item in data]
# print('Преобразованный список кортежей в список списков:', data_2)


# №2 Решение через инпут

data = input("Введите исходный список кортежей: ")
print(f'\nИсходный список кортежей: {data}')

# Обработка исходного списка кортежей
data = data.strip(' [()]').replace('(', '').split('),')
# print(data)  # DEBUG

# Работа элементами кортежа
# # №1  # Расширенная версия
# result = []
# for item in data:
#     # print(item.split(','))  # DEBUG
#     item = [int(n.strip()) for n in item.split(',')]
#     # print(item)  # DEBUG
#     result.append(item)


# Работа элементами кортежа
# №2  # C помощью вложенных генераторов списка
result = [[int(n.strip()) for n in item.split(',')] for item in data]

print(f'Преобразованный список кортежей в список списков:{result}')
"""
[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 5)]
"""
