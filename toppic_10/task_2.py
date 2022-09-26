# data = input().split()
f_list = [3, 4, 5, 6, 7]
s_list = ["a", "b", "c", "d"]
# print(*data)
print(*f_list)
print(*s_list)

# Отличное решение!

# Вот ещё другие варианты
print(' '.join(s_list))
print(' '.join((str(item) for item in f_list)))

