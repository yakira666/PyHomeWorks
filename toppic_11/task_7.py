# data = ("P", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g")

# print(f"Исходный кортеж: {data}")
# print("".join(data))
# как решить через инпут

data = [i for i in
        input("Введите исходный кортеж: ")
        .replace(" ", "")
        .strip("()")
        .replace(",", "")
        .replace("\'", "")
        .replace("\"", "")
        ]

print(f'Исходный кортеж: {data}')
print(f'{"".join(data)}')
