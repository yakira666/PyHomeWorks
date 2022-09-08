start_range = int(input("Начало диапозона: "))
finish_range = int(input("Конец диапозона: "))
print("Простые число от", start_range, "до", finish_range)
for i in range(start_range, finish_range + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

'''
# Твое решение
Начало диапозона: 0
Конец диапозона: 7
Простые число от 0 до 7
0
1
2
3
5
7


# моё решение
Начало диапазона: 0
Конец диапазона: 7
Простые числа от 0 до 7
2
3
5
7

0 и 1 не являются простыми числами
'''
