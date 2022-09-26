data = [int(i) for i in input().split()]  # Молодец!
data.sort(reverse=True)
ind = 0
if len(data) > 0:
    print(data[0], data[-1])
else:
    print(None)
# Зачем тратить время на сортировку, если можно использовать встроеннные функции для нахождения макс и мин :)
