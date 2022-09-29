while data := input("Введите любую строку (оставьте пустым для выхода): "):
    char_space, char_upper, char_lower, char_digit, char_symbol = 0, 0, 0, 0, 0
    print()
    print(f'В строке \"{data}\"'.center(len(data) + 50))

    for i in data:
        if i.isspace():
            char_space += 1
        elif i.isupper():
            char_upper += 1
        elif i.islower():
            char_lower += 1
        elif i.isdigit():
            char_digit += 1
        elif i in "\'\")%$&/*^:;/\\|+-_(]}@!?[{<=>,.`":
            char_symbol += 1

    print(f'Пробелы: {char_space}\n'
          f'Прописные буквы: {char_upper}\n'
          f'Строчные буквы: {char_lower}\n'
          f'Числа: {char_digit}\n'
          f'Специальные символы: {char_symbol}\n')

    # Это очень плохое решение, подумай как можно обнулить значение глобавльных переменных не назначая их снова?
    # char_space = 0
    # char_upper = 0
    # char_lower = 0
    # char_digit = 0
    # char_symbol = 0
# data_chars = "\'\")%$&/*^:;/\\|+-_(]}@!?[{<=>,.`"
# print(f"В строке \"{data: >20}\"")
# print(f'Пробелы: {data.count(" ")}')
# print(f'Прописные буквы: {sum(i.isupper() for i in data)}')
# print(f'Строчные буквы: {sum(i.islower() for i in data)}')
# print(f'Числа: {sum(i.isdigit() for i in data)}')
# print(f'Специальные строки: {sum(i in data_chars for i in data)}\n')

'''
ДЛЯ ТЕСТА

# Это строка содержит числа 50 & 160 & 234 & 3 & 1. Специальные символы `))"%$
# J20WF $ W10|ikz* ?poqde6u ?.Ieays.VC %B2<{= S**
'''
