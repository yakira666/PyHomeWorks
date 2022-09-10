soglasniy = ["а", "у", "е", "о", "э", "я", "ы", "и", "ё"]
data = input("Введите любое слово: ")
g = 0
sg = 0
for i in data:
    if i in soglasniy:
        g += 1
    else:
        sg += 1
print("Количество гласных букв: ", g)
print("Количество согласных букв: ", sg)
