data = tuple(input("Введите ваш текст: ").split())
ind = int(input("Укажите шаг, положительное целое число: "))

print(f'Исходный кортеж: {data}\nИзмененный кортеж: {data[::ind]}')

# Молодец!
