fnum = int(input("Введите первое число: "))
snum = int(input("Введите второе число: "))

if fnum < 0 and snum < 0:
    print("Нет")
else:
    print("Да")  # Молодец!

# если решить по другой логике, если одно из значений положительное
print("Да") if (fnum > 0) or (snum > 0) else print("Нет")
