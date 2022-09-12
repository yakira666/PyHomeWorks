data = input("Введите любую строку: ")
# №1
data_split = len(data.split())
if data_split > 1:
    print("В строке", "\""+data+"\"", "-", data_split, "слов")
elif data_split == 1:
    print("Строка состоит из одного слова")
else:
    print("Строка пустая")

# №2

#     print(data.count(" ")+1)
