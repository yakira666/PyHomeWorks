# f_or_s_word = "первое"
# sort_word = {}
# for i in range(2):
#     sort_word.setdefault(i,
#                          sorted([str(ch) for ch in input(f"Введите {f_or_s_word} слово: ").replace(" ", "").lower()]))
#     f_or_s_word = "второе"
#
# if sort_word.get(0) == sort_word.get(1):
#     print("ДА")
# else:
#     print("НЕТ")
# # ====================================================================================================

first_word = sorted(input("Введите первое слово: ").lower().strip())
second_word = sorted(input("Введите второе слово: ").lower().strip())
# print(set(first_word) == set(second_word))

# ======================================================================================================
res_1 = dict(zip(range(len(first_word)), first_word))
res_2 = dict(zip(range(len(second_word)), second_word))
if res_1 == res_2:
    print("ДА")
else:
    print("НЕТ")
