data = input("Введите любую строку: ")
char_count = int(input("Введите количество символов, которые нужно извлечь слева: "))
if char_count < len(data):
    print(data[-char_count::])
else:
    print("Введите меньше символов...")

# Моё решение
inp_str = input("Введите любую строку: ")
num = int(input("Введите количество символов: "))
length = len(inp_str)

if num > len(inp_str):
    print("Введите меньше символов...")
elif num <= len(inp_str):
    print(inp_str[length - num::])
