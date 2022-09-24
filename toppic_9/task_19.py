ascii_char = 65
if (data := int(input("Введите число от 1 до 7: "))) > 7:
    print("Введите число в диапозоне от 1 до 7...")
else:
    for i in range(1, data + 1):
        for _ in range(i):
            print(chr(ascii_char), end=" ")
            ascii_char += 1
        print()
