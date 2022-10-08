# print(f'Исходный кортеж: {tuple(data_given := [4, 6, 2, 8, 3, 1])}')
# data_given.append(data := input("Укажите элемент для добавления в кортеж: "))
# print("Изменненый кортеж: ", (tuple(data_given)))

data_given = (4, 6, 2, 8, 3, 1)
# data = ("10", )
# print(data_given+data)

print(f'Исходный кортеж: {data_given}')
user_inp = input('Введите элемент для добавления в кортеж: ')
print('Изменённый кортеж:', data_given + (user_inp,))

# Добавлена возможность получить значение от пользователя и добавить его в конец кортежа
