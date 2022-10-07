data = input("Введите ваш текст: ").split()
ind = int(input("Укажите шаг, положительное целое число: "))
a = tuple(data)
b = data[::ind]
# print(a, b)
print(f'Исходный кортеж: {tuple(data)}\nИзмененный кортеж: {tuple(data[::ind])}')