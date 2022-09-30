data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]
if len(data) == 1:
    print(data[0])
else:
    for i in range(0, len(data)):
        print(data[(i+1) % len(data)] + data[i-1], end=' ')
