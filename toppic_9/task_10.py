data = input("Введите любую строку: ")
data_split = data.split()
for i in range(len(data_split)):
    print((" ").join(data_split[0:i + 1:1]))
