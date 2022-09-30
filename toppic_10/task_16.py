data = input('Введите название городов: ').split()

if "Москва" not in data:
    data.append("Москва")
print(data)
