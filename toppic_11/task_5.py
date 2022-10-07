# print(tuple(data := [i for i in input("Введите исходный кортеж: ")]))
# sim = input("Укажите элемент для удаления: ")
# if sim in data:
#     data.remove(sim)
#     print(f'Изменненый кортеж: {data}')
# else:
#     print(f'"{sim}" нет в кортеже')

data = list(input("Введите исходный кортеж: "))
print(tuple(data))
sim = input("Укажите элемент для удаления: ")
if sim in data:
    data.remove(sim)
    print(f'Изменненый кортеж: {tuple(data)}')
else:
    print(f'"{sim}" нет в кортеже')
