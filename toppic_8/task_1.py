for i in range(10, 16):
    print(i)
else:
    print("Готово!")

count = 10  # будет хорошей практикой называть переменные на английском языке: schet -> count
# while count <= 15:
#     print(count)
#     count += 1
# else:
#     print("Готово!")
# ===================================================================
count_1 = 9
while count_1 <= 15:
    count_1 += 1
    if count_1 <= 15:
        print(count_1)
    else:
        print("Готово!")

# задача должна была быть реализована с помощью блоков else в циклах
for i in range(10, 16):
    if i < 15:
        print(i)
    else:
        print(i)
        print("Готово!")

