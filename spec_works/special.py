# special_task
# b = 1
# a = int(input("Введите кол-во звезд: "))
# v = a
# for i in range(a, 0, -1):
#     print(" " * i + "*" * b * 2)
#     b += 1
# for j in range(1, a+1):
#     print(" " * j + "*" * v * 2)
#     v -= 1
N = int(input())  # 4
for i in range(N, 0, -1):
    # пустые пробелы перед символами строки
    for j in range(i):
        print(' ', end='')

    # символы строки
    for k in range(i, N, 1):
        print('**', end='')
    print()  # переход на новую строку
for i in range(1, N+1, 1):
    # пустые пробелы перед символами строки
    for j in range(i):
        print(' ', end='')

    # символы строки
    for k in range(N, i, -1):
        print('**', end='')
    print()  # переход на новую строку