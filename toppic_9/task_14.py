data_str = input("Введите строку: ")
data_chars = input("Введите букву: ")

print(data_str[:data_str.find(data_chars)] +
      data_str[data_str.rfind(data_chars):data_str.find(data_chars):-1] +
      data_str[data_str.rfind(data_chars):])
