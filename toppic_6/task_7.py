collor_mix_1 = input("Укажите первый цвет: ")
collor_mix_2 = input("Укажите второй цвет: ")
if collor_mix_1 == "красный" and collor_mix_2 == "желтый":
    print("оранжевый")
elif collor_mix_1 == "красный" and collor_mix_2 == "синий":
    print("фиолетовый")
elif collor_mix_1 == "синий" and collor_mix_2 == "желтый":
    print("зеленый")
else:
    print("Ошибка цвета ...")
