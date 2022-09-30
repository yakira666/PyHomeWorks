data = [int(i) for i in input("Введите числа, разделенные пробелом: ").split()]
for i in range(1, len(data)):
    if data[i-1] < data[i]:
        print(data[i], end=" ")

