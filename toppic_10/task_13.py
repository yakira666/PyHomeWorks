data = input("Введите ваш текст: ").split()

counter = 0
for i in range(len(data)):
    if len(data[i]) >= 3 and data[i][0] == data[i][-1]:
        counter += 1
print(counter)

# Отлично!
# Было бы проще решить задачу с помощью итератора, вместо range()
