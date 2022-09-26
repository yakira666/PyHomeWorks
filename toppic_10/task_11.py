data = input("Введите ваш текст: ").split()
print(*(data[::-1]))
print(*(data[i][::-1] for i in range(len(data)-1, -1, -1)))
