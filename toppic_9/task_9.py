# data = input("Введите любую строку: ")
#
# print("Исходная строка:", data)
# print("Измененная строка:", data.title())  # Отлично!

# Как можно решить задачу не использую встроенных методов?

# №2
data = input("Введите любую строку: ").split()
for i in data:
    print(i.capitalize(), end=" ")

