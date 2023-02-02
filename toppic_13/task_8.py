first_word = sorted(input("Введите первое слово: ").lower().strip())
second_word = sorted(input("Введите второе слово: ").lower().strip())

res_1 = dict(zip(range(len(first_word)), first_word))
res_2 = dict(zip(range(len(second_word)), second_word))

if res_1 == res_2:
    print("ДА")
else:
    print("НЕТ")
