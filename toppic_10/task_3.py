data = int(input("Введите число для умножения каждого элемента: "))
# f_list = [3, 4, 5, 6]
f_list = ['a', 'b', 'c', 'd']
s_list = [i * data for i in f_list]
print(s_list)