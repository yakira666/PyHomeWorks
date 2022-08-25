fnum = int(input("Введите положительное трёхзначное число: "))
# print("Сумма цифр =", fnum % 10 + (fnum % 100) // 10 + (fnum % 1000) // 100)
# print("Произведение цифр =", (fnum % 10) * ((fnum % 100) // 10) * ((fnum % 1000) // 100))

# Почему было бы лучше использовать переменные?

hundreds = fnum // 100  # сотни
dozens = fnum % 100 // 10  # дестяки
units = fnum % 10  # единицы

print('Сумма цифр =', hundreds + dozens + units)
print('Произведение цифр =', hundreds * dozens * units)
