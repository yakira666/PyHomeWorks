num = int(input("Введите число: "))
count = 0

for i in range(1, num+1):
    count += i
    if count > 100:
        print("Сумма всех числе в диапозоне от 1 до", num, "больше 100")
        break
else:
    print("Сумма всех числе в диапозоне от 1 до", num, "=", count)

# Отлично!