data = [int(i) for i in input('Введите оценки через пробелы: ').split()]
print(data)
print('Отчислен') if data.count(2) > 1 else print('Учится')
