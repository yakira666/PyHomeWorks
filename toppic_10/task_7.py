f_list = [3, 3, 2, 1, 5, 3, 8, 11]
data = int(input("Укажите элеменет для удаления: "))
if data not in f_list:
    print("Не найден")
else:
    for i in f_list:
        if data in f_list:
            f_list.remove(data)
    print(f_list)
