# Я сделаль, не было времени как-то подумать над оптимизацией, предлагаю обсудить на занятии
# month = input("Введите название месяца: ")
# day = int(input("Введите день: "))
#
# season = ''

# if month == "Март" or month == "Апрель" or month == "Май" or month == "Июнь":
#     if (month == "Апрель" or month == "Май") and 0 < day <= 31:
#         print(month, day, "Соответствуют сезону Весна")
#     elif month == "Март" and 20 <= day <= 31:
#         print(month, day, "Соответствуют сезону Весна")
#     elif month == "Июнь" and 0 < day <= 20:
#         print(month, day, "Соответствуют сезону Весна")
# if month == "Июнь" or month == "Июль" or month == "Август" or month == "Сентябрь":
#     if (month == "Июль" or month == "Август") and 0 < day <= 31:
#         print(month, day, "Соответствуют сезону Лето")
#     elif month == "Июнь" and 20 < day <= 31:
#         print(month, day, "Соответствуют сезону Лето")
#     elif month == "Сентябрь" and 0 < day <= 21:
#         print(month, day, "Соответствуют сезону Лето")
# if month == "Сентябрь" or month == "Октябрь" or month == "Ноябрь" or month == "Декабрь":
#     if (month == "Октябрь" or month == "Ноябрь") and 0 < day <= 31:
#         print(month, day, "Соответствуют сезону Осень")
#     elif month == "Сентябрь" and 22 <= day <= 31:
#         print(month, day, "Соответствуют сезону Осень")
#     elif month == "Декабрь" and 0 < day <= 20:
#         print(month, day, "Соответствуют сезону Осень")
# if month == "Декабрь" or month == "Январь" or month == "Февраль" or month == "Март":
#     if (month == "Январь" or month == "Февраль") and 0 < day <= 31:
#         print(month, day, "Соответствуют сезону Зима")
#     elif month == "Декабрь" and 20 < day <= 31:
#         print(month, day, "Соответствуют сезону Зима")
#     elif month == "Март" and 0 < day <= 19:
#         print(month, day, "Соответствуют сезону Зима")

# print(month, day, "Соответствуют сезону", season)


# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====

month = input("Введите название месяца: ")
day = int(input("Введите день: "))

season = ''  # сезон при выходе

if month == 'Январь' or month == 'Февраль':
    season = 'Зима'

elif month == 'Март':
    if day < 20:
        season = 'Зима'
    else:
        season = 'Весна'


print(month, day, "Соответствуют сезону", season)

