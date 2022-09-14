data_str = input("Введите строку: ")
data_char = input("Введите букву: ")

print(data_str[:data_str.find(data_char)] + data_str[data_str.rfind(data_char) + 1:])
