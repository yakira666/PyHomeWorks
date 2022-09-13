data = input("Введите любую строку: ")
data_split = data.split()
for i in range(len(data_split)):
    print(" ".join(data_split[0:i + 1:1]))

# Отлично!

# Ещё одно решение
inp_str = input("Введите любую строку: ")

out_str = ""
for word in inp_str.split():
    out_str += word + " "
    print(out_str)
