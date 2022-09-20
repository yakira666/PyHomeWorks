sale = float(input("Введите размер скидки: "))
price = input("Введите цены через пробелы: ").split()
print("\n\tНазвание\tЦена\tСумма скидки\t Новая цена")
for i in range(0, len(price)):
    print(f'\tТовар '
          f'{i + 1: <6}'
          f'{(float(price[i])): <12.2f}'
          f'{(float(price[i]) * sale): <16.2f}'
          f'{(float(price[i]) - float(price[i]) * sale):.2f}')
print("\n\tОбщее колличество товаров: " f'{len(price)}')

'''
ДЛЯ ТЕСТА

5.99 9.95 3 14.99 19.49 17.99 26.55 10
'''
