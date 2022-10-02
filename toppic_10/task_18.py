data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] == data[j] and data[i] in data[:j:]:
            break
    else:
        print(data[i], end=" ")
