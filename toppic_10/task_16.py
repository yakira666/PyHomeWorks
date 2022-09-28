data = input('Введите название городов: ').split()
if "Москва" in data:
    print(data)
elif "Москва" not in data:
    data.append("Москва")
    print(data)
