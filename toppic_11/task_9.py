# data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print(f'Исходный список кортежей: {data}')
# num = int(input('Укажите значение: '))
# # # №1
# for item in data:
#     print(item[:-1]+(num, ))
# # №2
# print(f'Измененный список кортежей: {[item[:-1] + (num,) for item in data]}')
#
# # № 3
# data_2 = [[int(j) for j in data[i]]for i in range(len(data))]
# for i in range(len(data_2)):
#     for j in range(len(data_2[i])):
#         data_2[i][2] = num
# print(list(tuple(i) for i in data_2))

# Решение при получении черезе ввод
#
# Получили список с кортежами обрезали все лишнее, создали пстой списко для заполнения
data = input("Введите исходный кортеж: ").strip("] [()").replace("), (", "$").split("$")
data_2 = list()

# Перебираем элементы заполняя новый список, убрав все лишнее получаем строковые элементы
for i in range(len(data)):
    data_2.append(data[i].replace(",", "").split(" "))

# Преобразуем все элементы в целочисленые, создаем матрицу
data_2 = [[int(data_2[i][j]) for j in range(len(data_2[i]))]for i in range(len(data_2))]

# Получаем на ввод элемент для замены
num = int(input('Укажите значение: '))

# Заменяем последние элементы матрицы на введеный пользователем
for i in range(len(data_2)):
    for j in range(len(data_2[i])):
        data_2[i][-1] = num

# Выводим список с преобразоваными списками в кортеж
print("Измененный список кортежей:", list(tuple(i) for i in data_2))

"""
[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
[(10, 20, 40), (40, 50, 60), (70, 80, 90), (240, 250, 260), (170, 180, 190)]
"""
