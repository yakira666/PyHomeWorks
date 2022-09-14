data = input("Введите текст: ")
data_char = input("Введите букуву: ")

if data_char not in data:
    print(-1)

elif data.count(data_char) == 1:
    print(data.find(data_char))

else:
    print(data.find(data_char), data.rfind(data_char), sep=" ")

# Просто Браво!!!
