# №1
# data = [5, 10, 7, 4, 15, 3]
# print(f'Исходный список: {data}')
# print(f'Кортеж: {tuple(data)}')

# №2
data = [int(i) for i in input("Введите исходный список: ").strip(" []").replace(",", "").split()]

print(f'Исходный список: {data}')
print(f'Кортеж: {tuple(data)}')
