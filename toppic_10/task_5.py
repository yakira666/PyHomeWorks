data = int(input("Введите целое число: "))
f_list = [10,-2, 0, 4, -4, 3, 13, -2, 6, -1, 7]
counter = 0
for i in f_list:
    if int(i) > data:
        counter += 1
print(counter)
