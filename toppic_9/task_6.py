data = input("Введите любую строку: ")
char_count = int(input("Введите количество символов, которые нужно извлечь слева: "))
if char_count < len(data):
    print(data[:char_count])  # двоеточие шага указывать необъязательно
else:
    print("Введите меньше символов...")
