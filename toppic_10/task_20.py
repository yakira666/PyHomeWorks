data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]
f_dig = 1
s_dig = -1
for i in range(0, len(data)):
    print(data[f_dig % len(data)] + data[s_dig])
    f_dig += 1
    s_dig += 1
