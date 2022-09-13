data = input("Введите любую строку: ")
print("Исходная строка:", data)
print("Измененная строка: ", end="")
for i in data:
    if i != " ":
        print(i, end="")
print()

# Моё решение
text = input("Введите любую строку: ")
print("Исходная строка:", text)

out_str = ''
for let in text:
    if let != ' ':
        out_str += let

print("Измененная строка:", out_str)
