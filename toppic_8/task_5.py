data_list = [1852, 12.43, True, 4 + 3j, 'some text', (13, -5), 3.5e10, 100.95,
             [21, 49], {"name": 'Micky', "age": 17}]
for i in data_list:
    if type(i) == float:
        continue
    else:
        print("Тип элемента", i, type(i))

# задача решена неправильно
# переделано 08.09.2022