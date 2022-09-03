input_stars = int(input("Введите кол-во звезд: "))
for i in range(input_stars):
    print("* "*i)
for i in range(input_stars, -1, -1):
    print("* "*i)