input_stars = int(input("Введите кол-во звезд: "))
# for i in range(input_stars):
#     print("* " * i)
# for i in range(input_stars, -1, -1):
#     print("* " * i)

# Неправильный подход к решению задачи, после последней строки пустая лишняя строка
# Подсказка: Задача решается с помощью вложенных циклов

for i in range(input_stars):
    for k in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(input_stars - 1, 0, -1):
    for k in range(i, 0, -1):
        print("*", end=" ")
    print()


# моё решение
n = int(input("Введите количество звезд: "))

for i in range(n):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
# есть пустая строка сверху, узнать правильно ли это?