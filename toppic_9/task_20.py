# №1
data_num = input("Введите строку длинной 10 символов: ")
if len(data_num) > 10:
    print("Длинна строки должна быть 10 символов ...")
else:
    print(f"{f'{data_num:~>14}':,<18}")
