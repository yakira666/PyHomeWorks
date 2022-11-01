chars = [chr(char) for char in range(65, 91)]
dictionary = {}
for i in range(len(chars)):
    if chars[i] in "AEILNORSTU":
        dictionary[chars[i]] = 1
    elif chars[i] in "DG":
        dictionary[chars[i]] = 2
    elif chars[i] in "BCMP":
        dictionary[chars[i]] = 3
    elif chars[i] in "FHVWY":
        dictionary[chars[i]] = 4
    elif chars[i] in "K":
        dictionary[chars[i]] = 5
    elif chars[i] in "JX":
        dictionary[chars[i]] = 8
    elif chars[i] in "QZ":
        dictionary[chars[i]] = 10

data = input("Введите слово: ")
data_s = data.upper()

# №1
score = 0
for i in data_s:
    score += dictionary.get(i, 0)

print(f"{data} оценивается в {score} очков!")

# № 2
print(f"{data} оценивается в {sum([(dictionary.get(i, 0)) for i in data_s])} очков!")
