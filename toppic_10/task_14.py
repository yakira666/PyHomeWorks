data = input("Введите любую строку: ").split()
word = input("Введите слово для поиска: ")
print(f'Слово "{word}" существует в строке "{" ".join(data)}" на позиции {data.index(word)+1}')\
    if word in data else print(f'Слово "{word}" не существует в строке "{" ".join(data)}"')
