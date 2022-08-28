given_list = [16, 98, 77]

num = str(given_list[0]) + str(given_list[1]) + str(given_list[2])
print(int(num))

# здесь не преобразуется в целое число, но, конечно, мы получаем желаемый результат, это не совсем правильное решение
# given_list = [str(x) for x in given_list]
# print(given_list[0] + given_list[1] + given_list[2])

# можно было упростить твоё второе решение, если бы не нужно было преобразовывать в целое число
# print(*given_list, sep='')  # 169877
