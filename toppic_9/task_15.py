data = input("Введите любую строку: ")
data_char = input("Введите любую подстроку: ")
if data_char not in data:
    print("В строке", "\"" + data + "\"", "подстрока", "\"" + data_char + "\"",  "отсутствует")
else:
    print("В строке", "\"" + data + "\"", "подстрока", "\"" + data_char + "\"", "присутствуют!")
