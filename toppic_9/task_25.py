ascii_char = 65

if (data := int(input("Введите число от 1 до 26: "))) < 27:
    print('+___ ' * data)
    for i in range(data):
        # print(f'+___\n|{chr(ascii_char)} / \n|__\\ \n|   ') #  Оставил для пробы решения
        # print(f'+___\n'f'|{chr(ascii_char)} /\n'f'|__\\\n'f'|   ') #  Оставил для пробы решения
        print(f'|{chr(ascii_char)} / ', end="")
        ascii_char += 1
    print()
    print('|__\\ ' * data)
    print(f'|    ' * data)

else:
    print("Введите число от 1 до 26 ... ")
