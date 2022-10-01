data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] == data[j]:
            ...

# Как в задание №18, то же самое в этой задачи
# Только действия разные, если число уже встречалось тебе нужно его вывести
