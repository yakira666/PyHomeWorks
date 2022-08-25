# name_1, name_2 = int(input("Введите значение a: ")), int(input("Введите значение b: "))
num_a, num_b = int(input("Введите значение а: ")), int(input("Введите значение num_b: "))

num_a, num_b = num_b, num_a  # num_a получает значение num_b, num_b получает значение num_a
print("num_a = " + str(num_a), "num_b = " + str(num_b), sep="\n")
