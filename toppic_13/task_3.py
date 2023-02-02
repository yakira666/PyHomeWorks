chars = [chr(char) for char in range(65, 91)]
points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4,
          "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1,
          "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
          "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
          "Y": 4, "Z": 10}

data = input("Введите слово: ")
uppercase = data.upper()

# №1
# score = 0
# for ch in uppercase:
#     score += points.get(ch, 0)
#
# print(f"{data} оценивается в {score} очков!")

# № 2
print(f"{data} оценивается в {sum([points.get(ch) for ch in uppercase if points.get(ch)])} очков!")
