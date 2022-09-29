f_list = [int(i) for i in input().split()]
data = int(input("Укажите элеменет для удаления: "))

if len(f_list) == 0:
    print("Пустой список")
elif data not in f_list:
    print("Не найден")
else:
    for i in range(f_list.count(data)):
        f_list.remove(data)
    print(f_list)

# Молодец!
