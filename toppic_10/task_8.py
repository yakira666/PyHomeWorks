data = input("Введите ваш текст: ").split()
data.sort(key=len, reverse=True)
print(f'Самое длинное слово в предложении: {data[0]},'
      f'Самое короткое слово в предложении: {data[-1]}')
# print(f'Самое длинное слово в предложении: {max(data, key=len)}')
# print(f'Самое короткое слово в предложении: {min(data, key=len)}')
