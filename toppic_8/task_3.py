num = int(input("Введите число: "))
schet = 0
for i in range(1, num+1):
    schet += i
if schet < 100:
    print("Сумма всех чисел в диапозоне от 1 до", num, "=", schet)
else:
    print("Сумма всех чисел в деапозоне от 1 до", num, "больше 100")

