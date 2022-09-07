start_range = int(input("Начало диапозона: "))
finish_range = int(input("Конец диапозона: "))
print("Простые число от", start_range, "до", finish_range)
for i in range(start_range, finish_range + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
