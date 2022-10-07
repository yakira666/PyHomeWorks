data = (('363', '13'), ('1616', '55'), ('468', '10'))
d = list()
print(f'Исходные значения кортежа: {data}')

# print(f'Новые значения кортежа: {int(i) for i in data[][]}')
data_2 = tuple([tuple([int(j) for j in data[i]])for i in range(len(data))])
print(f'Новый значения кортежа: {data_2}')