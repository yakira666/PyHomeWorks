data = input("Введите любое слово: ")
for i in range(len(data)):
    print(data[0:i + 1:1])

# Отлично!

# Ещё одно решение
word = input("Введите любое слово: ")

out_word = ""
for char in word:
    out_word += char  # out_word = out_word + w
    print(out_word)
