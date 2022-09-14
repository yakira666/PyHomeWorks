# # №1
data = input("Введите строку: ")
print("Исходная стока:", data)
print("Изменненная строка:", data.replace("@", ""))

# №2
b = ""
for i in data:
    if i != "@":
        b += i
print(b)

# Супер, молодец!
