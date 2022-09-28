data = [int(i) for i in input("Введите числа, разделенные пробелом: ").split()]
for i in range(1, len(data)):
    a = 0
    if data[a] < data[i]:
        print(data[i], end=" ")
        a += 1
