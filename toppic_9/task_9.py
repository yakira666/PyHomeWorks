# data = input("Введите любую строку: ")
#
# print("Исходная строка:", data)
# print("Измененная строка:", data.title())  # Отлично!

# Как можно решить задачу не использую встроенных методов?

# №2
data = input("Введите любую строку: ").split()
for i in data:
    print(i.capitalize(), end=" ")

# Решение рабочее!


# Задачу можно решить таким образом не используя, capitalize() и title()
# Но, конечно, это решение не является оптимальным, но оно повышает понимание методов title() и capitalize()
inp_str = input("Введите любую строку: ")
out_str = ""
for word in inp_str.split():
    out_str += word[0].upper() + word[1:] + " "

print(f"\nИсходная строка: {inp_str}\nИзмененная строка: {out_str}")
