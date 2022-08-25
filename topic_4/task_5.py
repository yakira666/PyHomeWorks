population = int(input("Укажите население: "))
# print("Количество выживших: ", -1 * (-fnum // 2))
print("Количество выживших:", population // 2 + population % 2)
