# №1
# data = [5, 10, 7, 4, 15, 3]
# print(f'Исходный список: {data}')
# print(f'Кортеж: {tuple(data)}')

# №2
data = [int(i) for i in input("Введите исходный список: ").replace(" ", "").strip("[]").replace(",", "")]

print(f'Исходный список: {data}')
print(f'Кортеж: {tuple(data)}')
