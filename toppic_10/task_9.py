cities = input("Введите название городов через пробелы: ").split()
cities.sort(key=len, reverse=True)
print(cities[0:3])
