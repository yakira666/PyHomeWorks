data = input("Введите любую строку (оставьте пустым для выхода): ")
data_chars = "\'\")%$&/*^:;/\\|#]}@!?[{<>."
while data != "":
    print(f"\n\t\t\t\t\tВ строке \"{data}\"")
    print(f'Пробелы: {data.count(" ")}')
    print(f'Прописные буквы: {sum(i.isupper() for i in data)}')
    print(f'Строчные буквы: {sum(i.islower() for i in data)}')
    print(f'Числа: {sum(i.isdigit() for i in data)}')
    print(f'Специальные строки: {sum(i in data_chars for i in data)}\n')
    data = input("Введите любую строку (оставьте пустым для выхода): ")
#  Эта строка содержит числа 50 & 160 & 234 & 3 & 1. Специальные символы '))"%$
#  J20WF $ W10|ikz* ?poqde6u ?.Ieays. VC %B2<{= S**
