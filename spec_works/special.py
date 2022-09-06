# b = 1
# a = int(input("Введите кол-во звезд: "))
# v = a
# for i in range(a, 0, -1):
#     print(" " * i + "*" * b * 2)
#     b += 1
# for j in range(1, a + 1):
#     print(" " * j + "*" * v * 2)
#     v -= 1

N = int(input("Введите число: "))  # 4
for i in range(N, 0, -1):
    # пустые пробелы перед символами строки
    for j in range(i, 0, -1):
        print(' ', end='')

    # символы строки
    for k in range(i, N + 1, 1):
        print('**', end='')
        # переход на новую строку
    print()

for i in range(1, N + 1, 1):
    # пустые пробелы перед символами строки
    for j in range(1, i + 1, 1):
        print(' ', end='')

    # символы строки
    for k in range(N, i - 1, -1):
        print('**', end='')
    print()


# мой вариант
N = int(input("Введите число: "))

for i in range(N, 0, -1):
    for j in range(i):
        print(' ', end='')

    for k in range(i, N + 1):
        print('**', end='')
    print()

# вместо for i in range(1, N + 1, 1): я бы сделал как в первом цикле for i in range(N, 0, -1):
for i in range(N, 0, -1):

    # сюда просто вставлю вложенные циклы из первого внешнего цикла и переставлю условия вложенных циклов
    # так как, мне нужно построить такой же треугольник, только в обратном направлении
    for j in range(i, N + 1):
        print(' ', end='')

    for k in range(i):
        print('**', end='')
    print()
