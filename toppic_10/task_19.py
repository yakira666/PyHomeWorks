data = [int(i) for i in input("Введите числа, разделенные пробелами: ").split()]
for i in data:
    if data.count(i) > 1:
        print(i, end=" ")

# Неправильное решение, способ решения этой задачи, точно такой же, как в задаче №18 с помощью вложенных циклов
