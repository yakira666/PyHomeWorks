# Я сделаль, не было времени как-то подумать над оптимизацией, предлагаю обсудить на занятии
mounth = input("Введите название месяца: ")
day = int(input("Введите день: "))
if mounth == "Март" or mounth == "Апрель" or mounth == "Май" or mounth == "Июнь":
    if (mounth == "Апрель" or mounth == "Май") and 0 < day <= 31:
        print(mounth, day, "Соответствуют сезону Весна")
    elif mounth == "Март" and 20 <= day <= 31:
        print(mounth, day, "Соответствуют сезону Весна")
    elif mounth == "Июнь" and 0 < day <= 20:
        print(mounth, day, "Соответствуют сезону Весна")
elif mounth == "Июнь" or mounth == "Июль" or mounth == "Август" or mounth == "Сентябрь":
    if (mounth == "Июль" or mounth == "Август") and 0 < day <= 31:
        print(mounth, day, "Соответствуют сезону Лето")
    elif mounth == "Июнь" and 20 < day <= 31:
        print(mounth, day, "Соответствуют сезону Лето")
    elif mounth == "Сентябрь" and 0 < day <= 21:
        print(mounth, day, "Соответствуют сезону Лето")
elif mounth == "Сентябрь" or mounth == "Октябрь" or mounth == "Ноябрь" or mounth == "Декабрь":
    if (mounth == "Октябрь" or mounth == "Ноябрь") and 0 < day <= 31:
        print(mounth, day, "Соответствуют сезону Осень")
    elif mounth == "Сентябрь" and 22 <= day <= 31:
        print(mounth, day, "Соответствуют сезону Осень")
    elif mounth == "Декабрь" and 0 < day <= 20:
        print(mounth, day, "Соответствуют сезону Осень")
elif mounth == "Декабрь" or mounth == "Январь" or mounth == "Февраль" or mounth == "Март":
    if (mounth == "Январь" or mounth == "Февраль") and 0 < day <= 31:
        print(mounth, day, "Соответствуют сезону Зима")
    elif mounth == "Декабрь" and 20 < day <= 31:
        print(mounth, day, "Соответствуют сезону Зима")
    elif mounth == "Март" and 0 < day <= 19:
        print(mounth, day, "Соответствуют сезону Зима")
