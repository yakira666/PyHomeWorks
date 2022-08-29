# ввод 2-х чисел
fnum = int(input("Введите первое число: "))
snum = int(input("Введите второе число: "))
# алгоритм проверки через операторы: меньше\больше\равно
if fnum == snum:
    print("Числа равны")
else:
    if snum < fnum:
        print("Меньше число", snum)
    elif snum > fnum:
        print("Меньше число", fnum)
