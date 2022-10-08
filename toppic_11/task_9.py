data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f'Исходный список кортежей: {data}')
num = int(input('Укажите значение: '))
# # №1
# for item in data:
#     print(item[:-1]+(num, ))
# # №2
print(f'Измененный список кортежей: {[item[:-1] + (num,) for item in data]}')

# # № 3
# data_2 = [[int(j) for j in data[i]]for i in range(len(data))]
# for i in range(len(data_2)):
#     for j in range(len(data_2[i])):
#         data_2[i][2] = num
# print(list(tuple(i) for i in data_2))

# # № 4 Доделать на инпут
