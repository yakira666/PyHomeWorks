motherland = {}

for _ in range(int(input("Введите количество записей: "))):
    country, *cities = input("Введите страну и города: ").split()
    new_city = dict.fromkeys(cities, country)  # Классно!
    motherland.update(new_city)

for _ in range(int(input("Введите количество искомых записей: "))):
    the_desired_city = input("Введите название города: ").capitalize().strip()
    print(motherland.get(the_desired_city, "город не был найден..."))
