data_str = input("Введите строку: ")
data_char = input("Введите букву: ")

print(data_str[:data_str.find(data_char)+1] +
      (data_str[data_str.find(data_char)+1:data_str.rfind(data_char)].replace(data_char, data_char.upper())) +
      data_str[data_str.rfind(data_char):])
