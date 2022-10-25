scrabble = {1: [".", ",", "?", "!", ":"],
            2: ["A", "B", "C"],
            3: ["D", "E", "F"],
            4: ["G", "H", "I"],
            5: ["J", "K", "L"],
            6: ["M", "N", "O"],
            7: ["P", "Q", "R", "S"],
            8: ["T", "U", "V"],
            9: ["W", "X", "Y", "Z"],
            0: [" "]
            }
data = input("Введите ваш текст: ")
data_s = data.upper()
for i in data_s:
    for j in scrabble:
        if i in scrabble.get(j):
            print(str(j)*((scrabble.get(j)).index(i)+1), end="")
