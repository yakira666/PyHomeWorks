scrabble = {1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"]
            }
counter = 0
data = input("Введите слово: ")
data_s = data.upper()
for i in data_s:
    for k in scrabble:
        if i in (scrabble.get(k)):
            counter += k
print(f"{data} оценивается в {counter} очков!")
