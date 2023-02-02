first_text = sorted(ch for ch in input("Введите первое предложение: ").lower().strip() if ch.isalnum())
second_text = sorted(ch for ch in input("Введите второе предложение: ").lower().strip() if ch.isalnum())

res_1 = dict(zip(range(len(first_text)), first_text))
res_2 = dict(zip(range(len(second_text)), second_text))

if res_1 == res_2:
    print("ДА")
else:
    print("НЕТ")
print(res_1, res_2)


"""
игнорировать знаки препинания, заглавные буквы и пробелы
обработать строку одним из методов isalnum
"""