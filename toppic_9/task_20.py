# №1
if len(data_num := input("Введите строку длинной 10 символов: ")) == 10:
    print(f'{data_num[:5]:~>9}{data_num[5:]:,<9}')
else:
    # print(f"{f'{data_num:~>14}':,<18}") #  Опасно использование f внутри f
    # data_num = f"{data_num:~>14}"
    # print(f"{data_num:,<18}")
    print("Длинна строки должна быть 10 символов ...")
