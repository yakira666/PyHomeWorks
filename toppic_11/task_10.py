# data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # №1
# data_2 = []
# for i in range(len(data)):
#     if data[i] != ():  # так делать не стоит, как можно написать это условие с помощью логического оператора?
#         data_2.append(data[i])
# print(data_2)

# №3
# Получаем на ввод список с кортежами, удаляем сразу все лишнее и пустые кортежи, преобразуем в список
data = input().strip("] [(,)") \
    .replace("), (", "@") \
    .replace("(", "") \
    .replace(")", "") \
    .split("@")
# Создаем пустой список куда будем добавлять готовые объекты
data_2 = []

# Перебираем полученый лист поэлементно удаляя лишнее и добавляя в новый лист
#                                                                    (все элементы - строковые), создаем матрицу
for i in range(len(data)):
    data_2.append(data[i].replace(",", "").replace("\'", "").replace("\"", "").split(" "))

# С помощью генератора преобразуем элементы нового списка в кортежи
data_2 = [tuple([data_2[i][j] for j in range(len(data_2[i]))]) for i in range(len(data_2))]
print(data_2)
