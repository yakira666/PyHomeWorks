baby, child, adult, elderly = 0, 0, 0, 0  # Количество детей   # Количество детей от
# 3 до 12 # Количество взрослых  # Количество пенсионеров
price_for_baby, price_for_child, price_for_abult, price_for_elderly = 0, 1055, 2099, 1449
plank_1, plank_2, plank_3, plank_4 = 0, 2, 12, 65  # Ввод возрастных планок

while (people_age := int(input("Введите возраст посетителя (0 для окончания ввода): "))) != 0:
    if plank_1 < people_age <= plank_2:
        baby += 1
    elif plank_2 < people_age <= plank_3:
        child += 1
    elif plank_3 < people_age <= plank_4:
        adult += 1
    elif people_age > plank_4:
        elderly += 1

full_price = (elderly * price_for_elderly) + (adult * price_for_abult) + \
             (baby * price_for_baby) + (child * price_for_child)  # Подсчет полной цены
print(
    f'\nКоличестово детей до двух лет: {baby}\n'
    f'Количестово детей от 3-х до 12 лет: {child}\n'
    f'Количестово взрослых: {adult}\n'
    f'Количестово пенсионер: {elderly}\n'
    f'\nОбщая стоимость билетов '
    f'{full_price:,.2f}'
    f'{chr(8381)}')

# Отлично!
