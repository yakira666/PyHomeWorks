sale = float(input("Введите размер скидки: "))
price = input("Введите цены через пробелы: ").split()

print("\n\tНазвание\tЦена\tСумма скидки\t Новая цена")
for i in range(0, len(price)):
    item = float(price[i])  # цена

    sale_sum = sale * item  # сумма скидки
    new_price = item - sale_sum  # новая цена
    print(f'\tТовар{i + 1: <6} {item:<12.2f}{sale_sum: <16.2f}{new_price:.2f}')

print("\n\tОбщее колличество товаров: " f'{len(price)}')

'''
ДЛЯ ТЕСТА

5.99 9.95 3 14.99 19.49 17.99 26.55 10
'''

# Молоодец, отлично справился с задачей!
# Улучшил читаемость кода :)
