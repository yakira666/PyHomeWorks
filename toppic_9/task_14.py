data_str = input("Введите строку: ")
data_chars = input("Введите букву: ")

first = data_str.index(data_chars)
# first = data_str.find(data_chars)
last = data_str.rindex(data_chars)
# last = data_str.rfind(data_chars)

print(data_str[:first] + data_str[last:first:-1] + data_str[last:])

'''
Молодец!

В задании №12 подробно описал, почему необходимо использовать index() вместо find()

Также поместил индексы в отдельные переменные, что упрощает читаемость кода
'''
