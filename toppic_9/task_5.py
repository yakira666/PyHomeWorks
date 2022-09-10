data = input("Введите любую строку: ")
print("Исходная строка:", data)
print("Измененная строка: ", end="")
for i in data:
    if i != " ":
        print(i, end="")
print()
