nums = {1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        0: "ноль"
        }
get_data = input()
for i in get_data:
    if i.isdigit():
        print(nums.get(int(i)), end=" ")

# Просто молодец!


# №2
# Также ты можешь всё это написать в одну строку кода
print(*[nums.get(int(key)) for key in input() if key.isdigit()])
