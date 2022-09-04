num = int(input("Введите целое число: "))
# for i in range(num, 0, -1):
#     for j in range(num):
#         a = i - j
#         if a > 0:
#             print(a, "", end="")
#     print()
# Неверное решение задачи
# Как можно решить эту задачу, без использования условного оператора и без допольнительной переменной

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
