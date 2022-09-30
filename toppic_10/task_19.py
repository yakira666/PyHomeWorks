data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]
# for i in data:
#     if data.count(i) > 1:
#         print(i, end=" ")
counter = 0
for i in range(len(data)):
    for j in range(len(data)):
        if data[i] == data[j]:
            counter += 1
        continue
    if counter > 1:
        print(data[i], end=" ")
    counter = 0
