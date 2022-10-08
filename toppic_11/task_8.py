# data = tuple(input("Введите исходный кортеж: ").split())
# data = (2, 4, 5, 6, 2, 3, 4, 4, 7)
data = [int(i) for i in
        input("Введите исходный кортеж: ")
        .replace(' ', "")
        .replace(",", "")
        .strip(" ()")]

print(f"Исходный кортеж: {tuple(data)}")
char_count = int(input("Укажите искомый элемент: "))
if char_count in data:
    print(data.count(char_count))
else:
    print(f"\"{char_count}\" нет в кортеже")

# Вместо замены круглых скобок лучше использовать strip
