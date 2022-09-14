data = input("Введите любую строку: ").split()
print(data)
for i in data:
    print(i[0] + i[1], end=" ")
