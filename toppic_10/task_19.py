data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]
for i in data:
    if data.count(i) > 1:
        print(i, end=" ")