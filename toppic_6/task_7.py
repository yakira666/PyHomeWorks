collor_mix_1 = input("Укажите первый цвет: ")
collor_mix_2 = input("Укажите второй цвет: ")

if (collor_mix_1 == "красный" and collor_mix_2 == "желтый") or (collor_mix_2 == "красный" and collor_mix_1 == "желтый"):
    print("оранжевый")
elif (collor_mix_1 == "красный" and collor_mix_2 == "синий") or (collor_mix_2 == "красный" and collor_mix_1 == "синий"):
    print("фиолетовый")
elif (collor_mix_1 == "синий" and collor_mix_2 == "желтый") or (collor_mix_2 == "синий" and collor_mix_1 == "желтый"):
    print("зеленый")
else:
    print("Ошибка цвета ...")

# Программа работает, но ее необходимо доработать

# например
# красный желтый -> оранжевый
# желтый красный -> Выдает ошибку "Ошибка цвета..."

# также с остальными цветами
