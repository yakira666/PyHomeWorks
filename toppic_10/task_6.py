# #  №1
f_list = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]

s_list = []
for i in range(0, len(f_list)):
    if f_list[i] not in s_list:
        s_list.append(f_list[i])

f_list = s_list
print(f_list)

# Отлично!
