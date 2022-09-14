data_str = input("Введите строку: ")
data_char = input("Введите букву: ")

# first = data_str.find(data_char) + 1
first = data_str.index(data_char) + 1
# last = data_str.rfind(data_char)
last = data_str.rindex(data_char)

print(data_str[:first] + data_str[first:last].replace(data_char, data_char.upper()) + data_str[last:])

# Супер!
