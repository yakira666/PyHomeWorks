nums = {1: "один", 2: "два", 3: "три", 4: "четыре",
        5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
        9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать",
        13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестьнадцать",
        17: "семьнадцать", 18: "восемьнадцать", 19: "девятнадцать", 20: "двадцать",
        30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят",
        70: "семьдесят", 80: "восемьдесят", 90: "девяносто", 100: "сто",
        200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",
        600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот", 0: "ноль",
        }

get_data = input().split()

for i in get_data:
    hundredths = nums.get((int(i) // 100) * 100)
    tenth = nums.get(int(i) % 100)
    single = int(i) % 100

    if i.isdigit() and 19 < int(i) < 100:
        print(nums.get((int(i) // 10) * 10), nums.get(int(i[1])), end="; ")
    elif i.isdigit() and 1000 > int(i) > 99:
        if 0 < single < 10:
            print(hundredths, nums.get(int(i[2])), end="; ")
        elif 9 < single < 20:
            print(hundredths, tenth, end="; ")
        else:
            print(hundredths, nums.get(((int(i) // 10) % 10) * 10), nums.get(int(i[2])), end="; ")
    elif i.isdigit() and int(i) < 20:
        print(tenth, end="; ")
    else:
        print("Введите число меньше 1000!")
# №2
# print(*[nums.get(int(key)) for key in input() if key.isdigit()]
