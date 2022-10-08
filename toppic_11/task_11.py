data = input("Введите ваш текст: ")

print(f'Исходная строка{data}\n'
      f'Тип:{type(data)}\n'
      f'Строка преобразована в кортеж: {tuple(data.replace(" ", ""))}')

