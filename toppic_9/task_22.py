sale = float(input("Введите размер скидки: "))
price = input("Введите цены через пробелы: ").split()

print("\n\tНазвание\tЦена\tСумма скидки\t Новая цена")
for i in range(0, len(price)):
    print("\tТовар "
          f'{i + 1}'  # столб номера товара
          f'\t\t{(float(price[i])):.2f}'  # столб цены по товару 
          f'\t\t{(float(price[i]) * sale):.2f}'  # столб скидки по товару
          f'\t\t\t{(float(price[i]) - float(price[i]) * sale):.2f}')  # новая цена
print("\n\tОбщее колличество товаров: " f'{len(price)}')
