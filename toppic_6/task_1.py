# Ввод трех чилес
arithmetic_progression_fnum = int(input("Введите число a: "))
arithmetic_progression_snum = int(input("Введите число b: "))
arithmetic_progression_tnum = int(input("Введите число c: "))
# Проверка являются ли числа арифметической прогрессией
if arithmetic_progression_tnum - arithmetic_progression_snum == \
        arithmetic_progression_snum - arithmetic_progression_fnum:
    print("Да, является!")
else:
    print("Не является!")
